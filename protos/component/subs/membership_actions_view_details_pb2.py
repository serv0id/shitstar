# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: component/subs/membership_actions_view_details.proto
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
    'component/subs/membership_actions_view_details.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4component/subs/membership_actions_view_details.proto\x12\x0e\x63omponent.subs\"\x8c\x01\n\x1cMembershipActionsViewDetails\x12\x16\n\nplan_names\x18\x01 \x03(\tB\x02\x18\x01\x12T\n\x1fmembership_actions_view_details\x18\x02 \x03(\x0b\x32+.component.subs.MembershipActionsViewDetail\"G\n\x1bMembershipActionsViewDetail\x12\x11\n\tplan_name\x18\x01 \x01(\t\x12\x15\n\ractions_types\x18\x02 \x03(\tBj\n!com.hotstar.event.model.componentP\x01ZCgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/subsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.subs.membership_actions_view_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.event.model.componentP\001ZCgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/subs'
  _globals['_MEMBERSHIPACTIONSVIEWDETAILS'].fields_by_name['plan_names']._loaded_options = None
  _globals['_MEMBERSHIPACTIONSVIEWDETAILS'].fields_by_name['plan_names']._serialized_options = b'\030\001'
  _globals['_MEMBERSHIPACTIONSVIEWDETAILS']._serialized_start=73
  _globals['_MEMBERSHIPACTIONSVIEWDETAILS']._serialized_end=213
  _globals['_MEMBERSHIPACTIONSVIEWDETAIL']._serialized_start=215
  _globals['_MEMBERSHIPACTIONSVIEWDETAIL']._serialized_end=286
# @@protoc_insertion_point(module_scope)
