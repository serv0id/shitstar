# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: spacedata/tabbed_feed.proto
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
    'spacedata/tabbed_feed.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import space_data_commons_pb2 as base_dot_space__data__commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bspacedata/tabbed_feed.proto\x12\tspacedata\x1a\x1d\x62\x61se/space_data_commons.proto\"\xbb\x01\n\x13TabbedFeedSpaceData\x12\x32\n\x12space_data_commons\x18\x01 \x01(\x0b\x32\x16.base.SpaceDataCommons\x12\x37\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32).spacedata.TabbedFeedSpaceData.TabbedName\x12\x1b\n\x13hide_tabbed_headers\x18\x03 \x01(\x08\x1a\x1a\n\nTabbedName\x12\x0c\n\x04name\x18\x01 \x01(\tBU\n\x1e\x63om.hotstar.ui.model.spacedataP\x01Z1github.com/hotstar/hs-core-ui-models-go/spacedatab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'spacedata.tabbed_feed_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.hotstar.ui.model.spacedataP\001Z1github.com/hotstar/hs-core-ui-models-go/spacedata'
  _globals['_TABBEDFEEDSPACEDATA']._serialized_start=74
  _globals['_TABBEDFEEDSPACEDATA']._serialized_end=261
  _globals['_TABBEDFEEDSPACEDATA_TABBEDNAME']._serialized_start=235
  _globals['_TABBEDFEEDSPACEDATA_TABBEDNAME']._serialized_end=261
# @@protoc_insertion_point(module_scope)
