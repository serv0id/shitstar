# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: base/page_data_commons.proto
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
    'base/page_data_commons.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import analytics_pb2 as base_dot_analytics__pb2
from base import actions_pb2 as base_dot_actions__pb2
from base import cache_control_pb2 as base_dot_cache__control__pb2
from feature.app_event import app_event_pb2 as feature_dot_app__event_dot_app__event__pb2
from feature.refresh import refresh_info_pb2 as feature_dot_refresh_dot_refresh__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x62\x61se/page_data_commons.proto\x12\x04\x62\x61se\x1a\x14\x62\x61se/analytics.proto\x1a\x12\x62\x61se/actions.proto\x1a\x18\x62\x61se/cache_control.proto\x1a!feature/app_event/app_event.proto\x1a\"feature/refresh/refresh_info.proto\"\xcb\x02\n\x0fPageDataCommons\x12.\n\x0finstrumentation\x18\x01 \x01(\x0b\x32\x15.base.Instrumentation\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x32\n\rinvalidate_on\x18\x03 \x03(\x0e\x32\x1b.feature.app_event.AppEvent\x12\x17\n\x0frefresh_api_url\x18\x04 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x12\x32\n\x0crefresh_info\x18\x06 \x01(\x0b\x32\x1c.feature.refresh.RefreshInfo\x12/\n\x0c\x63\x61\x63he_config\x18\x07 \x01(\x0b\x32\x15.base.PageCacheConfigB\x02\x18\x01\x12)\n\rcache_control\x18\x08 \x01(\x0b\x32\x12.base.CacheControl\"8\n\x0fPageCacheConfig\x12\x14\n\x0cis_cacheable\x18\x02 \x01(\x08\x12\x0f\n\x07ttl_sec\x18\x03 \x01(\x03\x42K\n\x19\x63om.hotstar.ui.model.baseP\x01Z,github.com/hotstar/hs-core-ui-models-go/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.page_data_commons_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031com.hotstar.ui.model.baseP\001Z,github.com/hotstar/hs-core-ui-models-go/base'
  _globals['_PAGEDATACOMMONS'].fields_by_name['cache_config']._loaded_options = None
  _globals['_PAGEDATACOMMONS'].fields_by_name['cache_config']._serialized_options = b'\030\001'
  _globals['_PAGEDATACOMMONS']._serialized_start=178
  _globals['_PAGEDATACOMMONS']._serialized_end=509
  _globals['_PAGECACHECONFIG']._serialized_start=511
  _globals['_PAGECACHECONFIG']._serialized_end=567
# @@protoc_insertion_point(module_scope)
