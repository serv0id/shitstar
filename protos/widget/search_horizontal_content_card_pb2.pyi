from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.search import badge_pb2 as _badge_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchHorizontalContentCardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "title", "sub_title", "duration", "playable", "actions", "expanded_content_poster", "badge", "play")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        PLAYABLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        PLAY_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        title: str
        sub_title: str
        duration: str
        playable: bool
        actions: _actions_pb2.Actions
        expanded_content_poster: SearchHorizontalContentCardWidget.ExpandedContentPoster
        badge: _badge_pb2.Badge
        play: _illustration_pb2.Illustration
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., duration: _Optional[str] = ..., playable: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., expanded_content_poster: _Optional[_Union[SearchHorizontalContentCardWidget.ExpandedContentPoster, _Mapping]] = ..., badge: _Optional[_Union[_badge_pb2.Badge, _Mapping]] = ..., play: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
    class ExpandedContentPoster(_message.Message):
        __slots__ = ("image", "content_info")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        content_info: SearchHorizontalContentCardWidget.ContentInfo
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[SearchHorizontalContentCardWidget.ContentInfo, _Mapping]] = ...) -> None: ...
    class ContentInfo(_message.Message):
        __slots__ = ("title", "title_cutout", "description", "tags", "languages", "progress", "primary_cta", "watchlist_cta", "see_more_cta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_CTA_FIELD_NUMBER: _ClassVar[int]
        SEE_MORE_CTA_FIELD_NUMBER: _ClassVar[int]
        title: str
        title_cutout: _image_pb2.Image
        description: str
        tags: _containers.RepeatedCompositeFieldContainer[SearchHorizontalContentCardWidget.Tag]
        languages: _containers.RepeatedCompositeFieldContainer[SearchHorizontalContentCardWidget.Language]
        progress: int
        primary_cta: SearchHorizontalContentCardWidget.IconLabelButton
        watchlist_cta: SearchHorizontalContentCardWidget.WatchlistButton
        see_more_cta: SearchHorizontalContentCardWidget.IconLabelButton
        def __init__(self, title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[SearchHorizontalContentCardWidget.Tag, _Mapping]]] = ..., languages: _Optional[_Iterable[_Union[SearchHorizontalContentCardWidget.Language, _Mapping]]] = ..., progress: _Optional[int] = ..., primary_cta: _Optional[_Union[SearchHorizontalContentCardWidget.IconLabelButton, _Mapping]] = ..., watchlist_cta: _Optional[_Union[SearchHorizontalContentCardWidget.WatchlistButton, _Mapping]] = ..., see_more_cta: _Optional[_Union[SearchHorizontalContentCardWidget.IconLabelButton, _Mapping]] = ...) -> None: ...
    class IconLabelButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class WatchlistButton(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _watchlist_info_pb2.WatchlistInfo
        def __init__(self, info: _Optional[_Union[_watchlist_info_pb2.WatchlistInfo, _Mapping]] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("value", "actions")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        value: str
        actions: _actions_pb2.Actions
        def __init__(self, value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Language(_message.Message):
        __slots__ = ("key", "value", "is_default")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        is_default: bool
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., is_default: bool = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SearchHorizontalContentCardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SearchHorizontalContentCardWidget.Data, _Mapping]] = ...) -> None: ...
