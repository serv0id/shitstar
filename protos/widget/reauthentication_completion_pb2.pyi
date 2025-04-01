from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReauthenticationCompletionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("success_state_view", "failure_state_view")
        SUCCESS_STATE_VIEW_FIELD_NUMBER: _ClassVar[int]
        FAILURE_STATE_VIEW_FIELD_NUMBER: _ClassVar[int]
        success_state_view: ReauthenticationCompletionWidget.StateView
        failure_state_view: ReauthenticationCompletionWidget.StateView
        def __init__(self, success_state_view: _Optional[_Union[ReauthenticationCompletionWidget.StateView, _Mapping]] = ..., failure_state_view: _Optional[_Union[ReauthenticationCompletionWidget.StateView, _Mapping]] = ...) -> None: ...
    class StateView(_message.Message):
        __slots__ = ("title", "desc", "illustration", "primary_btn", "secondary_btn")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BTN_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BTN_FIELD_NUMBER: _ClassVar[int]
        title: str
        desc: str
        illustration: _image_pb2.Image
        primary_btn: ReauthenticationCompletionWidget.Button
        secondary_btn: ReauthenticationCompletionWidget.Button
        def __init__(self, title: _Optional[str] = ..., desc: _Optional[str] = ..., illustration: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., primary_btn: _Optional[_Union[ReauthenticationCompletionWidget.Button, _Mapping]] = ..., secondary_btn: _Optional[_Union[ReauthenticationCompletionWidget.Button, _Mapping]] = ...) -> None: ...
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
    data: ReauthenticationCompletionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ReauthenticationCompletionWidget.Data, _Mapping]] = ...) -> None: ...
