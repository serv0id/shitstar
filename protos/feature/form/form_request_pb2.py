# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature/form/form_request.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from context import form_context_pb2 as context_dot_form__context__pb2
from feature.form import form_input_pb2 as feature_dot_form_dot_form__input__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x66\x65\x61ture/form/form_request.proto\x12\x0c\x66\x65\x61ture.form\x1a\x1a\x63ontext/form_context.proto\x1a\x1d\x66\x65\x61ture/form/form_input.proto\"g\n\x0b\x46ormRequest\x12*\n\x0c\x66orm_context\x18\x01 \x01(\x0b\x32\x14.context.FormContext\x12,\n\x0b\x66orm_inputs\x18\x02 \x03(\x0b\x32\x17.feature.form.FormInputB[\n!com.hotstar.ui.model.feature.formP\x01Z4github.com/hotstar/hs-core-ui-models-go/feature/formb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.form.form_request_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.hotstar.ui.model.feature.formP\001Z4github.com/hotstar/hs-core-ui-models-go/feature/form'
  _globals['_FORMREQUEST']._serialized_start=108
  _globals['_FORMREQUEST']._serialized_end=211
# @@protoc_insertion_point(module_scope)