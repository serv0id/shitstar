# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/watch/nudge_viewed.proto
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
    'client/watch/nudge_viewed.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63lient/watch/nudge_viewed.proto\x12\x0c\x63lient.watch\"\xb1\x01\n\x0bNudgeViewed\x12+\n\nnudge_type\x18\x01 \x01(\x0e\x32\x17.client.watch.NudgeType\x12,\n\x04meta\x18\x02 \x01(\x0b\x32\x1e.client.watch.NudgeViewed.Meta\x1aG\n\x04Meta\x12\x37\n\x0fnetwork_problem\x18\x01 \x01(\x0b\x32\x1c.client.watch.NetworkProblemH\x00\x42\x06\n\x04meta\"F\n\x0eNetworkProblem\x12\x14\n\x0c\x62itrate_kbps\x18\x01 \x01(\x02\x12\x1e\n\x16indicated_bitrate_kbps\x18\x02 \x01(\x02*G\n\tNudgeType\x12\x1a\n\x16NUDGE_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aNUDGE_TYPE_NETWORK_PROBLEM\x10\x01\x42k\n$com.hotstar.event.model.client.watchP\x01ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.watch.nudge_viewed_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.hotstar.event.model.client.watchP\001ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watch'
  _globals['_NUDGETYPE']._serialized_start=301
  _globals['_NUDGETYPE']._serialized_end=372
  _globals['_NUDGEVIEWED']._serialized_start=50
  _globals['_NUDGEVIEWED']._serialized_end=227
  _globals['_NUDGEVIEWED_META']._serialized_start=156
  _globals['_NUDGEVIEWED_META']._serialized_end=227
  _globals['_NETWORKPROBLEM']._serialized_start=229
  _globals['_NETWORKPROBLEM']._serialized_end=299
# @@protoc_insertion_point(module_scope)
