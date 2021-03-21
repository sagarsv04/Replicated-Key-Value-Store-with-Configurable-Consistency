# Replicated Key-Value Store with Configurable Consistency

An implementation of the distributed key-value store for communication among different entities in the system.


Author :
============
Sagar Vishwakarma (svishwa2@binghamton.edu)

State University of New York, Binghamton


File :
============

1)	./src/key_value_store.proto          - Contains message formats for communication
2)	./src/key_value_store_pb2.py         - protoc generated message descriptors based on .proto file
4)	./src/server.py                      - Py File contains implementation of key value store with consistency
5)	./src/client.py                      - Py File contains implementation to test the server implementation
5)	./res/replica_list                   - Text file containing information of replicas


Run :
============

- Open a terminal in project directory
- Run all the replica servers            : python ./src/server.py <replica name> <port number>
- Type python ./src/server.py -h to know more about the arguments expected
- Run client request                     : python ./src/client.py <ip> <port number> <operation type> <consistency level> <key> <value>
- Type python ./src/client.py -h to know more about the arguments expected


Note :
============
- Language & Framework  : Python 3.6.12
- Generate <xyz>_pb2.py" file : Run command protoc --python_out=./ ./<xyz>.proto


Setup :
============

- Prerequisites : sudo apt-get install autoconf automake libtool curl make g++ unzip
- Download wget https://github.com/google/protobuf/releases/download/v3.6.1/protoc-3.6.1-linux-x86_64.zip
- unzip protoc-3.6.1-linux-x86_64.zip -d protoc3
- Move protoc to /usr/local/bin/ : sudo mv protoc3/bin/* /usr/local/bin/
- Move protoc3/include to /usr/local/include/ : sudo mv protoc3/include/* /usr/local/include/
- Optional: Change Owner : sudo chown $USER /usr/local/bin/protoc, sudo chown -R $USER /usr/local/include/google
- Git Clone : https://github.com/protocolbuffers/protobuf.git
- Git Checkout : git checkout 3.6.x
- Add files path : sys.path.append("./protobuf/python/")
- /protoc --python_out=/home/svishwa2/protobuf/python/ /home/svishwa2/protoc3/include/google/protobuf/descriptor.proto
