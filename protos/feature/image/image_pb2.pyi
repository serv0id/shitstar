from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Image(_message.Message):
    __slots__ = ["src", "alt", "dimension", "type", "src_prefix"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        DEFAULT: _ClassVar[Image.Type]
        QR: _ClassVar[Image.Type]
    DEFAULT: Image.Type
    QR: Image.Type
    class ImageDimension(_message.Message):
        __slots__ = ["width", "height"]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    SRC_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    DIMENSION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_PREFIX_FIELD_NUMBER: _ClassVar[int]
    src: str
    alt: str
    dimension: Image.ImageDimension
    type: Image.Type
    src_prefix: str
    def __init__(self, src: _Optional[str] = ..., alt: _Optional[str] = ..., dimension: _Optional[_Union[Image.ImageDimension, _Mapping]] = ..., type: _Optional[_Union[Image.Type, str]] = ..., src_prefix: _Optional[str] = ...) -> None: ...
