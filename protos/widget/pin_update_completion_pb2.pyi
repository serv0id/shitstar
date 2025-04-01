from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PinUpdateCompletionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("pin_status", "successStateView", "failureStateView")
        PIN_STATUS_FIELD_NUMBER: _ClassVar[int]
        SUCCESSSTATEVIEW_FIELD_NUMBER: _ClassVar[int]
        FAILURESTATEVIEW_FIELD_NUMBER: _ClassVar[int]
        pin_status: bool
        successStateView: PinUpdateCompletionWidget.PinUpdateStatus
        failureStateView: PinUpdateCompletionWidget.PinUpdateStatus
        def __init__(self, pin_status: bool = ..., successStateView: _Optional[_Union[PinUpdateCompletionWidget.PinUpdateStatus, _Mapping]] = ..., failureStateView: _Optional[_Union[PinUpdateCompletionWidget.PinUpdateStatus, _Mapping]] = ...) -> None: ...
    class PinUpdateStatus(_message.Message):
        __slots__ = ("title", "desc", "illustration", "primary_btn", "secondary_btn", "recaptcha_enabled")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BTN_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BTN_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        title: str
        desc: str
        illustration: _image_pb2.Image
        primary_btn: PinUpdateCompletionWidget.Button
        secondary_btn: PinUpdateCompletionWidget.Button
        recaptcha_enabled: bool
        def __init__(self, title: _Optional[str] = ..., desc: _Optional[str] = ..., illustration: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., primary_btn: _Optional[_Union[PinUpdateCompletionWidget.Button, _Mapping]] = ..., secondary_btn: _Optional[_Union[PinUpdateCompletionWidget.Button, _Mapping]] = ..., recaptcha_enabled: bool = ...) -> None: ...
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
    data: PinUpdateCompletionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PinUpdateCompletionWidget.Data, _Mapping]] = ...) -> None: ...
