from base import widget_commons_pb2 as _widget_commons_pb2
from widget import promo_landing_pb2 as _promo_landing_pb2
from widget import grid_pb2 as _grid_pb2
from widget import usp_item_pb2 as _usp_item_pb2
from widget import usp_details_pb2 as _usp_details_pb2
from widget import divider_pb2 as _divider_pb2
from widget import promo_landing_header_pb2 as _promo_landing_header_pb2
from widget import faq_pb2 as _faq_pb2
from widget import prelaunch_hero_pb2 as _prelaunch_hero_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PromoLandingContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[PromoLandingContainerWidget.Item]
        def __init__(self, items: _Optional[_Iterable[_Union[PromoLandingContainerWidget.Item, _Mapping]]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("header", "promo_landing", "usp_detail", "grid", "divider", "faq", "prelaunch_hero")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        PROMO_LANDING_FIELD_NUMBER: _ClassVar[int]
        USP_DETAIL_FIELD_NUMBER: _ClassVar[int]
        GRID_FIELD_NUMBER: _ClassVar[int]
        DIVIDER_FIELD_NUMBER: _ClassVar[int]
        FAQ_FIELD_NUMBER: _ClassVar[int]
        PRELAUNCH_HERO_FIELD_NUMBER: _ClassVar[int]
        header: _promo_landing_header_pb2.PromoLandingHeaderWidget
        promo_landing: _promo_landing_pb2.PromoLandingWidget
        usp_detail: _usp_details_pb2.USPDetailsWidget
        grid: _grid_pb2.GridWidget
        divider: _divider_pb2.DividerWidget
        faq: _faq_pb2.FAQWidget
        prelaunch_hero: _prelaunch_hero_pb2.PrelaunchHeroWidget
        def __init__(self, header: _Optional[_Union[_promo_landing_header_pb2.PromoLandingHeaderWidget, _Mapping]] = ..., promo_landing: _Optional[_Union[_promo_landing_pb2.PromoLandingWidget, _Mapping]] = ..., usp_detail: _Optional[_Union[_usp_details_pb2.USPDetailsWidget, _Mapping]] = ..., grid: _Optional[_Union[_grid_pb2.GridWidget, _Mapping]] = ..., divider: _Optional[_Union[_divider_pb2.DividerWidget, _Mapping]] = ..., faq: _Optional[_Union[_faq_pb2.FAQWidget, _Mapping]] = ..., prelaunch_hero: _Optional[_Union[_prelaunch_hero_pb2.PrelaunchHeroWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PromoLandingContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PromoLandingContainerWidget.Data, _Mapping]] = ...) -> None: ...
