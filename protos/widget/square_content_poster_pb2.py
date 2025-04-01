# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/square_content_poster.proto
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
    'widget/square_content_poster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"widget/square_content_poster.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\xea\t\n\x19SquareContentPosterWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x34\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32&.widget.SquareContentPosterWidget.Data\x1a\xfa\x01\n\x04\x44\x61ta\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x12X\n\x17\x65xpanded_content_poster\x18\x03 \x01(\x0b\x32\x37.widget.SquareContentPosterWidget.ExpandedContentPoster\x12?\n\nlive_badge\x18\x04 \x01(\x0b\x32+.widget.SquareContentPosterWidget.LiveBadge\x12\x12\n\ncontent_id\x18\x05 \x01(\t\x1a\x81\x01\n\x15\x45xpandedContentPoster\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x43\n\x0c\x63ontent_info\x18\x02 \x01(\x0b\x32-.widget.SquareContentPosterWidget.ContentInfo\x1a\xbe\x03\n\x0b\x43ontentInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12*\n\x0ctitle_cutout\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x33\n\x04tags\x18\x04 \x03(\x0b\x32%.widget.SquareContentPosterWidget.Tag\x12=\n\tlanguages\x18\x05 \x03(\x0b\x32*.widget.SquareContentPosterWidget.Language\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12\x46\n\x0bprimary_cta\x18\x07 \x01(\x0b\x32\x31.widget.SquareContentPosterWidget.IconLabelButton\x12H\n\rwatchlist_cta\x18\x08 \x01(\x0b\x32\x31.widget.SquareContentPosterWidget.IconLabelButton\x12G\n\x0csee_more_cta\x18\t \x01(\x0b\x32\x31.widget.SquareContentPosterWidget.IconLabelButton\x1aS\n\x0fIconLabelButton\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1a\x34\n\x03Tag\x12\r\n\x05value\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a:\n\x08Language\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x12\n\nis_default\x18\x03 \x01(\x08\x1a\x35\n\tLiveBadge\x12(\n\ntext_image\x18\x01 \x01(\x0b\x32\x14.feature.image.ImageJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.square_content_poster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_SQUARECONTENTPOSTERWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_SQUARECONTENTPOSTERWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_SQUARECONTENTPOSTERWIDGET']._serialized_start=142
  _globals['_SQUARECONTENTPOSTERWIDGET']._serialized_end=1400
  _globals['_SQUARECONTENTPOSTERWIDGET_DATA']._serialized_start=309
  _globals['_SQUARECONTENTPOSTERWIDGET_DATA']._serialized_end=559
  _globals['_SQUARECONTENTPOSTERWIDGET_EXPANDEDCONTENTPOSTER']._serialized_start=562
  _globals['_SQUARECONTENTPOSTERWIDGET_EXPANDEDCONTENTPOSTER']._serialized_end=691
  _globals['_SQUARECONTENTPOSTERWIDGET_CONTENTINFO']._serialized_start=694
  _globals['_SQUARECONTENTPOSTERWIDGET_CONTENTINFO']._serialized_end=1140
  _globals['_SQUARECONTENTPOSTERWIDGET_ICONLABELBUTTON']._serialized_start=1142
  _globals['_SQUARECONTENTPOSTERWIDGET_ICONLABELBUTTON']._serialized_end=1225
  _globals['_SQUARECONTENTPOSTERWIDGET_TAG']._serialized_start=1227
  _globals['_SQUARECONTENTPOSTERWIDGET_TAG']._serialized_end=1279
  _globals['_SQUARECONTENTPOSTERWIDGET_LANGUAGE']._serialized_start=1281
  _globals['_SQUARECONTENTPOSTERWIDGET_LANGUAGE']._serialized_end=1339
  _globals['_SQUARECONTENTPOSTERWIDGET_LIVEBADGE']._serialized_start=1341
  _globals['_SQUARECONTENTPOSTERWIDGET_LIVEBADGE']._serialized_end=1394
# @@protoc_insertion_point(module_scope)
