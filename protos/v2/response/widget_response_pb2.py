# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v2/response/widget_response.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.v2 import widget_pb2 as v2_dot_widget__pb2
from protos.v2 import error_pb2 as v2_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!v2/response/widget_response.proto\x12\x0bv2.response\x1a\x0fv2/widget.proto\x1a\x0ev2/error.proto\"\x96\x01\n\x0eWidgetResponse\x12\x34\n\x07success\x18\x01 \x01(\x0b\x32#.v2.response.WidgetResponse.Success\x12\x18\n\x05\x65rror\x18\x02 \x01(\x0b\x32\t.v2.Error\x1a\x34\n\x07Success\x12)\n\x0ewidget_wrapper\x18\x01 \x01(\x0b\x32\x11.v2.WidgetWrapperBR\n\x1f\x63om.hotstar.bff.api.v2.responseP\x01Z-github.com/hotstar/hs-core-api-go/v2/responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.response.widget_response_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037com.hotstar.bff.api.v2.responseP\001Z-github.com/hotstar/hs-core-api-go/v2/response'
  _globals['_WIDGETRESPONSE']._serialized_start=84
  _globals['_WIDGETRESPONSE']._serialized_end=234
  _globals['_WIDGETRESPONSE_SUCCESS']._serialized_start=182
  _globals['_WIDGETRESPONSE_SUCCESS']._serialized_end=234
# @@protoc_insertion_point(module_scope)