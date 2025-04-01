from widget import selectable_horizontal_content_card_pb2 as _selectable_horizontal_content_card_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GridCardSelectionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ScrollDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERTICAL: _ClassVar[GridCardSelectionWidget.ScrollDirection]
        HORIZONTAL: _ClassVar[GridCardSelectionWidget.ScrollDirection]
    VERTICAL: GridCardSelectionWidget.ScrollDirection
    HORIZONTAL: GridCardSelectionWidget.ScrollDirection
    class Data(_message.Message):
        __slots__ = ("skip_cta", "header", "selectable_items", "primary_cta", "min_selected_items", "footer_info", "disclaimer_info", "next_items_url", "show_entry_animation", "list_scroll_direction", "non_scrolling_direction_item_count")
        SKIP_CTA_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        SELECTABLE_ITEMS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        MIN_SELECTED_ITEMS_FIELD_NUMBER: _ClassVar[int]
        FOOTER_INFO_FIELD_NUMBER: _ClassVar[int]
        DISCLAIMER_INFO_FIELD_NUMBER: _ClassVar[int]
        NEXT_ITEMS_URL_FIELD_NUMBER: _ClassVar[int]
        SHOW_ENTRY_ANIMATION_FIELD_NUMBER: _ClassVar[int]
        LIST_SCROLL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
        NON_SCROLLING_DIRECTION_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
        skip_cta: GridCardSelectionWidget.SkipCTA
        header: GridCardSelectionWidget.Header
        selectable_items: _containers.RepeatedCompositeFieldContainer[GridCardSelectionWidget.SelectableItem]
        primary_cta: GridCardSelectionWidget.CTA
        min_selected_items: int
        footer_info: str
        disclaimer_info: str
        next_items_url: str
        show_entry_animation: bool
        list_scroll_direction: GridCardSelectionWidget.ScrollDirection
        non_scrolling_direction_item_count: int
        def __init__(self, skip_cta: _Optional[_Union[GridCardSelectionWidget.SkipCTA, _Mapping]] = ..., header: _Optional[_Union[GridCardSelectionWidget.Header, _Mapping]] = ..., selectable_items: _Optional[_Iterable[_Union[GridCardSelectionWidget.SelectableItem, _Mapping]]] = ..., primary_cta: _Optional[_Union[GridCardSelectionWidget.CTA, _Mapping]] = ..., min_selected_items: _Optional[int] = ..., footer_info: _Optional[str] = ..., disclaimer_info: _Optional[str] = ..., next_items_url: _Optional[str] = ..., show_entry_animation: bool = ..., list_scroll_direction: _Optional[_Union[GridCardSelectionWidget.ScrollDirection, str]] = ..., non_scrolling_direction_item_count: _Optional[int] = ...) -> None: ...
    class SelectableItem(_message.Message):
        __slots__ = ("selectable_horizontal_content_card",)
        SELECTABLE_HORIZONTAL_CONTENT_CARD_FIELD_NUMBER: _ClassVar[int]
        selectable_horizontal_content_card: _selectable_horizontal_content_card_pb2.SelectableHorizontalContentCardWidget
        def __init__(self, selectable_horizontal_content_card: _Optional[_Union[_selectable_horizontal_content_card_pb2.SelectableHorizontalContentCardWidget, _Mapping]] = ...) -> None: ...
    class SkipCTA(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("title", "sub_title", "icon_name", "description", "lottie", "image")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        icon_name: str
        description: str
        lottie: _lottie_pb2.Lottie
        image: _image_pb2.Image
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., icon_name: _Optional[str] = ..., description: _Optional[str] = ..., lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("final_text", "actions", "icon_name")
        FINAL_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        final_text: str
        actions: _actions_pb2.Actions
        icon_name: str
        def __init__(self, final_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon_name: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: GridCardSelectionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[GridCardSelectionWidget.Data, _Mapping]] = ...) -> None: ...
