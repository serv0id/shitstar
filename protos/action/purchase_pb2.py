# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action/purchase.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61\x63tion/purchase.proto\x12\x06\x61\x63tion\"\xa8\x01\n\x0ePurchaseAction\x12+\n\rpurchase_type\x18\x01 \x01(\x0e\x32\x14.action.PurchaseType\x12\x1a\n\x12\x63ommercial_pack_id\x18\x02 \x01(\t\x12\x13\n\x0bpayment_url\x18\x03 \x01(\t\x12\"\n\x1apayment_success_widget_url\x18\x04 \x01(\t\x12\x14\n\x0creplace_page\x18\x05 \x01(\x08*.\n\x0cPurchaseType\x12\x07\n\x03WEB\x10\x00\x12\x0c\n\x08WEB_VIEW\x10\x01\x12\x07\n\x03IAP\x10\x02\x42O\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.purchase_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_PURCHASETYPE']._serialized_start=204
  _globals['_PURCHASETYPE']._serialized_end=250
  _globals['_PURCHASEACTION']._serialized_start=34
  _globals['_PURCHASEACTION']._serialized_end=202
# @@protoc_insertion_point(module_scope)