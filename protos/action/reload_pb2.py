# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action/reload.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x61\x63tion/reload.proto\x12\x06\x61\x63tion\"\x83\x03\n\x0cReloadAction\x12-\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x1c.action.ReloadAction.Context\x1a\xc8\x01\n\x07\x43ontext\x12\x38\n\x0cpage_context\x18\x01 \x01(\x0b\x32 .action.ReloadAction.PageContextH\x00\x12:\n\rspace_context\x18\x02 \x01(\x0b\x32!.action.ReloadAction.SpaceContextH\x00\x12<\n\x0ewidget_context\x18\x03 \x01(\x0b\x32\".action.ReloadAction.WidgetContextH\x00\x42\t\n\x07\x63ontext\x1a&\n\x0bPageContext\x12\x17\n\x0freload_with_url\x18\x01 \x01(\t\x1a\'\n\x0cSpaceContext\x12\x17\n\x0freload_with_url\x18\x01 \x01(\t\x1a(\n\rWidgetContext\x12\x17\n\x0freload_with_url\x18\x01 \x01(\tBO\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.reload_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_RELOADACTION']._serialized_start=32
  _globals['_RELOADACTION']._serialized_end=419
  _globals['_RELOADACTION_CONTEXT']._serialized_start=96
  _globals['_RELOADACTION_CONTEXT']._serialized_end=296
  _globals['_RELOADACTION_PAGECONTEXT']._serialized_start=298
  _globals['_RELOADACTION_PAGECONTEXT']._serialized_end=336
  _globals['_RELOADACTION_SPACECONTEXT']._serialized_start=338
  _globals['_RELOADACTION_SPACECONTEXT']._serialized_end=377
  _globals['_RELOADACTION_WIDGETCONTEXT']._serialized_start=379
  _globals['_RELOADACTION_WIDGETCONTEXT']._serialized_end=419
# @@protoc_insertion_point(module_scope)