from client.watch import card_type_pb2 as _card_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CardViewed(_message.Message):
    __slots__ = ("event_name", "card_type", "click_enabled", "card_position", "card_createdat", "card_cta", "card_title", "card_id")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLICK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CARD_POSITION_FIELD_NUMBER: _ClassVar[int]
    CARD_CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    CARD_CTA_FIELD_NUMBER: _ClassVar[int]
    CARD_TITLE_FIELD_NUMBER: _ClassVar[int]
    CARD_ID_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    card_type: _card_type_pb2.CardType
    click_enabled: bool
    card_position: int
    card_createdat: int
    card_cta: str
    card_title: str
    card_id: str
    def __init__(self, event_name: _Optional[str] = ..., card_type: _Optional[_Union[_card_type_pb2.CardType, str]] = ..., click_enabled: bool = ..., card_position: _Optional[int] = ..., card_createdat: _Optional[int] = ..., card_cta: _Optional[str] = ..., card_title: _Optional[str] = ..., card_id: _Optional[str] = ...) -> None: ...
