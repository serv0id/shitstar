# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: composable/base/border.proto
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
    'composable/base/border.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from composable.tokens import dls_tokens_pb2 as composable_dot_tokens_dot_dls__tokens__pb2
from feature.color import color_pb2 as feature_dot_color_dot_color__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63omposable/base/border.proto\x12\ncomposable\x1a\"composable/tokens/dls_tokens.proto\x1a\x19\x66\x65\x61ture/color/color.proto\"_\n\x06\x42order\x12\x30\n\x05width\x18\x01 \x01(\x0e\x32!.composable.tokens.DLSBorderWidth\x12#\n\x05\x63olor\x18\x02 \x01(\x0b\x32\x14.feature.color.ColorB\\\n\x1f\x63om.hotstar.ui.model.composableP\x01Z7github.com/hotstar/hs-core-ui-models-go/composable/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'composable.base.border_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.hotstar.ui.model.composableP\001Z7github.com/hotstar/hs-core-ui-models-go/composable/base'
  _globals['_BORDER']._serialized_start=107
  _globals['_BORDER']._serialized_end=202
# @@protoc_insertion_point(module_scope)
