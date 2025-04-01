from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.trackers import communication_banner_trackers_pb2 as _communication_banner_trackers_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.text import text_pb2 as _text_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommnBannerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("bg_image", "hero_image", "title", "cta", "actions", "title_color", "background_color", "communication_banner_trackers", "refresh_info", "subtitle_info", "primary_button")
        BG_IMAGE_FIELD_NUMBER: _ClassVar[int]
        HERO_IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TITLE_COLOR_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
        COMMUNICATION_BANNER_TRACKERS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_INFO_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        bg_image: _image_pb2.Image
        hero_image: _image_pb2.Image
        title: str
        cta: CommnBannerWidget.CTA
        actions: _actions_pb2.Actions
        title_color: str
        background_color: CommnBannerWidget.BackgroundColor
        communication_banner_trackers: _communication_banner_trackers_pb2.CommunicationBannerTrackers
        refresh_info: CommnBannerWidget.RefreshInfo
        subtitle_info: CommnBannerWidget.SubtitleInfo
        primary_button: _button_pb2.Button
        def __init__(self, bg_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., hero_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., cta: _Optional[_Union[CommnBannerWidget.CTA, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., title_color: _Optional[str] = ..., background_color: _Optional[_Union[CommnBannerWidget.BackgroundColor, _Mapping]] = ..., communication_banner_trackers: _Optional[_Union[_communication_banner_trackers_pb2.CommunicationBannerTrackers, _Mapping]] = ..., refresh_info: _Optional[_Union[CommnBannerWidget.RefreshInfo, _Mapping]] = ..., subtitle_info: _Optional[_Union[CommnBannerWidget.SubtitleInfo, _Mapping]] = ..., primary_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    class RefreshInfo(_message.Message):
        __slots__ = ("url", "max_age_ms")
        URL_FIELD_NUMBER: _ClassVar[int]
        MAX_AGE_MS_FIELD_NUMBER: _ClassVar[int]
        url: str
        max_age_ms: int
        def __init__(self, url: _Optional[str] = ..., max_age_ms: _Optional[int] = ...) -> None: ...
    class BackgroundColor(_message.Message):
        __slots__ = ("start", "end")
        START_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        start: str
        end: str
        def __init__(self, start: _Optional[str] = ..., end: _Optional[str] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("text", "color", "icon_name")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        text: str
        color: str
        icon_name: str
        def __init__(self, text: _Optional[str] = ..., color: _Optional[str] = ..., icon_name: _Optional[str] = ...) -> None: ...
    class SubtitleInfo(_message.Message):
        __slots__ = ("sub_title", "icon_name", "alignment", "sub_title_text")
        class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEFAULT: _ClassVar[CommnBannerWidget.SubtitleInfo.Alignment]
            ABOVE_TITLE: _ClassVar[CommnBannerWidget.SubtitleInfo.Alignment]
        DEFAULT: CommnBannerWidget.SubtitleInfo.Alignment
        ABOVE_TITLE: CommnBannerWidget.SubtitleInfo.Alignment
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_TEXT_FIELD_NUMBER: _ClassVar[int]
        sub_title: str
        icon_name: str
        alignment: CommnBannerWidget.SubtitleInfo.Alignment
        sub_title_text: _text_pb2.Text
        def __init__(self, sub_title: _Optional[str] = ..., icon_name: _Optional[str] = ..., alignment: _Optional[_Union[CommnBannerWidget.SubtitleInfo.Alignment, str]] = ..., sub_title_text: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CommnBannerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CommnBannerWidget.Data, _Mapping]] = ...) -> None: ...
