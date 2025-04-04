# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/payment_method_wallets.proto
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
    'widget/payment_method_wallets.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.payment import validations_pb2 as feature_dot_payment_dot_validations__pb2
from feature.payment import restrictions_pb2 as feature_dot_payment_dot_restrictions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from base import actions_pb2 as base_dot_actions__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from widget import payment_method_commons_pb2 as widget_dot_payment__method__commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#widget/payment_method_wallets.proto\x12\x06widget\x1a!feature/payment/validations.proto\x1a\"feature/payment/restrictions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a#widget/payment_method_commons.proto\"\xcf\x14\n\x1aPaymentMethodWalletsWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12=\n\nwallet_arr\x18\x0b \x03(\x0b\x32).widget.PaymentMethodWalletsWidget.Wallet\x12?\n\x13payment_method_meta\x18\x0c \x01(\x0b\x32\".widget.PaymentMethodCommonsWidget\x1a\xc3\x0f\n\x06Wallet\x12@\n\x05paytm\x18\x01 \x01(\x0b\x32/.widget.PaymentMethodWalletsWidget.Wallet.PaytmH\x00\x12M\n\x0cother_wallet\x18\x02 \x01(\x0b\x32\x35.widget.PaymentMethodWalletsWidget.Wallet.OtherWalletH\x00\x1a\xbd\r\n\x05Paytm\x12]\n\x13verify_phone_number\x18\x01 \x01(\x0b\x32@.widget.PaymentMethodWalletsWidget.Wallet.Paytm.VerifyPhoneNumer\x12M\n\nverify_otp\x18\x02 \x01(\x0b\x32\x39.widget.PaymentMethodWalletsWidget.Wallet.Paytm.VerifyOtp\x12R\n\x0epayment_failed\x18\x03 \x01(\x0b\x32:.widget.PaymentMethodWalletsWidget.Wallet.Paytm.PaytmError\x12?\n\x13payment_method_meta\x18\x04 \x01(\x0b\x32\".widget.PaymentMethodCommonsWidget\x12X\n\x12sufficient_balance\x18\x05 \x01(\x0b\x32<.widget.PaymentMethodWalletsWidget.Wallet.Paytm.PaytmSuccess\x12\x1e\n\x07\x61\x63tions\x18\x06 \x01(\x0b\x32\r.base.Actions\x12\x12\n\nprefixNode\x18\x07 \x01(\t\x1a\xcb\x01\n\x10VerifyPhoneNumer\x12\r\n\x05title\x18\x01 \x01(\t\x12=\n\x0binput_phone\x18\x02 \x01(\x0b\x32(.widget.PaymentMethodWalletsWidget.Input\x12\x33\n\x03\x63ta\x18\x03 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12\x34\n\x16\x61uto_triggered_actions\x18\x04 \x03(\x0b\x32\x14.base.Actions.Action\x1a\x8c\x03\n\tVerifyOtp\x12\r\n\x05title\x18\x01 \x01(\t\x12\x12\n\notp_length\x18\x02 \x01(\x05\x12\x38\n\x08\x65\x64it_btn\x18\x03 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12:\n\nresend_btn\x18\x04 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12?\n\x0fverify_via_call\x18\x05 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12\x37\n\x05timer\x18\x06 \x01(\x0b\x32(.widget.PaymentMethodWalletsWidget.Timer\x12\x36\n\x06submit\x18\x07 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12\x34\n\x16\x61uto_triggered_actions\x18\x08 \x03(\x0b\x32\x14.base.Actions.Action\x1a\xf9\x02\n\nPaytmError\x12\r\n\x05title\x18\x01 \x01(\t\x12;\n\x0bprimary_cta\x18\x03 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12=\n\rsecondary_cta\x18\x04 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12\x38\n\x08\x65\x64it_btn\x18\x05 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12=\n\ntitle_desc\x18\x06 \x01(\x0b\x32).widget.PaymentMethodWalletsWidget.Titles\x12\x38\n\x16\x61uto_triggered_actions\x18\x07 \x03(\x0b\x32\x14.base.Actions.ActionB\x02\x18\x01\x12-\n\x0fon_load_actions\x18\x08 \x03(\x0b\x32\x14.base.Actions.Action\x1a\x89\x02\n\x0cPaytmSuccess\x12\r\n\x05title\x18\x01 \x01(\t\x12\x38\n\x08\x65\x64it_btn\x18\x02 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12;\n\x0bprimary_cta\x18\x03 \x01(\x0b\x32&.widget.PaymentMethodWalletsWidget.Cta\x12=\n\ntitle_desc\x18\x04 \x01(\x0b\x32).widget.PaymentMethodWalletsWidget.Titles\x12\x34\n\x16\x61uto_triggered_actions\x18\x05 \x03(\x0b\x32\x14.base.Actions.Action\x1a^\n\x0bOtherWallet\x12\x0c\n\x04name\x18\x01 \x01(\t\x12!\n\x03img\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.ActionsB\x08\n\x06wallet\x1a*\n\x06Titles\x12\r\n\x05title\x18\x01 \x01(\t\x12\x11\n\tsub_title\x18\x02 \x01(\t\x1ap\n\x03\x43ta\x12\x0c\n\x04text\x18\x0b \x01(\t\x12\x11\n\ticon_name\x18\x0c \x01(\t\x12!\n\x06\x61\x63tion\x18\r \x01(\x0b\x32\r.base.ActionsB\x02\x18\x01\x12%\n\x07\x61\x63tions\x18\x0e \x03(\x0b\x32\x14.base.Actions.Action\x1aJ\n\x05Timer\x12\x0c\n\x04text\x18\x0b \x01(\t\x12\x10\n\x08sub_text\x18\x0c \x01(\t\x12\x13\n\x0btimeoutInMS\x18\r \x01(\x03\x12\x0c\n\x04icon\x18\x0e \x01(\t\x1a\xcd\x01\n\x05Input\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bplaceholder\x18\x02 \x01(\t\x12\x30\n\x0bvalidations\x18\x03 \x03(\x0b\x32\x1b.feature.payment.Validation\x12\x32\n\x0crestrictions\x18\x04 \x03(\x0b\x32\x1c.feature.payment.Restriction\x12#\n\x05image\x18\x05 \x01(\x0b\x32\x14.feature.image.Image\x12\x15\n\rdefault_value\x18\x06 \x01(\tJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.payment_method_wallets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_PAYTMERROR'].fields_by_name['auto_triggered_actions']._loaded_options = None
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_PAYTMERROR'].fields_by_name['auto_triggered_actions']._serialized_options = b'\030\001'
  _globals['_PAYMENTMETHODWALLETSWIDGET_CTA'].fields_by_name['action']._loaded_options = None
  _globals['_PAYMENTMETHODWALLETSWIDGET_CTA'].fields_by_name['action']._serialized_options = b'\030\001'
  _globals['_PAYMENTMETHODWALLETSWIDGET']._serialized_start=230
  _globals['_PAYMENTMETHODWALLETSWIDGET']._serialized_end=2869
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET']._serialized_start=434
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET']._serialized_end=2421
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM']._serialized_start=590
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM']._serialized_end=2315
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_VERIFYPHONENUMER']._serialized_start=1065
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_VERIFYPHONENUMER']._serialized_end=1268
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_VERIFYOTP']._serialized_start=1271
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_VERIFYOTP']._serialized_end=1667
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_PAYTMERROR']._serialized_start=1670
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_PAYTMERROR']._serialized_end=2047
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_PAYTMSUCCESS']._serialized_start=2050
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_PAYTM_PAYTMSUCCESS']._serialized_end=2315
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_OTHERWALLET']._serialized_start=2317
  _globals['_PAYMENTMETHODWALLETSWIDGET_WALLET_OTHERWALLET']._serialized_end=2411
  _globals['_PAYMENTMETHODWALLETSWIDGET_TITLES']._serialized_start=2423
  _globals['_PAYMENTMETHODWALLETSWIDGET_TITLES']._serialized_end=2465
  _globals['_PAYMENTMETHODWALLETSWIDGET_CTA']._serialized_start=2467
  _globals['_PAYMENTMETHODWALLETSWIDGET_CTA']._serialized_end=2579
  _globals['_PAYMENTMETHODWALLETSWIDGET_TIMER']._serialized_start=2581
  _globals['_PAYMENTMETHODWALLETSWIDGET_TIMER']._serialized_end=2655
  _globals['_PAYMENTMETHODWALLETSWIDGET_INPUT']._serialized_start=2658
  _globals['_PAYMENTMETHODWALLETSWIDGET_INPUT']._serialized_end=2863
# @@protoc_insertion_point(module_scope)
