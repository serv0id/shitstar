# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/subcontrollers/onboarding/pre_registration_form_request.proto
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
    'v2/subcontrollers/onboarding/pre_registration_form_request.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2.subcontrollers.onboarding import submit_consent_request_pb2 as v2_dot_subcontrollers_dot_onboarding_dot_submit__consent__request__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@v2/subcontrollers/onboarding/pre_registration_form_request.proto\x12\x12\x66\x65\x61ture.onboarding\x1a\x39v2/subcontrollers/onboarding/submit_consent_request.proto\"\xbb\x03\n\x1aPreRegistrationFormRequest\x12\x11\n\tfull_name\x18\x01 \x01(\t\x12\x14\n\x0cphone_number\x18\x02 \x01(\t\x12\x16\n\x0e\x63ountry_prefix\x18\x03 \x01(\t\x12\r\n\x05\x65mail\x18\x04 \x01(\t\x12\x17\n\x0b\x63onsent_ids\x18\x06 \x03(\x05\x42\x02\x18\x01\x12N\n\x0binitiate_by\x18\x07 \x01(\x0e\x32\x39.feature.onboarding.PreRegistrationFormRequest.InitiateBy\x12\x45\n\x06source\x18\x08 \x01(\x0e\x32\x35.feature.onboarding.PreRegistrationFormRequest.Source\x12H\n\x16submit_consent_request\x18\t \x01(\x0b\x32(.feature.onboarding.SubmitConsentRequest\"*\n\nInitiateBy\x12\r\n\tPHONE_OTP\x10\x00\x12\r\n\tPHONE_IVR\x10\x01\"#\n\x06Source\x12\t\n\x05LOGIN\x10\x00\x12\x0e\n\nPRE_LAUNCH\x10\x01:\x02\x18\x01\x42k\n\'com.hotstar.ui.model.feature.onboardingP\x01Z>github.com/hotstar/hs-core-api-go/v2/subcontrollers/onboardingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.subcontrollers.onboarding.pre_registration_form_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.hotstar.ui.model.feature.onboardingP\001Z>github.com/hotstar/hs-core-api-go/v2/subcontrollers/onboarding'
  _globals['_PREREGISTRATIONFORMREQUEST'].fields_by_name['consent_ids']._loaded_options = None
  _globals['_PREREGISTRATIONFORMREQUEST'].fields_by_name['consent_ids']._serialized_options = b'\030\001'
  _globals['_PREREGISTRATIONFORMREQUEST']._loaded_options = None
  _globals['_PREREGISTRATIONFORMREQUEST']._serialized_options = b'\030\001'
  _globals['_PREREGISTRATIONFORMREQUEST']._serialized_start=148
  _globals['_PREREGISTRATIONFORMREQUEST']._serialized_end=591
  _globals['_PREREGISTRATIONFORMREQUEST_INITIATEBY']._serialized_start=508
  _globals['_PREREGISTRATIONFORMREQUEST_INITIATEBY']._serialized_end=550
  _globals['_PREREGISTRATIONFORMREQUEST_SOURCE']._serialized_start=552
  _globals['_PREREGISTRATIONFORMREQUEST_SOURCE']._serialized_end=587
# @@protoc_insertion_point(module_scope)
