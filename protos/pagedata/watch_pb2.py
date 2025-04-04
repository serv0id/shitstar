# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pagedata/watch.proto
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
    'pagedata/watch.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import page_data_commons_pb2 as base_dot_page__data__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.watch import watch_ab_config_pb2 as feature_dot_watch_dot_watch__ab__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14pagedata/watch.proto\x12\x08pagedata\x1a\x1c\x62\x61se/page_data_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a#feature/watch/watch_ab_config.proto\"\xe1\x06\n\rWatchPageData\x12\x30\n\x11page_data_commons\x18\x01 \x01(\x0b\x32\x15.base.PageDataCommons\x12\x41\n\x0breport_data\x18\x02 \x01(\x0b\x32,.pagedata.WatchPageData.PlayerReportMenuData\x12\x30\n\x0cwatch_config\x18\x03 \x01(\x0b\x32\x1a.feature.watch.WatchConfig\x12I\n\x12page_event_actions\x18\x04 \x03(\x0b\x32-.pagedata.WatchPageData.PageEventActionsEntry\x12;\n\rplayer_config\x18\x05 \x01(\x0b\x32$.pagedata.WatchPageData.PlayerConfig\x1ak\n\x14PlayerReportMenuData\x12\r\n\x05title\x18\x01 \x01(\t\x12\x44\n\x0ereport_options\x18\x02 \x03(\x0b\x32,.pagedata.WatchPageData.PlayerReportMenuItem\x1aM\n\x15PageEventActionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.base.Actions.Action:\x02\x38\x01\x1aL\n\x0cPlayerConfig\x12\x13\n\x0b\x61v1_decoder\x18\x01 \x01(\t\x12\'\n\x1fhsdav1d_thread_count_percentage\x18\x02 \x01(\x05\x1a\x99\x01\n\x14PlayerReportMenuItem\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06result\x18\x04 \x01(\t\x12:\n\x04type\x18\x05 \x01(\x0e\x32,.pagedata.WatchPageData.PlayerReportItemType\"{\n\x14PlayerReportItemType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x18\n\x14\x42UFFERING_CONNECTION\x10\x01\x12\x11\n\rVIDEO_QUALITY\x10\x02\x12\x11\n\rAUDIO_QUALITY\x10\x03\x12\x16\n\x12SUBTITLES_CAPTIONS\x10\x04\x42S\n\x1d\x63om.hotstar.ui.model.pagedataP\x01Z0github.com/hotstar/hs-core-ui-models-go/pagedatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pagedata.watch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.hotstar.ui.model.pagedataP\001Z0github.com/hotstar/hs-core-ui-models-go/pagedata'
  _globals['_WATCHPAGEDATA_PAGEEVENTACTIONSENTRY']._loaded_options = None
  _globals['_WATCHPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_options = b'8\001'
  _globals['_WATCHPAGEDATA']._serialized_start=122
  _globals['_WATCHPAGEDATA']._serialized_end=987
  _globals['_WATCHPAGEDATA_PLAYERREPORTMENUDATA']._serialized_start=442
  _globals['_WATCHPAGEDATA_PLAYERREPORTMENUDATA']._serialized_end=549
  _globals['_WATCHPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_start=551
  _globals['_WATCHPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_end=628
  _globals['_WATCHPAGEDATA_PLAYERCONFIG']._serialized_start=630
  _globals['_WATCHPAGEDATA_PLAYERCONFIG']._serialized_end=706
  _globals['_WATCHPAGEDATA_PLAYERREPORTMENUITEM']._serialized_start=709
  _globals['_WATCHPAGEDATA_PLAYERREPORTMENUITEM']._serialized_end=862
  _globals['_WATCHPAGEDATA_PLAYERREPORTITEMTYPE']._serialized_start=864
  _globals['_WATCHPAGEDATA_PLAYERREPORTITEMTYPE']._serialized_end=987
# @@protoc_insertion_point(module_scope)
