# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/enhancements/collection_transformer.proto
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
    'feature/enhancements/collection_transformer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1feature/enhancements/collection_transformer.proto\x12\x14\x66\x65\x61ture.enhancements\"\xec\x03\n\x15\x43ollectionTransformer\x12H\n\x07\x63onfigs\x18\x01 \x03(\x0b\x32\x37.feature.enhancements.CollectionTransformer.Transformer\x1a\xab\x01\n\x0bTransformer\x12G\n\x06\x64\x65rank\x18\x01 \x01(\x0b\x32\x35.feature.enhancements.CollectionTransformer.DerankingH\x00\x12K\n\x08\x64iscount\x18\x02 \x01(\x0b\x32\x37.feature.enhancements.CollectionTransformer.DiscountingH\x00\x42\x06\n\x04type\x1aR\n\tDeranking\x12\x45\n\x08services\x18\x01 \x03(\x0e\x32\x33.feature.enhancements.CollectionTransformer.Service\x1aT\n\x0b\x44iscounting\x12\x45\n\x08services\x18\x01 \x03(\x0e\x32\x33.feature.enhancements.CollectionTransformer.Service\"1\n\x07Service\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\r\n\tWATCHLIST\x10\x01\x12\x06\n\x02\x43W\x10\x02\x42k\n)com.hotstar.ui.model.feature.enhancementsP\x01Z<github.com/hotstar/hs-core-ui-models-go/feature/enhancementsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.enhancements.collection_transformer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)com.hotstar.ui.model.feature.enhancementsP\001Z<github.com/hotstar/hs-core-ui-models-go/feature/enhancements'
  _globals['_COLLECTIONTRANSFORMER']._serialized_start=76
  _globals['_COLLECTIONTRANSFORMER']._serialized_end=568
  _globals['_COLLECTIONTRANSFORMER_TRANSFORMER']._serialized_start=176
  _globals['_COLLECTIONTRANSFORMER_TRANSFORMER']._serialized_end=347
  _globals['_COLLECTIONTRANSFORMER_DERANKING']._serialized_start=349
  _globals['_COLLECTIONTRANSFORMER_DERANKING']._serialized_end=431
  _globals['_COLLECTIONTRANSFORMER_DISCOUNTING']._serialized_start=433
  _globals['_COLLECTIONTRANSFORMER_DISCOUNTING']._serialized_end=517
  _globals['_COLLECTIONTRANSFORMER_SERVICE']._serialized_start=519
  _globals['_COLLECTIONTRANSFORMER_SERVICE']._serialized_end=568
# @@protoc_insertion_point(module_scope)
