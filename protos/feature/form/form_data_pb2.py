# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: feature/form/form_data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x66\x65\x61ture/form/form_data.proto\x12\x0c\x66\x65\x61ture.form\"\x99\x02\n\x08\x46ormData\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x12\x34\n\nform_value\x18\x02 \x01(\x0b\x32 .feature.form.FormData.FormValue\x1a\x88\x01\n\tFormValue\x12\x36\n\ntext_value\x18\x01 \x01(\x0b\x32 .feature.form.FormData.TextValueH\x00\x12:\n\x0coption_value\x18\x02 \x01(\x0b\x32\".feature.form.FormData.OptionValueH\x00\x42\x07\n\x05value\x1a\x1a\n\tTextValue\x12\r\n\x05value\x18\x01 \x01(\t\x1a\x1e\n\x0bOptionValue\x12\x0f\n\x07options\x18\x01 \x03(\tB[\n!com.hotstar.ui.model.feature.formP\x01Z4github.com/hotstar/hs-core-ui-models-go/feature/formb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.form.form_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n!com.hotstar.ui.model.feature.formP\001Z4github.com/hotstar/hs-core-ui-models-go/feature/form'
  _globals['_FORMDATA']._serialized_start=47
  _globals['_FORMDATA']._serialized_end=328
  _globals['_FORMDATA_FORMVALUE']._serialized_start=132
  _globals['_FORMDATA_FORMVALUE']._serialized_end=268
  _globals['_FORMDATA_TEXTVALUE']._serialized_start=270
  _globals['_FORMDATA_TEXTVALUE']._serialized_end=296
  _globals['_FORMDATA_OPTIONVALUE']._serialized_start=298
  _globals['_FORMDATA_OPTIONVALUE']._serialized_end=328
# @@protoc_insertion_point(module_scope)