from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DismissNotificationAction(_message.Message):
    __slots__ = ["notification_id"]
    NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
    notification_id: int
    def __init__(self, notification_id: _Optional[int] = ...) -> None: ...
