# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/intervention/interventions.proto
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
    'feature/intervention/interventions.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.intervention import preroll_intervention_pb2 as feature_dot_intervention_dot_preroll__intervention__pb2
from feature.intervention import action_intervention_pb2 as feature_dot_intervention_dot_action__intervention__pb2
from feature.intervention import refresh_intervention_pb2 as feature_dot_intervention_dot_refresh__intervention__pb2
from feature.intervention import widget_visibility_intervention_pb2 as feature_dot_intervention_dot_widget__visibility__intervention__pb2
from feature.intervention import compose_display_intervention_pb2 as feature_dot_intervention_dot_compose__display__intervention__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(feature/intervention/interventions.proto\x12\x14\x66\x65\x61ture.intervention\x1a/feature/intervention/preroll_intervention.proto\x1a.feature/intervention/action_intervention.proto\x1a/feature/intervention/refresh_intervention.proto\x1a\x39\x66\x65\x61ture/intervention/widget_visibility_intervention.proto\x1a\x37\x66\x65\x61ture/intervention/compose_display_intervention.proto\x1a\x19google/protobuf/any.proto\"\xe1\x04\n\x0cIntervention\x12\x14\n\x0c\x65vent_time_s\x18\x01 \x01(\x05\x12\x14\n\x0cis_skippable\x18\x02 \x01(\x08\x12\x35\n\x04meta\x18\x03 \x01(\x0b\x32\'.feature.intervention.Intervention.Meta\x12\x39\n\x06repeat\x18\x04 \x01(\x0b\x32).feature.intervention.Intervention.Repeat\x1a\x8f\x03\n\x04Meta\x12<\n\x07preroll\x18\x01 \x01(\x0b\x32).feature.intervention.PrerollInterventionH\x00\x12I\n\x0e\x61\x63tion_handler\x18\x02 \x01(\x0b\x32/.feature.intervention.ActionHandlerInterventionH\x00\x12\'\n\x07refresh\x18\x03 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12/\n\x0fplayback_action\x18\x04 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12O\n\x11widget_visibility\x18\x05 \x01(\x0b\x32\x32.feature.intervention.WidgetVisibilityInterventionH\x00\x12K\n\x0f\x63ompose_display\x18\x06 \x01(\x0b\x32\x30.feature.intervention.ComposeDisplayInterventionH\x00\x42\x06\n\x04meta\x1a!\n\x06Repeat\x12\x17\n\x0f\x64uration_time_s\x18\x01 \x01(\x05\x42k\n)com.hotstar.ui.model.feature.interventionP\x01Z<github.com/hotstar/hs-core-ui-models-go/feature/interventionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.intervention.interventions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n)com.hotstar.ui.model.feature.interventionP\001Z<github.com/hotstar/hs-core-ui-models-go/feature/intervention'
  _globals['_INTERVENTION']._serialized_start=356
  _globals['_INTERVENTION']._serialized_end=965
  _globals['_INTERVENTION_META']._serialized_start=531
  _globals['_INTERVENTION_META']._serialized_end=930
  _globals['_INTERVENTION_REPEAT']._serialized_start=932
  _globals['_INTERVENTION_REPEAT']._serialized_end=965
# @@protoc_insertion_point(module_scope)
