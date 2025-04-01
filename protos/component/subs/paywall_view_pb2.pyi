from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaywallViewProperties(_message.Message):
    __slots__ = ("page_form", "page_language", "paywall_type")
    class PageForm(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAGE_FORM_UNSPECIFIED: _ClassVar[PaywallViewProperties.PageForm]
        PAGE_FORM_FULL_PAGE: _ClassVar[PaywallViewProperties.PageForm]
        PAGE_FORM_BOTTOM_SHEET: _ClassVar[PaywallViewProperties.PageForm]
    PAGE_FORM_UNSPECIFIED: PaywallViewProperties.PageForm
    PAGE_FORM_FULL_PAGE: PaywallViewProperties.PageForm
    PAGE_FORM_BOTTOM_SHEET: PaywallViewProperties.PageForm
    PAGE_FORM_FIELD_NUMBER: _ClassVar[int]
    PAGE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PAYWALL_TYPE_FIELD_NUMBER: _ClassVar[int]
    page_form: PaywallViewProperties.PageForm
    page_language: str
    paywall_type: str
    def __init__(self, page_form: _Optional[_Union[PaywallViewProperties.PageForm, str]] = ..., page_language: _Optional[str] = ..., paywall_type: _Optional[str] = ...) -> None: ...
