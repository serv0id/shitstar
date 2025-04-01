from base import template_pb2 as _template_pb2
from widget import player_settings_pb2 as _player_settings_pb2
from widget import player_settings_v2_pb2 as _player_settings_v2_pb2
from widget import player_report_menu_pb2 as _player_report_menu_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchOverlayWidget(_message.Message):
    __slots__ = ("template", "data")
    class Data(_message.Message):
        __slots__ = ("settings", "report_menu", "settings_v2")
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        REPORT_MENU_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_V2_FIELD_NUMBER: _ClassVar[int]
        settings: _player_settings_pb2.PlayerSettingsWidget
        report_menu: _player_report_menu_pb2.PlayerReportMenuWidget
        settings_v2: _player_settings_v2_pb2.PlayerSettingsWidgetV2
        def __init__(self, settings: _Optional[_Union[_player_settings_pb2.PlayerSettingsWidget, _Mapping]] = ..., report_menu: _Optional[_Union[_player_report_menu_pb2.PlayerReportMenuWidget, _Mapping]] = ..., settings_v2: _Optional[_Union[_player_settings_v2_pb2.PlayerSettingsWidgetV2, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    data: WatchOverlayWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., data: _Optional[_Union[WatchOverlayWidget.Data, _Mapping]] = ...) -> None: ...
