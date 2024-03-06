from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeLanguageAction(_message.Message):
    __slots__ = ["lang_code"]
    LANG_CODE_FIELD_NUMBER: _ClassVar[int]
    lang_code: str
    def __init__(self, lang_code: _Optional[str] = ...) -> None: ...
