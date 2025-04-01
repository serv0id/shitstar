from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextBoxWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("id", "placeholder", "size")
        class Size(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SMALL: _ClassVar[TextBoxWidget.Data.Size]
            MEDIUM: _ClassVar[TextBoxWidget.Data.Size]
            LARGE: _ClassVar[TextBoxWidget.Data.Size]
        SMALL: TextBoxWidget.Data.Size
        MEDIUM: TextBoxWidget.Data.Size
        LARGE: TextBoxWidget.Data.Size
        ID_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        id: str
        placeholder: str
        size: TextBoxWidget.Data.Size
        def __init__(self, id: _Optional[str] = ..., placeholder: _Optional[str] = ..., size: _Optional[_Union[TextBoxWidget.Data.Size, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TextBoxWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TextBoxWidget.Data, _Mapping]] = ...) -> None: ...
