# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/bugreporting/bug_reporting_events.proto
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
    'client/bugreporting/bug_reporting_events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.client/bugreporting/bug_reporting_events.proto\x12\x13\x63lient.bugreporting\"\x9c\x06\n\x0e\x42ugReportEvent\x12N\n\x0e\x62rt_event_type\x18\x01 \x01(\x0e\x32\x36.client.bugreporting.BugReportEvent.BugReportEventType\x12\x11\n\tcpu_usage\x18\x02 \x01(\x05\x12\x14\n\x0cmemory_usage\x18\x03 \x01(\x01\x12\x17\n\x0f\x62rt_sdk_version\x18\x04 \x01(\t\"\xf7\x04\n\x12\x42ugReportEventType\x12)\n%BUG_REPORT_EVENT_TYPE_BRT_UNSPECIFIED\x10\x00\x12%\n!BUG_REPORT_EVENT_TYPE_BRT_INVOKED\x10\x01\x12\x36\n2BUG_REPORT_EVENT_TYPE_BRT_DB_INITIALIZATION_FAILED\x10\x02\x12,\n(BUG_REPORT_EVENT_TYPE_BRT_DB_INITIALIZED\x10\x03\x12\x30\n,BUG_REPORT_EVENT_TYPE_BRT_BUG_SCREEN_INVOKED\x10\x04\x12\x31\n-BUG_REPORT_EVENT_TYPE_BRT_BUG_REPORT_DROP_OFF\x10\x05\x12.\n*BUG_REPORT_EVENT_TYPE_BRT_BUG_REPORT_SAVED\x10\x06\x12)\n%BUG_REPORT_EVENT_TYPE_BRT_NO_INTERNET\x10\x07\x12\x35\n1BUG_REPORT_EVENT_TYPE_BRT_NON_REPORTED_BUGS_COUNT\x10\x08\x12,\n(BUG_REPORT_EVENT_TYPE_BRT_REPORT_SUCCESS\x10\t\x12,\n(BUG_REPORT_EVENT_TYPE_BRT_REPORT_FAILURE\x10\n\x12+\n\'BUG_REPORT_EVENT_TYPE_BRT_REPORT_DELETE\x10\x0b\x12)\n%BUG_REPORT_EVENT_TYPE_BRT_INITIALIZED\x10\x0c\x42y\n+com.hotstar.event.model.client.bugreportingP\x01ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/bugreportingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.bugreporting.bug_reporting_events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n+com.hotstar.event.model.client.bugreportingP\001ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/bugreporting'
  _globals['_BUGREPORTEVENT']._serialized_start=72
  _globals['_BUGREPORTEVENT']._serialized_end=868
  _globals['_BUGREPORTEVENT_BUGREPORTEVENTTYPE']._serialized_start=237
  _globals['_BUGREPORTEVENT_BUGREPORTEVENTTYPE']._serialized_end=868
# @@protoc_insertion_point(module_scope)
