# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/enrichment/client_cache.proto
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
    'v2/enrichment/client_cache.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n v2/enrichment/client_cache.proto\x12\rv2.enrichment\"\x99\x02\n\x0b\x43lientCache\x12\x39\n\x05items\x18\x01 \x03(\x0b\x32*.v2.enrichment.ClientCache.ClientCacheItem\x1a\x8b\x01\n\x0f\x43lientCacheItem\x12;\n\titem_type\x18\x01 \x01(\x0e\x32(.v2.enrichment.ClientCache.CacheItemType\x12\x19\n\x11unique_identifier\x18\x02 \x01(\x04\x12 \n\x18last_updated_at_in_epoch\x18\x03 \x01(\x04\"A\n\rCacheItemType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\n\n\x06WIDGET\x10\x01\x12\x08\n\x04PAGE\x10\x02\x12\t\n\x05SPACE\x10\x03\x42V\n!com.hotstar.bff.api.v2.enrichmentP\x01Z/github.com/hotstar/hs-core-api-go/v2/enrichmentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.enrichment.client_cache_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.bff.api.v2.enrichmentP\001Z/github.com/hotstar/hs-core-api-go/v2/enrichment'
  _globals['_CLIENTCACHE']._serialized_start=52
  _globals['_CLIENTCACHE']._serialized_end=333
  _globals['_CLIENTCACHE_CLIENTCACHEITEM']._serialized_start=127
  _globals['_CLIENTCACHE_CLIENTCACHEITEM']._serialized_end=266
  _globals['_CLIENTCACHE_CACHEITEMTYPE']._serialized_start=268
  _globals['_CLIENTCACHE_CACHEITEMTYPE']._serialized_end=333
# @@protoc_insertion_point(module_scope)
