# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/notification.proto
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
    'client/notification.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x63lient/notification.proto\x12\x06\x63lient\"\xa6\x01\n\x0cNotification\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61mpaign_id\x18\x02 \x01(\t\x12\x42\n\x19notification_render_state\x18\x03 \x01(\x0e\x32\x1f.client.NotificationRenderState\x12\x1a\n\x12ts_pt_timer_end_ms\x18\x04 \x01(\x04\x12\x14\n\x0cis_staggered\x18\x05 \x01(\x08*\xa1\x03\n\x17NotificationRenderState\x12)\n%NOTIFICATION_RENDER_STATE_UNSPECIFIED\x10\x00\x12%\n!NOTIFICATION_RENDER_STATE_SUCCESS\x10\x01\x12<\n8NOTIFICATION_RENDER_STATE_DISCARD_DUPLICATE_PN_SENT_TIME\x10\x02\x12\x33\n/NOTIFICATION_RENDER_STATE_DISCARD_PID_MIS_MATCH\x10\x03\x12=\n9NOTIFICATION_RENDER_STATE_DISCARD_SAME_CONTENT_IS_PLAYING\x10\x04\x12>\n:NOTIFICATION_RENDER_STATE_DISCARD_APP_PN_PERMISSION_DENIED\x10\x05\x12\x42\n>NOTIFICATION_RENDER_STATE_DISCARD_PN_CHANNEL_PERMISSION_DENIED\x10\x06\x42_\n\x1e\x63om.hotstar.event.model.clientP\x01Z;github.com/hotstar/data-event-schemas-go/hsanalytics/clientb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.notification_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036com.hotstar.event.model.clientP\001Z;github.com/hotstar/data-event-schemas-go/hsanalytics/client'
  _globals['_NOTIFICATIONRENDERSTATE']._serialized_start=207
  _globals['_NOTIFICATIONRENDERSTATE']._serialized_end=624
  _globals['_NOTIFICATION']._serialized_start=38
  _globals['_NOTIFICATION']._serialized_end=204
# @@protoc_insertion_point(module_scope)
