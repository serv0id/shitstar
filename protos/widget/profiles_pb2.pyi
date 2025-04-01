from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfilesWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("edit_button", "profiles", "title")
        EDIT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        PROFILES_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        edit_button: ProfilesWidget.EditButton
        profiles: _containers.RepeatedCompositeFieldContainer[ProfilesWidget.Profile]
        title: str
        def __init__(self, edit_button: _Optional[_Union[ProfilesWidget.EditButton, _Mapping]] = ..., profiles: _Optional[_Iterable[_Union[ProfilesWidget.Profile, _Mapping]]] = ..., title: _Optional[str] = ...) -> None: ...
    class Profile(_message.Message):
        __slots__ = ("id", "icon_name", "profile_name", "actions", "is_selected")
        ID_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        PROFILE_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        id: str
        icon_name: str
        profile_name: str
        actions: _actions_pb2.Actions
        is_selected: bool
        def __init__(self, id: _Optional[str] = ..., icon_name: _Optional[str] = ..., profile_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., is_selected: bool = ...) -> None: ...
    class EditButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ProfilesWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ProfilesWidget.Data, _Mapping]] = ...) -> None: ...
