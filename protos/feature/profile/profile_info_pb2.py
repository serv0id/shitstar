# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/profile/profile_info.proto
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
    'feature/profile/profile_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"feature/profile/profile_info.proto\x12\x0f\x66\x65\x61ture.profile\x1a\x19\x66\x65\x61ture/image/image.proto\"]\n\x0bProfileInfo\x12\x12\n\nprofile_id\x18\x01 \x01(\t\x12$\n\x06\x61vatar\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x14\n\x0cis_celebrity\x18\x03 \x01(\x08\x42\x61\n$com.hotstar.ui.model.feature.profileP\x01Z7github.com/hotstar/hs-core-ui-models-go/feature/profileb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.profile.profile_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.hotstar.ui.model.feature.profileP\001Z7github.com/hotstar/hs-core-ui-models-go/feature/profile'
  _globals['_PROFILEINFO']._serialized_start=82
  _globals['_PROFILEINFO']._serialized_end=175
# @@protoc_insertion_point(module_scope)
