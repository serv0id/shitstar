# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/feature/device/network.proto
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
    'api/feature/device/network.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n api/feature/device/network.proto\x12\x12\x61pi.feature.device\"\xf4\x01\n\x0bNetworkInfo\x12\x12\n\nis_wifi_on\x18\x01 \x01(\x08\x12\x11\n\twifi_ssid\x18\x02 \x01(\t\x12\x16\n\x0eis_cellular_on\x18\x03 \x01(\x08\x12\x18\n\x10\x63\x65llular_mcc_mnc\x18\x04 \x01(\t\x12\x0f\n\x03\x61sn\x18\x05 \x01(\rB\x02\x18\x01\x12\x35\n\x0cnetwork_type\x18\x06 \x01(\x0e\x32\x1f.api.feature.device.NetworkType\x12\x17\n\x0fis_bluetooth_on\x18\x07 \x01(\x08\x12\x1a\n\x12network_speed_kbps\x18\x08 \x01(\r\x12\x0f\n\x07\x63\x61rrier\x18\t \x01(\t*\xb0\x01\n\x0bNetworkType\x12\x1c\n\x18NETWORK_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14NETWORK_TYPE_OFFLINE\x10\x01\x12\x13\n\x0fNETWORK_TYPE_2G\x10\x02\x12\x13\n\x0fNETWORK_TYPE_3G\x10\x03\x12\x13\n\x0fNETWORK_TYPE_4G\x10\x04\x12\x13\n\x0fNETWORK_TYPE_5G\x10\x05\x12\x15\n\x11NETWORK_TYPE_WIFI\x10\x06\x42w\n*com.hotstar.event.model.api.feature.deviceP\x01ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/deviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.feature.device.network_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.hotstar.event.model.api.feature.deviceP\001ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/device'
  _globals['_NETWORKINFO'].fields_by_name['asn']._loaded_options = None
  _globals['_NETWORKINFO'].fields_by_name['asn']._serialized_options = b'\030\001'
  _globals['_NETWORKTYPE']._serialized_start=304
  _globals['_NETWORKTYPE']._serialized_end=480
  _globals['_NETWORKINFO']._serialized_start=57
  _globals['_NETWORKINFO']._serialized_end=301
# @@protoc_insertion_point(module_scope)
