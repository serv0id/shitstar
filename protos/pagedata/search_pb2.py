# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pagedata/search.proto
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
    'pagedata/search.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import page_data_commons_pb2 as base_dot_page__data__commons__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15pagedata/search.proto\x12\x08pagedata\x1a\x1c\x62\x61se/page_data_commons.proto\x1a\x19google/protobuf/any.proto\"\x9c\x04\n\x0eSearchPageData\x12\x30\n\x11page_data_commons\x18\x01 \x01(\x0b\x32\x15.base.PageDataCommons\x12\r\n\x05query\x18\x02 \x01(\t\x12\x35\n\x17instrumentation_context\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x10\n\x08tab_name\x18\x04 \x01(\t\x12\x30\n\x07\x66ilters\x18\x05 \x03(\x0b\x32\x1f.pagedata.SearchPageData.Filter\x12\x44\n\x11suggested_queries\x18\x06 \x03(\x0b\x32).pagedata.SearchPageData.SuggestedQueries\x12\x18\n\x10result_one_liner\x18\x07 \x01(\t\x12\x45\n\x12search_survey_info\x18\x08 \x01(\x0b\x32).pagedata.SearchPageData.SearchSurveyInfo\x1a&\n\x06\x46ilter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06values\x18\x02 \x03(\t\x1a\x41\n\x10SuggestedQueries\x12\x14\n\x0c\x64isplay_name\x18\x01 \x01(\t\x12\x17\n\x0fsuggested_query\x18\x02 \x01(\t\x1a<\n\x10SearchSurveyInfo\x12\x12\n\nwidget_url\x18\x01 \x01(\t\x12\x14\n\x0csurvey_index\x18\x02 \x01(\tBS\n\x1d\x63om.hotstar.ui.model.pagedataP\x01Z0github.com/hotstar/hs-core-ui-models-go/pagedatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pagedata.search_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.hotstar.ui.model.pagedataP\001Z0github.com/hotstar/hs-core-ui-models-go/pagedata'
  _globals['_SEARCHPAGEDATA']._serialized_start=93
  _globals['_SEARCHPAGEDATA']._serialized_end=633
  _globals['_SEARCHPAGEDATA_FILTER']._serialized_start=466
  _globals['_SEARCHPAGEDATA_FILTER']._serialized_end=504
  _globals['_SEARCHPAGEDATA_SUGGESTEDQUERIES']._serialized_start=506
  _globals['_SEARCHPAGEDATA_SUGGESTEDQUERIES']._serialized_end=571
  _globals['_SEARCHPAGEDATA_SEARCHSURVEYINFO']._serialized_start=573
  _globals['_SEARCHPAGEDATA_SEARCHSURVEYINFO']._serialized_end=633
# @@protoc_insertion_point(module_scope)
