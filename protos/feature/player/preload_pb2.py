# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/player/preload.proto
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
    'feature/player/preload.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66\x65\x61ture/player/preload.proto\x12\x0e\x66\x65\x61ture.player\"\xb0\x04\n\rPreloadConfig\x12\x1f\n\x13trigger_position_ms\x18\x01 \x01(\rB\x02\x18\x01\x12?\n\rpreload_items\x18\x02 \x03(\x0b\x32(.feature.player.PreloadConfig.ConfigItem\x12\x1a\n\x12milisecs_remaining\x18\x03 \x01(\r\x12\x11\n\twifi_only\x18\x04 \x01(\x08\x12\x1e\n\x16\x65xpiration_duration_ms\x18\x05 \x01(\r\x1a\xed\x02\n\nConfigItem\x12#\n\x1bmultiplayer_preload_enabled\x18\x01 \x01(\x08\x12 \n\x18manifest_preload_enabled\x18\x02 \x01(\x08\x12\x1c\n\x14proxy_server_enabled\x18\x03 \x01(\x08\x12\x34\n\napi_params\x18\x04 \x01(\x0b\x32 .feature.player.PreloadApiParams\x12\x44\n\x12multiplayer_params\x18\x05 \x01(\x0b\x32(.feature.player.PreloadMultiPlayerParams\x12>\n\x0fmanifest_params\x18\x06 \x01(\x0b\x32%.feature.player.PreloadManifestParams\x12>\n\x13proxy_server_config\x18\x07 \x01(\x0b\x32!.feature.player.ProxyServerConfig\"}\n\x10PreloadApiParams\x12\x10\n\x08\x65ndpoint\x18\x01 \x01(\t\x12\x36\n\x04type\x18\x02 \x01(\x0e\x32(.feature.player.PreloadApiParams.ApiType\"\x1f\n\x07\x41piType\x12\x0c\n\x08page_bff\x10\x00\x12\x06\n\x02PC\x10\x01\"7\n\x18PreloadMultiPlayerParams\x12\x1b\n\x13preload_duration_ms\x18\x01 \x01(\r\"\x17\n\x15PreloadManifestParams\"\x13\n\x11ProxyServerConfigB_\n#com.hotstar.ui.model.feature.playerP\x01Z6github.com/hotstar/hs-core-ui-models-go/feature/playerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.player.preload_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.hotstar.ui.model.feature.playerP\001Z6github.com/hotstar/hs-core-ui-models-go/feature/player'
  _globals['_PRELOADCONFIG'].fields_by_name['trigger_position_ms']._loaded_options = None
  _globals['_PRELOADCONFIG'].fields_by_name['trigger_position_ms']._serialized_options = b'\030\001'
  _globals['_PRELOADCONFIG']._serialized_start=49
  _globals['_PRELOADCONFIG']._serialized_end=609
  _globals['_PRELOADCONFIG_CONFIGITEM']._serialized_start=244
  _globals['_PRELOADCONFIG_CONFIGITEM']._serialized_end=609
  _globals['_PRELOADAPIPARAMS']._serialized_start=611
  _globals['_PRELOADAPIPARAMS']._serialized_end=736
  _globals['_PRELOADAPIPARAMS_APITYPE']._serialized_start=705
  _globals['_PRELOADAPIPARAMS_APITYPE']._serialized_end=736
  _globals['_PRELOADMULTIPLAYERPARAMS']._serialized_start=738
  _globals['_PRELOADMULTIPLAYERPARAMS']._serialized_end=793
  _globals['_PRELOADMANIFESTPARAMS']._serialized_start=795
  _globals['_PRELOADMANIFESTPARAMS']._serialized_end=818
  _globals['_PROXYSERVERCONFIG']._serialized_start=820
  _globals['_PROXYSERVERCONFIG']._serialized_end=839
# @@protoc_insertion_point(module_scope)
