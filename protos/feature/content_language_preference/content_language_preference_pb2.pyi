from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContentLanguagePreference(_message.Message):
    __slots__ = ("user_language_preference_id", "timestamp", "lang_code")
    USER_LANGUAGE_PREFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LANG_CODE_FIELD_NUMBER: _ClassVar[int]
    user_language_preference_id: str
    timestamp: int
    lang_code: str
    def __init__(self, user_language_preference_id: _Optional[str] = ..., timestamp: _Optional[int] = ..., lang_code: _Optional[str] = ...) -> None: ...
