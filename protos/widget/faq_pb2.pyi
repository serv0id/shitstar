from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FAQWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "question_answer_pairs")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        QUESTION_ANSWER_PAIRS_FIELD_NUMBER: _ClassVar[int]
        title: str
        question_answer_pairs: _containers.RepeatedCompositeFieldContainer[FAQWidget.QuestionAnswerPair]
        def __init__(self, title: _Optional[str] = ..., question_answer_pairs: _Optional[_Iterable[_Union[FAQWidget.QuestionAnswerPair, _Mapping]]] = ...) -> None: ...
    class QuestionAnswerPair(_message.Message):
        __slots__ = ("question", "answer")
        QUESTION_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        question: str
        answer: str
        def __init__(self, question: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: FAQWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[FAQWidget.Data, _Mapping]] = ...) -> None: ...
