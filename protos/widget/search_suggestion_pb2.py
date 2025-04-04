# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/search_suggestion.proto
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
    'widget/search_suggestion.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.search import badge_pb2 as feature_dot_search_dot_badge__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ewidget/search_suggestion.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x1a\x66\x65\x61ture/search/badge.proto\"\x81\x05\n\x16SearchSuggestionWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x31\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32#.widget.SearchSuggestionWidget.Data\x1a\x7f\n\x04\x44\x61ta\x12\x0e\n\x06header\x18\x01 \x01(\t\x12\x32\n\x05items\x18\x02 \x03(\x0b\x32#.widget.SearchSuggestionWidget.Item\x12\x33\n\x07widgets\x18\x03 \x03(\x0b\x32\".widget.SearchSuggestionItemWidget\x1a\xe1\x01\n\x04Item\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.widget.SearchSuggestionWidget.SuggestionType\x12\r\n\x05title\x18\x02 \x01(\t\x12#\n\x05image\x18\x03 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x04 \x01(\x0b\x32\r.base.Actions\x12\x10\n\x08\x64uration\x18\x05 \x01(\t\x12\x10\n\x08playable\x18\x06 \x01(\x08\x12$\n\x05\x62\x61\x64ge\x18\x07 \x01(\x0b\x32\x15.feature.search.Badge\"v\n\x0eSuggestionType\x12\x12\n\x0eTRENDING_QUERY\x10\x00\x12\x14\n\x10TRENDING_CONTENT\x10\x01\x12\x11\n\rHISTORY_QUERY\x10\x02\x12\x13\n\x0fHISTORY_CONTENT\x10\x03\x12\x12\n\x0eRELATED_SEARCH\x10\x04J\x04\x08\x03\x10\x0b\"\xea\x02\n\x1aSearchSuggestionItemWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x35\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\'.widget.SearchSuggestionItemWidget.Data\x1a\xe1\x01\n\x04\x44\x61ta\x12;\n\x04type\x18\x01 \x01(\x0e\x32-.widget.SearchSuggestionWidget.SuggestionType\x12\r\n\x05title\x18\x02 \x01(\t\x12#\n\x05image\x18\x03 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x04 \x01(\x0b\x32\r.base.Actions\x12\x10\n\x08\x64uration\x18\x05 \x01(\t\x12\x10\n\x08playable\x18\x06 \x01(\x08\x12$\n\x05\x62\x61\x64ge\x18\x07 \x01(\x0b\x32\x15.feature.search.BadgeJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.search_suggestion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_SEARCHSUGGESTIONWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_SEARCHSUGGESTIONWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_SEARCHSUGGESTIONWIDGET']._serialized_start=166
  _globals['_SEARCHSUGGESTIONWIDGET']._serialized_end=807
  _globals['_SEARCHSUGGESTIONWIDGET_DATA']._serialized_start=326
  _globals['_SEARCHSUGGESTIONWIDGET_DATA']._serialized_end=453
  _globals['_SEARCHSUGGESTIONWIDGET_ITEM']._serialized_start=456
  _globals['_SEARCHSUGGESTIONWIDGET_ITEM']._serialized_end=681
  _globals['_SEARCHSUGGESTIONWIDGET_SUGGESTIONTYPE']._serialized_start=683
  _globals['_SEARCHSUGGESTIONWIDGET_SUGGESTIONTYPE']._serialized_end=801
  _globals['_SEARCHSUGGESTIONITEMWIDGET']._serialized_start=810
  _globals['_SEARCHSUGGESTIONITEMWIDGET']._serialized_end=1172
  _globals['_SEARCHSUGGESTIONITEMWIDGET_DATA']._serialized_start=941
  _globals['_SEARCHSUGGESTIONITEMWIDGET_DATA']._serialized_end=1166
# @@protoc_insertion_point(module_scope)
