# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/web_footer.proto
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
    'widget/web_footer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17widget/web_footer.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\xad\x08\n\x0fWebFooterWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12*\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1c.widget.WebFooterWidget.Data\x1a\xba\x07\n\x04\x44\x61ta\x12:\n\nparagraphs\x18\x01 \x03(\x0b\x32&.widget.WebFooterWidget.Data.Paragraph\x12\x34\n\x07\x63olumns\x18\x02 \x03(\x0b\x32#.widget.WebFooterWidget.Data.Column\x12\x42\n\x0esocial_handles\x18\x03 \x01(\x0b\x32*.widget.WebFooterWidget.Data.SocialHandles\x12\x31\n\x05legal\x18\x04 \x01(\x0b\x32\".widget.WebFooterWidget.Data.Legal\x12\x37\n\tapp_links\x18\x05 \x03(\x0b\x32$.widget.WebFooterWidget.Data.AppLink\x1a+\n\tParagraph\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x1a\xa4\x01\n\x06\x43olumn\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x30\n\x05links\x18\x02 \x03(\x0b\x32!.widget.WebFooterWidget.Data.Link\x12\x17\n\x0b\x63olumn_type\x18\x03 \x01(\tB\x02\x18\x01\x12?\n\x0e\x63olumn_type_v2\x18\x04 \x01(\x0e\x32\'.widget.WebFooterWidget.Data.ColumnType\x1a\xab\x01\n\rSocialHandles\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x42\n\x07handles\x18\x02 \x03(\x0b\x32\x31.widget.WebFooterWidget.Data.SocialHandles.Handle\x1a\x46\n\x06Handle\x12\x0e\n\x06handle\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1aL\n\x05Legal\x12\x11\n\tparagraph\x18\x01 \x01(\t\x12\x30\n\x05links\x18\x02 \x03(\x0b\x32!.widget.WebFooterWidget.Data.Link\x1aN\n\x07\x41ppLink\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a\x34\n\x04Link\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\":\n\nColumnType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04LINK\x10\x01\x12\x15\n\x11LANGUAGE_SELECTOR\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.web_footer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_WEBFOOTERWIDGET_DATA_COLUMN'].fields_by_name['column_type']._loaded_options = None
  _globals['_WEBFOOTERWIDGET_DATA_COLUMN'].fields_by_name['column_type']._serialized_options = b'\030\001'
  _globals['_WEBFOOTERWIDGET']._serialized_start=131
  _globals['_WEBFOOTERWIDGET']._serialized_end=1200
  _globals['_WEBFOOTERWIDGET_DATA']._serialized_start=240
  _globals['_WEBFOOTERWIDGET_DATA']._serialized_end=1194
  _globals['_WEBFOOTERWIDGET_DATA_PARAGRAPH']._serialized_start=538
  _globals['_WEBFOOTERWIDGET_DATA_PARAGRAPH']._serialized_end=581
  _globals['_WEBFOOTERWIDGET_DATA_COLUMN']._serialized_start=584
  _globals['_WEBFOOTERWIDGET_DATA_COLUMN']._serialized_end=748
  _globals['_WEBFOOTERWIDGET_DATA_SOCIALHANDLES']._serialized_start=751
  _globals['_WEBFOOTERWIDGET_DATA_SOCIALHANDLES']._serialized_end=922
  _globals['_WEBFOOTERWIDGET_DATA_SOCIALHANDLES_HANDLE']._serialized_start=852
  _globals['_WEBFOOTERWIDGET_DATA_SOCIALHANDLES_HANDLE']._serialized_end=922
  _globals['_WEBFOOTERWIDGET_DATA_LEGAL']._serialized_start=924
  _globals['_WEBFOOTERWIDGET_DATA_LEGAL']._serialized_end=1000
  _globals['_WEBFOOTERWIDGET_DATA_APPLINK']._serialized_start=1002
  _globals['_WEBFOOTERWIDGET_DATA_APPLINK']._serialized_end=1080
  _globals['_WEBFOOTERWIDGET_DATA_LINK']._serialized_start=1082
  _globals['_WEBFOOTERWIDGET_DATA_LINK']._serialized_end=1134
  _globals['_WEBFOOTERWIDGET_DATA_COLUMNTYPE']._serialized_start=1136
  _globals['_WEBFOOTERWIDGET_DATA_COLUMNTYPE']._serialized_end=1194
# @@protoc_insertion_point(module_scope)
