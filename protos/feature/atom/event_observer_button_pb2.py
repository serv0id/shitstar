# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/atom/event_observer_button.proto
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
    'feature/atom/event_observer_button.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.atom import button_pb2 as feature_dot_atom_dot_button__pb2
from feature.atom import toggle_button_pb2 as feature_dot_atom_dot_toggle__button__pb2
from feature.atom import toggle_lottie_button_pb2 as feature_dot_atom_dot_toggle__lottie__button__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(feature/atom/event_observer_button.proto\x12\x0c\x66\x65\x61ture.atom\x1a\x19\x66\x65\x61ture/atom/button.proto\x1a feature/atom/toggle_button.proto\x1a\'feature/atom/toggle_lottie_button.proto\"c\n\x13\x45ventObserverButton\x12)\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1a.feature.atom.FeatureEvent\x12!\n\x06\x62utton\x18\x02 \x01(\x0b\x32\x11.feature.atom.CTA\"]\n\x0c\x46\x65\x61tureEvent\x12\x12\n\nevent_name\x18\x01 \x01(\t\x12\x12\n\nidentifier\x18\x02 \x01(\t\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.feature.atom.EventData\"\xab\x01\n\x03\x43TA\x12\x33\n\rtoggle_button\x18\x01 \x01(\x0b\x32\x1a.feature.atom.ToggleButtonH\x00\x12@\n\x14toggle_lottie_button\x18\x02 \x01(\x0b\x32 .feature.atom.ToggleLottieButtonH\x00\x12&\n\x06\x62utton\x18\x03 \x01(\x0b\x32\x14.feature.atom.ButtonH\x00\x42\x05\n\x03\x63ta\"\xa1\x01\n\tEventData\x12:\n\x11toggle_event_data\x18\x01 \x01(\x0b\x32\x1d.feature.atom.ToggleEventDataH\x00\x12J\n\x16player_subs_nudge_data\x18\x02 \x01(\x0b\x32(.feature.atom.PlayerFreePreviewNudgeDataH\x00\x42\x0c\n\nevent_data\"&\n\x0fToggleEventData\x12\x13\n\x0bis_selected\x18\x01 \x01(\x08\"\xcf\x01\n\x1aPlayerFreePreviewNudgeData\x12\x18\n\x10total_duration_s\x18\x01 \x01(\x03\x12\x1e\n\x16start_shown_duration_s\x18\x02 \x01(\x03\x12\x1c\n\x14\x65nd_shown_duration_s\x18\x03 \x01(\x03\x12\x19\n\x11timer_placeholder\x18\x04 \x01(\t\x12\x1c\n\x14\x63urrent_time_stamp_s\x18\x05 \x01(\x03\x12 \n\x18seek_thumbnail_subs_info\x18\x06 \x01(\tB[\n!com.hotstar.ui.model.feature.atomP\x01Z4github.com/hotstar/hs-core-ui-models-go/feature/atomb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.atom.event_observer_button_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.ui.model.feature.atomP\001Z4github.com/hotstar/hs-core-ui-models-go/feature/atom'
  _globals['_EVENTOBSERVERBUTTON']._serialized_start=160
  _globals['_EVENTOBSERVERBUTTON']._serialized_end=259
  _globals['_FEATUREEVENT']._serialized_start=261
  _globals['_FEATUREEVENT']._serialized_end=354
  _globals['_CTA']._serialized_start=357
  _globals['_CTA']._serialized_end=528
  _globals['_EVENTDATA']._serialized_start=531
  _globals['_EVENTDATA']._serialized_end=692
  _globals['_TOGGLEEVENTDATA']._serialized_start=694
  _globals['_TOGGLEEVENTDATA']._serialized_end=732
  _globals['_PLAYERFREEPREVIEWNUDGEDATA']._serialized_start=735
  _globals['_PLAYERFREEPREVIEWNUDGEDATA']._serialized_end=942
# @@protoc_insertion_point(module_scope)
