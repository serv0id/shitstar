# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base/widget_commons.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.base import analytics_pb2 as base_dot_analytics__pb2
from protos.base import actions_pb2 as base_dot_actions__pb2
from protos.base import data_bind_mechanism_pb2 as base_dot_data__bind__mechanism__pb2
from feature.motion_system import dynamic_visual_asset_config_pb2 as feature_dot_motion__system_dot_dynamic__visual__asset__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x62\x61se/widget_commons.proto\x12\x04\x62\x61se\x1a\x14\x62\x61se/analytics.proto\x1a\x12\x62\x61se/actions.proto\x1a\x1e\x62\x61se/data_bind_mechanism.proto\x1a\x37\x66\x65\x61ture/motion_system/dynamic_visual_asset_config.proto\"\x86\x02\n\rWidgetCommons\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12.\n\x0finstrumentation\x18\x03 \x01(\x0b\x32\x15.base.Instrumentation\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x12\x34\n\x13\x64\x61ta_bind_mechanism\x18\x06 \x01(\x0b\x32\x17.base.DataBindMechanism\x12\x44\n\x0bvda_configs\x18\x07 \x03(\x0b\x32/.feature.motion_system.DynamicVisualAssetConfigBK\n\x19\x63om.hotstar.ui.model.baseP\x01Z,github.com/hotstar/hs-core-ui-models-go/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'base.widget_commons_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031com.hotstar.ui.model.baseP\001Z,github.com/hotstar/hs-core-ui-models-go/base'
  _globals['_WIDGETCOMMONS']._serialized_start=167
  _globals['_WIDGETCOMMONS']._serialized_end=429
# @@protoc_insertion_point(module_scope)
