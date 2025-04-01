from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import video_settings_pb2 as _video_settings_pb2
from widget import notification_settings_pb2 as _notification_settings_pb2
from widget import downloads_settings_pb2 as _downloads_settings_pb2
from widget import help_and_support_settings_pb2 as _help_and_support_settings_pb2
from widget import profile_settings_pb2 as _profile_settings_pb2
from widget import parental_control_settings_pb2 as _parental_control_settings_pb2
from widget import account_settings_pb2 as _account_settings_pb2
from widget import account_settings_container_pb2 as _account_settings_container_pb2
from widget import membership_actions_pb2 as _membership_actions_pb2
from widget import generic_settings_pb2 as _generic_settings_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettingsTabWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("before_icon_name", "after_icon_name", "tab_header", "tab_sub_header", "tab_content", "has_divider", "is_preselected", "before_icon_url")
        BEFORE_ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        AFTER_ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TAB_HEADER_FIELD_NUMBER: _ClassVar[int]
        TAB_SUB_HEADER_FIELD_NUMBER: _ClassVar[int]
        TAB_CONTENT_FIELD_NUMBER: _ClassVar[int]
        HAS_DIVIDER_FIELD_NUMBER: _ClassVar[int]
        IS_PRESELECTED_FIELD_NUMBER: _ClassVar[int]
        BEFORE_ICON_URL_FIELD_NUMBER: _ClassVar[int]
        before_icon_name: str
        after_icon_name: str
        tab_header: str
        tab_sub_header: str
        tab_content: SettingsTabWidget.TabContent
        has_divider: bool
        is_preselected: bool
        before_icon_url: str
        def __init__(self, before_icon_name: _Optional[str] = ..., after_icon_name: _Optional[str] = ..., tab_header: _Optional[str] = ..., tab_sub_header: _Optional[str] = ..., tab_content: _Optional[_Union[SettingsTabWidget.TabContent, _Mapping]] = ..., has_divider: bool = ..., is_preselected: bool = ..., before_icon_url: _Optional[str] = ...) -> None: ...
    class TabContent(_message.Message):
        __slots__ = ("download_settings", "video_settings", "notification_settings", "profile_settings", "parental_settings", "account_settings", "help_and_support_info", "membership_actions", "generic_settings", "account_settings_container", "actions")
        DOWNLOAD_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        PROFILE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        PARENTAL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        HELP_AND_SUPPORT_INFO_FIELD_NUMBER: _ClassVar[int]
        MEMBERSHIP_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        GENERIC_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_SETTINGS_CONTAINER_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        download_settings: _downloads_settings_pb2.DownloadsSettingsWidget
        video_settings: _video_settings_pb2.VideoSettingsWidget
        notification_settings: _notification_settings_pb2.NotificationSettingsWidget
        profile_settings: _profile_settings_pb2.ProfileSettingsWidget
        parental_settings: _parental_control_settings_pb2.ParentalControlSettingsWidget
        account_settings: _account_settings_pb2.AccountSettingsWidget
        help_and_support_info: _help_and_support_settings_pb2.HelpAndSupportSettingsWidget
        membership_actions: _membership_actions_pb2.MembershipActionsWidget
        generic_settings: _generic_settings_pb2.GenericSettingsWidget
        account_settings_container: _account_settings_container_pb2.AccountSettingsContainerWidget
        actions: _actions_pb2.Actions
        def __init__(self, download_settings: _Optional[_Union[_downloads_settings_pb2.DownloadsSettingsWidget, _Mapping]] = ..., video_settings: _Optional[_Union[_video_settings_pb2.VideoSettingsWidget, _Mapping]] = ..., notification_settings: _Optional[_Union[_notification_settings_pb2.NotificationSettingsWidget, _Mapping]] = ..., profile_settings: _Optional[_Union[_profile_settings_pb2.ProfileSettingsWidget, _Mapping]] = ..., parental_settings: _Optional[_Union[_parental_control_settings_pb2.ParentalControlSettingsWidget, _Mapping]] = ..., account_settings: _Optional[_Union[_account_settings_pb2.AccountSettingsWidget, _Mapping]] = ..., help_and_support_info: _Optional[_Union[_help_and_support_settings_pb2.HelpAndSupportSettingsWidget, _Mapping]] = ..., membership_actions: _Optional[_Union[_membership_actions_pb2.MembershipActionsWidget, _Mapping]] = ..., generic_settings: _Optional[_Union[_generic_settings_pb2.GenericSettingsWidget, _Mapping]] = ..., account_settings_container: _Optional[_Union[_account_settings_container_pb2.AccountSettingsContainerWidget, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SettingsTabWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SettingsTabWidget.Data, _Mapping]] = ...) -> None: ...
