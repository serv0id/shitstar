# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/ads/ads_properties.proto
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
    'client/ads/ads_properties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.ads import common_pb2 as client_dot_ads_dot_common__pb2
from client.ads import error_pb2 as client_dot_ads_dot_error__pb2
from client.ads import play_error_pb2 as client_dot_ads_dot_play__error__pb2
from client.ads import received_pb2 as client_dot_ads_dot_received__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63lient/ads/ads_properties.proto\x12\nclient.ads\x1a\x17\x63lient/ads/common.proto\x1a\x16\x63lient/ads/error.proto\x1a\x1b\x63lient/ads/play_error.proto\x1a\x19\x63lient/ads/received.proto\"\xd8\x02\n\rAdsProperties\x12\x19\n\ruser_segments\x18\x01 \x03(\tB\x02\x18\x01\x12\x0f\n\x03pid\x18\x02 \x01(\tB\x02\x18\x01\x12\x10\n\x04\x61\x61id\x18\x03 \x01(\tB\x02\x18\x01\x12\x14\n\x08\x61\x61id_lat\x18\x04 \x01(\tB\x02\x18\x01\x12\x10\n\x04idfa\x18\x05 \x01(\tB\x02\x18\x01\x12\x14\n\x08idfa_lat\x18\x06 \x01(\tB\x02\x18\x01\x12-\n\x11\x63ommon_properties\x18\x07 \x01(\x0b\x32\x12.client.ads.Common\x12\x35\n\x13received_properties\x18\x08 \x01(\x0b\x32\x14.client.ads.ReceivedB\x02\x18\x01\x12+\n\x10\x65rror_properties\x18\t \x01(\x0b\x32\x11.client.ads.Error\x12\x38\n\x15play_error_properties\x18\n \x01(\x0b\x32\x15.client.ads.PlayErrorB\x02\x18\x01\x42g\n\"com.hotstar.event.model.client.adsP\x01Z?github.com/hotstar/data-event-schemas-go/hsanalytics/client/adsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.ads.ads_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hotstar.event.model.client.adsP\001Z?github.com/hotstar/data-event-schemas-go/hsanalytics/client/ads'
  _globals['_ADSPROPERTIES'].fields_by_name['user_segments']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['user_segments']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES'].fields_by_name['pid']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['pid']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES'].fields_by_name['aaid']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['aaid']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES'].fields_by_name['aaid_lat']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['aaid_lat']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES'].fields_by_name['idfa']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['idfa']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES'].fields_by_name['idfa_lat']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['idfa_lat']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES'].fields_by_name['received_properties']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['received_properties']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES'].fields_by_name['play_error_properties']._loaded_options = None
  _globals['_ADSPROPERTIES'].fields_by_name['play_error_properties']._serialized_options = b'\030\001'
  _globals['_ADSPROPERTIES']._serialized_start=153
  _globals['_ADSPROPERTIES']._serialized_end=497
# @@protoc_insertion_point(module_scope)
