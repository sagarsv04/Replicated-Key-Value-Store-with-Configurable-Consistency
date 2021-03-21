#!/usr/bin/env python3

import os
import sys
import time
import pickle
import socket
import hashlib
import argparse
import operator
import threading

base_dir = "../"
# base_dir = "./"
# os.chdir("{0}src/".format(base_dir))

import logger as log
from client import get_replica_info, BUFFER_SIZE, DEBUG, HALF_SERVER


TIMEOUT = 1
READ_WRITE_COUNT = [0,0]
TIMESTAMP = 0.0
KEY_VALUE_STORE = {}
HINTED_HANDOFF_DICT = {}
GET = 0
PUT = 1
CONSISTENCY_LEVEL_ONE = 1
CONSISTENCY_LEVEL_QUORUM = 2
READ = 0
WRITE = 1


THREAD_LOCK = threading.Lock()


if not DEBUG:
    # sys.path.append("/home/sting/protobuf/python/")
    sys.path.append("/home/svishwa2/protobuf/python/")
    pass

import key_value_store_pb2 as kvs_pb2




def get_replica_id(replica_name):
   return int("".join(x for x in replica_name if x.isdigit()))


def get_replica_name(replica_id):
   return "replica{0}".format(replica_id)


def load_store_key_value_store(logger, is_store):
    global KEY_VALUE_STORE

    if not os.path.exists("{0}out/".format(base_dir)):
        logger.info("Creating Other directory: {0}".format("{0}out/".format(base_dir)))
        os.mkdir("{0}out/".format(base_dir))
        with open("{0}out/key_value_store.db".format(base_dir), "wb") as fp:
            pickle.dump(KEY_VALUE_STORE, fp)
    elif not os.path.isfile("{0}out/key_value_store.db".format(base_dir)):
        logger.info("Creating file: {0}".format("{0}out/key_value_store.db".format(base_dir)))
        with open("{0}out/key_value_store.db".format(base_dir), "wb") as fp:
            pickle.dump(KEY_VALUE_STORE, fp)
    else:
        if is_store:
            logger.info("Storing file: {0}".format("{0}out/key_value_store.db".format(base_dir)))
            with open("{0}out/key_value_store.db".format(base_dir), "wb") as fp:
                pickle.dump(KEY_VALUE_STORE, fp)
        else:
            logger.info("Loading file: {0}".format("{0}out/key_value_store.db".format(base_dir)))
            with open("{0}out/key_value_store.db".format(base_dir), "rb") as fp:
                KEY_VALUE_STORE = pickle.load(fp)
    return 0


def create_hint_dictionary(logger, replica_info, replica_name):
    global HINTED_HANDOFF_DICT

    logger.info("Creating HINTED_HANDOFF_DICT...")

    for key in replica_info:
        if key != replica_name:
            HINTED_HANDOFF_DICT[str(get_replica_id(key))] = []
    if DEBUG:
        logger.info("HINTED_HANDOFF_DICT Info: {0}".format(HINTED_HANDOFF_DICT))

    return 0


def get_replica_list(logger, key):
    global HALF_SERVER

    logger.info("Fetching Replicat List for key: {0}".format(key))

    replica_list = []

    if HALF_SERVER:
        if 0<=key<128:
            replica_list = [0,1]
        elif 128<=key<256:
            replica_list = [1,0]
        else:
            logger.info("Invalid Key Passed...")
    else:
        if 0<=key<64:
            replica_list = [0,1,2]
        elif 64<=key<128:
            replica_list = [1,2,3]
        elif 128<=key<192:
            replica_list = [2,3,0]
        elif 192<=key<256:
            replica_list = [3,0,1]
        else:
            logger.info("Invalid Key Passed...")

    if DEBUG:
        logger.info("Replicat List for key: {0} : {1}".format(key, replica_list))
    return replica_list


def update_key_value_store(logger, key, value, timestamp):
    global KEY_VALUE_STORE, THREAD_LOCK

    ret = False

    if str(key) in KEY_VALUE_STORE:
        if  KEY_VALUE_STORE[str(key)][1] < timestamp:
            THREAD_LOCK.acquire()
            KEY_VALUE_STORE[str(key)] = [value, timestamp]
            THREAD_LOCK.release()
            logger.info("Updated the key: {0} : T {1}".format(key, timestamp))
            ret = True
            load_store_key_value_store(logger, True)
        else:
            logger.info("Skipped Update for key: {0} : Old T {1}, Curr T {2}".format(key, KEY_VALUE_STORE[str(key)][1], timestamp))
    else:
        THREAD_LOCK.acquire()
        KEY_VALUE_STORE[str(key)] = [value, timestamp]
        THREAD_LOCK.release()
        logger.info("Added the key: {0} : T {1}".format(key, timestamp))
        ret = True
        load_store_key_value_store(logger, True)

    return ret


