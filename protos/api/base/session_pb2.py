# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/base/session.proto
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
    'api/base/session.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from options import opts_pb2 as options_dot_opts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/base/session.proto\x12\x08\x61pi.base\x1a\x12options/opts.proto\"\xc9\x02\n\x07Session\x12\x37\n\nsession_id\x18\x01 \x01(\x0b\x32#.api.base.Session.SessionIdentifier\x12,\n\x08\x63\x61mpaign\x18\x02 \x01(\x0b\x32\x1a.api.base.Session.Campaign\x12\x1b\n\x13ts_session_start_ms\x18\x03 \x01(\x04\x12\x13\n\x0b\x61ppsuite_id\x18\x04 \x01(\t\x12\x15\n\rappsuite_type\x18\x05 \x01(\t\x12\x14\n\x0cseo_referrer\x18\x06 \x01(\t\x1a\x1f\n\x11SessionIdentifier\x12\n\n\x02id\x18\x01 \x01(\t\x1aW\n\x08\x43\x61mpaign\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0e\n\x06medium\x18\x03 \x01(\t\x12\x0c\n\x04term\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\tBc\n com.hotstar.event.model.api.baseP\x01Z=github.com/hotstar/data-event-schemas-go/hsanalytics/api/baseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.base.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n com.hotstar.event.model.api.baseP\001Z=github.com/hotstar/data-event-schemas-go/hsanalytics/api/base'
  _globals['_SESSION']._serialized_start=57
  _globals['_SESSION']._serialized_end=386
  _globals['_SESSION_SESSIONIDENTIFIER']._serialized_start=266
  _globals['_SESSION_SESSIONIDENTIFIER']._serialized_end=297
  _globals['_SESSION_CAMPAIGN']._serialized_start=299
  _globals['_SESSION_CAMPAIGN']._serialized_end=386
# @@protoc_insertion_point(module_scope)
