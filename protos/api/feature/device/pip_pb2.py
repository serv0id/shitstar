# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/feature/device/pip.proto
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
    'api/feature/device/pip.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/feature/device/pip.proto\x12\x12\x61pi.feature.device\"w\n\x07PipInfo\x12\x33\n\x0bplayer_type\x18\x01 \x01(\x0e\x32\x1e.api.feature.device.PlayerType\x12\x37\n\rplayer_status\x18\x02 \x01(\x0e\x32 .api.feature.device.PlayerStatus\"\x7f\n\tPipInfoV2\x12\x36\n\x0eplayer_type_v2\x18\x01 \x01(\x0e\x32\x1e.api.feature.device.PlayerType\x12:\n\x10player_status_v2\x18\x02 \x01(\x0e\x32 .api.feature.device.PlayerStatus*y\n\nPlayerType\x12\x1b\n\x17PLAYER_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16PLAYER_TYPE_IN_APP_PIP\x10\x01\x12\x16\n\x12PLAYER_TYPE_NORMAL\x10\x02\x12\x1a\n\x16PLAYER_TYPE_NOT_ACTIVE\x10\x03*\x7f\n\x0cPlayerStatus\x12\x1d\n\x19PLAYER_STATUS_UNSPECIFIED\x10\x00\x12\x1b\n\x17PLAYER_STATUS_STREAMING\x10\x01\x12\x18\n\x14PLAYER_STATUS_PAUSED\x10\x02\x12\x19\n\x15PLAYER_STATUS_LOADING\x10\x03\x42w\n*com.hotstar.event.model.api.feature.deviceP\x01ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/deviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.feature.device.pip_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.hotstar.event.model.api.feature.deviceP\001ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/device'
  _globals['_PLAYERTYPE']._serialized_start=302
  _globals['_PLAYERTYPE']._serialized_end=423
  _globals['_PLAYERSTATUS']._serialized_start=425
  _globals['_PLAYERSTATUS']._serialized_end=552
  _globals['_PIPINFO']._serialized_start=52
  _globals['_PIPINFO']._serialized_end=171
  _globals['_PIPINFOV2']._serialized_start=173
  _globals['_PIPINFOV2']._serialized_end=300
# @@protoc_insertion_point(module_scope)
