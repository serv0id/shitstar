# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action/player_control_action.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos.feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"action/player_control_action.proto\x12\x06\x61\x63tion\x1a\x19\x66\x65\x61ture/image/image.proto\"\xf2\x01\n\x13PlayerControlAction\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\".action.PlayerControlAction.Params\x1ao\n\x06Params\x12[\n\x1b\x63hange_video_quality_params\x18\x01 \x01(\x0b\x32\x34.action.PlayerControlAction.ChangeVideoQualityParamsH\x00\x42\x08\n\x06params\x1a\x36\n\x18\x43hangeVideoQualityParams\x12\x1a\n\x12video_quality_code\x18\x01 \x01(\tBO\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.player_control_action_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_PLAYERCONTROLACTION']._serialized_start=74
  _globals['_PLAYERCONTROLACTION']._serialized_end=316
  _globals['_PLAYERCONTROLACTION_PARAMS']._serialized_start=149
  _globals['_PLAYERCONTROLACTION_PARAMS']._serialized_end=260
  _globals['_PLAYERCONTROLACTION_CHANGEVIDEOQUALITYPARAMS']._serialized_start=262
  _globals['_PLAYERCONTROLACTION_CHANGEVIDEOQUALITYPARAMS']._serialized_end=316
# @@protoc_insertion_point(module_scope)
