# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/spotlight_info_gec.proto
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
    'widget/spotlight_info_gec.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.live import live_info_pb2 as feature_dot_live_dot_live__info__pb2
from feature.callout_tag import callout_tag_pb2 as feature_dot_callout__tag_dot_callout__tag__pb2
from widget import timer_pb2 as widget_dot_timer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwidget/spotlight_info_gec.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x1c\x66\x65\x61ture/live/live_info.proto\x1a%feature/callout_tag/callout_tag.proto\x1a\x12widget/timer.proto\"\xa0\n\n\x16SpotlightInfoGecWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x31\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32#.widget.SpotlightInfoGecWidget.Data\x1a\xf4\x04\n\x04\x44\x61ta\x12\r\n\x05title\x18\x01 \x01(\t\x12*\n\x0ctitle_cutout\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0c\x63\x61llout_text\x18\x04 \x01(\t\x12@\n\x10superscript_tags\x18\x05 \x03(\x0b\x32\".widget.SpotlightInfoGecWidget.TagB\x02\x18\x01\x12>\n\x0esubscript_tags\x18\x06 \x03(\x0b\x32\".widget.SpotlightInfoGecWidget.TagB\x02\x18\x01\x12\x39\n\rsubscript_usp\x18\x07 \x01(\x0b\x32\".widget.SpotlightInfoGecWidget.Tag\x12:\n\x0e\x63ore_meta_tags\x18\x08 \x03(\x0b\x32\".widget.SpotlightInfoGecWidget.Tag\x12>\n\x12\x65nriched_meta_tags\x18\t \x03(\x0b\x32\".widget.SpotlightInfoGecWidget.Tag\x12)\n\tlive_info\x18\n \x01(\x0b\x32\x16.feature.live.LiveInfo\x12=\n\x11\x63\x61llout_meta_tags\x18\x0b \x03(\x0b\x32\".widget.SpotlightInfoGecWidget.Tag\x12\"\n\x05timer\x18\x0c \x01(\x0b\x32\x13.widget.TimerWidget\x12?\n\x13secondary_meta_tags\x18\r \x03(\x0b\x32\".widget.SpotlightInfoGecWidget.Tag\x1a\xe5\x02\n\x03Tag\x12\x38\n\x04type\x18\x01 \x01(\x0e\x32&.widget.SpotlightInfoGecWidget.TagTypeB\x02\x18\x01\x12\x11\n\x05value\x18\x02 \x01(\tB\x02\x18\x01\x12\x1a\n\x0e\x66\x61llback_value\x18\x03 \x01(\tB\x02\x18\x01\x12:\n\x08text_tag\x18\x04 \x01(\x0b\x32&.widget.SpotlightInfoGecWidget.TextTagH\x00\x12<\n\tbadge_tag\x18\x05 \x01(\x0b\x32\'.widget.SpotlightInfoGecWidget.BadgeTagH\x00\x12<\n\timage_tag\x18\x06 \x01(\x0b\x32\'.widget.SpotlightInfoGecWidget.ImageTagH\x00\x12\x36\n\x0b\x63\x61llout_tag\x18\x07 \x01(\x0b\x32\x1f.feature.callout_tag.CalloutTagH\x00\x42\x05\n\x03tag\x1a\x18\n\x07TextTag\x12\r\n\x05value\x18\x01 \x01(\t\x1a\x19\n\x08\x42\x61\x64geTag\x12\r\n\x05value\x18\x01 \x01(\t\x1a/\n\x08ImageTag\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\"5\n\x07TagType\x12\x0c\n\x04TEXT\x10\x00\x1a\x02\x08\x01\x12\r\n\x05\x42\x41\x44GE\x10\x01\x1a\x02\x08\x01\x12\r\n\x05IMAGE\x10\x02\x1a\x02\x08\x01J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.spotlight_info_gec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_SPOTLIGHTINFOGECWIDGET_DATA'].fields_by_name['superscript_tags']._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_DATA'].fields_by_name['superscript_tags']._serialized_options = b'\030\001'
  _globals['_SPOTLIGHTINFOGECWIDGET_DATA'].fields_by_name['subscript_tags']._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_DATA'].fields_by_name['subscript_tags']._serialized_options = b'\030\001'
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG'].fields_by_name['type']._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG'].fields_by_name['type']._serialized_options = b'\030\001'
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG'].fields_by_name['value']._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG'].fields_by_name['value']._serialized_options = b'\030\001'
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG'].fields_by_name['fallback_value']._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG'].fields_by_name['fallback_value']._serialized_options = b'\030\001'
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE'].values_by_name["TEXT"]._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE'].values_by_name["TEXT"]._serialized_options = b'\010\001'
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE'].values_by_name["BADGE"]._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE'].values_by_name["BADGE"]._serialized_options = b'\010\001'
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE'].values_by_name["IMAGE"]._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE'].values_by_name["IMAGE"]._serialized_options = b'\010\001'
  _globals['_SPOTLIGHTINFOGECWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_SPOTLIGHTINFOGECWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_SPOTLIGHTINFOGECWIDGET']._serialized_start=208
  _globals['_SPOTLIGHTINFOGECWIDGET']._serialized_end=1520
  _globals['_SPOTLIGHTINFOGECWIDGET_DATA']._serialized_start=369
  _globals['_SPOTLIGHTINFOGECWIDGET_DATA']._serialized_end=997
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG']._serialized_start=1000
  _globals['_SPOTLIGHTINFOGECWIDGET_TAG']._serialized_end=1357
  _globals['_SPOTLIGHTINFOGECWIDGET_TEXTTAG']._serialized_start=1359
  _globals['_SPOTLIGHTINFOGECWIDGET_TEXTTAG']._serialized_end=1383
  _globals['_SPOTLIGHTINFOGECWIDGET_BADGETAG']._serialized_start=1385
  _globals['_SPOTLIGHTINFOGECWIDGET_BADGETAG']._serialized_end=1410
  _globals['_SPOTLIGHTINFOGECWIDGET_IMAGETAG']._serialized_start=1412
  _globals['_SPOTLIGHTINFOGECWIDGET_IMAGETAG']._serialized_end=1459
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE']._serialized_start=1461
  _globals['_SPOTLIGHTINFOGECWIDGET_TAGTYPE']._serialized_end=1514
# @@protoc_insertion_point(module_scope)
