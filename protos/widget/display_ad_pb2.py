# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/display_ad.proto
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
    'widget/display_ad.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17widget/display_ad.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\"\xca\x04\n\x0f\x44isplayAdWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12*\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1c.widget.DisplayAdWidget.Data\x1a\x9a\x02\n\x04\x44\x61ta\x12.\n\x04type\x18\x01 \x01(\x0e\x32 .widget.DisplayAdWidget.TypeOfAd\x12\x38\n\tplacement\x18\x02 \x01(\x0e\x32%.widget.DisplayAdWidget.PlacementType\x12\x17\n\x0brefresh_url\x18\x05 \x01(\tB\x02\x18\x01\x12\x39\n\x0crefresh_info\x18\x06 \x01(\x0b\x32#.widget.DisplayAdWidget.RefreshInfo\x12\x1e\n\x07\x61\x63tions\x18\x07 \x01(\x0b\x32\r.base.Actions\x12\x14\n\nserver_url\x18\x03 \x01(\tH\x00\x12\x11\n\x07payload\x18\x04 \x01(\tH\x00\x42\x0b\n\titem_type\x1a\x36\n\x0bRefreshInfo\x12\x12\n\nmax_age_ms\x18\x01 \x01(\x03\x12\x13\n\x0brefresh_url\x18\x02 \x01(\t\"*\n\x08TypeOfAd\x12\x0e\n\nFirstParty\x10\x00\x12\x0e\n\nThirdParty\x10\x01\"1\n\rPlacementType\x12\t\n\x05IMAGE\x10\x00\x12\t\n\x05VIDEO\x10\x01\x12\n\n\x06SKINNY\x10\x03J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.display_ad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_DISPLAYADWIDGET_DATA'].fields_by_name['refresh_url']._loaded_options = None
  _globals['_DISPLAYADWIDGET_DATA'].fields_by_name['refresh_url']._serialized_options = b'\030\001'
  _globals['_DISPLAYADWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_DISPLAYADWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_DISPLAYADWIDGET']._serialized_start=104
  _globals['_DISPLAYADWIDGET']._serialized_end=690
  _globals['_DISPLAYADWIDGET_DATA']._serialized_start=251
  _globals['_DISPLAYADWIDGET_DATA']._serialized_end=533
  _globals['_DISPLAYADWIDGET_REFRESHINFO']._serialized_start=535
  _globals['_DISPLAYADWIDGET_REFRESHINFO']._serialized_end=589
  _globals['_DISPLAYADWIDGET_TYPEOFAD']._serialized_start=591
  _globals['_DISPLAYADWIDGET_TYPEOFAD']._serialized_end=633
  _globals['_DISPLAYADWIDGET_PLACEMENTTYPE']._serialized_start=635
  _globals['_DISPLAYADWIDGET_PLACEMENTTYPE']._serialized_end=684
# @@protoc_insertion_point(module_scope)
