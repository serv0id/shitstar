# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: component/search/search_info.proto
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
    'component/search/search_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.search import search_session_info_pb2 as client_dot_search_dot_search__session__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"component/search/search_info.proto\x12\x10\x63omponent.search\x1a\'client/search/search_session_info.proto\"\xcb\x01\n\x14SearchInfoProperties\x12\x37\n\x0einterface_type\x18\x01 \x01(\x0e\x32\x1f.component.search.InterfaceType\x12\x12\n\nquery_text\x18\x02 \x01(\t\x12\x31\n\tpage_type\x18\x03 \x01(\x0e\x32\x1a.component.search.PageTypeB\x02\x18\x01\x12\x1c\n\x10primary_language\x18\x04 \x01(\tB\x02\x18\x01\x12\x15\n\rwidget_filter\x18\x05 \x01(\t*\xec\x03\n\rInterfaceType\x12\x1e\n\x1aINTERFACE_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16INTERFACE_TYPE_HISTORY\x10\x01\x12\x1b\n\x17INTERFACE_TYPE_TRENDING\x10\x02\x12\x1d\n\x19INTERFACE_TYPE_TOP_RESULT\x10\x03\x12\x1e\n\x1aINTERFACE_TYPE_HERO_RESULT\x10\x04\x12\x1e\n\x1aINTERFACE_TYPE_MORE_RESULT\x10\x05\x12!\n\x1dINTERFACE_TYPE_RELATED_SEARCH\x10\x06\x12\x1c\n\x18INTERFACE_TYPE_TYPEAHEAD\x10\x07\x12\x1a\n\x16INTERFACE_TYPE_EXPLORE\x10\x08\x12\x1d\n\x19INTERFACE_TYPE_SCOREBOARD\x10\t\x12\x19\n\x15INTERFACE_TYPE_FILTER\x10\n\x12!\n\x1dINTERFACE_TYPE_SIMILAR_RESULT\x10\x0b\x12!\n\x1dINTERFACE_TYPE_MORE_LIKE_THIS\x10\x0c\x12$\n INTERFACE_TYPE_YOU_MAY_ALSO_LIKE\x10\r\x12 \n\x1cINTERFACE_TYPE_POPULAR_CLIPS\x10\x0e*m\n\x08PageType\x12\x19\n\x15PAGE_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11PAGE_TYPE_EXPLORE\x10\x01\x12\x14\n\x10PAGE_TYPE_SEARCH\x10\x02\x12\x19\n\x15PAGE_TYPE_SEARCH_ZERO\x10\x03\x42l\n!com.hotstar.event.model.componentP\x01ZEgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/searchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.search.search_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.event.model.componentP\001ZEgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/search'
  _globals['_SEARCHINFOPROPERTIES'].fields_by_name['page_type']._loaded_options = None
  _globals['_SEARCHINFOPROPERTIES'].fields_by_name['page_type']._serialized_options = b'\030\001'
  _globals['_SEARCHINFOPROPERTIES'].fields_by_name['primary_language']._loaded_options = None
  _globals['_SEARCHINFOPROPERTIES'].fields_by_name['primary_language']._serialized_options = b'\030\001'
  _globals['_INTERFACETYPE']._serialized_start=304
  _globals['_INTERFACETYPE']._serialized_end=796
  _globals['_PAGETYPE']._serialized_start=798
  _globals['_PAGETYPE']._serialized_end=907
  _globals['_SEARCHINFOPROPERTIES']._serialized_start=98
  _globals['_SEARCHINFOPROPERTIES']._serialized_end=301
# @@protoc_insertion_point(module_scope)
