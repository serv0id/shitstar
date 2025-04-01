from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import gec_masthead_pb2 as _gec_masthead_pb2
from widget import sports_masthead_pb2 as _sports_masthead_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MastheadWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class SlideIndicatorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[MastheadWidget.SlideIndicatorType]
        CAROUSEL_SLIDE_INDICATOR: _ClassVar[MastheadWidget.SlideIndicatorType]
        NUMBER_SLIDE_INDICATOR: _ClassVar[MastheadWidget.SlideIndicatorType]
    DEFAULT: MastheadWidget.SlideIndicatorType
    CAROUSEL_SLIDE_INDICATOR: MastheadWidget.SlideIndicatorType
    NUMBER_SLIDE_INDICATOR: MastheadWidget.SlideIndicatorType
    class Data(_message.Message):
        __slots__ = ("auto_scroll", "interval_in_ms", "items", "refresh_info", "slide_indicator_type", "alt_swipe_hint")
        AUTO_SCROLL_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_IN_MS_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        SLIDE_INDICATOR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ALT_SWIPE_HINT_FIELD_NUMBER: _ClassVar[int]
        auto_scroll: bool
        interval_in_ms: int
        items: _containers.RepeatedCompositeFieldContainer[MastheadWidget.Item]
        refresh_info: MastheadWidget.RefreshInfo
        slide_indicator_type: MastheadWidget.SlideIndicatorType
        alt_swipe_hint: _accessibility_pb2.Accessibility
        def __init__(self, auto_scroll: bool = ..., interval_in_ms: _Optional[int] = ..., items: _Optional[_Iterable[_Union[MastheadWidget.Item, _Mapping]]] = ..., refresh_info: _Optional[_Union[MastheadWidget.RefreshInfo, _Mapping]] = ..., slide_indicator_type: _Optional[_Union[MastheadWidget.SlideIndicatorType, str]] = ..., alt_swipe_hint: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class RefreshInfo(_message.Message):
        __slots__ = ("max_age_ms", "refresh_url")
        MAX_AGE_MS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        max_age_ms: int
        refresh_url: str
        def __init__(self, max_age_ms: _Optional[int] = ..., refresh_url: _Optional[str] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("gec_masthead", "sports_masthead")
        GEC_MASTHEAD_FIELD_NUMBER: _ClassVar[int]
        SPORTS_MASTHEAD_FIELD_NUMBER: _ClassVar[int]
        gec_masthead: _gec_masthead_pb2.GECMastheadWidget
        sports_masthead: _sports_masthead_pb2.SportsMastheadWidget
        def __init__(self, gec_masthead: _Optional[_Union[_gec_masthead_pb2.GECMastheadWidget, _Mapping]] = ..., sports_masthead: _Optional[_Union[_sports_masthead_pb2.SportsMastheadWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MastheadWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MastheadWidget.Data, _Mapping]] = ...) -> None: ...