def send_acknowledgment(logger, client_conn, key, value):

    ack_response = kvs_pb2.KeyValueMessage()
    ack_response.coordinator_response.key = key
    ack_response.coordinator_response.value = value
    ack_response.coordinator_response.status = True
    logger.info("Sending Ack Response...")
    if DEBUG:
        logger.info("Response Message: {0}".format(ack_response))
    client_conn.sendall(ack_response.SerializeToString())

    return 0


def send_heart_beat(logger, client_conn):

    ack_response = kvs_pb2.KeyValueMessage()
    ack_response.heart_beat.status = True
    logger.info("Sending Heart Beat Response...")
    if DEBUG:
        logger.info("Response Message: {0}".format(ack_response))
    client_conn.sendall(ack_response.SerializeToString())

    return 0


def send_error_message(logger, client_conn, str_msg):

    err_response = kvs_pb2.KeyValueMessage()
    err_response.error_message.msg = str_msg
    logger.info("Sending Error Response...")
    if DEBUG:
        logger.info("Response Message: {0}".format(err_response))
    client_conn.sendall(err_response.SerializeToString())

    return 0


def print_key_value_store(logger):
    global KEY_VALUE_STORE

    logger.info("Printing key value store...\n")

    for key in KEY_VALUE_STORE:
        logger.info("\t Key: {0}, Value: {1}, Timestamp: {2}".format(key, KEY_VALUE_STORE[key][0], KEY_VALUE_STORE[key][1]))

    logger.info("\nDone Printing key value store...\n")
    return 0


