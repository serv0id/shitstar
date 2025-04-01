from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("id", "style", "text")
        class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NONE: _ClassVar[TextWidget.Data.Style]
            NUMBER: _ClassVar[TextWidget.Data.Style]
            BULLET: _ClassVar[TextWidget.Data.Style]
            PARAGRAPH: _ClassVar[TextWidget.Data.Style]
        NONE: TextWidget.Data.Style
        NUMBER: TextWidget.Data.Style
        BULLET: TextWidget.Data.Style
        PARAGRAPH: TextWidget.Data.Style
        ID_FIELD_NUMBER: _ClassVar[int]
        STYLE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        id: str
        style: TextWidget.Data.Style
        text: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., style: _Optional[_Union[TextWidget.Data.Style, str]] = ..., text: _Optional[_Iterable[str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TextWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TextWidget.Data, _Mapping]] = ...) -> None: ...
