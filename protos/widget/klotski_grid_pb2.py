# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/klotski_grid.proto
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
    'widget/klotski_grid.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.search import badge_pb2 as feature_dot_search_dot_badge__pb2
from widget import horizontal_content_card_pb2 as widget_dot_horizontal__content__card__pb2
from widget import vertical_content_poster_pb2 as widget_dot_vertical__content__poster__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19widget/klotski_grid.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x1a\x66\x65\x61ture/search/badge.proto\x1a$widget/horizontal_content_card.proto\x1a$widget/vertical_content_poster.proto\"\xa3\x07\n\x11KlotskiGridWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12,\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1e.widget.KlotskiGridWidget.Data\x1a\xa5\x01\n\x04\x44\x61ta\x12\x31\n\x04type\x18\x01 \x01(\x0e\x32#.widget.KlotskiGridWidget.BlockType\x12\x1c\n\x14parallel_unit_number\x18\x02 \x01(\r\x12\x35\n\x06\x62locks\x18\x03 \x03(\x0b\x32%.widget.KlotskiGridWidget.BlockWidget\x12\x15\n\rklotski_title\x18\x04 \x01(\t\x1a\xab\x01\n\x0b\x42lockWidget\x12\x1c\n\x14vertical_unit_number\x18\x01 \x01(\r\x12@\n\x0csingle_items\x18\x02 \x03(\x0b\x32*.widget.KlotskiGridWidget.SingleItemWidget\x12<\n\talignment\x18\x03 \x01(\x0e\x32).widget.KlotskiGridWidget.WidgetAlignment\x1a\xc1\x01\n\x10SingleItemWidget\x12\x12\n\nwidth_unit\x18\x01 \x01(\r\x12\x13\n\x0bheight_unit\x18\x02 \x01(\r\x12\x17\n\x0fx_position_unit\x18\x03 \x01(\r\x12\x17\n\x0fy_position_unit\x18\x04 \x01(\r\x12,\n\x04item\x18\x05 \x01(\x0b\x32\x1e.widget.KlotskiGridWidget.Item\x12$\n\x05\x62\x61\x64ge\x18\x06 \x01(\x0b\x32\x15.feature.search.Badge\x1a\xa0\x01\n\x04Item\x12\x46\n\x17horizontal_content_card\x18\x01 \x01(\x0b\x32#.widget.HorizontalContentCardWidgetH\x00\x12\x46\n\x17vertical_content_poster\x18\x02 \x01(\x0b\x32#.widget.VerticalContentPosterWidgetH\x00\x42\x08\n\x06widget\";\n\tBlockType\x12\x10\n\x0c\x44\x45\x46\x41ULT_TYPE\x10\x00\x12\x0c\n\x08VERTICAL\x10\x01\x12\x0e\n\nHORIZONTAL\x10\x02\"3\n\x0fWidgetAlignment\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04LEFT\x10\x01\x12\t\n\x05RIGHT\x10\x02J\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.klotski_grid_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_KLOTSKIGRIDWIDGET']._serialized_start=169
  _globals['_KLOTSKIGRIDWIDGET']._serialized_end=1100
  _globals['_KLOTSKIGRIDWIDGET_DATA']._serialized_start=282
  _globals['_KLOTSKIGRIDWIDGET_DATA']._serialized_end=447
  _globals['_KLOTSKIGRIDWIDGET_BLOCKWIDGET']._serialized_start=450
  _globals['_KLOTSKIGRIDWIDGET_BLOCKWIDGET']._serialized_end=621
  _globals['_KLOTSKIGRIDWIDGET_SINGLEITEMWIDGET']._serialized_start=624
  _globals['_KLOTSKIGRIDWIDGET_SINGLEITEMWIDGET']._serialized_end=817
  _globals['_KLOTSKIGRIDWIDGET_ITEM']._serialized_start=820
  _globals['_KLOTSKIGRIDWIDGET_ITEM']._serialized_end=980
  _globals['_KLOTSKIGRIDWIDGET_BLOCKTYPE']._serialized_start=982
  _globals['_KLOTSKIGRIDWIDGET_BLOCKTYPE']._serialized_end=1041
  _globals['_KLOTSKIGRIDWIDGET_WIDGETALIGNMENT']._serialized_start=1043
  _globals['_KLOTSKIGRIDWIDGET_WIDGETALIGNMENT']._serialized_end=1094
# @@protoc_insertion_point(module_scope)
