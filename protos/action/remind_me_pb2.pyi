from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemindMeAction(_message.Message):
    __slots__ = ("info", "is_toast_disabled")
    INFO_FIELD_NUMBER: _ClassVar[int]
    IS_TOAST_DISABLED_FIELD_NUMBER: _ClassVar[int]
    info: RemindMeInfo
    is_toast_disabled: bool
    def __init__(self, info: _Optional[_Union[RemindMeInfo, _Mapping]] = ..., is_toast_disabled: bool = ...) -> None: ...

class RemindMeInfo(_message.Message):
    __slots__ = ("content_id", "is_reminder_set", "content_title", "is_client_assisted")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REMINDER_SET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    IS_CLIENT_ASSISTED_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    is_reminder_set: bool
    content_title: str
    is_client_assisted: bool
    def __init__(self, content_id: _Optional[str] = ..., is_reminder_set: bool = ..., content_title: _Optional[str] = ..., is_client_assisted: bool = ...) -> None: ...
