# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/content_rating_cta.proto
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
    'widget/content_rating_cta.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from widget import tooltip_action_menu_pb2 as widget_dot_tooltip__action__menu__pb2
from feature.image import lottie_pb2 as feature_dot_image_dot_lottie__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwidget/content_rating_cta.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a widget/tooltip_action_menu.proto\x1a\x1a\x66\x65\x61ture/image/lottie.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x12\x62\x61se/actions.proto\"\x8b\x04\n\x16\x43ontentRatingCtaWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x31\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32#.widget.ContentRatingCtaWidget.Data\x1a\xc0\x02\n\x04\x44\x61ta\x12\x12\n\ncontent_id\x18\x01 \x01(\t\x12\x12\n\nrate_label\x18\x02 \x01(\t\x12\x13\n\x0brated_label\x18\x03 \x01(\t\x12\x10\n\x08is_rated\x18\x04 \x01(\x08\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x12%\n\x06lottie\x18\x06 \x01(\x0b\x32\x15.feature.image.Lottie\x12#\n\x05image\x18\x07 \x01(\x0b\x32\x14.feature.image.Image\x12\x43\n\x1atooltip_action_menu_widget\x18\x08 \x01(\x0b\x32\x1f.widget.TooltipActionMenuWidget\x12\x38\n\x08\x63ta_type\x18\t \x01(\x0e\x32&.widget.ContentRatingCtaWidget.CTAType\"B\n\x07\x43TAType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x13\n\x0f\x43\x45NTER_VERTICAL\x10\x01\x12\x15\n\x11\x43\x45NTER_HORIZONTAL\x10\x02J\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.content_rating_cta_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_CONTENTRATINGCTAWIDGET']._serialized_start=180
  _globals['_CONTENTRATINGCTAWIDGET']._serialized_end=703
  _globals['_CONTENTRATINGCTAWIDGET_DATA']._serialized_start=303
  _globals['_CONTENTRATINGCTAWIDGET_DATA']._serialized_end=623
  _globals['_CONTENTRATINGCTAWIDGET_CTATYPE']._serialized_start=625
  _globals['_CONTENTRATINGCTAWIDGET_CTATYPE']._serialized_end=691
# @@protoc_insertion_point(module_scope)
