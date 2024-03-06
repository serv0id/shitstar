from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WebViewNavigationAction(_message.Message):
    __slots__ = ["web_view_url"]
    WEB_VIEW_URL_FIELD_NUMBER: _ClassVar[int]
    web_view_url: str
    def __init__(self, web_view_url: _Optional[str] = ...) -> None: ...
