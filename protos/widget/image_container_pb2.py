# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/image_container.proto
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
    'widget/image_container.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cwidget/image_container.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\x9d\x03\n\x14ImageContainerWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.ImageContainerWidget.Data\x1a\x41\n\x04\x44\x61ta\x12\x39\n\tthumbnail\x18\x01 \x01(\x0b\x32&.widget.ImageContainerWidget.Thumbnail\x1a\x8f\x01\n\tThumbnail\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x31\n\x05shape\x18\x02 \x01(\x0e\x32\".widget.ImageContainerWidget.Shape\x12*\n\x0ctablet_image\x18\x03 \x01(\x0b\x32\x14.feature.image.Image\"&\n\x05Shape\x12\x0f\n\x0bRECTANGULAR\x10\x00\x12\x0c\n\x08\x43IRCULAR\x10\x01J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.image_container_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_IMAGECONTAINERWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_IMAGECONTAINERWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_IMAGECONTAINERWIDGET']._serialized_start=116
  _globals['_IMAGECONTAINERWIDGET']._serialized_end=529
  _globals['_IMAGECONTAINERWIDGET_DATA']._serialized_start=272
  _globals['_IMAGECONTAINERWIDGET_DATA']._serialized_end=337
  _globals['_IMAGECONTAINERWIDGET_THUMBNAIL']._serialized_start=340
  _globals['_IMAGECONTAINERWIDGET_THUMBNAIL']._serialized_end=483
  _globals['_IMAGECONTAINERWIDGET_SHAPE']._serialized_start=485
  _globals['_IMAGECONTAINERWIDGET_SHAPE']._serialized_end=523
# @@protoc_insertion_point(module_scope)
