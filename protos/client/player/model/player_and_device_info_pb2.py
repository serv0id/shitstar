# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/player/model/player_and_device_info.proto
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
    'client/player/model/player_and_device_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.player.model import client_capabilities_pb2 as client_dot_player_dot_model_dot_client__capabilities__pb2
from client.player.model import drm_parameters_pb2 as client_dot_player_dot_model_dot_drm__parameters__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0client/player/model/player_and_device_info.proto\x12\x13\x63lient.player.model\x1a-client/player/model/client_capabilities.proto\x1a(client/player/model/drm_parameters.proto\"\x8e\x05\n\x13PlayerAndDeviceInfo\x12\x44\n\x13\x63lient_capabilities\x18\x01 \x01(\x0b\x32\'.client.player.model.ClientCapabilities\x12:\n\x0e\x64rm_parameters\x18\x02 \x01(\x0b\x32\".client.player.model.DrmParameters\x12H\n\x0bplayer_name\x18\x03 \x01(\x0e\x32\x33.client.player.model.PlayerAndDeviceInfo.PlayerName\x12\x16\n\x0eplayer_version\x18\x04 \x01(\t\x12\x1a\n\x12widevine_system_id\x18\x05 \x01(\t\x12\x43\n\x17widevine_security_level\x18\x06 \x01(\x0e\x32\".client.player.model.WidevineLevel\x12\x10\n\x08\x64\x65\x63oders\x18\x07 \x03(\t\x12\x45\n\x18playready_security_level\x18\x08 \x01(\x0e\x32#.client.player.model.PlayreadyLevel\"\xd8\x01\n\nPlayerName\x12\x1b\n\x17PLAYER_NAME_UNSPECIFIED\x10\x00\x12\"\n\x1ePLAYER_NAME_HSPLAYER_EXOPLAYER\x10\x01\x12!\n\x1dPLAYER_NAME_HSPLAYER_AVPLAYER\x10\x02\x12\x1e\n\x1aPLAYER_NAME_HSPLAYER_SHAKA\x10\x03\x12#\n\x1fPLAYER_NAME_HSPLAYER_TILEDMEDIA\x10\x04\x12!\n\x1dPLAYER_NAME_MULTICAST_LIVE_TV\x10\x05*t\n\rWidevineLevel\x12\x1e\n\x1aWIDEVINE_LEVEL_UNSPECIFIED\x10\x00\x12\x15\n\x11WIDEVINE_LEVEL_L1\x10\x01\x12\x15\n\x11WIDEVINE_LEVEL_L2\x10\x02\x12\x15\n\x11WIDEVINE_LEVEL_L3\x10\x03*\x84\x01\n\x0ePlayreadyLevel\x12\x1f\n\x1bPLAYREADY_LEVEL_UNSPECIFIED\x10\x00\x12\x19\n\x15PLAYREADY_LEVEL_SL150\x10\x01\x12\x1a\n\x16PLAYREADY_LEVEL_SL2000\x10\x02\x12\x1a\n\x16PLAYREADY_LEVEL_SL3000\x10\x03\x42y\n+com.hotstar.event.model.client.player.modelP\x01ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/player/modelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.player.model.player_and_device_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n+com.hotstar.event.model.client.player.modelP\001ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/player/model'
  _globals['_WIDEVINELEVEL']._serialized_start=819
  _globals['_WIDEVINELEVEL']._serialized_end=935
  _globals['_PLAYREADYLEVEL']._serialized_start=938
  _globals['_PLAYREADYLEVEL']._serialized_end=1070
  _globals['_PLAYERANDDEVICEINFO']._serialized_start=163
  _globals['_PLAYERANDDEVICEINFO']._serialized_end=817
  _globals['_PLAYERANDDEVICEINFO_PLAYERNAME']._serialized_start=601
  _globals['_PLAYERANDDEVICEINFO_PLAYERNAME']._serialized_end=817
# @@protoc_insertion_point(module_scope)
