from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SquareContentPosterWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "actions", "expanded_content_poster", "live_badge", "content_id")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        expanded_content_poster: SquareContentPosterWidget.ExpandedContentPoster
        live_badge: SquareContentPosterWidget.LiveBadge
        content_id: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., expanded_content_poster: _Optional[_Union[SquareContentPosterWidget.ExpandedContentPoster, _Mapping]] = ..., live_badge: _Optional[_Union[SquareContentPosterWidget.LiveBadge, _Mapping]] = ..., content_id: _Optional[str] = ...) -> None: ...
    class ExpandedContentPoster(_message.Message):
        __slots__ = ("image", "content_info")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        content_info: SquareContentPosterWidget.ContentInfo
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[SquareContentPosterWidget.ContentInfo, _Mapping]] = ...) -> None: ...
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
        tags: _containers.RepeatedCompositeFieldContainer[SquareContentPosterWidget.Tag]
        languages: _containers.RepeatedCompositeFieldContainer[SquareContentPosterWidget.Language]
        progress: int
        primary_cta: SquareContentPosterWidget.IconLabelButton
        watchlist_cta: SquareContentPosterWidget.IconLabelButton
        see_more_cta: SquareContentPosterWidget.IconLabelButton
        def __init__(self, title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[SquareContentPosterWidget.Tag, _Mapping]]] = ..., languages: _Optional[_Iterable[_Union[SquareContentPosterWidget.Language, _Mapping]]] = ..., progress: _Optional[int] = ..., primary_cta: _Optional[_Union[SquareContentPosterWidget.IconLabelButton, _Mapping]] = ..., watchlist_cta: _Optional[_Union[SquareContentPosterWidget.IconLabelButton, _Mapping]] = ..., see_more_cta: _Optional[_Union[SquareContentPosterWidget.IconLabelButton, _Mapping]] = ...) -> None: ...
    class IconLabelButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
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
    class LiveBadge(_message.Message):
        __slots__ = ("text_image",)
        TEXT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        text_image: _image_pb2.Image
        def __init__(self, text_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SquareContentPosterWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SquareContentPosterWidget.Data, _Mapping]] = ...) -> None: ...
