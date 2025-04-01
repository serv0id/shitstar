from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoSettingsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class SettingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DROPDOWN: _ClassVar[VideoSettingsWidget.SettingType]
        TOGGLE: _ClassVar[VideoSettingsWidget.SettingType]
    DROPDOWN: VideoSettingsWidget.SettingType
    TOGGLE: VideoSettingsWidget.SettingType
    class Data(_message.Message):
        __slots__ = ("video_quality_on_wifi", "video_quality_on_mobile_data", "autoplay_trailer", "picture_in_picture_mode")
        VIDEO_QUALITY_ON_WIFI_FIELD_NUMBER: _ClassVar[int]
        VIDEO_QUALITY_ON_MOBILE_DATA_FIELD_NUMBER: _ClassVar[int]
        AUTOPLAY_TRAILER_FIELD_NUMBER: _ClassVar[int]
        PICTURE_IN_PICTURE_MODE_FIELD_NUMBER: _ClassVar[int]
        video_quality_on_wifi: VideoSettingsWidget.VideoQualitySelector
        video_quality_on_mobile_data: VideoSettingsWidget.VideoQualitySelector
        autoplay_trailer: VideoSettingsWidget.ToggleSetting
        picture_in_picture_mode: VideoSettingsWidget.ToggleSetting
        def __init__(self, video_quality_on_wifi: _Optional[_Union[VideoSettingsWidget.VideoQualitySelector, _Mapping]] = ..., video_quality_on_mobile_data: _Optional[_Union[VideoSettingsWidget.VideoQualitySelector, _Mapping]] = ..., autoplay_trailer: _Optional[_Union[VideoSettingsWidget.ToggleSetting, _Mapping]] = ..., picture_in_picture_mode: _Optional[_Union[VideoSettingsWidget.ToggleSetting, _Mapping]] = ...) -> None: ...
    class DropdownSetting(_message.Message):
        __slots__ = ("settingType", "title", "selected_option", "options", "actions")
        SETTINGTYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SELECTED_OPTION_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        settingType: VideoSettingsWidget.SettingType
        title: str
        selected_option: str
        options: _containers.RepeatedScalarFieldContainer[str]
        actions: _actions_pb2.Actions
        def __init__(self, settingType: _Optional[_Union[VideoSettingsWidget.SettingType, str]] = ..., title: _Optional[str] = ..., selected_option: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class ToggleSetting(_message.Message):
        __slots__ = ("settingType", "icon_name", "title", "description", "actions")
        SETTINGTYPE_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        settingType: VideoSettingsWidget.SettingType
        icon_name: str
        title: str
        description: str
        actions: _actions_pb2.Actions
        def __init__(self, settingType: _Optional[_Union[VideoSettingsWidget.SettingType, str]] = ..., icon_name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class VideoQuality(_message.Message):
        __slots__ = ("id", "quality", "upgrade_footer", "resolution_pixels", "description")
        ID_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_FOOTER_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_PIXELS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        id: str
        quality: str
        upgrade_footer: str
        resolution_pixels: str
        description: str
        def __init__(self, id: _Optional[str] = ..., quality: _Optional[str] = ..., upgrade_footer: _Optional[str] = ..., resolution_pixels: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class VideoQualitySelector(_message.Message):
        __slots__ = ("title", "bottom_popup_title", "video_quality", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_POPUP_TITLE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_QUALITY_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        bottom_popup_title: str
        video_quality: _containers.RepeatedCompositeFieldContainer[VideoSettingsWidget.VideoQuality]
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., bottom_popup_title: _Optional[str] = ..., video_quality: _Optional[_Iterable[_Union[VideoSettingsWidget.VideoQuality, _Mapping]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VideoSettingsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VideoSettingsWidget.Data, _Mapping]] = ...) -> None: ...
