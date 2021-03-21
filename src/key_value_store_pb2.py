# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: key_value_store.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='key_value_store.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x15key_value_store.proto\"b\n\nPutRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\x12\x19\n\x11\x63onsistency_level\x18\x04 \x01(\r\x12\x11\n\ttimestamp\x18\x05 \x01(\x01\"b\n\nGetRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\x12\x19\n\x11\x63onsistency_level\x18\x04 \x01(\r\x12\x11\n\ttimestamp\x18\x05 \x01(\x01\";\n\nReadRepair\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\">\n\rHintedHandoff\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\t\x12\x11\n\ttimestamp\x18\x03 \x01(\x01\"!\n\x0f\x44isplayKeyValue\x12\x0e\n\x06status\x18\x01 \x01(\x08\"^\n\x0eReplicaRequest\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\x12\x11\n\toperation\x18\x04 \x01(\r\x12\x11\n\ttimestamp\x18\x05 \x01(\x01\"\x85\x01\n\x0fReplicaResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\x08\x12\x11\n\ttimestamp\x18\x05 \x01(\x01\x12\'\n\x0ehinted_handoff\x18\x06 \x03(\x0b\x32\x0f.ReplicaRequest\"`\n\x13\x43oordinatorResponse\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\r\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\x08\x12\x11\n\ttimestamp\x18\x05 \x01(\x01\"\x1b\n\x0c\x45rrorMessage\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\x1b\n\tHeartBeat\x12\x0e\n\x06status\x18\x01 \x01(\x08\"\xc5\x03\n\x0fKeyValueMessage\x12\"\n\x0bput_request\x18\x01 \x01(\x0b\x32\x0b.PutRequestH\x00\x12\"\n\x0bget_request\x18\x02 \x01(\x0b\x32\x0b.GetRequestH\x00\x12\"\n\x0bread_repair\x18\x03 \x01(\x0b\x32\x0b.ReadRepairH\x00\x12(\n\x0ehinted_handoff\x18\x04 \x01(\x0b\x32\x0e.HintedHandoffH\x00\x12-\n\x11\x64isplay_key_value\x18\x05 \x01(\x0b\x32\x10.DisplayKeyValueH\x00\x12*\n\x0freplica_request\x18\x06 \x01(\x0b\x32\x0f.ReplicaRequestH\x00\x12,\n\x10replica_response\x18\x07 \x01(\x0b\x32\x10.ReplicaResponseH\x00\x12\x34\n\x14\x63oordinator_response\x18\x08 \x01(\x0b\x32\x14.CoordinatorResponseH\x00\x12&\n\rerror_message\x18\t \x01(\x0b\x32\r.ErrorMessageH\x00\x12 \n\nheart_beat\x18\n \x01(\x0b\x32\n.HeartBeatH\x00\x42\x13\n\x11key_value_messageb\x06proto3')
)




_PUTREQUEST = _descriptor.Descriptor(
  name='PutRequest',
  full_name='PutRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PutRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='PutRequest.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='PutRequest.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consistency_level', full_name='PutRequest.consistency_level', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='PutRequest.timestamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=123,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='GetRequest.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='GetRequest.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consistency_level', full_name='GetRequest.consistency_level', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='GetRequest.timestamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=125,
  serialized_end=223,
)


_READREPAIR = _descriptor.Descriptor(
  name='ReadRepair',
  full_name='ReadRepair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ReadRepair.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReadRepair.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReadRepair.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=225,
  serialized_end=284,
)


_HINTEDHANDOFF = _descriptor.Descriptor(
  name='HintedHandoff',
  full_name='HintedHandoff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='HintedHandoff.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='HintedHandoff.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='HintedHandoff.timestamp', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=348,
)


_DISPLAYKEYVALUE = _descriptor.Descriptor(
  name='DisplayKeyValue',
  full_name='DisplayKeyValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='DisplayKeyValue.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=350,
  serialized_end=383,
)


_REPLICAREQUEST = _descriptor.Descriptor(
  name='ReplicaRequest',
  full_name='ReplicaRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ReplicaRequest.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaRequest.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReplicaRequest.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operation', full_name='ReplicaRequest.operation', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReplicaRequest.timestamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=385,
  serialized_end=479,
)


