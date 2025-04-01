from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class NotificationStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTIFICATION_STYLE_UNKNOWN: _ClassVar[NotificationWidget.NotificationStyle]
        NOTIFICATION_STYLE_DEFAULT: _ClassVar[NotificationWidget.NotificationStyle]
    NOTIFICATION_STYLE_UNKNOWN: NotificationWidget.NotificationStyle
    NOTIFICATION_STYLE_DEFAULT: NotificationWidget.NotificationStyle
    class Data(_message.Message):
        __slots__ = ("timestamp", "refresh_info", "show_notification_action", "hide_notification_action")
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        SHOW_NOTIFICATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        HIDE_NOTIFICATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        timestamp: int
        refresh_info: _refresh_info_pb2.RefreshInfo
        show_notification_action: NotificationWidget.ShowNotificationAction
        hide_notification_action: NotificationWidget.HideNotificationAction
        def __init__(self, timestamp: _Optional[int] = ..., refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ..., show_notification_action: _Optional[_Union[NotificationWidget.ShowNotificationAction, _Mapping]] = ..., hide_notification_action: _Optional[_Union[NotificationWidget.HideNotificationAction, _Mapping]] = ...) -> None: ...
    class ShowNotificationAction(_message.Message):
        __slots__ = ("property", "ui_widget")
        PROPERTY_FIELD_NUMBER: _ClassVar[int]
        UI_WIDGET_FIELD_NUMBER: _ClassVar[int]
        property: NotificationWidget.Property
        ui_widget: NotificationWidget.UiWidget
        def __init__(self, property: _Optional[_Union[NotificationWidget.Property, _Mapping]] = ..., ui_widget: _Optional[_Union[NotificationWidget.UiWidget, _Mapping]] = ...) -> None: ...
    class HideNotificationAction(_message.Message):
        __slots__ = ("property",)
        PROPERTY_FIELD_NUMBER: _ClassVar[int]
        property: NotificationWidget.Property
        def __init__(self, property: _Optional[_Union[NotificationWidget.Property, _Mapping]] = ...) -> None: ...
    class Property(_message.Message):
        __slots__ = ("channel", "notification_id", "is_sticky", "channel_name")
        CHANNEL_FIELD_NUMBER: _ClassVar[int]
        NOTIFICATION_ID_FIELD_NUMBER: _ClassVar[int]
        IS_STICKY_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
        channel: str
        notification_id: int
        is_sticky: bool
        channel_name: str
        def __init__(self, channel: _Optional[str] = ..., notification_id: _Optional[int] = ..., is_sticky: bool = ..., channel_name: _Optional[str] = ...) -> None: ...
    class UiWidget(_message.Message):
        __slots__ = ("notification_style", "headline", "title", "summary", "description", "image", "cta")
        NOTIFICATION_STYLE_FIELD_NUMBER: _ClassVar[int]
        HEADLINE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        notification_style: NotificationWidget.NotificationStyle
        headline: str
        title: str
        summary: str
        description: str
        image: NotificationWidget.ImageCTA
        cta: _containers.RepeatedCompositeFieldContainer[NotificationWidget.CTA]
        def __init__(self, notification_style: _Optional[_Union[NotificationWidget.NotificationStyle, str]] = ..., headline: _Optional[str] = ..., title: _Optional[str] = ..., summary: _Optional[str] = ..., description: _Optional[str] = ..., image: _Optional[_Union[NotificationWidget.ImageCTA, _Mapping]] = ..., cta: _Optional[_Iterable[_Union[NotificationWidget.CTA, _Mapping]]] = ...) -> None: ...
    class ImageCTA(_message.Message):
        __slots__ = ("url", "actions")
        URL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        url: str
        actions: _actions_pb2.Actions
        def __init__(self, url: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: NotificationWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[NotificationWidget.Data, _Mapping]] = ...) -> None: ...
