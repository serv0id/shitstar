# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: action/web_view_navigation.proto
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
    'action/web_view_navigation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.request import http_token_request_pb2 as feature_dot_request_dot_http__token__request__pb2
from feature.color import color_pb2 as feature_dot_color_dot_color__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n action/web_view_navigation.proto\x12\x06\x61\x63tion\x1a(feature/request/http_token_request.proto\x1a\x19\x66\x65\x61ture/color/color.proto\"\xb6\x01\n\x17WebViewNavigationAction\x12\x14\n\x0cweb_view_url\x18\x02 \x01(\t\x12\x0f\n\x07replace\x18\x03 \x01(\x08\x12.\n\x03jit\x18\x04 \x01(\x0b\x32!.feature.request.HttpTokenRequest\x12.\n\x10\x62\x61\x63kground_color\x18\x05 \x01(\x0b\x32\x14.feature.color.Color\x12\x14\n\x0c\x64isable_zoom\x18\x06 \x01(\x08\x42O\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.web_view_navigation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_WEBVIEWNAVIGATIONACTION']._serialized_start=114
  _globals['_WEBVIEWNAVIGATIONACTION']._serialized_end=296
# @@protoc_insertion_point(module_scope)
