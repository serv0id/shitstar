from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import verify_otp_pb2 as _verify_otp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParentalLockSetUpWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("enter_pin", "confirm_pin", "error_message", "pin_size", "submit_pin_action", "title", "desc", "submit_pin_label")
        ENTER_PIN_FIELD_NUMBER: _ClassVar[int]
        CONFIRM_PIN_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PIN_SIZE_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_PIN_ACTION_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_PIN_LABEL_FIELD_NUMBER: _ClassVar[int]
        enter_pin: ParentalLockSetUpWidget.ScreenLabels
        confirm_pin: ParentalLockSetUpWidget.ScreenLabels
        error_message: str
        pin_size: int
        submit_pin_action: _actions_pb2.Actions
        title: str
        desc: str
        submit_pin_label: str
        def __init__(self, enter_pin: _Optional[_Union[ParentalLockSetUpWidget.ScreenLabels, _Mapping]] = ..., confirm_pin: _Optional[_Union[ParentalLockSetUpWidget.ScreenLabels, _Mapping]] = ..., error_message: _Optional[str] = ..., pin_size: _Optional[int] = ..., submit_pin_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., submit_pin_label: _Optional[str] = ...) -> None: ...
    class ScreenLabels(_message.Message):
        __slots__ = ("title", "desc", "action_label", "cancel_label", "continue_btn")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
        CANCEL_LABEL_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_BTN_FIELD_NUMBER: _ClassVar[int]
        title: str
        desc: str
        action_label: str
        cancel_label: str
        continue_btn: ParentalLockSetUpWidget.Button
        def __init__(self, title: _Optional[str] = ..., desc: _Optional[str] = ..., action_label: _Optional[str] = ..., cancel_label: _Optional[str] = ..., continue_btn: _Optional[_Union[ParentalLockSetUpWidget.Button, _Mapping]] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("label", "action")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        label: str
        action: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ParentalLockSetUpWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ParentalLockSetUpWidget.Data, _Mapping]] = ...) -> None: ...
