# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: component/content/tray_position.proto
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
    'component/content/tray_position.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from component.content import tray_pb2 as component_dot_content_dot_tray__pb2
from component.content import widget_pb2 as component_dot_content_dot_widget__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%component/content/tray_position.proto\x12\x11\x63omponent.content\x1a\x1c\x63omponent/content/tray.proto\x1a\x1e\x63omponent/content/widget.proto\"v\n\x0cTrayPosition\x12)\n\x04tray\x18\x01 \x01(\x0b\x32\x17.component.content.TrayB\x02\x18\x01\x12\x10\n\x08position\x18\x02 \x01(\x05\x12)\n\x06widget\x18\x03 \x01(\x0b\x32\x19.component.content.WidgetBm\n!com.hotstar.event.model.componentP\x01ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/contentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.content.tray_position_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.event.model.componentP\001ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/content'
  _globals['_TRAYPOSITION'].fields_by_name['tray']._loaded_options = None
  _globals['_TRAYPOSITION'].fields_by_name['tray']._serialized_options = b'\030\001'
  _globals['_TRAYPOSITION']._serialized_start=122
  _globals['_TRAYPOSITION']._serialized_end=240
# @@protoc_insertion_point(module_scope)
