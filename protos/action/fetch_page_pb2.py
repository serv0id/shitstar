# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: action/fetch_page.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from protos.context import form_context_pb2 as context_dot_form__context__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x61\x63tion/fetch_page.proto\x12\x06\x61\x63tion\x1a\x19google/protobuf/any.proto\x1a\x1a\x63ontext/form_context.proto\"\xf2\x02\n\x0f\x46\x65tchPageAction\x12\x0b\n\x03url\x18\x01 \x01(\t\x12<\n\x0b\x61\x63tion_type\x18\x02 \x01(\x0e\x32\'.action.FetchPageAction.FetchActionType\x12\x33\n\tpage_data\x18\x03 \x01(\x0b\x32 .action.FetchPageAction.PageData\x1au\n\x08PageData\x12$\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x37\n\nform_input\x18\x02 \x01(\x0b\x32!.action.FetchPageAction.FormInputH\x00\x42\n\n\x08pagedata\x1a\x37\n\tFormInput\x12*\n\x0c\x66orm_context\x18\x01 \x01(\x0b\x32\x14.context.FormContext\"/\n\x0f\x46\x65tchActionType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0f\n\x0b\x46ORM_SUBMIT\x10\x01\x42O\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.fetch_page_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_FETCHPAGEACTION']._serialized_start=91
  _globals['_FETCHPAGEACTION']._serialized_end=461
  _globals['_FETCHPAGEACTION_PAGEDATA']._serialized_start=238
  _globals['_FETCHPAGEACTION_PAGEDATA']._serialized_end=355
  _globals['_FETCHPAGEACTION_FORMINPUT']._serialized_start=357
  _globals['_FETCHPAGEACTION_FORMINPUT']._serialized_end=412
  _globals['_FETCHPAGEACTION_FETCHACTIONTYPE']._serialized_start=414
  _globals['_FETCHPAGEACTION_FETCHACTIONTYPE']._serialized_end=461
# @@protoc_insertion_point(module_scope)