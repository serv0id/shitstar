# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: context/state_context.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x63ontext/state_context.proto\x12\x07\x63ontext\">\n\x0cStateContext\x12.\n\x0e\x61\x63tion_context\x18\x01 \x01(\x0b\x32\x16.context.ActionContext\"\xd2\x01\n\rActionContext\x12\x41\n\x18subscribe_action_context\x18\x01 \x01(\x0b\x32\x1f.context.SubscribeActionContext\x12\x39\n\x14watch_action_context\x18\x02 \x01(\x0b\x32\x1b.context.WatchActionContext\x12\x43\n\x19onboarding_action_context\x18\x03 \x01(\x0b\x32 .context.OnboardingActionContext\"\xf2\x03\n\x16SubscribeActionContext\x12+\n\x07purpose\x18\x01 \x01(\x0e\x32\x1a.context.OnboardingPurpose\x12\x12\n\ncontent_id\x18\x02 \x01(\t\x12\x13\n\x0bplan_family\x18\x03 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x04 \x01(\t\x12&\n\x1e\x66\x61iled_pc_entitlement_required\x18\x05 \x01(\t\x12%\n\x1d\x66\x61iled_pc_entitlement_context\x18\x06 \x01(\t\x12\x17\n\x0fis_content_paid\x18\x07 \x01(\x08\x12\x12\n\npaywall_ts\x18\x08 \x01(\t\x12\x15\n\rcontent_title\x18\t \x01(\t\x12\x0f\n\x07pack_id\x18\n \x01(\t\x12\x15\n\rplan_duration\x18\x0b \x01(\t\x12\x16\n\x0eplan_frequency\x18\x0c \x01(\t\x12\x14\n\x0cpartner_name\x18\r \x01(\t\x12\x12\n\npromo_code\x18\x0e \x01(\t\x12\x12\n\nplan_title\x18\x0f \x01(\t\x12\x19\n\x11parent_content_id\x18\x10 \x01(\t\x12\x1c\n\x14parent_content_title\x18\x11 \x01(\t\x12\x12\n\nsport_type\x18\x12 \x01(\t\x12\x0e\n\x06source\x18\x13 \x01(\t\"\xc2\x02\n\x12WatchActionContext\x12+\n\x07purpose\x18\x01 \x01(\x0e\x32\x1a.context.OnboardingPurpose\x12\x12\n\ncontent_id\x18\x02 \x01(\t\x12\x15\n\rcontent_title\x18\x03 \x01(\t\x12\x19\n\x11\x63ontent_image_url\x18\x04 \x01(\t\x12\x14\n\x0c\x63ontent_type\x18\x05 \x01(\t\x12\x0e\n\x06source\x18\x06 \x01(\t\x12\x19\n\x11parent_content_id\x18\x07 \x01(\t\x12\x1c\n\x14parent_content_title\x18\x08 \x01(\t\x12\x12\n\nsport_type\x18\t \x01(\t\x12\x12\n\nskip_login\x18\n \x01(\x08\x12\x32\n\x10interactive_type\x18\x0b \x01(\x0e\x32\x18.context.InteractiveType\"F\n\x17OnboardingActionContext\x12+\n\x07purpose\x18\x01 \x01(\x0e\x32\x1a.context.OnboardingPurpose*@\n\x11OnboardingPurpose\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05LOGIN\x10\x01\x12\x13\n\x0fONBOARDING_LITE\x10\x02*D\n\x0fInteractiveType\x12\x10\n\x0cUNKNOWN_TYPE\x10\x00\x12\x08\n\x04QUIZ\x10\x01\x12\x0b\n\x07POLLING\x10\x02\x12\x08\n\x04\x43HAT\x10\x03\x42Q\n\x1c\x63om.hotstar.ui.model.contextP\x01Z/github.com/hotstar/hs-core-ui-models-go/contextb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'context.state_context_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\034com.hotstar.ui.model.contextP\001Z/github.com/hotstar/hs-core-ui-models-go/context'
  _globals['_ONBOARDINGPURPOSE']._serialized_start=1215
  _globals['_ONBOARDINGPURPOSE']._serialized_end=1279
  _globals['_INTERACTIVETYPE']._serialized_start=1281
  _globals['_INTERACTIVETYPE']._serialized_end=1349
  _globals['_STATECONTEXT']._serialized_start=40
  _globals['_STATECONTEXT']._serialized_end=102
  _globals['_ACTIONCONTEXT']._serialized_start=105
  _globals['_ACTIONCONTEXT']._serialized_end=315
  _globals['_SUBSCRIBEACTIONCONTEXT']._serialized_start=318
  _globals['_SUBSCRIBEACTIONCONTEXT']._serialized_end=816
  _globals['_WATCHACTIONCONTEXT']._serialized_start=819
  _globals['_WATCHACTIONCONTEXT']._serialized_end=1141
  _globals['_ONBOARDINGACTIONCONTEXT']._serialized_start=1143
  _globals['_ONBOARDINGACTIONCONTEXT']._serialized_end=1213
# @@protoc_insertion_point(module_scope)