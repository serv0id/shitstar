# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/watch/preloaded_artwork.proto
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
    'client/watch/preloaded_artwork.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$client/watch/preloaded_artwork.proto\x12\x0c\x63lient.watch\"\xfd\x04\n\x10PreloadedArtwork\x12M\n\x0e\x61rtwork_status\x18\x01 \x01(\x0e\x32\x35.client.watch.PreloadedArtwork.PreloadedArtworkStatus\x12M\n\x0e\x61rtwork_source\x18\x02 \x01(\x0e\x32\x35.client.watch.PreloadedArtwork.PreloadedArtworkSource\x12\x16\n\x0e\x64isplay_lag_ms\x18\x03 \x01(\x02\x12\x1c\n\x14video_failure_reason\x18\x04 \x01(\t\x12\x1e\n\x16\x61rtwork_failure_reason\x18\x05 \x01(\t\"\xde\x01\n\x16PreloadedArtworkStatus\x12(\n$PRELOADED_ARTWORK_STATUS_UNSPECIFIED\x10\x00\x12$\n PRELOADED_ARTWORK_STATUS_SUCCESS\x10\x01\x12#\n\x1fPRELOADED_ARTWORK_STATUS_FAILED\x10\x02\x12$\n PRELOADED_ARTWORK_STATUS_SKIPPED\x10\x03\x12)\n%PRELOADED_ARTWORK_STATUS_VIDEO_FAILED\x10\x04\"\x93\x01\n\x16PreloadedArtworkSource\x12(\n$PRELOADED_ARTWORK_SOURCE_UNSPECIFIED\x10\x00\x12&\n\"PRELOADED_ARTWORK_SOURCE_PRELOADED\x10\x01\x12\'\n#PRELOADED_ARTWORK_SOURCE_DOWNLOADED\x10\x02\x42k\n$com.hotstar.event.model.client.watchP\x01ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.watch.preloaded_artwork_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.hotstar.event.model.client.watchP\001ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watch'
  _globals['_PRELOADEDARTWORK']._serialized_start=55
  _globals['_PRELOADEDARTWORK']._serialized_end=692
  _globals['_PRELOADEDARTWORK_PRELOADEDARTWORKSTATUS']._serialized_start=320
  _globals['_PRELOADEDARTWORK_PRELOADEDARTWORKSTATUS']._serialized_end=542
  _globals['_PRELOADEDARTWORK_PRELOADEDARTWORKSOURCE']._serialized_start=545
  _globals['_PRELOADEDARTWORK_PRELOADEDARTWORKSOURCE']._serialized_end=692
# @@protoc_insertion_point(module_scope)
