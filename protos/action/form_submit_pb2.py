# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action/form_submit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from context import form_context_pb2 as context_dot_form__context__pb2
from feature.form import form_input_pb2 as feature_dot_form_dot_form__input__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61\x63tion/form_submit.proto\x12\x06\x61\x63tion\x1a\x1a\x63ontext/form_context.proto\x1a\x1d\x66\x65\x61ture/form/form_input.proto\"K\n\x10\x46ormSubmitAction\x12\x0b\n\x03url\x18\x01 \x01(\t\x12*\n\x0c\x66orm_context\x18\x02 \x01(\x0b\x32\x14.context.FormContextBO\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.form_submit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_FORMSUBMITACTION']._serialized_start=95
  _globals['_FORMSUBMITACTION']._serialized_end=170
# @@protoc_insertion_point(module_scope)
