# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: component/subs/plan.proto
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
    'component/subs/plan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from component.subs import plan_duration_pb2 as component_dot_subs_dot_plan__duration__pb2
from component.subs import plan_price_pb2 as component_dot_subs_dot_plan__price__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63omponent/subs/plan.proto\x12\x0e\x63omponent.subs\x1a\"component/subs/plan_duration.proto\x1a\x1f\x63omponent/subs/plan_price.proto\"\x90\x01\n\x04Plan\x12\x0f\n\x07plan_id\x18\x01 \x01(\t\x12\x13\n\x0bplan_family\x18\x02 \x01(\t\x12\x33\n\rplan_duration\x18\x03 \x01(\x0b\x32\x1c.component.subs.PlanDuration\x12-\n\nplan_price\x18\x04 \x01(\x0b\x32\x19.component.subs.PlanPriceBj\n!com.hotstar.event.model.componentP\x01ZCgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/subsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.subs.plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.event.model.componentP\001ZCgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/subs'
  _globals['_PLAN']._serialized_start=115
  _globals['_PLAN']._serialized_end=259
# @@protoc_insertion_point(module_scope)
