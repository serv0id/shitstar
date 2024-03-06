from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MailtoAction(_message.Message):
    __slots__ = ["mail_to_url"]
    MAIL_TO_URL_FIELD_NUMBER: _ClassVar[int]
    mail_to_url: str
    def __init__(self, mail_to_url: _Optional[str] = ...) -> None: ...
