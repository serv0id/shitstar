# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: composable/elements/media.proto
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
    'composable/elements/media.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.accessibility import accessibility_pb2 as feature_dot_accessibility_dot_accessibility__pb2
from composable.base import commons_pb2 as composable_dot_base_dot_commons__pb2
from composable.elements import composable_pb2 as composable_dot_elements_dot_composable__pb2
from base import actions_pb2 as base_dot_actions__pb2
from composable.base import layout_traits_pb2 as composable_dot_base_dot_layout__traits__pb2
from composable.base import corner_radius_pb2 as composable_dot_base_dot_corner__radius__pb2
from composable.elements import image_pb2 as composable_dot_elements_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63omposable/elements/media.proto\x12\ncomposable\x1a)feature/accessibility/accessibility.proto\x1a\x1d\x63omposable/base/commons.proto\x1a$composable/elements/composable.proto\x1a\x12\x62\x61se/actions.proto\x1a#composable/base/layout_traits.proto\x1a#composable/base/corner_radius.proto\x1a\x1f\x63omposable/elements/image.proto\"\xc8\x04\n\x05Media\x12%\n\x03src\x18\x01 \x01(\x0b\x32\x18.composable.Media.Source\x12;\n\raccessibility\x18\x02 \x01(\x0b\x32$.feature.accessibility.Accessibility\x12-\n\x0c\x61spect_ratio\x18\x03 \x01(\x0e\x32\x17.composable.AspectRatio\x12(\n\x0cmedia_height\x18\x04 \x01(\x0b\x32\x12.composable.Layout\x12\x30\n\x0bmedia_width\x18\x05 \x01(\x0b\x32\x1b.composable.LayoutFillFixed\x12&\n\x06height\x18\x06 \x01(\x0b\x32\x12.composable.HeightB\x02\x18\x01\x12$\n\x05width\x18\x07 \x01(\x0b\x32\x11.composable.WidthB\x02\x18\x01\x12+\n\x0bplaceholder\x18\x08 \x01(\x0b\x32\x16.composable.Composable\x12/\n\rcorner_radius\x18\t \x01(\x0b\x32\x18.composable.CornerRadius\x12\x39\n\x12\x63omposable_commons\x18\n \x01(\x0b\x32\x1d.composable.ComposableCommons\x12\x1e\n\x07\x61\x63tions\x18\x0b \x01(\x0b\x32\r.base.Actions\x1aI\n\x06Source\x12\x18\n\x10\x66\x61llbackImageUrl\x18\x03 \x01(\t\x12\r\n\x03url\x18\x01 \x01(\tH\x00\x12\x0e\n\x04name\x18\x02 \x01(\tH\x00\x42\x06\n\x04\x64\x61taB`\n\x1f\x63om.hotstar.ui.model.composableP\x01Z;github.com/hotstar/hs-core-ui-models-go/composable/elementsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'composable.elements.media_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.hotstar.ui.model.composableP\001Z;github.com/hotstar/hs-core-ui-models-go/composable/elements'
  _globals['_MEDIA'].fields_by_name['height']._loaded_options = None
  _globals['_MEDIA'].fields_by_name['height']._serialized_options = b'\030\001'
  _globals['_MEDIA'].fields_by_name['width']._loaded_options = None
  _globals['_MEDIA'].fields_by_name['width']._serialized_options = b'\030\001'
  _globals['_MEDIA']._serialized_start=287
  _globals['_MEDIA']._serialized_end=871
  _globals['_MEDIA_SOURCE']._serialized_start=798
  _globals['_MEDIA_SOURCE']._serialized_end=871
# @@protoc_insertion_point(module_scope)
