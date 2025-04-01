from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Page(_message.Message):
    __slots__ = ("type", "title", "sub_title", "id", "template")
    class PageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAGE_TYPE_UNSPECIFIED: _ClassVar[Page.PageType]
        PAGE_TYPE_MY_SPACE: _ClassVar[Page.PageType]
        PAGE_TYPE_DOWNLOAD: _ClassVar[Page.PageType]
        PAGE_TYPE_WATCH: _ClassVar[Page.PageType]
        PAGE_TYPE_SPLASH: _ClassVar[Page.PageType]
        PAGE_TYPE_ERROR: _ClassVar[Page.PageType]
    PAGE_TYPE_UNSPECIFIED: Page.PageType
    PAGE_TYPE_MY_SPACE: Page.PageType
    PAGE_TYPE_DOWNLOAD: Page.PageType
    PAGE_TYPE_WATCH: Page.PageType
    PAGE_TYPE_SPLASH: Page.PageType
    PAGE_TYPE_ERROR: Page.PageType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    type: Page.PageType
    title: str
    sub_title: str
    id: str
    template: str
    def __init__(self, type: _Optional[_Union[Page.PageType, str]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., id: _Optional[str] = ..., template: _Optional[str] = ...) -> None: ...
