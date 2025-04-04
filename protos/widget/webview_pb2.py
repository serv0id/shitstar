# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/webview.proto
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
    'widget/webview.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.trackers import url_trackers_pb2 as feature_dot_trackers_dot_url__trackers__pb2
from feature.request import http_token_request_pb2 as feature_dot_request_dot_http__token__request__pb2
from widget import header_pb2 as widget_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14widget/webview.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a#feature/trackers/url_trackers.proto\x1a(feature/request/http_token_request.proto\x1a\x13widget/header.proto\"\x8d\x07\n\rWebviewWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12(\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1a.widget.WebviewWidget.Data\x1a\x9e\x06\n\x04\x44\x61ta\x12\x33\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\".widget.WebviewWidget.Data.Content\x12.\n\x07tracker\x18\x02 \x01(\x0b\x32\x1d.feature.trackers.UrlTrackers\x12\x41\n\x0e\x61llowed_fields\x18\x03 \x03(\x0e\x32).widget.WebviewWidget.Data.JsBridgeFields\x12\x19\n\x11\x65nable_javascript\x18\x04 \x01(\x08\x12`\n\x1cwidget_additional_properties\x18\x05 \x03(\x0b\x32:.widget.WebviewWidget.Data.WidgetAdditionalPropertiesEntry\x12.\n\x03jit\x18\x06 \x01(\x0b\x32!.feature.request.HttpTokenRequest\x12\x14\n\x0c\x64isable_zoom\x18\x07 \x01(\x08\x1a\xd8\x01\n\x07\x43ontent\x12\x39\n\x04meta\x18\x02 \x01(\x0b\x32\'.widget.WebviewWidget.Data.Content.MetaB\x02\x18\x01\x12$\n\x06header\x18\x03 \x01(\x0b\x32\x14.widget.HeaderWidget\x12\x15\n\x0bwebview_url\x18\x01 \x01(\tH\x00\x1aM\n\x04Meta\x12*\n\x0cwebpage_logo\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x15\n\rwebpage_title\x18\x02 \x01(\t:\x02\x18\x01\x42\x06\n\x04\x64\x61ta\x1a\x41\n\x1fWidgetAdditionalPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x8c\x01\n\x0eJsBridgeFields\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PINCODE\x10\x01\x12\x08\n\x04NAME\x10\x02\x12\x10\n\x0cLOGIN_STATUS\x10\x03\x12\x0f\n\x0b\x46ORM_SUBMIT\x10\x04\x12\x10\n\x0c\x45XTERNAL_NAV\x10\x05\x12\x0c\n\x08\x41\x44_ERROR\x10\x06\x12\x08\n\x04\x43ITY\x10\x08\x12\t\n\x05STATE\x10\tJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.webview_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_WEBVIEWWIDGET_DATA_CONTENT_META']._loaded_options = None
  _globals['_WEBVIEWWIDGET_DATA_CONTENT_META']._serialized_options = b'\030\001'
  _globals['_WEBVIEWWIDGET_DATA_CONTENT'].fields_by_name['meta']._loaded_options = None
  _globals['_WEBVIEWWIDGET_DATA_CONTENT'].fields_by_name['meta']._serialized_options = b'\030\001'
  _globals['_WEBVIEWWIDGET_DATA_WIDGETADDITIONALPROPERTIESENTRY']._loaded_options = None
  _globals['_WEBVIEWWIDGET_DATA_WIDGETADDITIONALPROPERTIESENTRY']._serialized_options = b'8\001'
  _globals['_WEBVIEWWIDGET']._serialized_start=187
  _globals['_WEBVIEWWIDGET']._serialized_end=1096
  _globals['_WEBVIEWWIDGET_DATA']._serialized_start=292
  _globals['_WEBVIEWWIDGET_DATA']._serialized_end=1090
  _globals['_WEBVIEWWIDGET_DATA_CONTENT']._serialized_start=664
  _globals['_WEBVIEWWIDGET_DATA_CONTENT']._serialized_end=880
  _globals['_WEBVIEWWIDGET_DATA_CONTENT_META']._serialized_start=795
  _globals['_WEBVIEWWIDGET_DATA_CONTENT_META']._serialized_end=872
  _globals['_WEBVIEWWIDGET_DATA_WIDGETADDITIONALPROPERTIESENTRY']._serialized_start=882
  _globals['_WEBVIEWWIDGET_DATA_WIDGETADDITIONALPROPERTIESENTRY']._serialized_end=947
  _globals['_WEBVIEWWIDGET_DATA_JSBRIDGEFIELDS']._serialized_start=950
  _globals['_WEBVIEWWIDGET_DATA_JSBRIDGEFIELDS']._serialized_end=1090
# @@protoc_insertion_point(module_scope)
