# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/pack_info.proto
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
    'widget/pack_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16widget/pack_info.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\xe8\x11\n\x0ePackInfoWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12)\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1b.widget.PackInfoWidget.Data\x1a\xf9\x02\n\x04\x44\x61ta\x12.\n\tpack_list\x18\x01 \x03(\x0b\x32\x1b.widget.PackInfoWidget.Pack\x12G\n\x14payment_mode_consent\x18\x02 \x01(\x0b\x32).widget.PackInfoWidget.PaymentModeConsent\x12\x36\n\x0b\x66ilter_data\x18\x03 \x03(\x0b\x32!.widget.PackInfoWidget.FilterItem\x12\x38\n\x0cpartner_info\x18\x04 \x01(\x0b\x32\".widget.PackInfoWidget.PartnerInfo\x12\x1d\n\x15pack_unavailable_info\x18\x05 \x01(\t\x12\x31\n\rsecondary_cta\x18\x06 \x01(\x0b\x32\x1a.widget.PackInfoWidget.CTA\x12\x34\n\x0ctertiary_cta\x18\x07 \x01(\x0b\x32\x1a.widget.PackInfoWidget.CTAB\x02\x18\x01\x1a\xc9\x04\n\x04Pack\x12\x13\n\x0bis_selected\x18\x01 \x01(\x08\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsub_title\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\x12+\n\x05offer\x18\x05 \x01(\x0b\x32\x1c.widget.PackInfoWidget.Offer\x12\x36\n\x0b\x66ilter_meta\x18\x0c \x01(\x0b\x32!.widget.PackInfoWidget.FilterMeta\x12\x13\n\x0bis_disabled\x18\r \x01(\x08\x12\x1e\n\x07\x61\x63tions\x18\x0e \x01(\x0b\x32\r.base.Actions\x12\x14\n\x0csavings_text\x18\x0f \x01(\t\x12-\n\x05price\x18\x06 \x01(\x0b\x32\x1c.widget.PackInfoWidget.PriceH\x00\x12\x1b\n\x11pack_details_text\x18\x07 \x01(\tH\x00\x12\x39\n\tsubscribe\x18\x08 \x01(\x0b\x32$.widget.PackInfoWidget.SubscribeInfoH\x01\x12\x35\n\x07upgrade\x18\t \x01(\x0b\x32\".widget.PackInfoWidget.UpgradeInfoH\x01\x12:\n\x11\x63ontinue_watching\x18\n \x01(\x0b\x32\x1d.widget.PackInfoWidget.CWInfoH\x01\x12\x39\n\x04text\x18\x0b \x01(\x0b\x32).widget.PackInfoWidget.PurchaseDisclaimerH\x01\x42\x0e\n\x0cpack_detailsB\x06\n\x04info\x1a\x34\n\nFilterMeta\x12\x12\n\nfilter_key\x18\x01 \x01(\t\x12\x12\n\nidentifier\x18\x02 \x01(\t\x1a\xb4\x01\n\nFilterItem\x12\x13\n\x0bis_selected\x18\x01 \x01(\x08\x12\r\n\x05title\x18\x02 \x01(\t\x12\x36\n\x0b\x66ilter_meta\x18\x03 \x01(\x0b\x32!.widget.PackInfoWidget.FilterMeta\x12\x1e\n\x07\x61\x63tions\x18\x04 \x01(\x0b\x32\r.base.Actions\x12*\n\x0coffer_lottie\x18\x05 \x01(\x0b\x32\x14.feature.image.Image\x1a\x8d\x01\n\x12PaymentModeConsent\x12\x31\n\x05paytm\x18\x01 \x01(\x0b\x32 .widget.PackInfoWidget.PaytmModeH\x00\x12<\n\x0biap_upgrade\x18\x02 \x01(\x0b\x32%.widget.PackInfoWidget.IAPUpgradeModeH\x00\x42\x06\n\x04mode\x1a\x1a\n\tPaytmMode\x12\r\n\x05value\x18\x01 \x01(\t\x1a\x1f\n\x0eIAPUpgradeMode\x12\r\n\x05value\x18\x01 \x01(\t\x1a;\n\x05Price\x12\x0e\n\x06\x61mount\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\t\x1a\x32\n\x05Offer\x12\x1b\n\x13strike_through_text\x18\x01 \x01(\t\x12\x0c\n\x04info\x18\x02 \x01(\t\x1a<\n\rSubscribeInfo\x12\x0b\n\x03\x63ta\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a\xb7\x01\n\x0bUpgradeInfo\x12\x0b\n\x03\x63ta\x18\x01 \x01(\t\x12\x38\n\tdeduction\x18\x02 \x01(\x0b\x32%.widget.PackInfoWidget.PriceDeduction\x12\x41\n\x11\x64\x65\x64uction_details\x18\x03 \x03(\x0b\x32&.widget.PackInfoWidget.DeductionDetail\x12\x1e\n\x07\x61\x63tions\x18\x04 \x01(\x0b\x32\r.base.Actions\x1aW\n\x0ePriceDeduction\x12\r\n\x05label\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x11\n\tnew_price\x18\x03 \x01(\t\x12\x11\n\told_price\x18\x04 \x01(\t\x1a.\n\x0f\x44\x65\x64uctionDetail\x12\x0c\n\x04info\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\t\x1a\x35\n\x06\x43WInfo\x12\x0b\n\x03\x63ta\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a*\n\x12PurchaseDisclaimer\x12\x14\n\x0ctext_message\x18\x01 \x01(\t\x1a\x45\n\x0bPartnerInfo\x12\x11\n\trich_text\x18\x01 \x01(\t\x12#\n\x05image\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x1a\x34\n\x03\x43TA\x12\r\n\x05label\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.ActionsJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.pack_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PACKINFOWIDGET_DATA'].fields_by_name['tertiary_cta']._loaded_options = None
  _globals['_PACKINFOWIDGET_DATA'].fields_by_name['tertiary_cta']._serialized_options = b'\030\001'
  _globals['_PACKINFOWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_PACKINFOWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_PACKINFOWIDGET']._serialized_start=130
  _globals['_PACKINFOWIDGET']._serialized_end=2410
  _globals['_PACKINFOWIDGET_DATA']._serialized_start=275
  _globals['_PACKINFOWIDGET_DATA']._serialized_end=652
  _globals['_PACKINFOWIDGET_PACK']._serialized_start=655
  _globals['_PACKINFOWIDGET_PACK']._serialized_end=1240
  _globals['_PACKINFOWIDGET_FILTERMETA']._serialized_start=1242
  _globals['_PACKINFOWIDGET_FILTERMETA']._serialized_end=1294
  _globals['_PACKINFOWIDGET_FILTERITEM']._serialized_start=1297
  _globals['_PACKINFOWIDGET_FILTERITEM']._serialized_end=1477
  _globals['_PACKINFOWIDGET_PAYMENTMODECONSENT']._serialized_start=1480
  _globals['_PACKINFOWIDGET_PAYMENTMODECONSENT']._serialized_end=1621
  _globals['_PACKINFOWIDGET_PAYTMMODE']._serialized_start=1623
  _globals['_PACKINFOWIDGET_PAYTMMODE']._serialized_end=1649
  _globals['_PACKINFOWIDGET_IAPUPGRADEMODE']._serialized_start=1651
  _globals['_PACKINFOWIDGET_IAPUPGRADEMODE']._serialized_end=1682
  _globals['_PACKINFOWIDGET_PRICE']._serialized_start=1684
  _globals['_PACKINFOWIDGET_PRICE']._serialized_end=1743
  _globals['_PACKINFOWIDGET_OFFER']._serialized_start=1745
  _globals['_PACKINFOWIDGET_OFFER']._serialized_end=1795
  _globals['_PACKINFOWIDGET_SUBSCRIBEINFO']._serialized_start=1797
  _globals['_PACKINFOWIDGET_SUBSCRIBEINFO']._serialized_end=1857
  _globals['_PACKINFOWIDGET_UPGRADEINFO']._serialized_start=1860
  _globals['_PACKINFOWIDGET_UPGRADEINFO']._serialized_end=2043
  _globals['_PACKINFOWIDGET_PRICEDEDUCTION']._serialized_start=2045
  _globals['_PACKINFOWIDGET_PRICEDEDUCTION']._serialized_end=2132
  _globals['_PACKINFOWIDGET_DEDUCTIONDETAIL']._serialized_start=2134
  _globals['_PACKINFOWIDGET_DEDUCTIONDETAIL']._serialized_end=2180
  _globals['_PACKINFOWIDGET_CWINFO']._serialized_start=2182
  _globals['_PACKINFOWIDGET_CWINFO']._serialized_end=2235
  _globals['_PACKINFOWIDGET_PURCHASEDISCLAIMER']._serialized_start=2237
  _globals['_PACKINFOWIDGET_PURCHASEDISCLAIMER']._serialized_end=2279
  _globals['_PACKINFOWIDGET_PARTNERINFO']._serialized_start=2281
  _globals['_PACKINFOWIDGET_PARTNERINFO']._serialized_end=2350
  _globals['_PACKINFOWIDGET_CTA']._serialized_start=2352
  _globals['_PACKINFOWIDGET_CTA']._serialized_end=2404
# @@protoc_insertion_point(module_scope)
