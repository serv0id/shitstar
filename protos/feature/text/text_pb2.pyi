from feature.color import color_pb2 as _color_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Text(_message.Message):
    __slots__ = ("segments",)
    class FontStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[Text.FontStyle]
        BODY_MEDIUM_2: _ClassVar[Text.FontStyle]
        CAPTION_MEDIUM_1: _ClassVar[Text.FontStyle]
        CAPTION_SEMIBOLD_1: _ClassVar[Text.FontStyle]
        CAPTION_SEMIBOLD_2: _ClassVar[Text.FontStyle]
        CAPTION_SEMIBOLD_3: _ClassVar[Text.FontStyle]
    DEFAULT: Text.FontStyle
    BODY_MEDIUM_2: Text.FontStyle
    CAPTION_MEDIUM_1: Text.FontStyle
    CAPTION_SEMIBOLD_1: Text.FontStyle
    CAPTION_SEMIBOLD_2: Text.FontStyle
    CAPTION_SEMIBOLD_3: Text.FontStyle
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_FORMAT: _ClassVar[Text.Format]
        STRIKETHROUGH: _ClassVar[Text.Format]
    DEFAULT_FORMAT: Text.Format
    STRIKETHROUGH: Text.Format
    class TextSegment(_message.Message):
        __slots__ = ("text", "attributes")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        text: str
        attributes: Text.TextAttributes
        def __init__(self, text: _Optional[str] = ..., attributes: _Optional[_Union[Text.TextAttributes, _Mapping]] = ...) -> None: ...
    class TextAttributes(_message.Message):
        __slots__ = ("color", "font_style", "format")
        COLOR_FIELD_NUMBER: _ClassVar[int]
        FONT_STYLE_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        color: _color_pb2.Color
        font_style: Text.FontStyle
        format: _containers.RepeatedScalarFieldContainer[Text.Format]
        def __init__(self, color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., font_style: _Optional[_Union[Text.FontStyle, str]] = ..., format: _Optional[_Iterable[_Union[Text.Format, str]]] = ...) -> None: ...
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[Text.TextSegment]
    def __init__(self, segments: _Optional[_Iterable[_Union[Text.TextSegment, _Mapping]]] = ...) -> None: ...
