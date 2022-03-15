# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v3lock.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from etcetra.grpc_api import gogo_pb2 as gogo__pb2
from etcetra.grpc_api import rpc_pb2 as rpc__pb2
from etcetra.grpc_api import annotations_pb2 as annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cv3lock.proto\x12\x08v3lockpb\x1a\ngogo.proto\x1a\trpc.proto\x1a\x11\x61nnotations.proto\"*\n\x0bLockRequest\x12\x0c\n\x04name\x18\x01 \x01(\x0c\x12\r\n\x05lease\x18\x02 \x01(\x03\"I\n\x0cLockResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader\x12\x0b\n\x03key\x18\x02 \x01(\x0c\"\x1c\n\rUnlockRequest\x12\x0b\n\x03key\x18\x01 \x01(\x0c\">\n\x0eUnlockResponse\x12,\n\x06header\x18\x01 \x01(\x0b\x32\x1c.etcdserverpb.ResponseHeader2\xb0\x01\n\x04Lock\x12O\n\x04Lock\x12\x15.v3lockpb.LockRequest\x1a\x16.v3lockpb.LockResponse\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v3/lock/lock:\x01*\x12W\n\x06Unlock\x12\x17.v3lockpb.UnlockRequest\x1a\x18.v3lockpb.UnlockResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v3/lock/unlock:\x01*B\x08\xc8\xe2\x1e\x01\xd0\xe2\x1e\x01\x62\x06proto3')



_LOCKREQUEST = DESCRIPTOR.message_types_by_name['LockRequest']
_LOCKRESPONSE = DESCRIPTOR.message_types_by_name['LockResponse']
_UNLOCKREQUEST = DESCRIPTOR.message_types_by_name['UnlockRequest']
_UNLOCKRESPONSE = DESCRIPTOR.message_types_by_name['UnlockResponse']
LockRequest = _reflection.GeneratedProtocolMessageType('LockRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOCKREQUEST,
  '__module__' : 'v3lock_pb2'
  # @@protoc_insertion_point(class_scope:v3lockpb.LockRequest)
  })
_sym_db.RegisterMessage(LockRequest)

LockResponse = _reflection.GeneratedProtocolMessageType('LockResponse', (_message.Message,), {
  'DESCRIPTOR' : _LOCKRESPONSE,
  '__module__' : 'v3lock_pb2'
  # @@protoc_insertion_point(class_scope:v3lockpb.LockResponse)
  })
_sym_db.RegisterMessage(LockResponse)

UnlockRequest = _reflection.GeneratedProtocolMessageType('UnlockRequest', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKREQUEST,
  '__module__' : 'v3lock_pb2'
  # @@protoc_insertion_point(class_scope:v3lockpb.UnlockRequest)
  })
_sym_db.RegisterMessage(UnlockRequest)

UnlockResponse = _reflection.GeneratedProtocolMessageType('UnlockResponse', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKRESPONSE,
  '__module__' : 'v3lock_pb2'
  # @@protoc_insertion_point(class_scope:v3lockpb.UnlockResponse)
  })
_sym_db.RegisterMessage(UnlockResponse)

_LOCK = DESCRIPTOR.services_by_name['Lock']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\310\342\036\001\320\342\036\001'
  _LOCK.methods_by_name['Lock']._options = None
  _LOCK.methods_by_name['Lock']._serialized_options = b'\202\323\344\223\002\022\"\r/v3/lock/lock:\001*'
  _LOCK.methods_by_name['Unlock']._options = None
  _LOCK.methods_by_name['Unlock']._serialized_options = b'\202\323\344\223\002\024\"\017/v3/lock/unlock:\001*'
  _LOCKREQUEST._serialized_start=68
  _LOCKREQUEST._serialized_end=110
  _LOCKRESPONSE._serialized_start=112
  _LOCKRESPONSE._serialized_end=185
  _UNLOCKREQUEST._serialized_start=187
  _UNLOCKREQUEST._serialized_end=215
  _UNLOCKRESPONSE._serialized_start=217
  _UNLOCKRESPONSE._serialized_end=279
  _LOCK._serialized_start=282
  _LOCK._serialized_end=458
# @@protoc_insertion_point(module_scope)