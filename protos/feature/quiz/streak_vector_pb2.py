# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/quiz/streak_vector.proto
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
    'feature/quiz/streak_vector.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.image import illustration_pb2 as feature_dot_image_dot_illustration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n feature/quiz/streak_vector.proto\x12\x0c\x66\x65\x61ture.quiz\x1a feature/image/illustration.proto\"K\n\x0cStreakVector\x12\r\n\x05title\x18\x01 \x01(\t\x12,\n\x07streaks\x18\x02 \x03(\x0b\x32\x1b.feature.image.IllustrationB[\n!com.hotstar.ui.model.feature.quizP\x01Z4github.com/hotstar/hs-core-ui-models-go/feature/quizb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.quiz.streak_vector_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.ui.model.feature.quizP\001Z4github.com/hotstar/hs-core-ui-models-go/feature/quiz'
  _globals['_STREAKVECTOR']._serialized_start=84
  _globals['_STREAKVECTOR']._serialized_end=159
# @@protoc_insertion_point(module_scope)
