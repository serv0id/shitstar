# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/list_item_v2.proto
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
    'widget/list_item_v2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.atom import button_pb2 as feature_dot_atom_dot_button__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19widget/list_item_v2.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x19\x66\x65\x61ture/atom/button.proto\"\xa8\x04\n\x10ListItemV2Widget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12+\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1d.widget.ListItemV2Widget.Data\x1ao\n\x04\x44\x61ta\x12\x34\n\rdefault_state\x18\x01 \x01(\x0b\x32\x1d.widget.ListItemV2Widget.Item\x12\x31\n\nedit_state\x18\x02 \x01(\x0b\x32\x1d.widget.ListItemV2Widget.Item\x1a\xc2\x02\n\x04Item\x12\r\n\x05title\x18\x01 \x01(\t\x12\x11\n\tsub_title\x18\x02 \x01(\t\x12>\n\x0fleading_section\x18\x03 \x01(\x0b\x32%.widget.ListItemV2Widget.Item.Section\x12?\n\x10trailing_section\x18\x04 \x01(\x0b\x32%.widget.ListItemV2Widget.Item.Section\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x1aw\n\x07Section\x12\x0e\n\x04icon\x18\x01 \x01(\tH\x00\x12%\n\x05image\x18\x02 \x01(\x0b\x32\x14.feature.image.ImageH\x00\x12&\n\x06\x62utton\x18\x03 \x01(\x0b\x32\x14.feature.atom.ButtonH\x00\x42\r\n\x0bSectionDataJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.list_item_v2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_LISTITEMV2WIDGET']._serialized_start=139
  _globals['_LISTITEMV2WIDGET']._serialized_end=691
  _globals['_LISTITEMV2WIDGET_DATA']._serialized_start=249
  _globals['_LISTITEMV2WIDGET_DATA']._serialized_end=360
  _globals['_LISTITEMV2WIDGET_ITEM']._serialized_start=363
  _globals['_LISTITEMV2WIDGET_ITEM']._serialized_end=685
  _globals['_LISTITEMV2WIDGET_ITEM_SECTION']._serialized_start=566
  _globals['_LISTITEMV2WIDGET_ITEM_SECTION']._serialized_end=685
# @@protoc_insertion_point(module_scope)
