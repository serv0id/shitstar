# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/offer.proto
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
    'widget/offer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import actions_pb2 as base_dot_actions__pb2
from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from action import external_navigation_pb2 as action_dot_external__navigation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12widget/offer.proto\x12\x06widget\x1a\x12\x62\x61se/actions.proto\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a action/external_navigation.proto\"\xe2\n\n\x0bOfferWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12&\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x18.widget.OfferWidget.Data\x1a\xf1\x02\n\x04\x44\x61ta\x12-\n\x05title\x18\x01 \x01(\x0b\x32\x1e.widget.OfferWidget.OfferTitle\x12\x34\n\tsub_title\x18\x02 \x01(\x0b\x32!.widget.OfferWidget.OfferSubtitle\x12!\n\x03img\x18\x03 \x01(\x0b\x32\x14.feature.image.Image\x12@\n\x0f\x62\x61\x63kground_meta\x18\x04 \x01(\x0b\x32\'.widget.OfferWidget.OfferBackgroundMeta\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12=\n\x08on_click\x18\x06 \x01(\x0b\x32\'.widget.OfferWidget.OfferOnclickActionsB\x02\x18\x01\x12\x1e\n\x07\x61\x63tions\x18\x07 \x01(\x0b\x32\r.base.Actions\x12\x32\n\x08tnc_meta\x18\x08 \x01(\x0b\x32 .widget.OfferWidget.OfferTncMeta\x1aM\n\nOfferTitle\x12\r\n\x05value\x18\x01 \x01(\t\x12\x30\n\x04type\x18\x02 \x01(\x0e\x32\".widget.OfferWidget.OfferTitleType\x1a\x64\n\rOfferSubtitle\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\nerror_text\x18\x02 \x01(\t\x12\x31\n\x05timer\x18\x03 \x01(\x0b\x32\".widget.OfferWidget.OfferTimerMeta\x1a\x43\n\x13OfferBackgroundMeta\x12\x16\n\x0egradient_start\x18\x01 \x01(\t\x12\x14\n\x0cgradient_end\x18\x02 \x01(\t\x1ag\n\x13OfferOnclickActions\x12?\n\x13\x65xternal_navigation\x18\x03 \x01(\x0b\x32 .action.ExternalNavigationActionH\x00\x42\x0f\n\roffer_actions\x1a%\n\x0eOfferTimerMeta\x12\x13\n\x0b\x65xpiry_time\x18\x01 \x01(\t\x1a\xbd\x01\n\x0cOfferTncMeta\x12\x12\n\nclose_icon\x18\x01 \x01(\t\x12)\n\x0btitle_image\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x12\n\ntitle_text\x18\x03 \x01(\t\x12\x31\n\x08tnc_list\x18\x04 \x03(\x0b\x32\x1f.widget.OfferWidget.TncListItem\x12\'\n\x03\x63ta\x18\x05 \x01(\x0b\x32\x1a.widget.OfferWidget.TncCta\x1aZ\n\x0bTncListItem\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x04link\x18\x02 \x01(\tB\x02\x18\x01\x12+\n\titem_link\x18\x03 \x01(\x0b\x32\x18.widget.OfferWidget.Link\x1aH\n\x06TncCta\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x10\n\x08\x63ta_icon\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1a\x35\n\x04Link\x12\r\n\x05label\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\"7\n\x0eOfferTitleType\x12\x0e\n\nTITLE_TEXT\x10\x00\x12\x15\n\x11TITLE_HIGHLIGHTED\x10\x01J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.offer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_OFFERWIDGET_DATA'].fields_by_name['on_click']._loaded_options = None
  _globals['_OFFERWIDGET_DATA'].fields_by_name['on_click']._serialized_options = b'\030\001'
  _globals['_OFFERWIDGET_TNCLISTITEM'].fields_by_name['link']._loaded_options = None
  _globals['_OFFERWIDGET_TNCLISTITEM'].fields_by_name['link']._serialized_options = b'\030\001'
  _globals['_OFFERWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_OFFERWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_OFFERWIDGET']._serialized_start=160
  _globals['_OFFERWIDGET']._serialized_end=1538
  _globals['_OFFERWIDGET_DATA']._serialized_start=299
  _globals['_OFFERWIDGET_DATA']._serialized_end=668
  _globals['_OFFERWIDGET_OFFERTITLE']._serialized_start=670
  _globals['_OFFERWIDGET_OFFERTITLE']._serialized_end=747
  _globals['_OFFERWIDGET_OFFERSUBTITLE']._serialized_start=749
  _globals['_OFFERWIDGET_OFFERSUBTITLE']._serialized_end=849
  _globals['_OFFERWIDGET_OFFERBACKGROUNDMETA']._serialized_start=851
  _globals['_OFFERWIDGET_OFFERBACKGROUNDMETA']._serialized_end=918
  _globals['_OFFERWIDGET_OFFERONCLICKACTIONS']._serialized_start=920
  _globals['_OFFERWIDGET_OFFERONCLICKACTIONS']._serialized_end=1023
  _globals['_OFFERWIDGET_OFFERTIMERMETA']._serialized_start=1025
  _globals['_OFFERWIDGET_OFFERTIMERMETA']._serialized_end=1062
  _globals['_OFFERWIDGET_OFFERTNCMETA']._serialized_start=1065
  _globals['_OFFERWIDGET_OFFERTNCMETA']._serialized_end=1254
  _globals['_OFFERWIDGET_TNCLISTITEM']._serialized_start=1256
  _globals['_OFFERWIDGET_TNCLISTITEM']._serialized_end=1346
  _globals['_OFFERWIDGET_TNCCTA']._serialized_start=1348
  _globals['_OFFERWIDGET_TNCCTA']._serialized_end=1420
  _globals['_OFFERWIDGET_LINK']._serialized_start=1422
  _globals['_OFFERWIDGET_LINK']._serialized_end=1475
  _globals['_OFFERWIDGET_OFFERTITLETYPE']._serialized_start=1477
  _globals['_OFFERWIDGET_OFFERTITLETYPE']._serialized_end=1532
# @@protoc_insertion_point(module_scope)
