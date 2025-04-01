from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import horizontal_content_card_pb2 as _horizontal_content_card_pb2
from widget import vertical_content_poster_pb2 as _vertical_content_poster_pb2
from widget import square_content_poster_pb2 as _square_content_poster_pb2
from widget import playable_content_pb2 as _playable_content_pb2
from widget import vertical_large_content_poster_pb2 as _vertical_large_content_poster_pb2
from widget import horizontal_content_poster_pb2 as _horizontal_content_poster_pb2
from widget import horizontal_medium_content_poster_pb2 as _horizontal_medium_content_poster_pb2
from widget import countdown_content_pb2 as _countdown_content_pb2
from widget import image_overlay_vertical_content_poster_pb2 as _image_overlay_vertical_content_poster_pb2
from widget import image_overlay_vertical_large_content_poster_pb2 as _image_overlay_vertical_large_content_poster_pb2
from widget import match_card_pb2 as _match_card_pb2
from widget import button_stack_pb2 as _button_stack_pb2
from widget import header_pb2 as _header_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import screen_size_image_pb2 as _screen_size_image_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScrollableTrayWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class TrayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ScrollableTrayWidget.TrayType]
        THEMED: _ClassVar[ScrollableTrayWidget.TrayType]
    UNSPECIFIED: ScrollableTrayWidget.TrayType
    THEMED: ScrollableTrayWidget.TrayType
    class Data(_message.Message):
        __slots__ = ("item_template_name", "num_rows", "header", "items", "next_tray_url", "refresh_info", "tray_header", "tray_background", "tray_type", "land_num_rows")
        ITEM_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        NEXT_TRAY_URL_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        TRAY_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
        TRAY_TYPE_FIELD_NUMBER: _ClassVar[int]
        LAND_NUM_ROWS_FIELD_NUMBER: _ClassVar[int]
        item_template_name: str
        num_rows: int
        header: ScrollableTrayWidget.Header
        items: _containers.RepeatedCompositeFieldContainer[ScrollableTrayWidget.Item]
        next_tray_url: str
        refresh_info: _refresh_info_pb2.RefreshInfo
        tray_header: _header_pb2.HeaderWidget
        tray_background: ScrollableTrayWidget.TrayBackground
        tray_type: ScrollableTrayWidget.TrayType
        land_num_rows: int
        def __init__(self, item_template_name: _Optional[str] = ..., num_rows: _Optional[int] = ..., header: _Optional[_Union[ScrollableTrayWidget.Header, _Mapping]] = ..., items: _Optional[_Iterable[_Union[ScrollableTrayWidget.Item, _Mapping]]] = ..., next_tray_url: _Optional[str] = ..., refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ..., tray_header: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ..., tray_background: _Optional[_Union[ScrollableTrayWidget.TrayBackground, _Mapping]] = ..., tray_type: _Optional[_Union[ScrollableTrayWidget.TrayType, str]] = ..., land_num_rows: _Optional[int] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("regular_tray_header", "anchored_tray_header", "branded_tray_header", "decorated_tray_header")
        REGULAR_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        ANCHORED_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        BRANDED_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        DECORATED_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        regular_tray_header: ScrollableTrayWidget.RegularTrayHeader
        anchored_tray_header: ScrollableTrayWidget.AnchoredTrayHeader
        branded_tray_header: ScrollableTrayWidget.BrandedTrayHeader
        decorated_tray_header: ScrollableTrayWidget.DecoratedTrayHeader
        def __init__(self, regular_tray_header: _Optional[_Union[ScrollableTrayWidget.RegularTrayHeader, _Mapping]] = ..., anchored_tray_header: _Optional[_Union[ScrollableTrayWidget.AnchoredTrayHeader, _Mapping]] = ..., branded_tray_header: _Optional[_Union[ScrollableTrayWidget.BrandedTrayHeader, _Mapping]] = ..., decorated_tray_header: _Optional[_Union[ScrollableTrayWidget.DecoratedTrayHeader, _Mapping]] = ...) -> None: ...
    class DecoratedTrayHeader(_message.Message):
        __slots__ = ("elements", "actions", "cta")
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[_callout_tag_pb2.CalloutTag]
        actions: _actions_pb2.Actions
        cta: ScrollableTrayWidget.IconLabelCTA
        def __init__(self, elements: _Optional[_Iterable[_Union[_callout_tag_pb2.CalloutTag, _Mapping]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[ScrollableTrayWidget.IconLabelCTA, _Mapping]] = ...) -> None: ...
    class RegularTrayHeader(_message.Message):
        __slots__ = ("title", "actions", "cta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        title: str
        actions: _actions_pb2.Actions
        cta: ScrollableTrayWidget.IconLabelCTA
        def __init__(self, title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[ScrollableTrayWidget.IconLabelCTA, _Mapping]] = ...) -> None: ...
    class AnchoredTrayHeader(_message.Message):
        __slots__ = ("title", "sub_title", "image", "actions", "cta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        cta: ScrollableTrayWidget.IconLabelCTA
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[ScrollableTrayWidget.IconLabelCTA, _Mapping]] = ...) -> None: ...
    class BrandedTrayHeader(_message.Message):
        __slots__ = ("image", "actions", "cta")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        cta: ScrollableTrayWidget.IconLabelCTA
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[ScrollableTrayWidget.IconLabelCTA, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("horizontal_content_card", "vertical_content_poster", "vertical_large_content_poster", "square_content_poster", "playable_content", "horizontal_content_poster", "countdown_content", "horizontal_medium_content_poster", "image_overlay_vertical_content_poster", "image_overlay_vertical_large_content_poster", "button_stack", "match_card")
        HORIZONTAL_CONTENT_CARD_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_LARGE_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        SQUARE_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        PLAYABLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
        HORIZONTAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        COUNTDOWN_CONTENT_FIELD_NUMBER: _ClassVar[int]
        HORIZONTAL_MEDIUM_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        IMAGE_OVERLAY_VERTICAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        IMAGE_OVERLAY_VERTICAL_LARGE_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        BUTTON_STACK_FIELD_NUMBER: _ClassVar[int]
        MATCH_CARD_FIELD_NUMBER: _ClassVar[int]
        horizontal_content_card: _horizontal_content_card_pb2.HorizontalContentCardWidget
        vertical_content_poster: _vertical_content_poster_pb2.VerticalContentPosterWidget
        vertical_large_content_poster: _vertical_large_content_poster_pb2.VerticalLargeContentPosterWidget
        square_content_poster: _square_content_poster_pb2.SquareContentPosterWidget
        playable_content: _playable_content_pb2.PlayableContentWidget
        horizontal_content_poster: _horizontal_content_poster_pb2.HorizontalContentPosterWidget
        countdown_content: _countdown_content_pb2.CountdownContentWidget
        horizontal_medium_content_poster: _horizontal_medium_content_poster_pb2.HorizontalMediumContentPosterWidget
        image_overlay_vertical_content_poster: _image_overlay_vertical_content_poster_pb2.ImageOverlayVerticalContentPosterWidget
        image_overlay_vertical_large_content_poster: _image_overlay_vertical_large_content_poster_pb2.ImageOverlayVerticalLargeContentPosterWidget
        button_stack: _button_stack_pb2.ButtonStackWidget
        match_card: _match_card_pb2.MatchCardWidget
        def __init__(self, horizontal_content_card: _Optional[_Union[_horizontal_content_card_pb2.HorizontalContentCardWidget, _Mapping]] = ..., vertical_content_poster: _Optional[_Union[_vertical_content_poster_pb2.VerticalContentPosterWidget, _Mapping]] = ..., vertical_large_content_poster: _Optional[_Union[_vertical_large_content_poster_pb2.VerticalLargeContentPosterWidget, _Mapping]] = ..., square_content_poster: _Optional[_Union[_square_content_poster_pb2.SquareContentPosterWidget, _Mapping]] = ..., playable_content: _Optional[_Union[_playable_content_pb2.PlayableContentWidget, _Mapping]] = ..., horizontal_content_poster: _Optional[_Union[_horizontal_content_poster_pb2.HorizontalContentPosterWidget, _Mapping]] = ..., countdown_content: _Optional[_Union[_countdown_content_pb2.CountdownContentWidget, _Mapping]] = ..., horizontal_medium_content_poster: _Optional[_Union[_horizontal_medium_content_poster_pb2.HorizontalMediumContentPosterWidget, _Mapping]] = ..., image_overlay_vertical_content_poster: _Optional[_Union[_image_overlay_vertical_content_poster_pb2.ImageOverlayVerticalContentPosterWidget, _Mapping]] = ..., image_overlay_vertical_large_content_poster: _Optional[_Union[_image_overlay_vertical_large_content_poster_pb2.ImageOverlayVerticalLargeContentPosterWidget, _Mapping]] = ..., button_stack: _Optional[_Union[_button_stack_pb2.ButtonStackWidget, _Mapping]] = ..., match_card: _Optional[_Union[_match_card_pb2.MatchCardWidget, _Mapping]] = ...) -> None: ...
    class IconLabelCTA(_message.Message):
        __slots__ = ("label", "icon_name", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class TrayBackground(_message.Message):
        __slots__ = ("background_image", "background_screen_size_image")
        BACKGROUND_IMAGE_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_SCREEN_SIZE_IMAGE_FIELD_NUMBER: _ClassVar[int]
        background_image: _image_pb2.Image
        background_screen_size_image: _screen_size_image_pb2.ScreenSizeImage
        def __init__(self, background_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., background_screen_size_image: _Optional[_Union[_screen_size_image_pb2.ScreenSizeImage, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ScrollableTrayWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ScrollableTrayWidget.Data, _Mapping]] = ...) -> None: ...
