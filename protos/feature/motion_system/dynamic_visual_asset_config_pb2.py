# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/motion_system/dynamic_visual_asset_config.proto
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
    'feature/motion_system/dynamic_visual_asset_config.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.motion_system import dynamic_visual_asset_name_pb2 as feature_dot_motion__system_dot_dynamic__visual__asset__name__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7feature/motion_system/dynamic_visual_asset_config.proto\x12\x15\x66\x65\x61ture.motion_system\x1a\x35\x66\x65\x61ture/motion_system/dynamic_visual_asset_name.proto\"\xbf\x04\n\x18\x44ynamicVisualAssetConfig\x12;\n\x04name\x18\x01 \x01(\x0e\x32-.feature.motion_system.DynamicVisualAssetName\x12\x14\n\x0cis_immediate\x18\x02 \x01(\x08\x12\x1a\n\x12remove_when_paused\x18\x03 \x01(\x08\x12\x13\n\x0bis_infinite\x18\x04 \x01(\x08\x12h\n\x0epriority_order\x18\x05 \x01(\x0e\x32P.feature.motion_system.DynamicVisualAssetConfig.DynamicVisaualAssetPriorityOrder\x12\\\n\x08\x63\x61tegory\x18\x06 \x01(\x0e\x32J.feature.motion_system.DynamicVisualAssetConfig.DynamicVisualAssetCategory\"}\n DynamicVisaualAssetPriorityOrder\x12\x1e\n\x1aUNSPECIFIED_PRIORITY_ORDER\x10\x00\x12\t\n\x05P_ONE\x10\x01\x12\t\n\x05P_TWO\x10\x02\x12\x0b\n\x07P_THREE\x10\x03\x12\n\n\x06P_FOUR\x10\x04\x12\n\n\x06P_FIVE\x10\x05\"X\n\x1a\x44ynamicVisualAssetCategory\x12\x18\n\x14UNSPECIFIED_CATEGORY\x10\x00\x12\t\n\x05HEAVY\x10\x01\x12\n\n\x06MEDIUM\x10\x02\x12\t\n\x05LIGHT\x10\x03\x42m\n*com.hotstar.ui.model.feature.motion_systemP\x01Z=github.com/hotstar/hs-core-ui-models-go/feature/motion_systemb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.motion_system.dynamic_visual_asset_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.hotstar.ui.model.feature.motion_systemP\001Z=github.com/hotstar/hs-core-ui-models-go/feature/motion_system'
  _globals['_DYNAMICVISUALASSETCONFIG']._serialized_start=138
  _globals['_DYNAMICVISUALASSETCONFIG']._serialized_end=713
  _globals['_DYNAMICVISUALASSETCONFIG_DYNAMICVISAUALASSETPRIORITYORDER']._serialized_start=498
  _globals['_DYNAMICVISUALASSETCONFIG_DYNAMICVISAUALASSETPRIORITYORDER']._serialized_end=623
  _globals['_DYNAMICVISUALASSETCONFIG_DYNAMICVISUALASSETCATEGORY']._serialized_start=625
  _globals['_DYNAMICVISUALASSETCONFIG_DYNAMICVISUALASSETCATEGORY']._serialized_end=713
# @@protoc_insertion_point(module_scope)
