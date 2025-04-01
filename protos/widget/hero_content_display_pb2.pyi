from feature.image import image_pb2 as _image_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from widget import timer_pb2 as _timer_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroContentDisplayWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[HeroContentDisplayWidget.Alignment]
        LEFT: _ClassVar[HeroContentDisplayWidget.Alignment]
    UNSPECIFIED: HeroContentDisplayWidget.Alignment
    LEFT: HeroContentDisplayWidget.Alignment
    class Data(_message.Message):
        __slots__ = ("timer", "info_section", "bg_image", "primary_cta", "secondary_cta", "actions", "alt")
        TIMER_FIELD_NUMBER: _ClassVar[int]
        INFO_SECTION_FIELD_NUMBER: _ClassVar[int]
        BG_IMAGE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        timer: _timer_pb2.TimerWidget
        info_section: HeroContentDisplayWidget.ContentInfoSection
        bg_image: _image_pb2.Image
        primary_cta: HeroContentDisplayWidget.CTA
        secondary_cta: HeroContentDisplayWidget.CTA
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        def __init__(self, timer: _Optional[_Union[_timer_pb2.TimerWidget, _Mapping]] = ..., info_section: _Optional[_Union[HeroContentDisplayWidget.ContentInfoSection, _Mapping]] = ..., bg_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., primary_cta: _Optional[_Union[HeroContentDisplayWidget.CTA, _Mapping]] = ..., secondary_cta: _Optional[_Union[HeroContentDisplayWidget.CTA, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("button", "watchlist_button")
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_BUTTON_FIELD_NUMBER: _ClassVar[int]
        button: _button_pb2.Button
        watchlist_button: HeroContentDisplayWidget.WatchlistCTA
        def __init__(self, button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., watchlist_button: _Optional[_Union[HeroContentDisplayWidget.WatchlistCTA, _Mapping]] = ...) -> None: ...
    class WatchlistCTA(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _watchlist_info_pb2.WatchlistInfo
        def __init__(self, info: _Optional[_Union[_watchlist_info_pb2.WatchlistInfo, _Mapping]] = ...) -> None: ...
    class ContentInfoSection(_message.Message):
        __slots__ = ("title_cutout", "callout_tags", "alignment", "alt_tags")
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_TAGS_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        ALT_TAGS_FIELD_NUMBER: _ClassVar[int]
        title_cutout: _image_pb2.Image
        callout_tags: _containers.RepeatedCompositeFieldContainer[_callout_tag_pb2.CalloutTag]
        alignment: HeroContentDisplayWidget.Alignment
        alt_tags: _accessibility_pb2.Accessibility
        def __init__(self, title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., callout_tags: _Optional[_Iterable[_Union[_callout_tag_pb2.CalloutTag, _Mapping]]] = ..., alignment: _Optional[_Union[HeroContentDisplayWidget.Alignment, str]] = ..., alt_tags: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HeroContentDisplayWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HeroContentDisplayWidget.Data, _Mapping]] = ...) -> None: ...
