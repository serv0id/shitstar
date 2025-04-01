# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/payment_methods.proto
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
    'widget/payment_methods.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import actions_pb2 as base_dot_actions__pb2
from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.payment import payment_gateway_pb2 as feature_dot_payment_dot_payment__gateway__pb2
from widget import payment_method_cards_pb2 as widget_dot_payment__method__cards__pb2
from widget import payment_method_net_banking_pb2 as widget_dot_payment__method__net__banking__pb2
from widget import payment_method_wallets_pb2 as widget_dot_payment__method__wallets__pb2
from widget import payment_method_quick_pay_pb2 as widget_dot_payment__method__quick__pay__pb2
from widget import payment_method_upi_pb2 as widget_dot_payment__method__upi__pb2
from widget import text_list_pb2 as widget_dot_text__list__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cwidget/payment_methods.proto\x12\x06widget\x1a\x12\x62\x61se/actions.proto\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a%feature/payment/payment_gateway.proto\x1a!widget/payment_method_cards.proto\x1a\'widget/payment_method_net_banking.proto\x1a#widget/payment_method_wallets.proto\x1a%widget/payment_method_quick_pay.proto\x1a\x1fwidget/payment_method_upi.proto\x1a\x16widget/text_list.proto\"\xc5\x15\n\x14PaymentMethodsWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.PaymentMethodsWidget.Data\x1a\xc8\x14\n\x04\x44\x61ta\x12H\n\x0fpayment_methods\x18\x01 \x03(\x0b\x32/.widget.PaymentMethodsWidget.Data.PaymentMethod\x12R\n\x14selected_method_meta\x18\x02 \x01(\x0b\x32\x34.widget.PaymentMethodsWidget.Data.SelectedMethodMeta\x12\x38\n\x06\x66ooter\x18\x03 \x01(\x0b\x32(.widget.PaymentMethodsWidget.Data.Footer\x12H\n\non_success\x18\x04 \x01(\x0b\x32\x34.widget.PaymentMethodsWidget.Data.PaymentSuccessMeta\x12H\n\x08on_error\x18\x05 \x01(\x0b\x32\x32.widget.PaymentMethodsWidget.Data.PaymentErrorMetaB\x02\x18\x01\x12M\n\x12offer_success_meta\x18\x06 \x03(\x0b\x32\x31.widget.PaymentMethodsWidget.Data.OfferSuccesMeta\x12G\n\x0b\x65rror_metas\x18\x07 \x03(\x0b\x32\x32.widget.PaymentMethodsWidget.Data.PaymentErrorMeta\x12K\n\x0e\x63\x61ncel_payment\x18\x08 \x01(\x0b\x32\x33.widget.PaymentMethodsWidget.Data.PaymentCancelMeta\x1a\x99\x04\n\rPaymentMethod\x12\x13\n\x0bmethod_name\x18\x01 \x01(\t\x12*\n\x0cmethod_image\x18\x07 \x01(\x0b\x32\x14.feature.image.Image\x12/\n\x0fmethod_features\x18\x08 \x01(\x0b\x32\x16.widget.TextListWidget\x12+\n\x0bmethod_info\x18\t \x01(\x0b\x32\x16.widget.TextListWidget\x12\x31\n\x08gateways\x18\n \x03(\x0b\x32\x1f.feature.payment.PaymentGateway\x12\x13\n\x0bis_expanded\x18\x0b \x01(\x08\x12\x31\n\x05\x63\x61rds\x18\x02 \x01(\x0b\x32 .widget.PaymentMethodCardsWidgetH\x00\x12\x35\n\x07wallets\x18\x03 \x01(\x0b\x32\".widget.PaymentMethodWalletsWidgetH\x00\x12-\n\x03upi\x18\x04 \x01(\x0b\x32\x1e.widget.PaymentMethodUpiWidgetH\x00\x12<\n\x0bnet_banking\x18\x05 \x01(\x0b\x32%.widget.PaymentMethodNetBankingWidgetH\x00\x12\x38\n\tquick_pay\x18\x06 \x01(\x0b\x32#.widget.PaymentMethodQuickPayWidgetH\x00\x42\x10\n\x0epayment_method\x1a#\n\x12SelectedMethodMeta\x12\r\n\x05title\x18\x01 \x01(\t\x1aq\n\x06\x46ooter\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x10\n\x08sub_text\x18\x03 \x01(\t\x12\x39\n\x07\x64\x65tails\x18\x04 \x03(\x0b\x32(.widget.PaymentMethodsWidget.Data.Detail\x1a\xa2\x01\n\x12PaymentSuccessMeta\x12\x11\n\tfetch_url\x18\x01 \x01(\t\x12#\n\x05image\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x03 \x01(\t\x12\x11\n\tsub_title\x18\x04 \x01(\t\x12\x32\n\x03\x63ta\x18\x05 \x01(\x0b\x32%.widget.PaymentMethodsWidget.Data.Cta\x1a\xf8\x04\n\x10PaymentErrorMeta\x12W\n\rtimer_expired\x18\x01 \x01(\x0b\x32>.widget.PaymentMethodsWidget.Data.PaymentErrorMeta.TimerExpiryH\x00\x12X\n\rdefault_error\x18\x02 \x01(\x0b\x32?.widget.PaymentMethodsWidget.Data.PaymentErrorMeta.DefaultErrorH\x00\x1a\xce\x01\n\x0bTimerExpiry\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsub_title\x18\x03 \x01(\t\x12:\n\x0bprimary_cta\x18\x04 \x01(\x0b\x32%.widget.PaymentMethodsWidget.Data.Cta\x12<\n\rsecondary_cta\x18\x05 \x01(\x0b\x32%.widget.PaymentMethodsWidget.Data.Cta\x1a\xd0\x01\n\x0c\x44\x65\x66\x61ultError\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x02 \x01(\t\x12\x12\n\nsub_titles\x18\x03 \x03(\t\x12:\n\x0bprimary_cta\x18\x04 \x01(\x0b\x32%.widget.PaymentMethodsWidget.Data.Cta\x12<\n\rsecondary_cta\x18\x05 \x01(\x0b\x32%.widget.PaymentMethodsWidget.Data.CtaB\r\n\x0b\x65rror_types\x1a;\n\x0fOfferSuccesMeta\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x1a\x8f\x02\n\x11PaymentCancelMeta\x12!\n\x03img\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x02 \x01(\t\x12\x39\n\x07\x64\x65tails\x18\x03 \x03(\x0b\x32(.widget.PaymentMethodsWidget.Data.Detail\x12:\n\x0bprimary_cta\x18\x04 \x01(\x0b\x32%.widget.PaymentMethodsWidget.Data.Cta\x12<\n\rsecondary_cta\x18\x05 \x01(\x0b\x32%.widget.PaymentMethodsWidget.Data.Cta\x12\x13\n\x0bis_closable\x18\x06 \x01(\x08\x1a\x45\n\x03\x43ta\x12\x0c\n\x04text\x18\x0b \x01(\t\x12\x11\n\ticon_name\x18\x0c \x01(\t\x12\x1d\n\x06\x61\x63tion\x18\r \x01(\x0b\x32\r.base.Actions\x1aT\n\x06\x44\x65tail\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x35\n\x05links\x18\x02 \x03(\x0b\x32&.widget.PaymentMethodsWidget.Data.Link\x1a/\n\x04Link\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\tJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.payment_methods_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PAYMENTMETHODSWIDGET_DATA'].fields_by_name['on_error']._loaded_options = None
  _globals['_PAYMENTMETHODSWIDGET_DATA'].fields_by_name['on_error']._serialized_options = b'\030\001'
  _globals['_PAYMENTMETHODSWIDGET']._serialized_start=384
  _globals['_PAYMENTMETHODSWIDGET']._serialized_end=3141
  _globals['_PAYMENTMETHODSWIDGET_DATA']._serialized_start=503
  _globals['_PAYMENTMETHODSWIDGET_DATA']._serialized_end=3135
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTMETHOD']._serialized_start=1105
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTMETHOD']._serialized_end=1642
  _globals['_PAYMENTMETHODSWIDGET_DATA_SELECTEDMETHODMETA']._serialized_start=1644
  _globals['_PAYMENTMETHODSWIDGET_DATA_SELECTEDMETHODMETA']._serialized_end=1679
  _globals['_PAYMENTMETHODSWIDGET_DATA_FOOTER']._serialized_start=1681
  _globals['_PAYMENTMETHODSWIDGET_DATA_FOOTER']._serialized_end=1794
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTSUCCESSMETA']._serialized_start=1797
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTSUCCESSMETA']._serialized_end=1959
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTERRORMETA']._serialized_start=1962
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTERRORMETA']._serialized_end=2594
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTERRORMETA_TIMEREXPIRY']._serialized_start=2162
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTERRORMETA_TIMEREXPIRY']._serialized_end=2368
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTERRORMETA_DEFAULTERROR']._serialized_start=2371
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTERRORMETA_DEFAULTERROR']._serialized_end=2579
  _globals['_PAYMENTMETHODSWIDGET_DATA_OFFERSUCCESMETA']._serialized_start=2596
  _globals['_PAYMENTMETHODSWIDGET_DATA_OFFERSUCCESMETA']._serialized_end=2655
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTCANCELMETA']._serialized_start=2658
  _globals['_PAYMENTMETHODSWIDGET_DATA_PAYMENTCANCELMETA']._serialized_end=2929
  _globals['_PAYMENTMETHODSWIDGET_DATA_CTA']._serialized_start=2931
  _globals['_PAYMENTMETHODSWIDGET_DATA_CTA']._serialized_end=3000
  _globals['_PAYMENTMETHODSWIDGET_DATA_DETAIL']._serialized_start=3002
  _globals['_PAYMENTMETHODSWIDGET_DATA_DETAIL']._serialized_end=3086
  _globals['_PAYMENTMETHODSWIDGET_DATA_LINK']._serialized_start=3088
  _globals['_PAYMENTMETHODSWIDGET_DATA_LINK']._serialized_end=3135
# @@protoc_insertion_point(module_scope)
