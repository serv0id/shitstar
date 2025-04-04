# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: composable/elements/tags_fixed.proto
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
    'composable/elements/tags_fixed.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.accessibility import accessibility_pb2 as feature_dot_accessibility_dot_accessibility__pb2
from composable.base import commons_pb2 as composable_dot_base_dot_commons__pb2
from composable.elements import composable_pb2 as composable_dot_elements_dot_composable__pb2
from composable.elements import icon_pb2 as composable_dot_elements_dot_icon__pb2
from composable.tokens import dls_tokens_pb2 as composable_dot_tokens_dot_dls__tokens__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$composable/elements/tags_fixed.proto\x12\ncomposable\x1a)feature/accessibility/accessibility.proto\x1a\x1d\x63omposable/base/commons.proto\x1a$composable/elements/composable.proto\x1a\x1e\x63omposable/elements/icon.proto\x1a\"composable/tokens/dls_tokens.proto\"\x92\x01\n\tTagsFixed\x12\x39\n\x12\x63omposable_commons\x18\x01 \x01(\x0b\x32\x1d.composable.ComposableCommons\x12\"\n\x04view\x18\x02 \x01(\x0b\x32\x14.composable.TagsView\x12&\n\x06prefix\x18\x03 \x01(\x0b\x32\x16.composable.Composable\"\xc4\x01\n\x08TagsView\x12%\n\x05items\x18\x01 \x03(\x0b\x32\x16.composable.Composable\x12#\n\tseparator\x18\x02 \x01(\x0b\x32\x10.composable.Icon\x12/\n\x07spacing\x18\x03 \x01(\x0e\x32\x1e.composable.tokens.DLSSpacings\x12;\n\raccessibility\x18\x04 \x01(\x0b\x32$.feature.accessibility.AccessibilityB`\n\x1f\x63om.hotstar.ui.model.composableP\x01Z;github.com/hotstar/hs-core-ui-models-go/composable/elementsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'composable.elements.tags_fixed_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.hotstar.ui.model.composableP\001Z;github.com/hotstar/hs-core-ui-models-go/composable/elements'
  _globals['_TAGSFIXED']._serialized_start=233
  _globals['_TAGSFIXED']._serialized_end=379
  _globals['_TAGSVIEW']._serialized_start=382
  _globals['_TAGSVIEW']._serialized_end=578
# @@protoc_insertion_point(module_scope)
