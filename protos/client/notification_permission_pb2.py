# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/notification_permission.proto
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
    'client/notification_permission.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$client/notification_permission.proto\x12\x06\x63lient\"\x83\x04\n\x16NotificationPermission\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x43\n\nchanged_to\x18\x02 \x01(\x0e\x32/.client.NotificationPermission.PermissionStatus\x12\x42\n\rcategory_type\x18\x03 \x01(\x0e\x32+.client.NotificationPermission.CategoryType\x12\x13\n\x0b\x63\x61tegory_id\x18\x04 \x01(\t\x12\x45\n\x0c\x63hanged_from\x18\x05 \x01(\x0e\x32/.client.NotificationPermission.PermissionStatus\"\x92\x01\n\x10PermissionStatus\x12!\n\x1dPERMISSION_STATUS_UNSPECIFIED\x10\x00\x12\x1c\n\x18PERMISSION_STATUS_DENIED\x10\x01\x12\x1d\n\x19PERMISSION_STATUS_GRANTED\x10\x02\x12\x1e\n\x1aPERMISSION_STATUS_SILENCED\x10\x03\"_\n\x0c\x43\x61tegoryType\x12\x1d\n\x19\x43\x41TEGORY_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x43\x41TEGORY_TYPE_APP\x10\x01\x12\x19\n\x15\x43\x41TEGORY_TYPE_CHANNEL\x10\x02\x42_\n\x1e\x63om.hotstar.event.model.clientP\x01Z;github.com/hotstar/data-event-schemas-go/hsanalytics/clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.notification_permission_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.hotstar.event.model.clientP\001Z;github.com/hotstar/data-event-schemas-go/hsanalytics/client'
  _globals['_NOTIFICATIONPERMISSION']._serialized_start=49
  _globals['_NOTIFICATIONPERMISSION']._serialized_end=564
  _globals['_NOTIFICATIONPERMISSION_PERMISSIONSTATUS']._serialized_start=321
  _globals['_NOTIFICATIONPERMISSION_PERMISSIONSTATUS']._serialized_end=467
  _globals['_NOTIFICATIONPERMISSION_CATEGORYTYPE']._serialized_start=469
  _globals['_NOTIFICATIONPERMISSION_CATEGORYTYPE']._serialized_end=564
# @@protoc_insertion_point(module_scope)
