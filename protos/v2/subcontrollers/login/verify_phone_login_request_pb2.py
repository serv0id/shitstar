# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/subcontrollers/login/verify_phone_login_request.proto
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
    'v2/subcontrollers/login/verify_phone_login_request.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from v2.commons import login_initiate_by_pb2 as v2_dot_commons_dot_login__initiate__by__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8v2/subcontrollers/login/verify_phone_login_request.proto\x12\rfeature.login\x1a\"v2/commons/login_initiate_by.proto\"\xc0\x05\n\x17VerifyPhoneLoginRequest\x12\x19\n\x11verification_code\x18\x03 \x01(\t\x12\x39\n\x04mode\x18\x04 \x01(\x0e\x32+.feature.login.VerifyPhoneLoginRequest.Mode\x12L\n\x0e\x63onsent_status\x18\x05 \x01(\x0e\x32\x34.feature.login.VerifyPhoneLoginRequest.ConsentStatus\x12Q\n\x11login_device_meta\x18\x06 \x01(\x0b\x32\x36.feature.login.VerifyPhoneLoginRequest.LoginDeviceMeta\x12=\n\x06source\x18\x07 \x01(\x0e\x32-.feature.login.VerifyPhoneLoginRequest.Source\x12\x46\n\x0binitiate_by\x18\x08 \x01(\x0e\x32-.v2.commons.login_initiate_by.LoginInitiateByB\x02\x18\x01\x12\x16\n\x0cphone_number\x18\x01 \x01(\tH\x00\x12\x1e\n\x14\x65ncrypted_identifier\x18\x02 \x01(\tH\x00\x12\x17\n\remail_address\x18\t \x01(\tH\x00\x1a&\n\x0fLoginDeviceMeta\x12\x13\n\x0b\x64\x65vice_name\x18\x01 \x01(\t\"\x1c\n\x04Mode\x12\n\n\x06MANUAL\x10\x00\x12\x08\n\x04\x41UTO\x10\x01\";\n\rConsentStatus\x12\x11\n\rALREADY_OPTED\x10\x00\x12\x0b\n\x07OPT_OUT\x10\x01\x12\n\n\x06OPT_IN\x10\x02\"8\n\x06Source\x12\t\n\x05LOGIN\x10\x00\x12\x0e\n\nPRE_LAUNCH\x10\x01\x12\x13\n\x0fSKIPPABLE_LOGIN\x10\x02\x42\x19\n\x17PhoneVerificationMethodBa\n\"com.hotstar.ui.model.feature.loginP\x01Z9github.com/hotstar/hs-core-api-go/v2/subcontrollers/loginb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.subcontrollers.login.verify_phone_login_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hotstar.ui.model.feature.loginP\001Z9github.com/hotstar/hs-core-api-go/v2/subcontrollers/login'
  _globals['_VERIFYPHONELOGINREQUEST'].fields_by_name['initiate_by']._loaded_options = None
  _globals['_VERIFYPHONELOGINREQUEST'].fields_by_name['initiate_by']._serialized_options = b'\030\001'
  _globals['_VERIFYPHONELOGINREQUEST']._serialized_start=112
  _globals['_VERIFYPHONELOGINREQUEST']._serialized_end=816
  _globals['_VERIFYPHONELOGINREQUEST_LOGINDEVICEMETA']._serialized_start=602
  _globals['_VERIFYPHONELOGINREQUEST_LOGINDEVICEMETA']._serialized_end=640
  _globals['_VERIFYPHONELOGINREQUEST_MODE']._serialized_start=642
  _globals['_VERIFYPHONELOGINREQUEST_MODE']._serialized_end=670
  _globals['_VERIFYPHONELOGINREQUEST_CONSENTSTATUS']._serialized_start=672
  _globals['_VERIFYPHONELOGINREQUEST_CONSENTSTATUS']._serialized_end=731
  _globals['_VERIFYPHONELOGINREQUEST_SOURCE']._serialized_start=733
  _globals['_VERIFYPHONELOGINREQUEST_SOURCE']._serialized_end=789
# @@protoc_insertion_point(module_scope)
