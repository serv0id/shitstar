# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pagedata/two_pane_content_page.proto
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
    'pagedata/two_pane_content_page.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import page_data_commons_pb2 as base_dot_page__data__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$pagedata/two_pane_content_page.proto\x12\x08pagedata\x1a\x1c\x62\x61se/page_data_commons.proto\x1a\x12\x62\x61se/actions.proto\"\xed\x01\n\x16TwoPaneContentPageData\x12\x30\n\x11page_data_commons\x18\x01 \x01(\x0b\x32\x15.base.PageDataCommons\x12R\n\x12page_event_actions\x18\x03 \x03(\x0b\x32\x36.pagedata.TwoPaneContentPageData.PageEventActionsEntry\x1aM\n\x15PageEventActionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.base.Actions.Action:\x02\x38\x01\x42S\n\x1d\x63om.hotstar.ui.model.pagedataP\x01Z0github.com/hotstar/hs-core-ui-models-go/pagedatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pagedata.two_pane_content_page_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.hotstar.ui.model.pagedataP\001Z0github.com/hotstar/hs-core-ui-models-go/pagedata'
  _globals['_TWOPANECONTENTPAGEDATA_PAGEEVENTACTIONSENTRY']._loaded_options = None
  _globals['_TWOPANECONTENTPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_options = b'8\001'
  _globals['_TWOPANECONTENTPAGEDATA']._serialized_start=101
  _globals['_TWOPANECONTENTPAGEDATA']._serialized_end=338
  _globals['_TWOPANECONTENTPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_start=261
  _globals['_TWOPANECONTENTPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_end=338
# @@protoc_insertion_point(module_scope)
