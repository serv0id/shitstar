from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import verify_otp_pb2 as _verify_otp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParentalLockSetupWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("label", "desc", "status", "verify_otp", "lockscreen", "change_lock", "turn_off_lock_action", "turn_on_lock_action")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VERIFY_OTP_FIELD_NUMBER: _ClassVar[int]
        LOCKSCREEN_FIELD_NUMBER: _ClassVar[int]
        CHANGE_LOCK_FIELD_NUMBER: _ClassVar[int]
        TURN_OFF_LOCK_ACTION_FIELD_NUMBER: _ClassVar[int]
        TURN_ON_LOCK_ACTION_FIELD_NUMBER: _ClassVar[int]
        label: str
        desc: str
        status: bool
        verify_otp: _verify_otp_pb2.VerifyOtpWidget
        lockscreen: ParentalLockSetupWidget.LockScreen
        change_lock: ParentalLockSetupWidget.ChangeParentalLock
        turn_off_lock_action: _actions_pb2.Actions
        turn_on_lock_action: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., desc: _Optional[str] = ..., status: bool = ..., verify_otp: _Optional[_Union[_verify_otp_pb2.VerifyOtpWidget, _Mapping]] = ..., lockscreen: _Optional[_Union[ParentalLockSetupWidget.LockScreen, _Mapping]] = ..., change_lock: _Optional[_Union[ParentalLockSetupWidget.ChangeParentalLock, _Mapping]] = ..., turn_off_lock_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., turn_on_lock_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LockScreen(_message.Message):
        __slots__ = ("label", "confirm_label", "desc", "confirm_desc", "action_label", "pin_size", "success", "save_continue")
        class ParentalLockSuccess(_message.Message):
            __slots__ = ("title", "desc", "action_label", "go_home")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            DESC_FIELD_NUMBER: _ClassVar[int]
            ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
            GO_HOME_FIELD_NUMBER: _ClassVar[int]
            title: str
            desc: str
            action_label: str
            go_home: _actions_pb2.Actions
            def __init__(self, title: _Optional[str] = ..., desc: _Optional[str] = ..., action_label: _Optional[str] = ..., go_home: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        LABEL_FIELD_NUMBER: _ClassVar[int]
        CONFIRM_LABEL_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        CONFIRM_DESC_FIELD_NUMBER: _ClassVar[int]
        ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
        PIN_SIZE_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        SAVE_CONTINUE_FIELD_NUMBER: _ClassVar[int]
        label: str
        confirm_label: str
        desc: str
        confirm_desc: str
        action_label: str
        pin_size: int
        success: ParentalLockSetupWidget.LockScreen.ParentalLockSuccess
        save_continue: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., confirm_label: _Optional[str] = ..., desc: _Optional[str] = ..., confirm_desc: _Optional[str] = ..., action_label: _Optional[str] = ..., pin_size: _Optional[int] = ..., success: _Optional[_Union[ParentalLockSetupWidget.LockScreen.ParentalLockSuccess, _Mapping]] = ..., save_continue: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class ChangeParentalLock(_message.Message):
        __slots__ = ("label", "desc", "change_pin_action")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        CHANGE_PIN_ACTION_FIELD_NUMBER: _ClassVar[int]
        label: str
        desc: str
        change_pin_action: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., desc: _Optional[str] = ..., change_pin_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ParentalLockSetupWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ParentalLockSetupWidget.Data, _Mapping]] = ...) -> None: ...
