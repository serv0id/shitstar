# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from protos.v2 import widget_pb2 as v2_dot_widget__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ev2/error.proto\x12\x02v2\x1a\x19google/protobuf/any.proto\x1a\x0fv2/widget.proto\"\x85\x01\n\x05\x45rror\x12\x12\n\nerror_code\x18\x01 \x01(\t\x12\x15\n\rerror_message\x18\x02 \x01(\t\x12&\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyB\x02\x18\x01\x12)\n\x0ewidget_wrapper\x18\x04 \x01(\x0b\x32\x11.v2.WidgetWrapperB@\n\x16\x63om.hotstar.bff.api.v2P\x01Z$github.com/hotstar/hs-core-api-go/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.error_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026com.hotstar.bff.api.v2P\001Z$github.com/hotstar/hs-core-api-go/v2'
  _ERROR.fields_by_name['data']._options = None
  _ERROR.fields_by_name['data']._serialized_options = b'\030\001'
  _globals['_ERROR']._serialized_start=67
  _globals['_ERROR']._serialized_end=200
# @@protoc_insertion_point(module_scope)
