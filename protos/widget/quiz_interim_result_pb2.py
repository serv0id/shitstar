# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/quiz_interim_result.proto
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
    'widget/quiz_interim_result.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.quiz import title_pb2 as feature_dot_quiz_dot_title__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n widget/quiz_interim_result.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x18\x66\x65\x61ture/quiz/title.proto\"\xb0\x02\n\x17QuizInterimResultWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x32\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32$.widget.QuizInterimResultWidget.Data\x1a\xad\x01\n\x04\x44\x61ta\x12\x17\n\x0fis_right_anwser\x18\x01 \x01(\x08\x12\x1c\n\x14\x62\x61\x63kground_color_hex\x18\x02 \x01(\t\x12$\n\x07results\x18\x03 \x01(\x0b\x32\x13.feature.quiz.Title\x12+\n\x0e\x65xtra_reminder\x18\x04 \x01(\x0b\x32\x13.feature.quiz.Title\x12\x1b\n\x13\x64uration_in_seconds\x18\x05 \x01(\x05J\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.quiz_interim_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_QUIZINTERIMRESULTWIDGET']._serialized_start=98
  _globals['_QUIZINTERIMRESULTWIDGET']._serialized_end=402
  _globals['_QUIZINTERIMRESULTWIDGET_DATA']._serialized_start=223
  _globals['_QUIZINTERIMRESULTWIDGET_DATA']._serialized_end=396
# @@protoc_insertion_point(module_scope)
