# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/languages_selection.proto
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
    'widget/languages_selection.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n widget/languages_selection.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\xd6\x05\n\x18LanguagesSelectionWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x37\n\x04meta\x18\x0b \x01(\x0b\x32%.widget.LanguagesSelectionWidget.MetaB\x02\x18\x01\x12\x35\n\x05icons\x18\x0c \x01(\x0b\x32&.widget.LanguagesSelectionWidget.Icons\x12<\n\tlanguages\x18\r \x03(\x0b\x32).widget.LanguagesSelectionWidget.Language\x12\x37\n\x06submit\x18\x0e \x01(\x0b\x32\'.widget.LanguagesSelectionWidget.Submit\x12@\n\x0bpage_header\x18\x0f \x01(\x0b\x32+.widget.LanguagesSelectionWidget.PageHeader\x1a:\n\x04Meta\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsub_title\x18\x03 \x01(\t:\x02\x18\x01\x1a-\n\x05Icons\x12\x12\n\nunselected\x18\x01 \x01(\t\x12\x10\n\x08selected\x18\x02 \x01(\t\x1ah\n\x08Language\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x13\n\x0bis_selected\x18\x03 \x01(\x08\x12\'\n\tthumbnail\x18\x04 \x01(\x0b\x32\x14.feature.image.Image\x1a\x45\n\x06Submit\x12\r\n\x05label\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1a<\n\nPageHeader\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsub_title\x18\x03 \x01(\tJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.languages_selection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_LANGUAGESSELECTIONWIDGET_META']._loaded_options = None
  _globals['_LANGUAGESSELECTIONWIDGET_META']._serialized_options = b'\030\001'
  _globals['_LANGUAGESSELECTIONWIDGET'].fields_by_name['meta']._loaded_options = None
  _globals['_LANGUAGESSELECTIONWIDGET'].fields_by_name['meta']._serialized_options = b'\030\001'
  _globals['_LANGUAGESSELECTIONWIDGET']._serialized_start=119
  _globals['_LANGUAGESSELECTIONWIDGET']._serialized_end=845
  _globals['_LANGUAGESSELECTIONWIDGET_META']._serialized_start=489
  _globals['_LANGUAGESSELECTIONWIDGET_META']._serialized_end=547
  _globals['_LANGUAGESSELECTIONWIDGET_ICONS']._serialized_start=549
  _globals['_LANGUAGESSELECTIONWIDGET_ICONS']._serialized_end=594
  _globals['_LANGUAGESSELECTIONWIDGET_LANGUAGE']._serialized_start=596
  _globals['_LANGUAGESSELECTIONWIDGET_LANGUAGE']._serialized_end=700
  _globals['_LANGUAGESSELECTIONWIDGET_SUBMIT']._serialized_start=702
  _globals['_LANGUAGESSELECTIONWIDGET_SUBMIT']._serialized_end=771
  _globals['_LANGUAGESSELECTIONWIDGET_PAGEHEADER']._serialized_start=773
  _globals['_LANGUAGESSELECTIONWIDGET_PAGEHEADER']._serialized_end=833
# @@protoc_insertion_point(module_scope)
