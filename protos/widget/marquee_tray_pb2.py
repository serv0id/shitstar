# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/marquee_tray.proto
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
    'widget/marquee_tray.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.refresh import refresh_info_pb2 as feature_dot_refresh_dot_refresh__info__pb2
from widget import header_pb2 as widget_dot_header__pb2
from widget import hero_content_display_pb2 as widget_dot_hero__content__display__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19widget/marquee_tray.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\"feature/refresh/refresh_info.proto\x1a\x13widget/header.proto\x1a!widget/hero_content_display.proto\"\x9e\x02\n\x11MarqueeTrayWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12,\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1e.widget.MarqueeTrayWidget.Data\x1a\xa7\x01\n\x04\x44\x61ta\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.widget.HeaderWidget\x12\x45\n\x1bhero_content_display_widget\x18\x02 \x01(\x0b\x32 .widget.HeroContentDisplayWidget\x12\x32\n\x0crefresh_info\x18\x03 \x01(\x0b\x32\x1c.feature.refresh.RefreshInfoJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.marquee_tray_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_MARQUEETRAYWIDGET']._serialized_start=157
  _globals['_MARQUEETRAYWIDGET']._serialized_end=443
  _globals['_MARQUEETRAYWIDGET_DATA']._serialized_start=270
  _globals['_MARQUEETRAYWIDGET_DATA']._serialized_end=437
# @@protoc_insertion_point(module_scope)
