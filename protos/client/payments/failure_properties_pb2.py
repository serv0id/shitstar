# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/payments/failure_properties.proto
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
    'client/payments/failure_properties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(client/payments/failure_properties.proto\x12\x0f\x63lient.payments\"\xe4\x01\n\x11\x46\x61ilureProperties\x12\x44\n\x0c\x66\x61ilure_type\x18\x02 \x01(\x0e\x32..client.payments.FailureProperties.FailureType\x12\x16\n\x0e\x66\x61ilure_reason\x18\x03 \x01(\t\"q\n\x0b\x46\x61ilureType\x12\x1c\n\x18\x46\x41ILURE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x46\x41ILURE_TYPE_SDK\x10\x01\x12\x15\n\x11\x46\x41ILURE_TYPE_INIT\x10\x02\x12\x17\n\x13\x46\x41ILURE_TYPE_NOTIFY\x10\x03\x42q\n\'com.hotstar.event.model.client.paymentsP\x01ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/paymentsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.payments.failure_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.hotstar.event.model.client.paymentsP\001ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/payments'
  _globals['_FAILUREPROPERTIES']._serialized_start=62
  _globals['_FAILUREPROPERTIES']._serialized_end=290
  _globals['_FAILUREPROPERTIES_FAILURETYPE']._serialized_start=177
  _globals['_FAILUREPROPERTIES_FAILURETYPE']._serialized_end=290
# @@protoc_insertion_point(module_scope)
