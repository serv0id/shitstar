# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/enrichment/routing_table.proto
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
    'v2/enrichment/routing_table.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!v2/enrichment/routing_table.proto\x12\rv2.enrichment\x1a\x19google/protobuf/any.proto\"\xcd\x04\n\x0cRoutingTable\x12\x44\n\rrouting_table\x18\x01 \x03(\x0b\x32-.v2.enrichment.RoutingTable.RoutingTableEntry\x12\x46\n\x0e\x63\x61\x63he_metadata\x18\x02 \x03(\x0b\x32..v2.enrichment.RoutingTable.CacheMetadataEntry\x1a[\n\x11RoutingTableEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x35\n\x05value\x18\x02 \x01(\x0b\x32&.v2.enrichment.RoutingTable.Operations:\x02\x38\x01\x1aJ\n\x12\x43\x61\x63heMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\x1a\x85\x02\n\nOperations\x12?\n\x07replace\x18\x01 \x01(\x0b\x32..v2.enrichment.RoutingTable.Operations.Replace\x12G\n\x0cquery_params\x18\x02 \x03(\x0b\x32\x31.v2.enrichment.RoutingTable.Operations.QueryParam\x12\x0e\n\x06\x64omain\x18\x03 \x01(\t\x1a\x33\n\x07Replace\x12\x12\n\nto_replace\x18\x01 \x01(\t\x12\x14\n\x0creplace_with\x18\x02 \x01(\t\x1a(\n\nQueryParam\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tBV\n!com.hotstar.bff.api.v2.enrichmentP\x01Z/github.com/hotstar/hs-core-api-go/v2/enrichmentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.enrichment.routing_table_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.bff.api.v2.enrichmentP\001Z/github.com/hotstar/hs-core-api-go/v2/enrichment'
  _globals['_ROUTINGTABLE_ROUTINGTABLEENTRY']._loaded_options = None
  _globals['_ROUTINGTABLE_ROUTINGTABLEENTRY']._serialized_options = b'8\001'
  _globals['_ROUTINGTABLE_CACHEMETADATAENTRY']._loaded_options = None
  _globals['_ROUTINGTABLE_CACHEMETADATAENTRY']._serialized_options = b'8\001'
  _globals['_ROUTINGTABLE']._serialized_start=80
  _globals['_ROUTINGTABLE']._serialized_end=669
  _globals['_ROUTINGTABLE_ROUTINGTABLEENTRY']._serialized_start=238
  _globals['_ROUTINGTABLE_ROUTINGTABLEENTRY']._serialized_end=329
  _globals['_ROUTINGTABLE_CACHEMETADATAENTRY']._serialized_start=331
  _globals['_ROUTINGTABLE_CACHEMETADATAENTRY']._serialized_end=405
  _globals['_ROUTINGTABLE_OPERATIONS']._serialized_start=408
  _globals['_ROUTINGTABLE_OPERATIONS']._serialized_end=669
  _globals['_ROUTINGTABLE_OPERATIONS_REPLACE']._serialized_start=576
  _globals['_ROUTINGTABLE_OPERATIONS_REPLACE']._serialized_end=627
  _globals['_ROUTINGTABLE_OPERATIONS_QUERYPARAM']._serialized_start=629
  _globals['_ROUTINGTABLE_OPERATIONS_QUERYPARAM']._serialized_end=669
# @@protoc_insertion_point(module_scope)
