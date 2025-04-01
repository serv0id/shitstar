from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAGE_TYPE_UNSPECIFIED: _ClassVar[PageType]
    PAGE_TYPE_HOME: _ClassVar[PageType]
    PAGE_TYPE_SEARCH: _ClassVar[PageType]
    PAGE_TYPE_TICKET: _ClassVar[PageType]
    PAGE_TYPE_CATEGORY_DETAIL: _ClassVar[PageType]
    PAGE_TYPE_ARTICLE_DETAIL: _ClassVar[PageType]
    PAGE_TYPE_LANG_PREF: _ClassVar[PageType]
    PAGE_TYPE_UPLOAD_FILES: _ClassVar[PageType]
    PAGE_TYPE_CANCEL_SUBS: _ClassVar[PageType]
    PAGE_TYPE_FEEDBACK: _ClassVar[PageType]
    PAGE_TYPE_NOT_FOUND: _ClassVar[PageType]
    PAGE_TYPE_REFUND_OFFER: _ClassVar[PageType]
PAGE_TYPE_UNSPECIFIED: PageType
PAGE_TYPE_HOME: PageType
PAGE_TYPE_SEARCH: PageType
PAGE_TYPE_TICKET: PageType
PAGE_TYPE_CATEGORY_DETAIL: PageType
PAGE_TYPE_ARTICLE_DETAIL: PageType
PAGE_TYPE_LANG_PREF: PageType
PAGE_TYPE_UPLOAD_FILES: PageType
PAGE_TYPE_CANCEL_SUBS: PageType
PAGE_TYPE_FEEDBACK: PageType
PAGE_TYPE_NOT_FOUND: PageType
PAGE_TYPE_REFUND_OFFER: PageType
