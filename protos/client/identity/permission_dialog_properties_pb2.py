# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/identity/permission_dialog_properties.proto
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
    'client/identity/permission_dialog_properties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from component.identity import enum_pb2 as component_dot_identity_dot_enum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2client/identity/permission_dialog_properties.proto\x12\x0f\x63lient.identity\x1a\x1d\x63omponent/identity/enum.proto\"o\n\x1aPermissionDialogProperties\x12\x14\n\x0c\x64isplay_text\x18\x01 \x01(\t\x12;\n\x0fpermission_type\x18\x02 \x01(\x0e\x32\".component.identity.PermissionTypeBq\n\'com.hotstar.event.model.client.identityP\x01ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/identityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.identity.permission_dialog_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.hotstar.event.model.client.identityP\001ZDgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/identity'
  _globals['_PERMISSIONDIALOGPROPERTIES']._serialized_start=102
  _globals['_PERMISSIONDIALOGPROPERTIES']._serialized_end=213
# @@protoc_insertion_point(module_scope)
