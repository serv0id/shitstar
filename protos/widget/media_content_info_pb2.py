# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/media_content_info.proto
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
    'widget/media_content_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from widget import media_content_info_small_pb2 as widget_dot_media__content__info__small__pb2
from widget import media_content_info_large_pb2 as widget_dot_media__content__info__large__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwidget/media_content_info.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a%widget/media_content_info_small.proto\x1a%widget/media_content_info_large.proto\"\x85\x02\n\x16MediaContentInfoWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x31\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32#.widget.MediaContentInfoWidget.Data\x1a\x84\x01\n\x04\x44\x61ta\x12\x39\n\nsmall_info\x18\x01 \x01(\x0b\x32#.widget.MediaContentInfoSmallWidgetH\x00\x12\x39\n\nlarge_info\x18\x02 \x01(\x0b\x32#.widget.MediaContentInfoLargeWidgetH\x00\x42\x06\n\x04infoJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.media_content_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_MEDIACONTENTINFOWIDGET']._serialized_start=149
  _globals['_MEDIACONTENTINFOWIDGET']._serialized_end=410
  _globals['_MEDIACONTENTINFOWIDGET_DATA']._serialized_start=272
  _globals['_MEDIACONTENTINFOWIDGET_DATA']._serialized_end=404
# @@protoc_insertion_point(module_scope)
