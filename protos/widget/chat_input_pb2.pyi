from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import text_area_pb2 as _text_area_pb2
from feature.atom import button_pb2 as _button_pb2
from widget import avatar_pb2 as _avatar_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatInputWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("avatar", "input", "send")
        AVATAR_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        SEND_FIELD_NUMBER: _ClassVar[int]
        avatar: _avatar_pb2.AvatarWidget
        input: _text_area_pb2.TextAreaWidget
        send: _button_pb2.Button
        def __init__(self, avatar: _Optional[_Union[_avatar_pb2.AvatarWidget, _Mapping]] = ..., input: _Optional[_Union[_text_area_pb2.TextAreaWidget, _Mapping]] = ..., send: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ChatInputWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ChatInputWidget.Data, _Mapping]] = ...) -> None: ...
