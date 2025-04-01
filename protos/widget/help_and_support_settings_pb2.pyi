from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelpAndSupportSettingsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("contact_us", "help_center", "title", "actions")
        CONTACT_US_FIELD_NUMBER: _ClassVar[int]
        HELP_CENTER_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        contact_us: HelpAndSupportSettingsWidget.ClickableSetting
        help_center: HelpAndSupportSettingsWidget.ClickableSetting
        title: str
        actions: _actions_pb2.Actions
        def __init__(self, contact_us: _Optional[_Union[HelpAndSupportSettingsWidget.ClickableSetting, _Mapping]] = ..., help_center: _Optional[_Union[HelpAndSupportSettingsWidget.ClickableSetting, _Mapping]] = ..., title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class ClickableSetting(_message.Message):
        __slots__ = ("title", "description", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HelpAndSupportSettingsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HelpAndSupportSettingsWidget.Data, _Mapping]] = ...) -> None: ...
