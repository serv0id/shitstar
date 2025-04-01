from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BridgeEventAction(_message.Message):
    __slots__ = ("event",)
    class Event(_message.Message):
        __slots__ = ("action_handler", "close_screen")
        ACTION_HANDLER_FIELD_NUMBER: _ClassVar[int]
        CLOSE_SCREEN_FIELD_NUMBER: _ClassVar[int]
        action_handler: BridgeEventAction.ActionHandler
        close_screen: BridgeEventAction.CloseScreen
        def __init__(self, action_handler: _Optional[_Union[BridgeEventAction.ActionHandler, _Mapping]] = ..., close_screen: _Optional[_Union[BridgeEventAction.CloseScreen, _Mapping]] = ...) -> None: ...
    class ActionHandler(_message.Message):
        __slots__ = ("url", "value")
        URL_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        url: str
        value: bytes
        def __init__(self, url: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
    class CloseScreen(_message.Message):
        __slots__ = ("is_cancelled",)
        IS_CANCELLED_FIELD_NUMBER: _ClassVar[int]
        is_cancelled: bool
        def __init__(self, is_cancelled: bool = ...) -> None: ...
    EVENT_FIELD_NUMBER: _ClassVar[int]
    event: BridgeEventAction.Event
    def __init__(self, event: _Optional[_Union[BridgeEventAction.Event, _Mapping]] = ...) -> None: ...