_REPLICARESPONSE = _descriptor.Descriptor(
  name='ReplicaResponse',
  full_name='ReplicaResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ReplicaResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='ReplicaResponse.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='ReplicaResponse.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='ReplicaResponse.status', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ReplicaResponse.timestamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hinted_handoff', full_name='ReplicaResponse.hinted_handoff', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=482,
  serialized_end=615,
)


_COORDINATORRESPONSE = _descriptor.Descriptor(
  name='CoordinatorResponse',
  full_name='CoordinatorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='CoordinatorResponse.id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='key', full_name='CoordinatorResponse.key', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='CoordinatorResponse.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='CoordinatorResponse.status', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='CoordinatorResponse.timestamp', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=617,
  serialized_end=713,
)


_ERRORMESSAGE = _descriptor.Descriptor(
  name='ErrorMessage',
  full_name='ErrorMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='ErrorMessage.msg', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=715,
  serialized_end=742,
)


_HEARTBEAT = _descriptor.Descriptor(
  name='HeartBeat',
  full_name='HeartBeat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='HeartBeat.status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=744,
  serialized_end=771,
)


_KEYVALUEMESSAGE = _descriptor.Descriptor(
  name='KeyValueMessage',
  full_name='KeyValueMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='put_request', full_name='KeyValueMessage.put_request', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='get_request', full_name='KeyValueMessage.get_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='read_repair', full_name='KeyValueMessage.read_repair', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hinted_handoff', full_name='KeyValueMessage.hinted_handoff', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='display_key_value', full_name='KeyValueMessage.display_key_value', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replica_request', full_name='KeyValueMessage.replica_request', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replica_response', full_name='KeyValueMessage.replica_response', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinator_response', full_name='KeyValueMessage.coordinator_response', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='KeyValueMessage.error_message', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heart_beat', full_name='KeyValueMessage.heart_beat', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='key_value_message', full_name='KeyValueMessage.key_value_message',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=774,
  serialized_end=1227,
)

_REPLICARESPONSE.fields_by_name['hinted_handoff'].message_type = _REPLICAREQUEST
_KEYVALUEMESSAGE.fields_by_name['put_request'].message_type = _PUTREQUEST
_KEYVALUEMESSAGE.fields_by_name['get_request'].message_type = _GETREQUEST
_KEYVALUEMESSAGE.fields_by_name['read_repair'].message_type = _READREPAIR
_KEYVALUEMESSAGE.fields_by_name['hinted_handoff'].message_type = _HINTEDHANDOFF
_KEYVALUEMESSAGE.fields_by_name['display_key_value'].message_type = _DISPLAYKEYVALUE
_KEYVALUEMESSAGE.fields_by_name['replica_request'].message_type = _REPLICAREQUEST
_KEYVALUEMESSAGE.fields_by_name['replica_response'].message_type = _REPLICARESPONSE
_KEYVALUEMESSAGE.fields_by_name['coordinator_response'].message_type = _COORDINATORRESPONSE
_KEYVALUEMESSAGE.fields_by_name['error_message'].message_type = _ERRORMESSAGE
_KEYVALUEMESSAGE.fields_by_name['heart_beat'].message_type = _HEARTBEAT
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['put_request'])
_KEYVALUEMESSAGE.fields_by_name['put_request'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['get_request'])
_KEYVALUEMESSAGE.fields_by_name['get_request'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['read_repair'])
_KEYVALUEMESSAGE.fields_by_name['read_repair'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['hinted_handoff'])
_KEYVALUEMESSAGE.fields_by_name['hinted_handoff'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['display_key_value'])
_KEYVALUEMESSAGE.fields_by_name['display_key_value'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['replica_request'])
_KEYVALUEMESSAGE.fields_by_name['replica_request'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['replica_response'])
_KEYVALUEMESSAGE.fields_by_name['replica_response'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['coordinator_response'])
_KEYVALUEMESSAGE.fields_by_name['coordinator_response'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['error_message'])
_KEYVALUEMESSAGE.fields_by_name['error_message'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
_KEYVALUEMESSAGE.oneofs_by_name['key_value_message'].fields.append(
  _KEYVALUEMESSAGE.fields_by_name['heart_beat'])
_KEYVALUEMESSAGE.fields_by_name['heart_beat'].containing_oneof = _KEYVALUEMESSAGE.oneofs_by_name['key_value_message']
DESCRIPTOR.message_types_by_name['PutRequest'] = _PUTREQUEST
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['ReadRepair'] = _READREPAIR
DESCRIPTOR.message_types_by_name['HintedHandoff'] = _HINTEDHANDOFF
DESCRIPTOR.message_types_by_name['DisplayKeyValue'] = _DISPLAYKEYVALUE
DESCRIPTOR.message_types_by_name['ReplicaRequest'] = _REPLICAREQUEST
DESCRIPTOR.message_types_by_name['ReplicaResponse'] = _REPLICARESPONSE
DESCRIPTOR.message_types_by_name['CoordinatorResponse'] = _COORDINATORRESPONSE
DESCRIPTOR.message_types_by_name['ErrorMessage'] = _ERRORMESSAGE
DESCRIPTOR.message_types_by_name['HeartBeat'] = _HEARTBEAT
DESCRIPTOR.message_types_by_name['KeyValueMessage'] = _KEYVALUEMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PutRequest = _reflection.GeneratedProtocolMessageType('PutRequest', (_message.Message,), dict(
  DESCRIPTOR = _PUTREQUEST,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:PutRequest)
  ))
