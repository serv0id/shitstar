# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/feature/device/push_notification.proto
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
    'api/feature/device/push_notification.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api.feature.device import platform_pb2 as api_dot_feature_dot_device_dot_platform__pb2
from options import opts_pb2 as options_dot_opts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/feature/device/push_notification.proto\x12\x12\x61pi.feature.device\x1a!api/feature/device/platform.proto\x1a\x12options/opts.proto\"\x8f\x02\n\x10PushNotification\x12\x14\n\x0c\x64\x65vice_token\x18\x01 \x01(\t\x12P\n\x11permission_status\x18\x02 \x01(\x0e\x32\x35.api.feature.device.PushNotification.PermissionStatus\"\x92\x01\n\x10PermissionStatus\x12!\n\x1dPERMISSION_STATUS_UNSPECIFIED\x10\x00\x12\x1c\n\x18PERMISSION_STATUS_DENIED\x10\x01\x12\x1d\n\x19PERMISSION_STATUS_GRANTED\x10\x02\x12\x1e\n\x1aPERMISSION_STATUS_SILENCED\x10\x03\x42w\n*com.hotstar.event.model.api.feature.deviceP\x01ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/deviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.feature.device.push_notification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.hotstar.event.model.api.feature.deviceP\001ZGgithub.com/hotstar/data-event-schemas-go/hsanalytics/api/feature/device'
  _globals['_PUSHNOTIFICATION']._serialized_start=122
  _globals['_PUSHNOTIFICATION']._serialized_end=393
  _globals['_PUSHNOTIFICATION_PERMISSIONSTATUS']._serialized_start=247
  _globals['_PUSHNOTIFICATION_PERMISSIONSTATUS']._serialized_end=393
# @@protoc_insertion_point(module_scope)
