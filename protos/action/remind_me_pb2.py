# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action/remind_me.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61\x63tion/remind_me.proto\x12\x06\x61\x63tion\"4\n\x0eRemindMeAction\x12\"\n\x04info\x18\x01 \x01(\x0b\x32\x14.action.RemindMeInfo\"R\n\x0cRemindMeInfo\x12\x12\n\ncontent_id\x18\x01 \x01(\t\x12\x17\n\x0fis_reminder_set\x18\x02 \x01(\x08\x12\x15\n\rcontent_title\x18\x03 \x01(\tBO\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.remind_me_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_REMINDMEACTION']._serialized_start=34
  _globals['_REMINDMEACTION']._serialized_end=86
  _globals['_REMINDMEINFO']._serialized_start=88
  _globals['_REMINDMEINFO']._serialized_end=170
# @@protoc_insertion_point(module_scope)
