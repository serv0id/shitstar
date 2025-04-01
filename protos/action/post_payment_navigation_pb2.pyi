from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PostPaymentNavigationAction(_message.Message):
    __slots__ = ("page_type", "page_url", "page_slug", "replace")
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SLUG_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    page_type: str
    page_url: str
    page_slug: str
    replace: bool
    def __init__(self, page_type: _Optional[str] = ..., page_url: _Optional[str] = ..., page_slug: _Optional[str] = ..., replace: bool = ...) -> None: ...
