from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemindMeAction(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: RemindMeInfo
    def __init__(self, info: _Optional[_Union[RemindMeInfo, _Mapping]] = ...) -> None: ...

class RemindMeInfo(_message.Message):
    __slots__ = ["content_id", "is_reminder_set", "content_title"]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REMINDER_SET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    is_reminder_set: bool
    content_title: str
    def __init__(self, content_id: _Optional[str] = ..., is_reminder_set: bool = ..., content_title: _Optional[str] = ...) -> None: ...
