from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StickyNotificationProperties(_message.Message):
    __slots__ = ("campaign_id", "text", "action_type", "utm_campaign_id")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    UTM_CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    text: str
    action_type: str
    utm_campaign_id: str
    def __init__(self, campaign_id: _Optional[str] = ..., text: _Optional[str] = ..., action_type: _Optional[str] = ..., utm_campaign_id: _Optional[str] = ...) -> None: ...
