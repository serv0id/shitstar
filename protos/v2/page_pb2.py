# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/page.proto
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
    'v2/page.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2 import space_pb2 as v2_dot_space__pb2
from v2 import refresh_page_pb2 as v2_dot_refresh__page__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rv2/page.proto\x12\x02v2\x1a\x0ev2/space.proto\x1a\x15v2/refresh_page.proto\x1a\x19google/protobuf/any.proto\"\xc1\x03\n\x04Page\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08template\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12$\n\x06spaces\x18\x04 \x03(\x0b\x32\x14.v2.Page.SpacesEntry\x12\"\n\x04\x64\x61ta\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x30\n\rdelivery_type\x18\x06 \x01(\x0e\x32\x19.v2.Page.PageDeliveryType\x12\x38\n\x14\x64ynamic_page_request\x18\x07 \x01(\x0b\x32\x16.v2.RefreshPageRequestB\x02\x18\x01\x12\x36\n\x15\x64\x65\x66\x65rred_page_request\x18\x08 \x01(\x0b\x32\x17.v2.DeferredPageRequest\x12\x10\n\x08page_url\x18\t \x01(\t\x12\x11\n\tpage_slug\x18\n \x01(\t\x1a\x38\n\x0bSpacesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x18\n\x05value\x18\x02 \x01(\x0b\x32\t.v2.Space:\x02\x38\x01\"=\n\x10PageDeliveryType\x12\n\n\x06STATIC\x10\x00\x12\x0f\n\x07\x44YNAMIC\x10\x01\x1a\x02\x08\x01\x12\x0c\n\x08\x44\x45\x46\x45RRED\x10\x02\x42@\n\x16\x63om.hotstar.bff.api.v2P\x01Z$github.com/hotstar/hs-core-api-go/v2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.page_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026com.hotstar.bff.api.v2P\001Z$github.com/hotstar/hs-core-api-go/v2'
  _globals['_PAGE_SPACESENTRY']._loaded_options = None
  _globals['_PAGE_SPACESENTRY']._serialized_options = b'8\001'
  _globals['_PAGE_PAGEDELIVERYTYPE'].values_by_name["DYNAMIC"]._loaded_options = None
  _globals['_PAGE_PAGEDELIVERYTYPE'].values_by_name["DYNAMIC"]._serialized_options = b'\010\001'
  _globals['_PAGE'].fields_by_name['dynamic_page_request']._loaded_options = None
  _globals['_PAGE'].fields_by_name['dynamic_page_request']._serialized_options = b'\030\001'
  _globals['_PAGE']._serialized_start=88
  _globals['_PAGE']._serialized_end=537
  _globals['_PAGE_SPACESENTRY']._serialized_start=418
  _globals['_PAGE_SPACESENTRY']._serialized_end=474
  _globals['_PAGE_PAGEDELIVERYTYPE']._serialized_start=476
  _globals['_PAGE_PAGEDELIVERYTYPE']._serialized_end=537
# @@protoc_insertion_point(module_scope)
