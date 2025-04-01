from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.trackers import tracker_pb2 as _tracker_pb2
from feature.trackers import communication_banner_trackers_pb2 as _communication_banner_trackers_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from widget import logo_pb2 as _logo_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShortHeadlineWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class TextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ShortHeadlineWidget.TextType]
        ALERT: _ClassVar[ShortHeadlineWidget.TextType]
        BRAND: _ClassVar[ShortHeadlineWidget.TextType]
    DEFAULT: ShortHeadlineWidget.TextType
    ALERT: ShortHeadlineWidget.TextType
    BRAND: ShortHeadlineWidget.TextType
    class Data(_message.Message):
        __slots__ = ("variant", "title_info", "sub_title_info", "primary_cta", "trackers", "refresh_info")
        VARIANT_FIELD_NUMBER: _ClassVar[int]
        TITLE_INFO_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_INFO_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        TRACKERS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        variant: _logo_pb2.LogoVariant
        title_info: ShortHeadlineWidget.TitleInfo
        sub_title_info: ShortHeadlineWidget.SubTitleInfo
        primary_cta: ShortHeadlineWidget.CTA
        trackers: _communication_banner_trackers_pb2.CommunicationBannerTrackers
        refresh_info: _refresh_info_pb2.RefreshInfo
        def __init__(self, variant: _Optional[_Union[_logo_pb2.LogoVariant, str]] = ..., title_info: _Optional[_Union[ShortHeadlineWidget.TitleInfo, _Mapping]] = ..., sub_title_info: _Optional[_Union[ShortHeadlineWidget.SubTitleInfo, _Mapping]] = ..., primary_cta: _Optional[_Union[ShortHeadlineWidget.CTA, _Mapping]] = ..., trackers: _Optional[_Union[_communication_banner_trackers_pb2.CommunicationBannerTrackers, _Mapping]] = ..., refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ...) -> None: ...
    class TitleInfo(_message.Message):
        __slots__ = ("text", "text_type")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
        text: str
        text_type: ShortHeadlineWidget.TextType
        def __init__(self, text: _Optional[str] = ..., text_type: _Optional[_Union[ShortHeadlineWidget.TextType, str]] = ...) -> None: ...
    class SubTitleInfo(_message.Message):
        __slots__ = ("text", "strikethrough_text")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        STRIKETHROUGH_TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        strikethrough_text: str
        def __init__(self, text: _Optional[str] = ..., strikethrough_text: _Optional[str] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("text", "strikethrough_text", "actions", "click_tracker")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        STRIKETHROUGH_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CLICK_TRACKER_FIELD_NUMBER: _ClassVar[int]
        text: str
        strikethrough_text: str
        actions: _actions_pb2.Actions
        click_tracker: _tracker_pb2.Tracker
        def __init__(self, text: _Optional[str] = ..., strikethrough_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., click_tracker: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ShortHeadlineWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ShortHeadlineWidget.Data, _Mapping]] = ...) -> None: ...
