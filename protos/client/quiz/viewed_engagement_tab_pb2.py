# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/quiz/viewed_engagement_tab.proto
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
    'client/quiz/viewed_engagement_tab.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from component.quiz import enum_pb2 as component_dot_quiz_dot_enum__pb2
from component.quiz import quiz_base_info_pb2 as component_dot_quiz_dot_quiz__base__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'client/quiz/viewed_engagement_tab.proto\x12\x0b\x63lient.quiz\x1a\x19\x63omponent/quiz/enum.proto\x1a#component/quiz/quiz_base_info.proto\"\x9d\x01\n\x1dViewedEngagementTabProperties\x12\x35\n\x0f\x62\x61se_properties\x18\x01 \x01(\x0b\x32\x1c.component.quiz.QuizBaseInfo\x12\x10\n\x08tab_name\x18\x02 \x01(\t\x12\x33\n\rcurrent_state\x18\x03 \x01(\x0e\x32\x1c.component.quiz.CurrentStateBi\n#com.hotstar.event.model.client.quizP\x01Z@github.com/hotstar/data-event-schemas-go/hsanalytics/client/quizb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.quiz.viewed_engagement_tab_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.hotstar.event.model.client.quizP\001Z@github.com/hotstar/data-event-schemas-go/hsanalytics/client/quiz'
  _globals['_VIEWEDENGAGEMENTTABPROPERTIES']._serialized_start=121
  _globals['_VIEWEDENGAGEMENTTABPROPERTIES']._serialized_end=278
# @@protoc_insertion_point(module_scope)
