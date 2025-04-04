# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: pagedata/payment_redirect.proto
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
    'pagedata/payment_redirect.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import page_data_commons_pb2 as base_dot_page__data__commons__pb2
from action import page_navigation_pb2 as action_dot_page__navigation__pb2
from action import purchase_pb2 as action_dot_purchase__pb2
from action import external_navigation_pb2 as action_dot_external__navigation__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fpagedata/payment_redirect.proto\x12\x08pagedata\x1a\x1c\x62\x61se/page_data_commons.proto\x1a\x1c\x61\x63tion/page_navigation.proto\x1a\x15\x61\x63tion/purchase.proto\x1a action/external_navigation.proto\x1a\x12\x62\x61se/actions.proto\"\x80\x06\n\x17PaymentRedirectPageData\x12\x30\n\x11page_data_commons\x18\x01 \x01(\x0b\x32\x15.base.PageDataCommons\x12Q\n\x13\x61uto_trigger_action\x18\x0e \x01(\x0b\x32\x34.pagedata.PaymentRedirectPageData.AutoTriggerActions\x12S\n\x12page_event_actions\x18\x0f \x03(\x0b\x32\x37.pagedata.PaymentRedirectPageData.PageEventActionsEntry\x1a\xe9\x01\n\x12\x41utoTriggerActions\x12@\n\x07on_load\x18\x03 \x03(\x0b\x32/.pagedata.PaymentRedirectPageData.OnloadActions\x12\x35\n\x0fpurchase_action\x18\x01 \x01(\x0b\x32\x16.action.PurchaseActionB\x02\x18\x01H\x00\x12\x43\n\x13\x65xternal_navigation\x18\x02 \x01(\x0b\x32 .action.ExternalNavigationActionB\x02\x18\x01H\x00\x42\x15\n\x13\x61uto_trigger_action\x1aM\n\x15PageEventActionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.base.Actions.Action:\x02\x38\x01\x1a\xcf\x01\n\rOnloadActions\x12\x31\n\x0fpurchase_action\x18\x01 \x01(\x0b\x32\x16.action.PurchaseActionH\x00\x12?\n\x13\x65xternal_navigation\x18\x02 \x01(\x0b\x32 .action.ExternalNavigationActionH\x00\x12\x37\n\x0fpage_navigation\x18\x03 \x01(\x0b\x32\x1c.action.PageNavigationActionH\x00\x42\x11\n\x0fon_load_actionsBS\n\x1d\x63om.hotstar.ui.model.pagedataP\x01Z0github.com/hotstar/hs-core-ui-models-go/pagedatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pagedata.payment_redirect_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035com.hotstar.ui.model.pagedataP\001Z0github.com/hotstar/hs-core-ui-models-go/pagedata'
  _globals['_PAYMENTREDIRECTPAGEDATA_AUTOTRIGGERACTIONS'].fields_by_name['purchase_action']._loaded_options = None
  _globals['_PAYMENTREDIRECTPAGEDATA_AUTOTRIGGERACTIONS'].fields_by_name['purchase_action']._serialized_options = b'\030\001'
  _globals['_PAYMENTREDIRECTPAGEDATA_AUTOTRIGGERACTIONS'].fields_by_name['external_navigation']._loaded_options = None
  _globals['_PAYMENTREDIRECTPAGEDATA_AUTOTRIGGERACTIONS'].fields_by_name['external_navigation']._serialized_options = b'\030\001'
  _globals['_PAYMENTREDIRECTPAGEDATA_PAGEEVENTACTIONSENTRY']._loaded_options = None
  _globals['_PAYMENTREDIRECTPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_options = b'8\001'
  _globals['_PAYMENTREDIRECTPAGEDATA']._serialized_start=183
  _globals['_PAYMENTREDIRECTPAGEDATA']._serialized_end=951
  _globals['_PAYMENTREDIRECTPAGEDATA_AUTOTRIGGERACTIONS']._serialized_start=429
  _globals['_PAYMENTREDIRECTPAGEDATA_AUTOTRIGGERACTIONS']._serialized_end=662
  _globals['_PAYMENTREDIRECTPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_start=664
  _globals['_PAYMENTREDIRECTPAGEDATA_PAGEEVENTACTIONSENTRY']._serialized_end=741
  _globals['_PAYMENTREDIRECTPAGEDATA_ONLOADACTIONS']._serialized_start=744
  _globals['_PAYMENTREDIRECTPAGEDATA_ONLOADACTIONS']._serialized_end=951
# @@protoc_insertion_point(module_scope)
