# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: component/content/show_additional_attributes.proto
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
    'component/content/show_additional_attributes.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2component/content/show_additional_attributes.proto\x12\x11\x63omponent.content\"o\n\x18ShowAdditionalAttributes\x12\x0e\n\x06is_btv\x18\x01 \x01(\x08\x12.\n\tshow_type\x18\x02 \x01(\x0e\x32\x1b.component.content.ShowType\x12\x13\n\x0bis_archived\x18\x03 \x01(\x08*W\n\x08ShowType\x12\x19\n\x15SHOW_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12SHOW_TYPE_SEASONAL\x10\x01\x12\x18\n\x14SHOW_TYPE_SEQUENTIAL\x10\x02\x42m\n!com.hotstar.event.model.componentP\x01ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/contentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.content.show_additional_attributes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.event.model.componentP\001ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/content'
  _globals['_SHOWTYPE']._serialized_start=186
  _globals['_SHOWTYPE']._serialized_end=273
  _globals['_SHOWADDITIONALATTRIBUTES']._serialized_start=73
  _globals['_SHOWADDITIONALATTRIBUTES']._serialized_end=184
# @@protoc_insertion_point(module_scope)