_sym_db.RegisterMessage(PutRequest)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

ReadRepair = _reflection.GeneratedProtocolMessageType('ReadRepair', (_message.Message,), dict(
  DESCRIPTOR = _READREPAIR,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:ReadRepair)
  ))
_sym_db.RegisterMessage(ReadRepair)

HintedHandoff = _reflection.GeneratedProtocolMessageType('HintedHandoff', (_message.Message,), dict(
  DESCRIPTOR = _HINTEDHANDOFF,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:HintedHandoff)
  ))
_sym_db.RegisterMessage(HintedHandoff)

DisplayKeyValue = _reflection.GeneratedProtocolMessageType('DisplayKeyValue', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYKEYVALUE,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:DisplayKeyValue)
  ))
_sym_db.RegisterMessage(DisplayKeyValue)

ReplicaRequest = _reflection.GeneratedProtocolMessageType('ReplicaRequest', (_message.Message,), dict(
  DESCRIPTOR = _REPLICAREQUEST,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:ReplicaRequest)
  ))
_sym_db.RegisterMessage(ReplicaRequest)

ReplicaResponse = _reflection.GeneratedProtocolMessageType('ReplicaResponse', (_message.Message,), dict(
  DESCRIPTOR = _REPLICARESPONSE,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:ReplicaResponse)
  ))
_sym_db.RegisterMessage(ReplicaResponse)

CoordinatorResponse = _reflection.GeneratedProtocolMessageType('CoordinatorResponse', (_message.Message,), dict(
  DESCRIPTOR = _COORDINATORRESPONSE,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:CoordinatorResponse)
  ))
_sym_db.RegisterMessage(CoordinatorResponse)

ErrorMessage = _reflection.GeneratedProtocolMessageType('ErrorMessage', (_message.Message,), dict(
  DESCRIPTOR = _ERRORMESSAGE,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:ErrorMessage)
  ))
_sym_db.RegisterMessage(ErrorMessage)

HeartBeat = _reflection.GeneratedProtocolMessageType('HeartBeat', (_message.Message,), dict(
  DESCRIPTOR = _HEARTBEAT,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:HeartBeat)
  ))
_sym_db.RegisterMessage(HeartBeat)

KeyValueMessage = _reflection.GeneratedProtocolMessageType('KeyValueMessage', (_message.Message,), dict(
  DESCRIPTOR = _KEYVALUEMESSAGE,
  __module__ = 'key_value_store_pb2'
  # @@protoc_insertion_point(class_scope:KeyValueMessage)
  ))
_sym_db.RegisterMessage(KeyValueMessage)


# @@protoc_insertion_point(module_scope)
