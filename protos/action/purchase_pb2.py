# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: action/purchase.proto
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
    'action/purchase.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61\x63tion/purchase.proto\x12\x06\x61\x63tion\"\x99\x04\n\x0ePurchaseAction\x12+\n\rpurchase_type\x18\x01 \x01(\x0e\x32\x14.action.PurchaseType\x12\x1a\n\x12\x63ommercial_pack_id\x18\x02 \x01(\t\x12\x13\n\x0bpayment_url\x18\x03 \x01(\t\x12\"\n\x1apayment_success_widget_url\x18\x04 \x01(\t\x12\x14\n\x0creplace_page\x18\x05 \x01(\x08\x12\x39\n\rweb_view_meta\x18\x06 \x01(\x0b\x32\".action.PurchaseAction.WebViewMeta\x12\x12\n\npromo_code\x18\x07 \x01(\t\x1a\x9f\x02\n\x0bWebViewMeta\x12@\n\x07headers\x18\x01 \x03(\x0b\x32/.action.PurchaseAction.WebViewMeta.HeadersEntry\x12\x13\n\x07\x63ookies\x18\x02 \x03(\tB\x02\x18\x01\x12Q\n\x10override_cookies\x18\x03 \x03(\x0b\x32\x37.action.PurchaseAction.WebViewMeta.OverrideCookiesEntry\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x36\n\x14OverrideCookiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*.\n\x0cPurchaseType\x12\x07\n\x03WEB\x10\x00\x12\x0c\n\x08WEB_VIEW\x10\x01\x12\x07\n\x03IAP\x10\x02\x42O\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.purchase_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_PURCHASEACTION_WEBVIEWMETA_HEADERSENTRY']._loaded_options = None
  _globals['_PURCHASEACTION_WEBVIEWMETA_HEADERSENTRY']._serialized_options = b'8\001'
  _globals['_PURCHASEACTION_WEBVIEWMETA_OVERRIDECOOKIESENTRY']._loaded_options = None
  _globals['_PURCHASEACTION_WEBVIEWMETA_OVERRIDECOOKIESENTRY']._serialized_options = b'8\001'
  _globals['_PURCHASEACTION_WEBVIEWMETA'].fields_by_name['cookies']._loaded_options = None
  _globals['_PURCHASEACTION_WEBVIEWMETA'].fields_by_name['cookies']._serialized_options = b'\030\001'
  _globals['_PURCHASETYPE']._serialized_start=573
  _globals['_PURCHASETYPE']._serialized_end=619
  _globals['_PURCHASEACTION']._serialized_start=34
  _globals['_PURCHASEACTION']._serialized_end=571
  _globals['_PURCHASEACTION_WEBVIEWMETA']._serialized_start=284
  _globals['_PURCHASEACTION_WEBVIEWMETA']._serialized_end=571
  _globals['_PURCHASEACTION_WEBVIEWMETA_HEADERSENTRY']._serialized_start=469
  _globals['_PURCHASEACTION_WEBVIEWMETA_HEADERSENTRY']._serialized_end=515
  _globals['_PURCHASEACTION_WEBVIEWMETA_OVERRIDECOOKIESENTRY']._serialized_start=517
  _globals['_PURCHASEACTION_WEBVIEWMETA_OVERRIDECOOKIESENTRY']._serialized_end=571
# @@protoc_insertion_point(module_scope)
