# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/hero_backdrop.proto
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
    'widget/hero_backdrop.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.animation import video_animation_pb2 as feature_dot_animation_dot_video__animation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1awidget/hero_backdrop.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\'feature/animation/video_animation.proto\"\xc9\x02\n\x12HeroBackdropWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12-\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1f.widget.HeroBackdropWidget.Data\x1a\xca\x01\n\x04\x44\x61ta\x12*\n\x0c\x62\x61\x63kdrop_img\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12*\n\x0ctitle_cutout\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x35\n\nhero_video\x18\x03 \x01(\x0b\x32!.feature.animation.VideoAnimation\x12\x33\n\x15\x66\x61llback_backdrop_img\x18\x04 \x01(\x0b\x32\x14.feature.image.ImageJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.hero_backdrop_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_HEROBACKDROPWIDGET']._serialized_start=134
  _globals['_HEROBACKDROPWIDGET']._serialized_end=463
  _globals['_HEROBACKDROPWIDGET_DATA']._serialized_start=249
  _globals['_HEROBACKDROPWIDGET_DATA']._serialized_end=451
# @@protoc_insertion_point(module_scope)
