# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/chromecast/casting_connection_state.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'client/chromecast/casting_connection_state.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0client/chromecast/casting_connection_state.proto\x12\x11\x63lient.chromecast*\xdd\x02\n\x16\x43\x61stingConnectionState\x12(\n$CASTING_CONNECTION_STATE_UNSPECIFIED\x10\x00\x12*\n&CASTING_CONNECTION_STATE_NOT_CONNECTED\x10\x01\x12$\n CASTING_CONNECTION_STATE_STARTED\x10\x02\x12)\n%CASTING_CONNECTION_STATE_START_FAILED\x10\x03\x12$\n CASTING_CONNECTION_STATE_RESUMED\x10\x04\x12*\n&CASTING_CONNECTION_STATE_RESUME_FAILED\x10\x05\x12\"\n\x1e\x43\x41STING_CONNECTION_STATE_ENDED\x10\x06\x12&\n\"CASTING_CONNECTION_STATE_SUSPENDED\x10\x07\x42u\n)com.hotstar.event.model.client.chromecastP\x01ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/chromecastb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.chromecast.casting_connection_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)com.hotstar.event.model.client.chromecastP\001ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/chromecast'
  _globals['_CASTINGCONNECTIONSTATE']._serialized_start=72
  _globals['_CASTINGCONNECTIONSTATE']._serialized_end=421
# @@protoc_insertion_point(module_scope)
