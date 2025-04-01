from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CARD_TYPE_UNSPECIFIED: _ClassVar[CardType]
    CARD_TYPE_COMMENTARY: _ClassVar[CardType]
    CARD_TYPE_OVER_SUMMARY: _ClassVar[CardType]
    CARD_TYPE_KEY_MOMENT: _ClassVar[CardType]
    CARD_TYPE_EDITORIAL: _ClassVar[CardType]
    CARD_TYPE_TEXT_DIVIDER: _ClassVar[CardType]
    CARD_TYPE_ADVERTISEMENT: _ClassVar[CardType]
CARD_TYPE_UNSPECIFIED: CardType
CARD_TYPE_COMMENTARY: CardType
CARD_TYPE_OVER_SUMMARY: CardType
CARD_TYPE_KEY_MOMENT: CardType
CARD_TYPE_EDITORIAL: CardType
CARD_TYPE_TEXT_DIVIDER: CardType
CARD_TYPE_ADVERTISEMENT: CardType
