# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/ads/sgai/sgai_error_properties.proto
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
    'client/ads/sgai/sgai_error_properties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.ads.sgai import content_meta_pb2 as client_dot_ads_dot_sgai_dot_content__meta__pb2
from client.ads.sgai import error_pb2 as client_dot_ads_dot_sgai_dot_error__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+client/ads/sgai/sgai_error_properties.proto\x12\x0f\x63lient.ads.sgai\x1a\"client/ads/sgai/content_meta.proto\x1a\x1b\x63lient/ads/sgai/error.proto\"\x82\x01\n\x13SgaiErrorProperties\x12\x32\n\x0c\x63ontent_meta\x18\x01 \x01(\x0b\x32\x1c.client.ads.sgai.ContentMeta\x12%\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x16.client.ads.sgai.Error\x12\x10\n\x08\x62reak_id\x18\x03 \x01(\tBq\n\'com.hotstar.event.model.client.ads.sgaiP\x01ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/ads/sgaib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.ads.sgai.sgai_error_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.hotstar.event.model.client.ads.sgaiP\001ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/ads/sgai'
  _globals['_SGAIERRORPROPERTIES']._serialized_start=130
  _globals['_SGAIERRORPROPERTIES']._serialized_end=260
# @@protoc_insertion_point(module_scope)
