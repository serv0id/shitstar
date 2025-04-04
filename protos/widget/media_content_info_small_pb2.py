# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/media_content_info_small.proto
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
    'widget/media_content_info_small.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.atom import button_pb2 as feature_dot_atom_dot_button__pb2
from feature.callout_tag import callout_tag_pb2 as feature_dot_callout__tag_dot_callout__tag__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%widget/media_content_info_small.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x19\x66\x65\x61ture/atom/button.proto\x1a%feature/callout_tag/callout_tag.proto\"\xb1\x03\n\x1bMediaContentInfoSmallWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x36\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32(.widget.MediaContentInfoSmallWidget.Data\x1a\xec\x01\n\x04\x44\x61ta\x12$\n\x06poster\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsub_title\x18\x03 \x01(\t\x12-\n\x04tags\x18\x04 \x03(\x0b\x32\x1f.feature.callout_tag.CalloutTag\x12#\n\x05kebab\x18\x05 \x01(\x0b\x32\x14.feature.atom.Button\x12H\n\x11poster_image_type\x18\x06 \x01(\x0e\x32-.widget.MediaContentInfoSmallWidget.ImageType\"8\n\tImageType\x12\x10\n\x0c\x44\x45\x46\x41ULT_TYPE\x10\x00\x12\n\n\x06\x43IRCLE\x10\x01\x12\r\n\tRECTANGLE\x10\x02J\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.media_content_info_small_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_MEDIACONTENTINFOSMALLWIDGET']._serialized_start=190
  _globals['_MEDIACONTENTINFOSMALLWIDGET']._serialized_end=623
  _globals['_MEDIACONTENTINFOSMALLWIDGET_DATA']._serialized_start=323
  _globals['_MEDIACONTENTINFOSMALLWIDGET_DATA']._serialized_end=559
  _globals['_MEDIACONTENTINFOSMALLWIDGET_IMAGETYPE']._serialized_start=561
  _globals['_MEDIACONTENTINFOSMALLWIDGET_IMAGETYPE']._serialized_end=617
# @@protoc_insertion_point(module_scope)
