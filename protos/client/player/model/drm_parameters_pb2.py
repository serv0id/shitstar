# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/player/model/drm_parameters.proto
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
    'client/player/model/drm_parameters.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from options import opts_pb2 as options_dot_opts__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(client/player/model/drm_parameters.proto\x12\x13\x63lient.player.model\x1a\x12options/opts.proto\"\xe4\x07\n\rDrmParameters\x12Z\n\x18widevine_security_levels\x18\x01 \x03(\x0e\x32\x38.client.player.model.DrmParameters.WidevineSecurityLevel\x12\x45\n\rhdcp_versions\x18\x02 \x03(\x0e\x32..client.player.model.DrmParameters.HdcpVersion\x12\\\n\x19playready_security_levels\x18\x03 \x03(\x0e\x32\x39.client.player.model.DrmParameters.PlayreadySecurityLevel\"\xa3\x02\n\x15WidevineSecurityLevel\x12\'\n#WIDEVINE_SECURITY_LEVEL_UNSPECIFIED\x10\x00\x12,\n(WIDEVINE_SECURITY_LEVEL_SW_SECURE_CRYPTO\x10\x01\x12,\n(WIDEVINE_SECURITY_LEVEL_SW_SECURE_DECODE\x10\x02\x12,\n(WIDEVINE_SECURITY_LEVEL_HW_SECURE_CRYPTO\x10\x03\x12,\n(WIDEVINE_SECURITY_LEVEL_HW_SECURE_DECODE\x10\x04\x12)\n%WIDEVINE_SECURITY_LEVEL_HW_SECURE_ALL\x10\x05\"\xf8\x01\n\x0bHdcpVersion\x12\x1c\n\x18HDCP_VERSION_UNSPECIFIED\x10\x00\x12\x1a\n\x16HDCP_VERSION_HDCP_NONE\x10\x01\x12\x18\n\x14HDCP_VERSION_HDCP_V1\x10\x02\x12\x18\n\x14HDCP_VERSION_HDCP_V2\x10\x03\x12\x1a\n\x16HDCP_VERSION_HDCP_V2_1\x10\x04\x12\x1a\n\x16HDCP_VERSION_HDCP_V2_2\x10\x05\x12\'\n#HDCP_VERSION_HDCP_NO_DIGITAL_OUTPUT\x10\x06\x12\x1a\n\x16HDCP_VERSION_HDCP_V2_3\x10\x07\"\xb0\x01\n\x16PlayreadySecurityLevel\x12(\n$PLAYREADY_SECURITY_LEVEL_UNSPECIFIED\x10\x00\x12#\n\x1fPLAYREADY_SECURITY_LEVEL_SL3000\x10\x01\x12#\n\x1fPLAYREADY_SECURITY_LEVEL_SL2000\x10\x02\x12\"\n\x1ePLAYREADY_SECURITY_LEVEL_SL150\x10\x03\x42y\n+com.hotstar.event.model.client.player.modelP\x01ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/player/modelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.player.model.drm_parameters_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n+com.hotstar.event.model.client.player.modelP\001ZHgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/player/model'
  _globals['_DRMPARAMETERS']._serialized_start=86
  _globals['_DRMPARAMETERS']._serialized_end=1082
  _globals['_DRMPARAMETERS_WIDEVINESECURITYLEVEL']._serialized_start=361
  _globals['_DRMPARAMETERS_WIDEVINESECURITYLEVEL']._serialized_end=652
  _globals['_DRMPARAMETERS_HDCPVERSION']._serialized_start=655
  _globals['_DRMPARAMETERS_HDCPVERSION']._serialized_end=903
  _globals['_DRMPARAMETERS_PLAYREADYSECURITYLEVEL']._serialized_start=906
  _globals['_DRMPARAMETERS_PLAYREADYSECURITYLEVEL']._serialized_end=1082
# @@protoc_insertion_point(module_scope)
