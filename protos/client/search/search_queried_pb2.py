# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/search/search_queried.proto
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
    'client/search/search_queried.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"client/search/search_queried.proto\x12\rclient.search\"\xc9\x01\n\x17SearchQueriedProperties\x12\x19\n\x11search_session_id\x18\x01 \x01(\t\x12\x11\n\tsearch_id\x18\x02 \x01(\t\x12.\n\x0bquery_input\x18\x03 \x01(\x0e\x32\x19.client.search.QueryInput\x12\x12\n\nquery_text\x18\x04 \x01(\t\x12<\n\x12referrer_interface\x18\x05 \x01(\x0e\x32 .client.search.ReferrerInterface*\xd6\x01\n\nQueryInput\x12\x1b\n\x17QUERY_INPUT_UNSPECIFIED\x10\x00\x12\x14\n\x10QUERY_INPUT_TYPE\x10\x01\x12\x15\n\x11QUERY_INPUT_VOICE\x10\x02\x12\x16\n\x12QUERY_INPUT_FILTER\x10\x03\x12\x14\n\x10QUERY_INPUT_TEXT\x10\x04\x12\x1a\n\x16QUERY_INPUT_TAB_CHANGE\x10\x05\x12\x16\n\x12QUERY_INPUT_GLOBAL\x10\x06\x12\x1c\n\x18QUERY_INPUT_VOICE_REMOTE\x10\x07*\xb4\x03\n\x11ReferrerInterface\x12\"\n\x1eREFERRER_INTERFACE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aREFERRER_INTERFACE_HISTORY\x10\x01\x12\x1f\n\x1bREFERRER_INTERFACE_TRENDING\x10\x02\x12!\n\x1dREFERRER_INTERFACE_USER_INPUT\x10\x03\x12\x1f\n\x1bREFERRER_INTERFACE_TV_SHOWS\x10\x04\x12\x1d\n\x19REFERRER_INTERFACE_MOVIES\x10\x05\x12%\n!REFERRER_INTERFACE_RELATED_SEARCH\x10\x06\x12 \n\x1cREFERRER_INTERFACE_TYPEAHEAD\x10\x07\x12\x1d\n\x19REFERRER_INTERFACE_FILTER\x10\x08\x12(\n$REFERRER_INTERFACE_USER_INPUT_GLOBAL\x10\t\x12#\n\x1fREFERRER_INTERFACE_AUTO_SUGGEST\x10\n\x12 \n\x1cREFERRER_INTERFACE_HINT_TEXT\x10\x0b\x42m\n%com.hotstar.event.model.client.searchP\x01ZBgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/searchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.search.search_queried_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%com.hotstar.event.model.client.searchP\001ZBgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/search'
  _globals['_QUERYINPUT']._serialized_start=258
  _globals['_QUERYINPUT']._serialized_end=472
  _globals['_REFERRERINTERFACE']._serialized_start=475
  _globals['_REFERRERINTERFACE']._serialized_end=911
  _globals['_SEARCHQUERIEDPROPERTIES']._serialized_start=54
  _globals['_SEARCHQUERIEDPROPERTIES']._serialized_end=255
# @@protoc_insertion_point(module_scope)
