# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/enrichment/device_location.proto
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
    'v2/enrichment/device_location.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#v2/enrichment/device_location.proto\x12\rv2.enrichment\"\x99\x02\n\x0e\x44\x65viceLocation\x12\x10\n\x04\x63ity\x18\x01 \x01(\tB\x02\x18\x01\x12\x13\n\x07pincode\x18\x02 \x01(\tB\x02\x18\x01\x12\x11\n\x05state\x18\x03 \x01(\tB\x02\x18\x01\x12\x13\n\x07\x63ountry\x18\x04 \x01(\tB\x02\x18\x01\x12\x37\n\x10preferred_source\x18\x05 \x01(\x0e\x32\x1d.v2.enrichment.LocationSource\x12\x35\n\x04\x64\x61ta\x18\x06 \x03(\x0b\x32\'.v2.enrichment.DeviceLocation.DataEntry\x1aH\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12*\n\x05value\x18\x02 \x01(\x0b\x32\x1b.v2.enrichment.LocationData:\x02\x38\x01\"\xa3\x01\n\x0cLocationData\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\r\n\x05state\x18\x02 \x01(\t\x12\x0f\n\x07\x63ountry\x18\x03 \x01(\t\x12\x0f\n\x07pincode\x18\x04 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x05 \x01(\t\x12\x0b\n\x03lat\x18\x06 \x01(\t\x12\x0c\n\x04long\x18\x07 \x01(\t\x12\x10\n\x08\x63ity_std\x18\x08 \x01(\t\x12\x11\n\tstate_std\x18\t \x01(\t*\x82\x01\n\x0eLocationSource\x12\x12\n\x0eUNKNOWN_SOURCE\x10\x00\x12\r\n\tNETACUITY\x10\x01\x12\n\n\x06\x41KAMAI\x10\x02\x12\x1d\n\x19LOCATION_VIEW_CURRENT_LOC\x10\x03\x12\"\n\x1eLOCATION_VIEW_EXTERNAL_TRACKER\x10\x04\x42V\n!com.hotstar.bff.api.v2.enrichmentP\x01Z/github.com/hotstar/hs-core-api-go/v2/enrichmentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.enrichment.device_location_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.bff.api.v2.enrichmentP\001Z/github.com/hotstar/hs-core-api-go/v2/enrichment'
  _globals['_DEVICELOCATION_DATAENTRY']._loaded_options = None
  _globals['_DEVICELOCATION_DATAENTRY']._serialized_options = b'8\001'
  _globals['_DEVICELOCATION'].fields_by_name['city']._loaded_options = None
  _globals['_DEVICELOCATION'].fields_by_name['city']._serialized_options = b'\030\001'
  _globals['_DEVICELOCATION'].fields_by_name['pincode']._loaded_options = None
  _globals['_DEVICELOCATION'].fields_by_name['pincode']._serialized_options = b'\030\001'
  _globals['_DEVICELOCATION'].fields_by_name['state']._loaded_options = None
  _globals['_DEVICELOCATION'].fields_by_name['state']._serialized_options = b'\030\001'
  _globals['_DEVICELOCATION'].fields_by_name['country']._loaded_options = None
  _globals['_DEVICELOCATION'].fields_by_name['country']._serialized_options = b'\030\001'
  _globals['_LOCATIONSOURCE']._serialized_start=505
  _globals['_LOCATIONSOURCE']._serialized_end=635
  _globals['_DEVICELOCATION']._serialized_start=55
  _globals['_DEVICELOCATION']._serialized_end=336
  _globals['_DEVICELOCATION_DATAENTRY']._serialized_start=264
  _globals['_DEVICELOCATION_DATAENTRY']._serialized_end=336
  _globals['_LOCATIONDATA']._serialized_start=339
  _globals['_LOCATIONDATA']._serialized_end=502
# @@protoc_insertion_point(module_scope)
