# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/enrichment/cachemetadata/watch_page_cache_meta.proto
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
    'v2/enrichment/cachemetadata/watch_page_cache_meta.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2.enrichment.cachemetadata import unified_cache_meta_pb2 as v2_dot_enrichment_dot_cachemetadata_dot_unified__cache__meta__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7v2/enrichment/cachemetadata/watch_page_cache_meta.proto\x12\x1bv2.enrichment.cachemetadata\x1a\x34v2/enrichment/cachemetadata/unified_cache_meta.proto\"\xd5\x01\n\x12WatchPageCacheMeta\x12\x14\n\x0cis_logged_in\x18\x01 \x01(\x08\x12\x0f\n\x07is_free\x18\x02 \x01(\x08\x12L\n\x13\x63lient_capabilities\x18\x03 \x01(\x0b\x32/.v2.enrichment.cachemetadata.ClientCapabilities\x12\x14\n\x0c\x61\x62_group_ids\x18\x04 \x03(\t\x12\x1c\n\x14\x63\x64n_distribution_key\x18\x05 \x01(\x05\x12\x16\n\x0emax_resolution\x18\x06 \x01(\tBd\n!com.hotstar.bff.api.v2.enrichmentP\x01Z=github.com/hotstar/hs-core-api-go/v2/enrichment/cachemetadatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.enrichment.cachemetadata.watch_page_cache_meta_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.bff.api.v2.enrichmentP\001Z=github.com/hotstar/hs-core-api-go/v2/enrichment/cachemetadata'
  _globals['_WATCHPAGECACHEMETA']._serialized_start=143
  _globals['_WATCHPAGECACHEMETA']._serialized_end=356
# @@protoc_insertion_point(module_scope)
