# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: options/opts.proto
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
    'options/opts.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12options/opts.proto\x12\x07options\x1a google/protobuf/descriptor.proto\"\\\n\x0fPropertyOptions\x12\x0e\n\x06is_pii\x18\x01 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\tis_traits\x18\x03 \x01(\x08\x12\x11\n\tjson_path\x18\x04 \x01(\t\"6\n\x0c\x45ventOptions\x12\x11\n\tis_native\x18\x01 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t:K\n\x08property\x12\x1d.google.protobuf.FieldOptions\x18\xa2\xc2\x1e \x01(\x0b\x32\x18.options.PropertyOptions:<\n\x13\x63hild_fields_prefix\x12\x1d.google.protobuf.FieldOptions\x18\xa4\xc2\x1e \x01(\t:>\n\x15\x64\x61ta_lake_column_name\x12\x1d.google.protobuf.FieldOptions\x18\xa5\xc2\x1e \x01(\t:D\n\x05\x65vent\x12\x1c.google.protobuf.FileOptions\x18\xa1\xc2\x1e \x01(\x0b\x32\x15.options.EventOptions:<\n\x11json_field_prefix\x12\x1f.google.protobuf.MessageOptions\x18\xa3\xc2\x1e \x01(\tBa\n\x1f\x63om.hotstar.event.model.optionsP\x01Z<github.com/hotstar/data-event-schemas-go/hsanalytics/optionsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'options.opts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.hotstar.event.model.optionsP\001Z<github.com/hotstar/data-event-schemas-go/hsanalytics/options'
  _globals['_PROPERTYOPTIONS']._serialized_start=65
  _globals['_PROPERTYOPTIONS']._serialized_end=157
  _globals['_EVENTOPTIONS']._serialized_start=159
  _globals['_EVENTOPTIONS']._serialized_end=213
# @@protoc_insertion_point(module_scope)
