# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/success_action.proto
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
    'widget/success_action.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import actions_pb2 as base_dot_actions__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bwidget/success_action.proto\x12\x06widget\x1a\x12\x62\x61se/actions.proto\x1a\x19\x62\x61se/widget_commons.proto\"\xc4\x01\n\x13SuccessActionWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12.\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32 .widget.SuccessActionWidget.Data\x1aJ\n\x04\x44\x61ta\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x31\n\x13on_complete_actions\x18\x02 \x03(\x0b\x32\x14.base.Actions.ActionJ\x04\x08\x02\x10\x0b\x42\x30Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.success_action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_SUCCESSACTIONWIDGET']._serialized_start=87
  _globals['_SUCCESSACTIONWIDGET']._serialized_end=283
  _globals['_SUCCESSACTIONWIDGET_DATA']._serialized_start=203
  _globals['_SUCCESSACTIONWIDGET_DATA']._serialized_end=277
# @@protoc_insertion_point(module_scope)
