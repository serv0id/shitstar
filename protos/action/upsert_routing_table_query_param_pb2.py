# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: action/upsert_routing_table_query_param.proto
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
    'action/upsert_routing_table_query_param.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-action/upsert_routing_table_query_param.proto\x12\x06\x61\x63tion\"\xb0\x01\n\"UpsertRoutingTableQueryParamAction\x12\x13\n\x0brouting_key\x18\x01 \x01(\t\x12K\n\x0cquery_params\x18\x02 \x03(\x0b\x32\x35.action.UpsertRoutingTableQueryParamAction.QueryParam\x1a(\n\nQueryParam\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tBO\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.upsert_routing_table_query_param_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_UPSERTROUTINGTABLEQUERYPARAMACTION']._serialized_start=58
  _globals['_UPSERTROUTINGTABLEQUERYPARAMACTION']._serialized_end=234
  _globals['_UPSERTROUTINGTABLEQUERYPARAMACTION_QUERYPARAM']._serialized_start=194
  _globals['_UPSERTROUTINGTABLEQUERYPARAMACTION_QUERYPARAM']._serialized_end=234
# @@protoc_insertion_point(module_scope)
