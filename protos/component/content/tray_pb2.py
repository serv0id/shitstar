# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: component/content/tray.proto
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
    'component/content/tray.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x63omponent/content/tray.proto\x12\x11\x63omponent.content\"\xd5\x01\n\x04Tray\x12\x0f\n\x07tray_id\x18\x01 \x01(\t\x12\x11\n\ttray_name\x18\x02 \x01(\t\x12\x15\n\rtray_position\x18\x03 \x01(\x03\x12\x1b\n\x13localised_tray_name\x18\x04 \x01(\t\x12-\n\x06source\x18\x05 \x01(\x0e\x32\x1d.component.content.TraySource\x12\r\n\x05logic\x18\x06 \x01(\t\x12\x18\n\x10\x64isplay_language\x18\x07 \x01(\t\x12\x19\n\x11initiation_source\x18\x08 \x01(\t:\x02\x18\x01*W\n\nTraySource\x12\x1b\n\x17TRAY_SOURCE_UNSPECIFIED\x10\x00\x12\x17\n\x13TRAY_SOURCE_PERSONA\x10\x01\x12\x13\n\x0fTRAY_SOURCE_CMS\x10\x02\x42m\n!com.hotstar.event.model.componentP\x01ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/contentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.content.tray_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.event.model.componentP\001ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/content'
  _globals['_TRAY']._loaded_options = None
  _globals['_TRAY']._serialized_options = b'\030\001'
  _globals['_TRAYSOURCE']._serialized_start=267
  _globals['_TRAYSOURCE']._serialized_end=354
  _globals['_TRAY']._serialized_start=52
  _globals['_TRAY']._serialized_end=265
# @@protoc_insertion_point(module_scope)
