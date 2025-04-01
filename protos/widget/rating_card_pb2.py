# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/rating_card.proto
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
    'widget/rating_card.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import actions_pb2 as base_dot_actions__pb2
from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from widget import media_container_pb2 as widget_dot_media__container__pb2
from widget import tooltip_action_menu_pb2 as widget_dot_tooltip__action__menu__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18widget/rating_card.proto\x12\x06widget\x1a\x12\x62\x61se/actions.proto\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x1cwidget/media_container.proto\x1a widget/tooltip_action_menu.proto\"\xb1\x03\n\x10RatingCardWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12+\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1d.widget.RatingCardWidget.Data\x1a\xea\x01\n\x04\x44\x61ta\x12\x12\n\ncontent_id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12+\n\x05media\x18\x04 \x01(\x0b\x32\x1c.widget.MediaContainerWidget\x12\x43\n\x1atooltip_action_menu_widget\x18\x05 \x01(\x0b\x32\x1f.widget.TooltipActionMenuWidget\x12>\n\x0elayout_variant\x18\x06 \x01(\x0e\x32&.widget.RatingCardWidget.LayoutVariant\"J\n\rLayoutVariant\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x16\n\x12REGULAR_HORIZONTAL\x10\x01\x12\x14\n\x10REGULAR_VERTICAL\x10\x02J\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.rating_card_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_RATINGCARDWIDGET']._serialized_start=169
  _globals['_RATINGCARDWIDGET']._serialized_end=602
  _globals['_RATINGCARDWIDGET_DATA']._serialized_start=280
  _globals['_RATINGCARDWIDGET_DATA']._serialized_end=514
  _globals['_RATINGCARDWIDGET_LAYOUTVARIANT']._serialized_start=516
  _globals['_RATINGCARDWIDGET_LAYOUTVARIANT']._serialized_end=590
# @@protoc_insertion_point(module_scope)
