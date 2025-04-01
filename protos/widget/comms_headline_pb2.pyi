from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.trackers import tracker_pb2 as _tracker_pb2
from feature.trackers import communication_banner_trackers_pb2 as _communication_banner_trackers_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommsHeadlineWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class UrlSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE: _ClassVar[CommsHeadlineWidget.UrlSourceType]
        LOTTIE: _ClassVar[CommsHeadlineWidget.UrlSourceType]
    IMAGE: CommsHeadlineWidget.UrlSourceType
    LOTTIE: CommsHeadlineWidget.UrlSourceType
    class TextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[CommsHeadlineWidget.TextType]
        ALERT: _ClassVar[CommsHeadlineWidget.TextType]
        BRAND: _ClassVar[CommsHeadlineWidget.TextType]
    DEFAULT: CommsHeadlineWidget.TextType
    ALERT: CommsHeadlineWidget.TextType
    BRAND: CommsHeadlineWidget.TextType
    class Data(_message.Message):
        __slots__ = ("url_source_type", "title", "sub_title_info", "primary_cta", "dismiss_icon", "trackers", "refresh_info", "secondary_cta", "title_info", "img_info", "lottie_url")
        URL_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_INFO_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        DISMISS_ICON_FIELD_NUMBER: _ClassVar[int]
        TRACKERS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        TITLE_INFO_FIELD_NUMBER: _ClassVar[int]
        IMG_INFO_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_URL_FIELD_NUMBER: _ClassVar[int]
        url_source_type: CommsHeadlineWidget.UrlSourceType
        title: str
        sub_title_info: CommsHeadlineWidget.SubTitleInfo
        primary_cta: CommsHeadlineWidget.PrimaryCTA
        dismiss_icon: CommsHeadlineWidget.DismissIcon
        trackers: _communication_banner_trackers_pb2.CommunicationBannerTrackers
        refresh_info: CommsHeadlineWidget.RefreshInfo
        secondary_cta: CommsHeadlineWidget.PrimaryCTA
        title_info: CommsHeadlineWidget.TitleInfo
        img_info: _image_pb2.Image
        lottie_url: str
        def __init__(self, url_source_type: _Optional[_Union[CommsHeadlineWidget.UrlSourceType, str]] = ..., title: _Optional[str] = ..., sub_title_info: _Optional[_Union[CommsHeadlineWidget.SubTitleInfo, _Mapping]] = ..., primary_cta: _Optional[_Union[CommsHeadlineWidget.PrimaryCTA, _Mapping]] = ..., dismiss_icon: _Optional[_Union[CommsHeadlineWidget.DismissIcon, _Mapping]] = ..., trackers: _Optional[_Union[_communication_banner_trackers_pb2.CommunicationBannerTrackers, _Mapping]] = ..., refresh_info: _Optional[_Union[CommsHeadlineWidget.RefreshInfo, _Mapping]] = ..., secondary_cta: _Optional[_Union[CommsHeadlineWidget.PrimaryCTA, _Mapping]] = ..., title_info: _Optional[_Union[CommsHeadlineWidget.TitleInfo, _Mapping]] = ..., img_info: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., lottie_url: _Optional[str] = ...) -> None: ...
    class SubTitleInfo(_message.Message):
        __slots__ = ("text", "text_type")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
        text: str
        text_type: CommsHeadlineWidget.TextType
        def __init__(self, text: _Optional[str] = ..., text_type: _Optional[_Union[CommsHeadlineWidget.TextType, str]] = ...) -> None: ...
    class TitleInfo(_message.Message):
        __slots__ = ("text", "text_type")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
        text: str
        text_type: CommsHeadlineWidget.TextType
        def __init__(self, text: _Optional[str] = ..., text_type: _Optional[_Union[CommsHeadlineWidget.TextType, str]] = ...) -> None: ...
    class PrimaryCTA(_message.Message):
        __slots__ = ("text", "sub_text", "actions", "click_tracker")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CLICK_TRACKER_FIELD_NUMBER: _ClassVar[int]
        text: str
        sub_text: str
        actions: _actions_pb2.Actions
        click_tracker: _tracker_pb2.Tracker
        def __init__(self, text: _Optional[str] = ..., sub_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., click_tracker: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ...) -> None: ...
    class DismissIcon(_message.Message):
        __slots__ = ("icon_name", "click_tracker", "label")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        CLICK_TRACKER_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        click_tracker: _tracker_pb2.Tracker
        label: str
        def __init__(self, icon_name: _Optional[str] = ..., click_tracker: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ..., label: _Optional[str] = ...) -> None: ...
    class RefreshInfo(_message.Message):
        __slots__ = ("url", "max_age_ms")
        URL_FIELD_NUMBER: _ClassVar[int]
        MAX_AGE_MS_FIELD_NUMBER: _ClassVar[int]
        url: str
        max_age_ms: int
        def __init__(self, url: _Optional[str] = ..., max_age_ms: _Optional[int] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CommsHeadlineWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CommsHeadlineWidget.Data, _Mapping]] = ...) -> None: ...
