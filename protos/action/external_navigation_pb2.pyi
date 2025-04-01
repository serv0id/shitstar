from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ExternalNavigationAction(_message.Message):
    __slots__ = ("external_url", "open_in_same_tab")
    EXTERNAL_URL_FIELD_NUMBER: _ClassVar[int]
    OPEN_IN_SAME_TAB_FIELD_NUMBER: _ClassVar[int]
    external_url: str
    open_in_same_tab: bool
    def __init__(self, external_url: _Optional[str] = ..., open_in_same_tab: bool = ...) -> None: ...
