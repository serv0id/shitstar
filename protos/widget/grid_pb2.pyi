from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import horizontal_content_card_pb2 as _horizontal_content_card_pb2
from widget import vertical_content_poster_pb2 as _vertical_content_poster_pb2
from widget import square_content_poster_pb2 as _square_content_poster_pb2
from widget import search_horizontal_content_card_pb2 as _search_horizontal_content_card_pb2
from widget import horizontal_content_poster_pb2 as _horizontal_content_poster_pb2
from widget import cw_card_pb2 as _cw_card_pb2
from widget import image_banner_pb2 as _image_banner_pb2
from widget import usp_item_pb2 as _usp_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GridWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class TitleStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[GridWidget.TitleStyle]
        DESKTOP_TITLE_TITLE_1: _ClassVar[GridWidget.TitleStyle]
        DESKTOP_TITLE_TITLE_3: _ClassVar[GridWidget.TitleStyle]
    DEFAULT: GridWidget.TitleStyle
    DESKTOP_TITLE_TITLE_1: GridWidget.TitleStyle
    DESKTOP_TITLE_TITLE_3: GridWidget.TitleStyle
    class Data(_message.Message):
        __slots__ = ("title", "column_number", "more_grid_items_url", "title_style", "items")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        COLUMN_NUMBER_FIELD_NUMBER: _ClassVar[int]
        MORE_GRID_ITEMS_URL_FIELD_NUMBER: _ClassVar[int]
        TITLE_STYLE_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        title: str
        column_number: int
        more_grid_items_url: str
        title_style: GridWidget.TitleStyle
        items: _containers.RepeatedCompositeFieldContainer[GridWidget.Item]
        def __init__(self, title: _Optional[str] = ..., column_number: _Optional[int] = ..., more_grid_items_url: _Optional[str] = ..., title_style: _Optional[_Union[GridWidget.TitleStyle, str]] = ..., items: _Optional[_Iterable[_Union[GridWidget.Item, _Mapping]]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("horizontal_content_card", "vertical_content_poster", "square_content_poster", "horizontal_content_poster", "search_horizontal_content_card", "image_banner", "usp_item", "cw_card")
        HORIZONTAL_CONTENT_CARD_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        SQUARE_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        HORIZONTAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        SEARCH_HORIZONTAL_CONTENT_CARD_FIELD_NUMBER: _ClassVar[int]
        IMAGE_BANNER_FIELD_NUMBER: _ClassVar[int]
        USP_ITEM_FIELD_NUMBER: _ClassVar[int]
        CW_CARD_FIELD_NUMBER: _ClassVar[int]
        horizontal_content_card: _horizontal_content_card_pb2.HorizontalContentCardWidget
        vertical_content_poster: _vertical_content_poster_pb2.VerticalContentPosterWidget
        square_content_poster: _square_content_poster_pb2.SquareContentPosterWidget
        horizontal_content_poster: _horizontal_content_poster_pb2.HorizontalContentPosterWidget
        search_horizontal_content_card: _search_horizontal_content_card_pb2.SearchHorizontalContentCardWidget
        image_banner: _image_banner_pb2.ImageBannerWidget
        usp_item: _usp_item_pb2.UspItemWidget
        cw_card: _cw_card_pb2.CWCardWidget
        def __init__(self, horizontal_content_card: _Optional[_Union[_horizontal_content_card_pb2.HorizontalContentCardWidget, _Mapping]] = ..., vertical_content_poster: _Optional[_Union[_vertical_content_poster_pb2.VerticalContentPosterWidget, _Mapping]] = ..., square_content_poster: _Optional[_Union[_square_content_poster_pb2.SquareContentPosterWidget, _Mapping]] = ..., horizontal_content_poster: _Optional[_Union[_horizontal_content_poster_pb2.HorizontalContentPosterWidget, _Mapping]] = ..., search_horizontal_content_card: _Optional[_Union[_search_horizontal_content_card_pb2.SearchHorizontalContentCardWidget, _Mapping]] = ..., image_banner: _Optional[_Union[_image_banner_pb2.ImageBannerWidget, _Mapping]] = ..., usp_item: _Optional[_Union[_usp_item_pb2.UspItemWidget, _Mapping]] = ..., cw_card: _Optional[_Union[_cw_card_pb2.CWCardWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: GridWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[GridWidget.Data, _Mapping]] = ...) -> None: ...
