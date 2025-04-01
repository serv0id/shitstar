# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/video_display_ad.proto
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
    'widget/video_display_ad.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import actions_pb2 as base_dot_actions__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.ad import display_video_pb2 as feature_dot_ad_dot_display__video__pb2
from feature.ad import display_image_pb2 as feature_dot_ad_dot_display__image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwidget/video_display_ad.proto\x12\x06widget\x1a\x12\x62\x61se/actions.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x1e\x66\x65\x61ture/ad/display_video.proto\x1a\x1e\x66\x65\x61ture/ad/display_image.proto\"\xf9\x01\n\x14VideoDisplayAdWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.VideoDisplayAdWidget.Data\x1a}\n\x04\x44\x61ta\x12*\n\x08video_ad\x18\x01 \x01(\x0b\x32\x18.feature.ad.DisplayVideo\x12*\n\x08image_ad\x18\x02 \x01(\x0b\x32\x18.feature.ad.DisplayImage\x12\x1d\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32\r.base.ActionsJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.video_display_ad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_VIDEODISPLAYADWIDGET']._serialized_start=153
  _globals['_VIDEODISPLAYADWIDGET']._serialized_end=402
  _globals['_VIDEODISPLAYADWIDGET_DATA']._serialized_start=271
  _globals['_VIDEODISPLAYADWIDGET_DATA']._serialized_end=396
# @@protoc_insertion_point(module_scope)