def update_replicas(logger, replica_info, replica_id, client_conn, replica_list, request, consistency, request_type):
    # consistency = CONSISTENCY_LEVEL_ONE
    # consistency = CONSISTENCY_LEVEL_QUORUM
    global READ_WRITE_COUNT, KEY_VALUE_STORE, TIMESTAMP, HINTED_HANDOFF_DICT

    key_value_store_list = []
    hinted_handoff_list = []
    replica_request = kvs_pb2.KeyValueMessage()
    absence_count = 0
    if request_type==PUT:
        replica_request.replica_request.id = replica_id
        replica_request.replica_request.key = request.put_request.key
        replica_request.replica_request.value = request.put_request.value
        replica_request.replica_request.operation = PUT
        replica_request.replica_request.timestamp = TIMESTAMP
    elif request_type==GET:
        if replica_id in replica_list:
            if str(request.get_request.key) in KEY_VALUE_STORE:
                key_data = KEY_VALUE_STORE[str(request.get_request.key)]
                key_value_store_list.append((replica_id, request.get_request.key, key_data[0], key_data[1]))
            else:
                absence_count += 1
        replica_request.replica_request.id = replica_id
        replica_request.replica_request.key = request.get_request.key
        replica_request.replica_request.operation = GET
        replica_request.replica_request.timestamp = TIMESTAMP

    for id in replica_list:
        # id = replica_list[1]
        if id != replica_id:
            replica_name = get_replica_name(id)
            ip_addr, port_num = replica_info[replica_name]

            try:
                logger.info("Connecting {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
                replica_socket = socket.socket()
                replica_socket.connect((ip_addr, port_num))
                replica_socket.sendall(replica_request.SerializeToString())
                response_data = replica_socket.recv(BUFFER_SIZE)
                replica_socket.close()
            except Exception as ex:
                logger.error("Error: {0}".format(ex))
                logger.info("Failed to Connect {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
                replica_socket.close()
                hinted_handoff_list.append(id)
                if request_type==PUT:
                    HINTED_HANDOFF_DICT[str(id)].append((request.put_request.key, request.put_request.value, TIMESTAMP))
                    logger.info("Storing Hint for {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
                continue

            replica_response = kvs_pb2.KeyValueMessage()
            replica_response.ParseFromString(response_data)

            if DEBUG:
                logger.info("Replica Request: {0}".format(replica_request))
                logger.info("Replica Response: {0}".format(replica_response))

            if replica_response.HasField("replica_response"):
                for hinted_handoff in replica_response.replica_response.hinted_handoff:
                    logger.info("Received HINT from {0}-Server".format(get_replica_name(hinted_handoff.id)))
                    if DEBUG:
                        logger.info("Received Data: K {0}, V {1}, T {2}".format(hinted_handoff.key, hinted_handoff.value, hinted_handoff.timestamp))
                    update_key_value_store(logger, hinted_handoff.key, hinted_handoff.value, hinted_handoff.timestamp)

                if replica_response.replica_response.status:
                    if request_type==GET:
                        READ_WRITE_COUNT[READ] += 1
                        key_value_store_list.append((id, replica_response.replica_response.key, replica_response.replica_response.value, replica_response.replica_response.timestamp))
                        logger.info("Increment READ counter: {0}".format(READ_WRITE_COUNT[READ]))
                        if READ_WRITE_COUNT[READ]==1 and consistency==CONSISTENCY_LEVEL_ONE:
                            request.get_request.value = replica_response.replica_response.value
                            send_acknowledgment(logger, client_conn, request.get_request.key, request.get_request.value)
                        elif READ_WRITE_COUNT[READ]<2 and consistency==CONSISTENCY_LEVEL_QUORUM:
                            logger.info("Quorum Consistency Not Satisfied Available Read Count: {0}".format(READ_WRITE_COUNT[READ]))
                            send_error_message(logger, client_conn, "Quorum Consistency Not Satisfied Available Read Count: {0}".format(READ_WRITE_COUNT[READ]))
                        elif consistency==CONSISTENCY_LEVEL_QUORUM and READ_WRITE_COUNT[READ]>1:
                            if absence_count==3:
                                logger.info("Key is not present absence count: {0}".format(absence_count))
                                send_error_message(logger, client_conn, "Key is not present absence count: {0}".format(absence_count))
                            else:
                                key_value_store_list.sort(key=operator.itemgetter(3), reverse=True) # sort in ascending
                                if DEBUG:
                                    logger.info("Sorted Key value store list: {0}".format(key_value_store_list))
                                _, key, value, _ = key_value_store_list[0]
                                send_acknowledgment(logger, client_conn, key, value)
                        else:
                            logger.info("YOU Should Handle This GET Case.....")
                    elif request_type==PUT:
                        READ_WRITE_COUNT[WRITE] += 1
                        logger.info("Increment WRITE counter: {0}".format(READ_WRITE_COUNT[WRITE]))
                        if READ_WRITE_COUNT[WRITE]==1 and consistency==CONSISTENCY_LEVEL_ONE:
                            send_acknowledgment(logger, client_conn, request.put_request.key, request.put_request.value)
                        elif READ_WRITE_COUNT[WRITE]>=2 and consistency==CONSISTENCY_LEVEL_QUORUM:
                            update_key_value_store(logger, request.put_request.key, request.put_request.value, request.put_request.timestamp)
                            send_acknowledgment(logger, client_conn, request.put_request.key, request.put_request.value)
                        elif consistency==CONSISTENCY_LEVEL_QUORUM and READ_WRITE_COUNT[WRITE]<2:
                            logger.info("Quorum Consistency Not Satisfied Available Write Count: {0}".format(READ_WRITE_COUNT[WRITE]))
                            send_error_message(logger, client_conn, "Quorum Consistency Not Satisfied Available Write Count: {0}".format(READ_WRITE_COUNT[WRITE]))
                        else:
                            logger.info("YOU Should Handle This PUT Case.....")
                else:
                    logger.info("Replica does not have the key...")
                    hinted_handoff_list.append(id)
                    key_value_store_list.append((id, replica_response.replica_response.key, replica_response.replica_response.value, replica_response.replica_response.timestamp))
                    if request_type==GET:
                        absence_count += 1
                        READ_WRITE_COUNT[READ] += 1

    logger.info("Done Processing Replica Request...")

    return 0


def process_consistency_one(logger, replica_info, replica_id, client_conn, request, request_type):
    # request_type = GET
    # request_type = PUT
    global READ_WRITE_COUNT, KEY_VALUE_STORE, TIMESTAMP

    replica_list = []
    if request_type==PUT:
        logger.info("Processing Consistency One Put Request")
        replica_list = get_replica_list(logger, request.put_request.key)
        if request.put_request.id in replica_list:
            READ_WRITE_COUNT[WRITE] += 1
            ret = update_key_value_store(logger, request.put_request.key, request.put_request.value, TIMESTAMP)
            if ret:
                send_acknowledgment(logger, client_conn, request.put_request.key, request.put_request.value)
            else:
                send_error_message(logger, client_conn, "Faled to Update Key Value Store, Check Server Logs")
        else:
            logger.info("Current Replica does not belong to key's replica list")
            # send_error_message(logger, client_conn, "Current Replica does not belong to key's replica list")
    else:
        logger.info("Processing Consistency One Get Request")
        replica_list = get_replica_list(logger, request.get_request.key)
        if request.get_request.id in replica_list:
            if str(request.get_request.key) in KEY_VALUE_STORE:
                READ_WRITE_COUNT[READ] += 1
                request.get_request.value = KEY_VALUE_STORE[str(request.get_request.key)][0]
                send_acknowledgment(logger, client_conn, request.get_request.key, request.get_request.value)
            else:
                logger.info("Current Replica does not store value for key: {0}".format(request.get_request.key))
                send_error_message(logger, client_conn, "Current Replica does not store value for key: {0}".format(request.get_request.key))
        else:
            logger.info("Current Replica does not belong to key's replica list")
            # send_error_message(logger, client_conn, "Current Replica does not belong to key's replica list")
    update_replicas(logger, replica_info, replica_id, client_conn, replica_list, request, CONSISTENCY_LEVEL_ONE, request_type)
    return 0


def process_consistency_quorum(logger, replica_info, replica_id, client_conn, request, request_type):
    # request_type = PUT
    global READ_WRITE_COUNT, KEY_VALUE_STORE

    replica_availability = 0
    replica_list = []

    if request_type==PUT:
        logger.info("Processing Consistency Quorum Put Request")
        replica_list = get_replica_list(logger, request.put_request.key)
        if request.put_request.id in replica_list:
            READ_WRITE_COUNT[WRITE] += 1
            replica_availability = READ_WRITE_COUNT[WRITE]
        else:
            logger.info("Current Replica does not belong to key's replica list")
    else:
        logger.info("Processing Consistency Quorum Get Request")
        replica_list = get_replica_list(logger, request.get_request.key)
        if request.get_request.id in replica_list:
            READ_WRITE_COUNT[READ] += 1
            replica_availability = READ_WRITE_COUNT[READ]
        else:
            logger.info("Current Replica does not belong to key's replica list")

    replica_request = kvs_pb2.KeyValueMessage()
    replica_request.heart_beat.status = False
    # check replicas
    for id in replica_list:
        # id = replica_list[1]
        if id != replica_id:
            replica_name = get_replica_name(id)
            ip_addr, port_num = replica_info[replica_name]
            try:
                logger.info("Connecting {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
                replica_socket = socket.socket()
                replica_socket.connect((ip_addr, port_num))
                replica_socket.sendall(replica_request.SerializeToString())
                response_data = replica_socket.recv(BUFFER_SIZE)
                replica_socket.close()
            except Exception as ex:
                logger.error("Error: {0}".format(ex))
                logger.info("Failed to Connect {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
                replica_socket.close()
                continue

            replica_response = kvs_pb2.KeyValueMessage()
            replica_response.ParseFromString(response_data)
            if replica_response.HasField("heart_beat"):
                if replica_response.heart_beat.status:
                    replica_availability += 1

    if replica_availability >= 2:
        update_replicas(logger, replica_info, replica_id, client_conn, replica_list, request, CONSISTENCY_LEVEL_QUORUM, request_type)
    else:
        logger.info("Quorum Not Satisfied, Available Replica: {0}".format(replica_availability))
        send_error_message(logger, client_conn, "Quorum Not Satisfied, Available Replica: {0}".format(replica_availability))

    return 0


def process_replica_request(logger, replica_info, replica_id, client_conn, request):
    global KEY_VALUE_STORE, HINTED_HANDOFF_DICT

    response = kvs_pb2.KeyValueMessage()
    response.replica_response.id = replica_id

    if request.replica_request.operation==WRITE:
        logger.info("Replica Write Request...")
        response.replica_response.key = request.replica_request.key
        ret = update_key_value_store(logger, request.replica_request.key, request.replica_request.value, request.replica_request.timestamp)
        if ret:
            response.replica_response.status = True
        else:
            response.replica_response.status = False
    elif request.replica_request.operation==READ:
        logger.info("Replica Read Request...")
        response.replica_response.key = request.replica_request.key
        if str(request.replica_request.key) in KEY_VALUE_STORE:
            response.replica_response.value, response.replica_response.timestamp = KEY_VALUE_STORE[str(request.replica_request.key)]
            response.replica_response.status = True
        else:
            response.replica_response.status = False

    if str(request.replica_request.id) in HINTED_HANDOFF_DICT:
        stale_data_list = HINTED_HANDOFF_DICT[str(request.replica_request.id)]
        for data in stale_data_list:
            hinted_handoff_message = response.replica_response.hinted_handoff.add()
            hinted_handoff_message.id = replica_id
            hinted_handoff_message.operation = PUT
            hinted_handoff_message.key = data[0]
            hinted_handoff_message.value = data[1]
            hinted_handoff_message.timestamp = data[2]
        logger.info("Resetting Hinted Data for Id: {0}".format(request.replica_request.id))
        HINTED_HANDOFF_DICT[str(request.replica_request.id)] = []

    client_conn.sendall(response.SerializeToString())
    logger.info("Sending Replica Response Message...")
    if DEBUG:
        logger.info("Replica Response Message: {0}".format(response))

    return 0


def run_server(logger, args):
    global TIMESTAMP, READ_WRITE_COUNT

    replica_name = args.name
    # replica_name = "replica0"
    # replica_name = "replica1"
    ip_addr = socket.gethostbyname(socket.getfqdn())
    port_num = args.port
    # port_num = 9090

    replica_info = get_replica_info(logger)
    replica_id = get_replica_id(replica_name)
    logger.info("Running {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
    load_store_key_value_store(logger, False)
    create_hint_dictionary(logger, replica_info, replica_name)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(TIMEOUT)
    server.bind((ip_addr, port_num))
    server.listen(5)

    run_flag = True

    while run_flag:
        try:
            request = kvs_pb2.KeyValueMessage()
            client_conn, client_addr = server.accept()
            if client_conn:
                request_data = client_conn.recv(BUFFER_SIZE)
                request.ParseFromString(request_data)
                if DEBUG:
                    client_ip, client_port = client_conn.getsockname()
                    logger.info("Request from: {0}:{1}".format(client_ip, client_port))
                    logger.info("Request Message: {0}".format(request))
                if request.HasField("get_request"):
                    # response a get request
                    request.get_request.id = replica_id
                    if request.get_request.consistency_level==CONSISTENCY_LEVEL_ONE:
                        process_consistency_one(logger, replica_info, replica_id, client_conn, request, GET)
                    elif request.get_request.consistency_level==CONSISTENCY_LEVEL_QUORUM:
                        process_consistency_quorum(logger, replica_info, replica_id, client_conn, request, GET)
                    else:
                        logger.info("Invalid Get Request: {0}".format(request))
                elif request.HasField("put_request"):
                    # response a put request
                    request.put_request.id = replica_id
                    TIMESTAMP = time.time()
                    READ_WRITE_COUNT[WRITE] = 0
                    if request.put_request.consistency_level==CONSISTENCY_LEVEL_ONE:
                        process_consistency_one(logger, replica_info, replica_id, client_conn, request, PUT)
                    elif request.put_request.consistency_level==CONSISTENCY_LEVEL_QUORUM:
                        process_consistency_quorum(logger, replica_info, replica_id, client_conn, request, PUT)
                    else:
                        logger.info("Invalid Put Request: {0}".format(request))
                elif request.HasField("replica_request"):
                    # response a replica request
                    process_replica_request(logger, replica_info, replica_id, client_conn, request)
                elif request.HasField("heart_beat"):
                    # response a hear beat request
                    send_heart_beat(logger, client_conn)
                elif request.HasField("display_key_value"):
                    # response a display request
                    print_key_value_store(logger)
                else:
                    logger.warn("Invalid Request Type...")
                    logger.info("Request Message: {0}".format(request))
            else:
                if DEBUG:
                    logger.info("No Request...")
        except socket.timeout:
            pass
        except KeyboardInterrupt as ex:
            logger.warn("You Pressed Ctrl+C")
            logger.info("Stopped {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
            run_flag = False
        except Exception as ex:
            logger.error("Error: {0}".format(ex))
            logger.info("Stopped {0}-Server at: {1}:{2}".format(replica_name, ip_addr, port_num))
            run_flag = False
        time.sleep(0.01)

    server.shutdown(socket.SHUT_RDWR)
    server.close()

    return 0


def main():
    parser = argparse.ArgumentParser(description="Replica-Server", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("name", type=str, help="name of replica server")
    parser.add_argument("port", type=int, help="port number of replica server")

    args = parser.parse_args()
    port_num = args.port
    # port_num = 9090
    logger = log.get_logger("Replica-Server-{0}".format(port_num))

    try:
        run_server(logger, args)
    except Exception as ex:
        logger.error("Error: {0}".format(ex))

    return 0


if __name__ == '__main__':
    main()
