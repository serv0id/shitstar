# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/payments/payment_response.proto
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
    'client/payments/payment_response.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.payments import payment_common_properties_pb2 as client_dot_payments_dot_payment__common__properties__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&client/payments/payment_response.proto\x12\x0f\x63lient.payments\x1a/client/payments/payment_common_properties.proto\"\x87\x01\n\x0fPaymentResponse\x12K\n\x19payment_common_properties\x18\x01 \x01(\x0b\x32(.client.payments.PaymentCommonProperties\x12\x15\n\rresponse_time\x18\x02 \x01(\x03\x12\x10\n\x08order_id\x18\x03 \x01(\tBq\n\'com.hotstar.event.model.client.paymentsP\x01ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/paymentsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.payments.payment_response_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.hotstar.event.model.client.paymentsP\001ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/payments'
  _globals['_PAYMENTRESPONSE']._serialized_start=109
  _globals['_PAYMENTRESPONSE']._serialized_end=244
# @@protoc_insertion_point(module_scope)
