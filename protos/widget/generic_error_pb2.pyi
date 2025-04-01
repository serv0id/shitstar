from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GenericErrorWidget(_message.Message):
    __slots__ = ("widget_commons", "image", "title", "description", "primary_button", "on_shown_actions", "on_dismiss_actions")
    class Button(_message.Message):
        __slots__ = ("label", "action")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        label: str
        action: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
    ON_SHOWN_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    ON_DISMISS_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    image: _image_pb2.Image
    title: str
    description: str
    primary_button: GenericErrorWidget.Button
    on_shown_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    on_dismiss_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., primary_button: _Optional[_Union[GenericErrorWidget.Button, _Mapping]] = ..., on_shown_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., on_dismiss_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
