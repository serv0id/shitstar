# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/paywall_summary.proto
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
    'widget/paywall_summary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from widget import auto_scroll_gallery_pb2 as widget_dot_auto__scroll__gallery__pb2
from widget import text_list_pb2 as widget_dot_text__list__pb2
from widget import offer_pb2 as widget_dot_offer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cwidget/paywall_summary.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a widget/auto_scroll_gallery.proto\x1a\x16widget/text_list.proto\x1a\x12widget/offer.proto\"\xda\t\n\x14PaywallSummaryWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.PaywallSummaryWidget.Data\x1a\x8f\x03\n\x04\x44\x61ta\x12+\n\rbg_image_list\x18\x01 \x03(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x02 \x01(\t\x12+\n\rcontent_image\x18\x03 \x01(\x0b\x32\x14.feature.image.Image\x12;\n\tsub_title\x18\x04 \x01(\x0b\x32(.widget.AutoScrollGalleryWidget.Subtitle\x12\x31\n\x08usp_list\x18\x06 \x03(\x0b\x32\x1b.widget.TextListWidget.TextB\x02\x18\x01\x12<\n\rusp_list_data\x18\x07 \x03(\x0b\x32%.widget.PaywallSummaryWidget.IconText\x12@\n\rplan_callouts\x18\x08 \x03(\x0b\x32).widget.PaywallSummaryWidget.PlanCallouts\x12\"\n\x05offer\x18\t \x01(\x0b\x32\x13.widget.OfferWidgetJ\x04\x08\x05\x10\x06R\x04info\x1a,\n\x08IconText\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1aZ\n\x0cPlanCallouts\x12\x12\n\nidentifier\x18\x01 \x03(\t\x12\x36\n\x07\x63\x61llout\x18\x02 \x01(\x0b\x32%.widget.PaywallSummaryWidget.Subtitle\x1a\xe4\x03\n\x08Subtitle\x12\x37\n\x04type\x18\x05 \x01(\x0e\x32).widget.PaywallSummaryWidget.SubtitleType\x12\x43\n\tinfo_text\x18\x01 \x01(\x0b\x32..widget.PaywallSummaryWidget.Subtitle.InfoTextH\x00\x12\x43\n\trich_text\x18\x02 \x01(\x0b\x32..widget.PaywallSummaryWidget.Subtitle.RichTextH\x00\x12\x43\n\ticon_text\x18\x03 \x01(\x0b\x32..widget.PaywallSummaryWidget.Subtitle.IconTextH\x00\x12G\n\x0b\x62ullet_text\x18\x04 \x01(\x0b\x32\x30.widget.PaywallSummaryWidget.Subtitle.BulletTextH\x00\x1a\x19\n\x08InfoText\x12\r\n\x05value\x18\x01 \x01(\t\x1a\x19\n\x08RichText\x12\r\n\x05value\x18\x01 \x01(\t\x1a,\n\x08IconText\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x1a\x1b\n\nBulletText\x12\r\n\x05value\x18\x01 \x01(\tB\x06\n\x04text\"5\n\x0cSubtitleType\x12\x0b\n\x07\x43\x41LLOUT\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x12\r\n\tHIGHLIGHT\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.paywall_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PAYWALLSUMMARYWIDGET_DATA'].fields_by_name['usp_list']._loaded_options = None
  _globals['_PAYWALLSUMMARYWIDGET_DATA'].fields_by_name['usp_list']._serialized_options = b'\030\001'
  _globals['_PAYWALLSUMMARYWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_PAYWALLSUMMARYWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_PAYWALLSUMMARYWIDGET']._serialized_start=194
  _globals['_PAYWALLSUMMARYWIDGET']._serialized_end=1436
  _globals['_PAYWALLSUMMARYWIDGET_DATA']._serialized_start=351
  _globals['_PAYWALLSUMMARYWIDGET_DATA']._serialized_end=750
  _globals['_PAYWALLSUMMARYWIDGET_ICONTEXT']._serialized_start=752
  _globals['_PAYWALLSUMMARYWIDGET_ICONTEXT']._serialized_end=796
  _globals['_PAYWALLSUMMARYWIDGET_PLANCALLOUTS']._serialized_start=798
  _globals['_PAYWALLSUMMARYWIDGET_PLANCALLOUTS']._serialized_end=888
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE']._serialized_start=891
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE']._serialized_end=1375
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_INFOTEXT']._serialized_start=1240
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_INFOTEXT']._serialized_end=1265
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_RICHTEXT']._serialized_start=1267
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_RICHTEXT']._serialized_end=1292
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_ICONTEXT']._serialized_start=752
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_ICONTEXT']._serialized_end=796
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_BULLETTEXT']._serialized_start=1340
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLE_BULLETTEXT']._serialized_end=1367
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLETYPE']._serialized_start=1377
  _globals['_PAYWALLSUMMARYWIDGET_SUBTITLETYPE']._serialized_end=1430
# @@protoc_insertion_point(module_scope)
