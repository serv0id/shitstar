# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: action/subscribe_message.proto
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
    'action/subscribe_message.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.communication import message_pb2 as feature_dot_communication_dot_message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61\x63tion/subscribe_message.proto\x12\x06\x61\x63tion\x1a#feature/communication/message.proto\"]\n\x18SubscribeToMessageAction\x12\x41\n\rmessage_names\x18\x01 \x03(\x0e\x32*.feature.communication.Message.MessageNameBO\n\x1b\x63om.hotstar.ui.model.actionP\x01Z.github.com/hotstar/hs-core-ui-models-go/actionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action.subscribe_message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.actionP\001Z.github.com/hotstar/hs-core-ui-models-go/action'
  _globals['_SUBSCRIBETOMESSAGEACTION']._serialized_start=79
  _globals['_SUBSCRIBETOMESSAGEACTION']._serialized_end=172
# @@protoc_insertion_point(module_scope)
