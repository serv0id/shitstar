# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/preload/preload_journey.proto
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
    'client/preload/preload_journey.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$client/preload/preload_journey.proto\x12\x0e\x63lient.preload\"w\n\x0fPreloadAddition\x12\x35\n\x0epreload_source\x18\x01 \x01(\x0b\x32\x1d.client.preload.PreloadSource\x12-\n\x06status\x18\x02 \x01(\x0e\x32\x1d.client.preload.PreloadStatus\"\xfe\x03\n\rPreloadSource\x12P\n\x13preload_source_type\x18\x03 \x01(\x0e\x32/.client.preload.PreloadSource.PreloadSourceTypeB\x02\x18\x01\x12H\n\x0f\x62\x66\x66_source_type\x18\x04 \x01(\x0e\x32/.client.preload.PreloadSource.PreloadSourceType\x12\x38\n\x07network\x18\x01 \x01(\x0b\x32%.client.preload.PreloadSource.NetworkH\x00\x12\x34\n\x05\x63\x61\x63he\x18\x02 \x01(\x0b\x32#.client.preload.PreloadSource.CacheH\x00\x1a\t\n\x07Network\x1aM\n\x05\x43\x61\x63he\x12\x16\n\nidentifier\x18\x01 \x01(\tB\x02\x18\x01\x12\x12\n\x06target\x18\x02 \x01(\tB\x02\x18\x01\x12\x18\n\x10\x63\x61\x63he_identifier\x18\x03 \x01(\t\"x\n\x11PreloadSourceType\x12#\n\x1fPRELOAD_SOURCE_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bPRELOAD_SOURCE_TYPE_NETWORK\x10\x01\x12\x1d\n\x19PRELOAD_SOURCE_TYPE_CACHE\x10\x02\x42\r\n\x0b\x64\x61ta_source\"\xf5\x05\n\x18PreloadJourneyProperties\x12=\n\x05stage\x18\x01 \x01(\x0e\x32..client.preload.PreloadJourneyProperties.Stage\x12\x42\n\x08\x61pi_type\x18\x02 \x01(\x0e\x32\x30.client.preload.PreloadJourneyProperties.ApiType\x12?\n\x06status\x18\x03 \x01(\x0e\x32/.client.preload.PreloadJourneyProperties.Status\x12N\n\x0e\x66\x61ilure_reason\x18\x04 \x01(\x0e\x32\x36.client.preload.PreloadJourneyProperties.FailureReason\x12\x1a\n\x12preload_session_id\x18\x05 \x01(\t\x12\x0b\n\x03url\x18\x06 \x01(\t\"z\n\x05Stage\x12\x15\n\x11STAGE_UNSPECIFIED\x10\x00\x12\x12\n\x0eSTAGE_RECEIVED\x10\x01\x12\x0f\n\x0bSTAGE_START\x10\x02\x12\x10\n\x0cSTAGE_FINISH\x10\x03\x12\x11\n\rSTAGE_CONSUME\x10\x04\x12\x10\n\x0cSTAGE_FAILED\x10\x05\"S\n\x07\x41piType\x12\x18\n\x14\x41PI_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x41PI_TYPE_PAGE_BFF\x10\x01\x12\x17\n\x13\x41PI_TYPE_WIDGET_BFF\x10\x02\"^\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x14\n\x10STATUS_TRIGGERED\x10\x01\x12\x12\n\x0eSTATUS_SUCCESS\x10\x02\x12\x12\n\x0eSTATUS_FAILURE\x10\x03\"g\n\rFailureReason\x12\x1e\n\x1a\x46\x41ILURE_REASON_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x46\x41ILURE_REASON_API_FAILED\x10\x01\x12\x17\n\x13\x46\x41ILURE_REASON_NONE\x10\x02:\x02\x18\x00*\xc8\x01\n\rPreloadStatus\x12\x1e\n\x1aPRELOAD_STATUS_UNSPECIFIED\x10\x00\x12\x1d\n\x19PRELOAD_STATUS_NO_PRELOAD\x10\x01\x12\x16\n\x12PRELOAD_STATUS_BFF\x10\x02\x12\x1b\n\x17PRELOAD_STATUS_MANIFEST\x10\x03\x12 \n\x1cPRELOAD_STATUS_VIDEO_SEGMENT\x10\x04\x12!\n\x1dPRELOAD_STATUS_NOT_APPLICABLE\x10\x05\x42o\n&com.hotstar.event.model.client.preloadP\x01ZCgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/preloadb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.preload.preload_journey_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.hotstar.event.model.client.preloadP\001ZCgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/preload'
  _globals['_PRELOADSOURCE_CACHE'].fields_by_name['identifier']._loaded_options = None
  _globals['_PRELOADSOURCE_CACHE'].fields_by_name['identifier']._serialized_options = b'\030\001'
  _globals['_PRELOADSOURCE_CACHE'].fields_by_name['target']._loaded_options = None
  _globals['_PRELOADSOURCE_CACHE'].fields_by_name['target']._serialized_options = b'\030\001'
  _globals['_PRELOADSOURCE'].fields_by_name['preload_source_type']._loaded_options = None
  _globals['_PRELOADSOURCE'].fields_by_name['preload_source_type']._serialized_options = b'\030\001'
  _globals['_PRELOADJOURNEYPROPERTIES']._loaded_options = None
  _globals['_PRELOADJOURNEYPROPERTIES']._serialized_options = b'\030\000'
  _globals['_PRELOADSTATUS']._serialized_start=1451
  _globals['_PRELOADSTATUS']._serialized_end=1651
  _globals['_PRELOADADDITION']._serialized_start=56
  _globals['_PRELOADADDITION']._serialized_end=175
  _globals['_PRELOADSOURCE']._serialized_start=178
  _globals['_PRELOADSOURCE']._serialized_end=688
  _globals['_PRELOADSOURCE_NETWORK']._serialized_start=463
  _globals['_PRELOADSOURCE_NETWORK']._serialized_end=472
  _globals['_PRELOADSOURCE_CACHE']._serialized_start=474
  _globals['_PRELOADSOURCE_CACHE']._serialized_end=551
  _globals['_PRELOADSOURCE_PRELOADSOURCETYPE']._serialized_start=553
  _globals['_PRELOADSOURCE_PRELOADSOURCETYPE']._serialized_end=673
  _globals['_PRELOADJOURNEYPROPERTIES']._serialized_start=691
  _globals['_PRELOADJOURNEYPROPERTIES']._serialized_end=1448
  _globals['_PRELOADJOURNEYPROPERTIES_STAGE']._serialized_start=1036
  _globals['_PRELOADJOURNEYPROPERTIES_STAGE']._serialized_end=1158
  _globals['_PRELOADJOURNEYPROPERTIES_APITYPE']._serialized_start=1160
  _globals['_PRELOADJOURNEYPROPERTIES_APITYPE']._serialized_end=1243
  _globals['_PRELOADJOURNEYPROPERTIES_STATUS']._serialized_start=1245
  _globals['_PRELOADJOURNEYPROPERTIES_STATUS']._serialized_end=1339
  _globals['_PRELOADJOURNEYPROPERTIES_FAILUREREASON']._serialized_start=1341
  _globals['_PRELOADJOURNEYPROPERTIES_FAILUREREASON']._serialized_end=1444
# @@protoc_insertion_point(module_scope)
