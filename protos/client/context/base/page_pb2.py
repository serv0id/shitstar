# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/context/base/page.proto
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
    'client/context/base/page.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from options import opts_pb2 as options_dot_opts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x63lient/context/base/page.proto\x12\x13\x63lient.context.base\x1a\x12options/opts.proto\"\x90\x02\n\x04Page\x12\x30\n\x04type\x18\x01 \x01(\x0e\x32\".client.context.base.Page.PageType\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsub_title\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\t\x12\x10\n\x08template\x18\x05 \x01(\t\"\x95\x01\n\x08PageType\x12\x19\n\x15PAGE_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12PAGE_TYPE_MY_SPACE\x10\x01\x12\x16\n\x12PAGE_TYPE_DOWNLOAD\x10\x02\x12\x13\n\x0fPAGE_TYPE_WATCH\x10\x03\x12\x14\n\x10PAGE_TYPE_SPLASH\x10\x04\x12\x13\n\x0fPAGE_TYPE_ERROR\x10\x05\x42~\n0com.hotstar.event.model.client.context.base.pageP\x01ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/context/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.context.base.page_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.hotstar.event.model.client.context.base.pageP\001ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/context/base'
  _globals['_PAGE']._serialized_start=76
  _globals['_PAGE']._serialized_end=348
  _globals['_PAGE_PAGETYPE']._serialized_start=199
  _globals['_PAGE_PAGETYPE']._serialized_end=348
# @@protoc_insertion_point(module_scope)
