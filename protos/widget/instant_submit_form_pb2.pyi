from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.form import option_pb2 as _option_pb2
from feature.form import question_pb2 as _question_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstantSubmitFormWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("question", "options", "submit")
        QUESTION_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_FIELD_NUMBER: _ClassVar[int]
        question: _question_pb2.FormQuestion
        options: _containers.RepeatedCompositeFieldContainer[_option_pb2.Option]
        submit: _actions_pb2.Actions
        def __init__(self, question: _Optional[_Union[_question_pb2.FormQuestion, _Mapping]] = ..., options: _Optional[_Iterable[_Union[_option_pb2.Option, _Mapping]]] = ..., submit: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: InstantSubmitFormWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[InstantSubmitFormWidget.Data, _Mapping]] = ...) -> None: ...
