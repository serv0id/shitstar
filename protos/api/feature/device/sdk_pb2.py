# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/feature/device/sdk.proto
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
    'api/feature/device/sdk.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from options import opts_pb2 as options_dot_opts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/feature/device/sdk.proto\x12\x12\x61pi.feature.device\x1a\x12options/opts.proto\"\x91\x02\n\x03Sdk\x12\x34\n\tappsflyer\x18\x01 \x01(\x0b\x32!.api.feature.device.Sdk.AppsFlyer\x1a\xd3\x01\n\tAppsFlyer\x12\n\n\x02id\x18\x01 \x01(\t\x12I\n\x0f\x63onversion_type\x18\x02 \x01(\x0e\x32\x30.api.feature.device.Sdk.AppsFlyer.ConversionType\"o\n\x0e\x43onversionType\x12\x1f\n\x1b\x43ONVERSION_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x43ONVERSION_TYPE_ORGANIC\x10\x01\x12\x1f\n\x1b\x43ONVERSION_TYPE_NON_ORGANIC\x10\x02\x42w\n*com.hotstar.event.model.api.feature.deviceP\x01ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/deviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.feature.device.sdk_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.hotstar.event.model.api.feature.deviceP\001ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/device'
  _globals['_SDK']._serialized_start=73
  _globals['_SDK']._serialized_end=346
  _globals['_SDK_APPSFLYER']._serialized_start=135
  _globals['_SDK_APPSFLYER']._serialized_end=346
  _globals['_SDK_APPSFLYER_CONVERSIONTYPE']._serialized_start=235
  _globals['_SDK_APPSFLYER_CONVERSIONTYPE']._serialized_end=346
# @@protoc_insertion_point(module_scope)
