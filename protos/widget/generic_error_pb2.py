# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/generic_error.proto
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
    'widget/generic_error.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1awidget/generic_error.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\xe5\x02\n\x12GenericErrorWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12#\n\x05image\x18\x0b \x01(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x0c \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\r \x01(\t\x12\x39\n\x0eprimary_button\x18\x0e \x01(\x0b\x32!.widget.GenericErrorWidget.Button\x12.\n\x10on_shown_actions\x18\x0f \x03(\x0b\x32\x14.base.Actions.Action\x12\x30\n\x12on_dismiss_actions\x18\x10 \x03(\x0b\x32\x14.base.Actions.Action\x1a\x36\n\x06\x42utton\x12\r\n\x05label\x18\x01 \x01(\t\x12\x1d\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\r.base.ActionsJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.generic_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_GENERICERRORWIDGET']._serialized_start=113
  _globals['_GENERICERRORWIDGET']._serialized_end=470
  _globals['_GENERICERRORWIDGET_BUTTON']._serialized_start=410
  _globals['_GENERICERRORWIDGET_BUTTON']._serialized_end=464
# @@protoc_insertion_point(module_scope)
