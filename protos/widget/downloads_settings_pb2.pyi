from base import widget_commons_pb2 as _widget_commons_pb2
from base import template_pb2 as _template_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadsSettingsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class SettingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DROPDOWN: _ClassVar[DownloadsSettingsWidget.SettingType]
        TOGGLE: _ClassVar[DownloadsSettingsWidget.SettingType]
    DROPDOWN: DownloadsSettingsWidget.SettingType
    TOGGLE: DownloadsSettingsWidget.SettingType
    class Data(_message.Message):
        __slots__ = ("download_video_quality", "delete_downloads", "phone_storage")
        DOWNLOAD_VIDEO_QUALITY_FIELD_NUMBER: _ClassVar[int]
        DELETE_DOWNLOADS_FIELD_NUMBER: _ClassVar[int]
        PHONE_STORAGE_FIELD_NUMBER: _ClassVar[int]
        download_video_quality: DownloadsSettingsWidget.DownloadVideoQuality
        delete_downloads: DownloadsSettingsWidget.DeleteDownloads
        phone_storage: DownloadsSettingsWidget.PhoneStorage
        def __init__(self, download_video_quality: _Optional[_Union[DownloadsSettingsWidget.DownloadVideoQuality, _Mapping]] = ..., delete_downloads: _Optional[_Union[DownloadsSettingsWidget.DeleteDownloads, _Mapping]] = ..., phone_storage: _Optional[_Union[DownloadsSettingsWidget.PhoneStorage, _Mapping]] = ...) -> None: ...
    class DropdownSetting(_message.Message):
        __slots__ = ("settingType", "title", "selected_option", "options", "actions")
        SETTINGTYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SELECTED_OPTION_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        settingType: DownloadsSettingsWidget.SettingType
        title: str
        selected_option: str
        options: _containers.RepeatedScalarFieldContainer[str]
        actions: _actions_pb2.Actions
        def __init__(self, settingType: _Optional[_Union[DownloadsSettingsWidget.SettingType, str]] = ..., title: _Optional[str] = ..., selected_option: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class ToggleSetting(_message.Message):
        __slots__ = ("settingType", "icon_name", "title", "description", "actions")
        SETTINGTYPE_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        settingType: DownloadsSettingsWidget.SettingType
        icon_name: str
        title: str
        description: str
        actions: _actions_pb2.Actions
        def __init__(self, settingType: _Optional[_Union[DownloadsSettingsWidget.SettingType, str]] = ..., icon_name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class SetAsDefaultQuality(_message.Message):
        __slots__ = ("set_as_default_quality", "actions")
        SET_AS_DEFAULT_QUALITY_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        set_as_default_quality: str
        actions: _actions_pb2.Actions
        def __init__(self, set_as_default_quality: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class DownloadVideoQuality(_message.Message):
        __slots__ = ("title", "qualities", "selected_quality_time", "set_as_default_quality", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        QUALITIES_FIELD_NUMBER: _ClassVar[int]
        SELECTED_QUALITY_TIME_FIELD_NUMBER: _ClassVar[int]
        SET_AS_DEFAULT_QUALITY_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        qualities: _containers.RepeatedScalarFieldContainer[str]
        selected_quality_time: str
        set_as_default_quality: DownloadsSettingsWidget.SetAsDefaultQuality
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., qualities: _Optional[_Iterable[str]] = ..., selected_quality_time: _Optional[str] = ..., set_as_default_quality: _Optional[_Union[DownloadsSettingsWidget.SetAsDefaultQuality, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class DeleteDownloads(_message.Message):
        __slots__ = ("title", "delete_btn_text", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DELETE_BTN_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        delete_btn_text: str
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., delete_btn_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PhoneStorage(_message.Message):
        __slots__ = ("used", "org_title", "actions")
        USED_FIELD_NUMBER: _ClassVar[int]
        ORG_TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        used: str
        org_title: str
        actions: _actions_pb2.Actions
        def __init__(self, used: _Optional[str] = ..., org_title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DownloadsSettingsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DownloadsSettingsWidget.Data, _Mapping]] = ...) -> None: ...
