# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/watch/player_manager_properties.proto
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
    'client/watch/player_manager_properties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,client/watch/player_manager_properties.proto\x12\x0c\x63lient.watch\"\xbb\x01\n\x17PlayerManagerProperties\x12\x1d\n\x15\x63reate_player_time_ms\x18\x01 \x01(\x03\x12\x1a\n\x12get_player_time_ms\x18\x02 \x01(\x03\x12\x1e\n\x16\x64\x65stroy_player_time_ms\x18\x03 \x01(\x03\x12\'\n\x1bwait_destroy_player_time_ms\x18\x04 \x01(\x08\x42\x02\x18\x01\x12\x1c\n\x14wait_destroy_time_ms\x18\x05 \x01(\x03\x42k\n$com.hotstar.event.model.client.watchP\x01ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.watch.player_manager_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.hotstar.event.model.client.watchP\001ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watch'
  _globals['_PLAYERMANAGERPROPERTIES'].fields_by_name['wait_destroy_player_time_ms']._loaded_options = None
  _globals['_PLAYERMANAGERPROPERTIES'].fields_by_name['wait_destroy_player_time_ms']._serialized_options = b'\030\001'
  _globals['_PLAYERMANAGERPROPERTIES']._serialized_start=63
  _globals['_PLAYERMANAGERPROPERTIES']._serialized_end=250
# @@protoc_insertion_point(module_scope)
