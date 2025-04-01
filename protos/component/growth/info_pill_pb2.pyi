from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InfoPillProperties(_message.Message):
    __slots__ = ("pill_type", "content_id", "match_content_id", "cta_display_text")
    class PillType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PILL_TYPE_UNSPECIFIED: _ClassVar[InfoPillProperties.PillType]
        PILL_TYPE_CRICKET: _ClassVar[InfoPillProperties.PillType]
        PILL_TYPE_TIMER_RUNNING: _ClassVar[InfoPillProperties.PillType]
    PILL_TYPE_UNSPECIFIED: InfoPillProperties.PillType
    PILL_TYPE_CRICKET: InfoPillProperties.PillType
    PILL_TYPE_TIMER_RUNNING: InfoPillProperties.PillType
    PILL_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    MATCH_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CTA_DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    pill_type: InfoPillProperties.PillType
    content_id: str
    match_content_id: str
    cta_display_text: str
    def __init__(self, pill_type: _Optional[_Union[InfoPillProperties.PillType, str]] = ..., content_id: _Optional[str] = ..., match_content_id: _Optional[str] = ..., cta_display_text: _Optional[str] = ...) -> None: ...
