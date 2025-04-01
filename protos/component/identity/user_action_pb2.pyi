from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserAction(_message.Message):
    __slots__ = ("display_name", "item_type", "page_title")
    class ItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ITEM_TYPE_UNSPECIFIED: _ClassVar[UserAction.ItemType]
        ITEM_TYPE_BUTTON: _ClassVar[UserAction.ItemType]
        ITEM_TYPE_TEXT_BOX: _ClassVar[UserAction.ItemType]
        ITEM_TYPE_HYPER_LINK: _ClassVar[UserAction.ItemType]
    ITEM_TYPE_UNSPECIFIED: UserAction.ItemType
    ITEM_TYPE_BUTTON: UserAction.ItemType
    ITEM_TYPE_TEXT_BOX: UserAction.ItemType
    ITEM_TYPE_HYPER_LINK: UserAction.ItemType
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
    display_name: str
    item_type: UserAction.ItemType
    page_title: str
    def __init__(self, display_name: _Optional[str] = ..., item_type: _Optional[_Union[UserAction.ItemType, str]] = ..., page_title: _Optional[str] = ...) -> None: ...
