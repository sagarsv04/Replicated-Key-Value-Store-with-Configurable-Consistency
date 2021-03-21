#!/usr/bin/env python3

import os
import sys
import socket
import hashlib
import argparse

base_dir = "../"
# base_dir = "./"
# os.chdir("{0}src/".format(base_dir))

DEBUG = False # make it false while deploying
HALF_SERVER = False # make it false while deploying

if not DEBUG:
    # sys.path.append("/home/sting/protobuf/python/")
    sys.path.append("/home/svishwa2/protobuf/python/")
    pass

import logger as log
import key_value_store_pb2 as kvs_pb2


BUFFER_SIZE = 1024


def operation_description():
   return """
Operation supports the following:
   1         - To Get Key
   2         - To Put Key
   3         - To Display

Consistency supports the following:
   1         - Level One
   2         - Level Quorum
"""


def get_operation_choices():
   return [1, 2, 3]


def get_replica_info(logger):

    logger.info("Fetching Replica Info")
    file_txt = None
    replica_info = {}
    with open("{0}res/replica_list".format(base_dir), "r") as fp:
        file_txt = fp.read()

    file_txt_list = [x for x in file_txt.split("\n") if x!= ""]
    for replica in file_txt_list:
        # replica = file_txt_list[0]
        replica_info[replica.split(" ")[0]] = [replica.split(" ")[1], int(replica.split(" ")[2])]

    if DEBUG:
        logger.info("Replica Info: {0}".format(replica_info))

    return replica_info


def get_request(logger, req_key, consistency_type):

    logger.info("Creating get request for key: {0}, consistency:{1}".format(req_key, consistency_type))

    request = kvs_pb2.KeyValueMessage()
    request.get_request.key = req_key
    request.get_request.consistency_level = consistency_type
    if DEBUG:
        logger.info("Get Request: {0}".format(request))
    return request


def put_request(logger, req_key, consistency_type, req_value):

    logger.info("Creating put request for key: {0}, consistency:{1}".format(req_key, consistency_type))
    request = kvs_pb2.KeyValueMessage()
    request.put_request.key = req_key
    request.put_request.consistency_level = consistency_type
    request.put_request.value = req_value
    if DEBUG:
        logger.info("Put Request: {0}".format(request))

    return request


def display_request(logger):

    logger.info("Creating display request")
    request = kvs_pb2.KeyValueMessage()
    request.display_key_value.status = True
    # request.SerializeToString()
    if DEBUG:
        logger.info("Display Request: {0}".format(request))

    return request


def get_server_response(logger, ip_addr, port_num, request):

    logger.info("Sending Client Request to: {0}:{1}".format(ip_addr, port_num))
    response = None
    try:
        client_socket = socket.socket()
        client_socket.connect((ip_addr, port_num))
        client_socket.sendall(request.SerializeToString())
        response_data = client_socket.recv(BUFFER_SIZE)
        # response_data = b'*\x02\x08\x01'
        response = kvs_pb2.KeyValueMessage()
        response.ParseFromString(response_data)
    except Exception as ex:
        logger.error("Error: {0}".format(ex))

    return response


def send_server_request(logger, replica_info, request):

    for replica in replica_info:
        logger.info("Sending Request to: {0} {1}:{2}".format(replica, replica_info[replica][0], replica_info[replica][1]))
        try:
            client_socket = socket.socket()
            client_socket.connect((replica_info[replica][0], replica_info[replica][1]))
            client_socket.sendall(request.SerializeToString())
            client_socket.close()
        except Exception as ex:
            logger.error("Error: {0}".format(ex))
            client_socket.close()
            continue

    return 0


def print_server_response(logger, response):

    if response.HasField("coordinator_response"):
        if response.coordinator_response.status:
            logger.info("Coordinator Respons: {0}".format(response))
        else:
            logger.info("Coordinator Invalid Status Respons: {0}".format(response))
    elif response.HasField("error_message"):
        logger.info("Coordinator Error Message: {0}".format(response.error_message.msg))
    else:
        logger.info("Client Receved Non-Coordinator Response...")
        if DEBUG:
            logger.info("Non-Coordinator Respons: {0}".format(response))
    return 0


def run_client(logger, args):

    ip_addr = args.ip
    # ip_addr = "127.0.0.1"
    port_num = args.port
    # port_num = 9090
    operation_type = args.operation
    req_key = args.key
    # req_key = 20
    consistency_type = args.consistency
    # consistency_type = 1
    req_value = args.value
    # req_value = "hey hey hey"
    logger.info("Running Client Request for: {0}:{1}".format(ip_addr, port_num))
    logger.info("Operation: {0}, Consistency: {1}, Key: {2}, Value: {3}".format(operation_type, consistency_type, req_key, req_value))

    if 0<=req_key<=255 or operation_type==3:
        if operation_type==1:
            request = get_request(logger, req_key, consistency_type)
            # make request on server
            response = get_server_response(logger, ip_addr, port_num, request)
            print_server_response(logger, response)
        elif operation_type==2:
            request = put_request(logger, req_key, consistency_type, req_value)
            # make request on server
            response = get_server_response(logger, ip_addr, port_num, request)
            print_server_response(logger, response)
        else:
            replica_info = get_replica_info(logger)
            request = display_request(logger)
            # make request on server
            send_server_request(logger, replica_info, request)
    else:
        logger.error("Error: Key out of 0-255 range...")
        logger.info("Stopped Client Request for: {0}:{1}".format(ip_addr, port_num))

    return 0


def main():
    parser = argparse.ArgumentParser(description="Client", formatter_class=argparse.RawTextHelpFormatter, epilog=operation_description())
    parser.add_argument("ip", type=str, help="ip address of replica server")
    parser.add_argument("port", type=int, help="port number of replica server")
    parser.add_argument("operation", type=int, choices=get_operation_choices(), help="Operation type")
    parser.add_argument("consistency", type=int, nargs="?", choices=get_operation_choices()[:-1], default=-1, help="request consistency level for server")
    parser.add_argument("key", type=int, nargs="?", default=-1, help="request key for server")
    parser.add_argument("value", type=str, nargs="?", default="", help="request value for server")

    args = parser.parse_args()
    port_num = args.port
    # port_num = 9090
    logger = log.get_logger("Client-{0}".format(port_num))

    if args.operation != 3 and args.key == -1:
        logger.info("Invalid Key: {0}".format(args.key))
        parser.print_help()
        sys.exit(os.EX_USAGE)
    elif args.operation != 3 and args.consistency == -1:
        logger.info("Invalid Consistency: {0}".format(args.consistency))
        parser.print_help()
        sys.exit(os.EX_USAGE)
    else:
        try:
            run_client(logger, args)
        except Exception as ex:
            logger.error("Error: {0}".format(ex))

    return 0


if __name__ == '__main__':
    main()
