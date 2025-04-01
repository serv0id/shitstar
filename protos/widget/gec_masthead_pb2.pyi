from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from feature.autoplay import autoplay_info_pb2 as _autoplay_info_pb2
from feature.live import live_info_pb2 as _live_info_pb2
from feature.content_language_preference import content_language_preference_pb2 as _content_language_preference_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from feature.animation import button_animation_pb2 as _button_animation_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from widget import timer_pb2 as _timer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GECMastheadWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("hero_img", "thumbnail", "content_info", "autoplay_info", "animating_vertical_img", "alt")
        HERO_IMG_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        AUTOPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
        ANIMATING_VERTICAL_IMG_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        hero_img: _image_pb2.Image
        thumbnail: _image_pb2.Image
        content_info: GECMastheadWidget.ContentInfo
        autoplay_info: _autoplay_info_pb2.AutoplayInfo
        animating_vertical_img: _image_pb2.Image
        alt: _accessibility_pb2.Accessibility
        def __init__(self, hero_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., thumbnail: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[GECMastheadWidget.ContentInfo, _Mapping]] = ..., autoplay_info: _Optional[_Union[_autoplay_info_pb2.AutoplayInfo, _Mapping]] = ..., animating_vertical_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class ContentInfo(_message.Message):
        __slots__ = ("title", "title_cutout", "description", "tags", "primary_cta", "watchlist_cta", "actions", "core_meta_tags", "enriched_meta_tags", "hero_image_type", "live_info", "language_preference_info", "callout_meta_tags", "timer", "secondary_meta_tags")
        class HeroImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[GECMastheadWidget.ContentInfo.HeroImageType]
            STANDARD: _ClassVar[GECMastheadWidget.ContentInfo.HeroImageType]
            FALLBACK: _ClassVar[GECMastheadWidget.ContentInfo.HeroImageType]
        UNKNOWN: GECMastheadWidget.ContentInfo.HeroImageType
        STANDARD: GECMastheadWidget.ContentInfo.HeroImageType
        FALLBACK: GECMastheadWidget.ContentInfo.HeroImageType
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CORE_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        ENRICHED_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        HERO_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LIVE_INFO_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_PREFERENCE_INFO_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        title: str
        title_cutout: _image_pb2.Image
        description: str
        tags: _containers.RepeatedCompositeFieldContainer[GECMastheadWidget.Tag]
        primary_cta: GECMastheadWidget.IconLabelButton
        watchlist_cta: GECMastheadWidget.WatchlistButton
        actions: _actions_pb2.Actions
        core_meta_tags: _containers.RepeatedCompositeFieldContainer[GECMastheadWidget.Tag]
        enriched_meta_tags: _containers.RepeatedCompositeFieldContainer[GECMastheadWidget.Tag]
        hero_image_type: GECMastheadWidget.ContentInfo.HeroImageType
        live_info: _live_info_pb2.LiveInfo
        language_preference_info: _content_language_preference_pb2.ContentLanguagePreference
        callout_meta_tags: _containers.RepeatedCompositeFieldContainer[GECMastheadWidget.Tag]
        timer: _timer_pb2.TimerWidget
        secondary_meta_tags: _containers.RepeatedCompositeFieldContainer[GECMastheadWidget.Tag]
        def __init__(self, title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[GECMastheadWidget.Tag, _Mapping]]] = ..., primary_cta: _Optional[_Union[GECMastheadWidget.IconLabelButton, _Mapping]] = ..., watchlist_cta: _Optional[_Union[GECMastheadWidget.WatchlistButton, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., core_meta_tags: _Optional[_Iterable[_Union[GECMastheadWidget.Tag, _Mapping]]] = ..., enriched_meta_tags: _Optional[_Iterable[_Union[GECMastheadWidget.Tag, _Mapping]]] = ..., hero_image_type: _Optional[_Union[GECMastheadWidget.ContentInfo.HeroImageType, str]] = ..., live_info: _Optional[_Union[_live_info_pb2.LiveInfo, _Mapping]] = ..., language_preference_info: _Optional[_Union[_content_language_preference_pb2.ContentLanguagePreference, _Mapping]] = ..., callout_meta_tags: _Optional[_Iterable[_Union[GECMastheadWidget.Tag, _Mapping]]] = ..., timer: _Optional[_Union[_timer_pb2.TimerWidget, _Mapping]] = ..., secondary_meta_tags: _Optional[_Iterable[_Union[GECMastheadWidget.Tag, _Mapping]]] = ...) -> None: ...
    class IconLabelButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions", "animation", "alt")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        animation: _button_animation_pb2.ButtonAnimation
        alt: _accessibility_pb2.Accessibility
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., animation: _Optional[_Union[_button_animation_pb2.ButtonAnimation, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class WatchlistButton(_message.Message):
        __slots__ = ("info", "alt", "alt_add", "alt_remove", "actions")
        INFO_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        ALT_ADD_FIELD_NUMBER: _ClassVar[int]
        ALT_REMOVE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        info: _watchlist_info_pb2.WatchlistInfo
        alt: _accessibility_pb2.Accessibility
        alt_add: _accessibility_pb2.Accessibility
        alt_remove: _accessibility_pb2.Accessibility
        actions: _actions_pb2.Actions
        def __init__(self, info: _Optional[_Union[_watchlist_info_pb2.WatchlistInfo, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alt_add: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alt_remove: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("value", "actions", "type", "text_tag", "badge_tag", "image_tag", "callout_tag")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TEXT_TAG_FIELD_NUMBER: _ClassVar[int]
        BADGE_TAG_FIELD_NUMBER: _ClassVar[int]
        IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_TAG_FIELD_NUMBER: _ClassVar[int]
        value: str
        actions: _actions_pb2.Actions
        type: str
        text_tag: GECMastheadWidget.TextTag
        badge_tag: GECMastheadWidget.BadgeTag
        image_tag: GECMastheadWidget.ImageTag
        callout_tag: _callout_tag_pb2.CalloutTag
        def __init__(self, value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., type: _Optional[str] = ..., text_tag: _Optional[_Union[GECMastheadWidget.TextTag, _Mapping]] = ..., badge_tag: _Optional[_Union[GECMastheadWidget.BadgeTag, _Mapping]] = ..., image_tag: _Optional[_Union[GECMastheadWidget.ImageTag, _Mapping]] = ..., callout_tag: _Optional[_Union[_callout_tag_pb2.CalloutTag, _Mapping]] = ...) -> None: ...
    class TextTag(_message.Message):
        __slots__ = ("value", "actions")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        value: str
        actions: _actions_pb2.Actions
        def __init__(self, value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class BadgeTag(_message.Message):
        __slots__ = ("value", "actions")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        value: str
        actions: _actions_pb2.Actions
        def __init__(self, value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class ImageTag(_message.Message):
        __slots__ = ("value", "actions")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        value: _image_pb2.Image
        actions: _actions_pb2.Actions
        def __init__(self, value: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: GECMastheadWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[GECMastheadWidget.Data, _Mapping]] = ...) -> None: ...
