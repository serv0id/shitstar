# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/title_bar_header.proto
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
    'widget/title_bar_header.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwidget/title_bar_header.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x12\x62\x61se/actions.proto\"\x82\x03\n\x14TitleBarHeaderWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.TitleBarHeaderWidget.Data\x1a\xbd\x01\n\x04\x44\x61ta\x12\r\n\x05title\x18\x01 \x01(\t\x12;\n\timage_btn\x18\x02 \x01(\x0b\x32(.widget.TitleBarHeaderWidget.ImageButton\x12G\n\x15trailing_image_button\x18\x03 \x01(\x0b\x32(.widget.TitleBarHeaderWidget.ImageButton\x12 \n\x18header_parallax_disabled\x18\x04 \x01(\x08\x1a@\n\x0bImageButton\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.ActionsJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.title_bar_header_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_TITLEBARHEADERWIDGET']._serialized_start=137
  _globals['_TITLEBARHEADERWIDGET']._serialized_end=523
  _globals['_TITLEBARHEADERWIDGET_DATA']._serialized_start=256
  _globals['_TITLEBARHEADERWIDGET_DATA']._serialized_end=445
  _globals['_TITLEBARHEADERWIDGET_IMAGEBUTTON']._serialized_start=447
  _globals['_TITLEBARHEADERWIDGET_IMAGEBUTTON']._serialized_end=511
# @@protoc_insertion_point(module_scope)
