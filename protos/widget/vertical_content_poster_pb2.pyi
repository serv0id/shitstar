from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.autoplay import autoplay_info_pb2 as _autoplay_info_pb2
from feature.content_language_preference import content_language_preference_pb2 as _content_language_preference_pb2
from feature.image import image_pb2 as _image_pb2
from feature.language import language_pb2 as _language_pb2
from feature.language_selector import language_selector_pb2 as _language_selector_pb2
from feature.remind_me import remind_me_info_pb2 as _remind_me_info_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from widget import spotlight_info_pb2 as _spotlight_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerticalContentPosterWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "actions", "expanded_content_poster", "spotlight_info", "live_badge", "alt", "watchlist_cta", "content_id")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_CTA_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        expanded_content_poster: VerticalContentPosterWidget.ExpandedContentPoster
        spotlight_info: _spotlight_info_pb2.SpotlightInfoWidget
        live_badge: VerticalContentPosterWidget.LiveBadge
        alt: _accessibility_pb2.Accessibility
        watchlist_cta: VerticalContentPosterWidget.WatchlistButton
        content_id: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., expanded_content_poster: _Optional[_Union[VerticalContentPosterWidget.ExpandedContentPoster, _Mapping]] = ..., spotlight_info: _Optional[_Union[_spotlight_info_pb2.SpotlightInfoWidget, _Mapping]] = ..., live_badge: _Optional[_Union[VerticalContentPosterWidget.LiveBadge, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., watchlist_cta: _Optional[_Union[VerticalContentPosterWidget.WatchlistButton, _Mapping]] = ..., content_id: _Optional[str] = ...) -> None: ...
    class ExpandedContentPoster(_message.Message):
        __slots__ = ("image", "content_info", "on_visible_actions")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        ON_VISIBLE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        content_info: VerticalContentPosterWidget.ContentInfo
        on_visible_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[VerticalContentPosterWidget.ContentInfo, _Mapping]] = ..., on_visible_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class ContentInfo(_message.Message):
        __slots__ = ("title", "title_cutout", "description", "tags", "languages", "progress", "primary_cta", "watchlist_cta", "see_more_cta", "autoplay_info", "language_selector", "language_preference_info", "content_language_selector", "primary_button", "secondary_meta_tags", "callout_meta_tags")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_CTA_FIELD_NUMBER: _ClassVar[int]
        SEE_MORE_CTA_FIELD_NUMBER: _ClassVar[int]
        AUTOPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_PREFERENCE_INFO_FIELD_NUMBER: _ClassVar[int]
        CONTENT_LANGUAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        title: str
        title_cutout: _image_pb2.Image
        description: str
        tags: _containers.RepeatedCompositeFieldContainer[VerticalContentPosterWidget.Tag]
        languages: _containers.RepeatedCompositeFieldContainer[VerticalContentPosterWidget.Language]
        progress: int
        primary_cta: VerticalContentPosterWidget.IconLabelButton
        watchlist_cta: VerticalContentPosterWidget.WatchlistButton
        see_more_cta: VerticalContentPosterWidget.IconLabelButton
        autoplay_info: _autoplay_info_pb2.AutoplayInfo
        language_selector: _language_selector_pb2.LanguageSelector
        language_preference_info: _content_language_preference_pb2.ContentLanguagePreference
        content_language_selector: VerticalContentPosterWidget.ContentLanguageSelector
        primary_button: VerticalContentPosterWidget.ContentCTAButton
        secondary_meta_tags: _containers.RepeatedCompositeFieldContainer[VerticalContentPosterWidget.Tag]
        callout_meta_tags: _containers.RepeatedCompositeFieldContainer[VerticalContentPosterWidget.Tag]
        def __init__(self, title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[VerticalContentPosterWidget.Tag, _Mapping]]] = ..., languages: _Optional[_Iterable[_Union[VerticalContentPosterWidget.Language, _Mapping]]] = ..., progress: _Optional[int] = ..., primary_cta: _Optional[_Union[VerticalContentPosterWidget.IconLabelButton, _Mapping]] = ..., watchlist_cta: _Optional[_Union[VerticalContentPosterWidget.WatchlistButton, _Mapping]] = ..., see_more_cta: _Optional[_Union[VerticalContentPosterWidget.IconLabelButton, _Mapping]] = ..., autoplay_info: _Optional[_Union[_autoplay_info_pb2.AutoplayInfo, _Mapping]] = ..., language_selector: _Optional[_Union[_language_selector_pb2.LanguageSelector, _Mapping]] = ..., language_preference_info: _Optional[_Union[_content_language_preference_pb2.ContentLanguagePreference, _Mapping]] = ..., content_language_selector: _Optional[_Union[VerticalContentPosterWidget.ContentLanguageSelector, _Mapping]] = ..., primary_button: _Optional[_Union[VerticalContentPosterWidget.ContentCTAButton, _Mapping]] = ..., secondary_meta_tags: _Optional[_Iterable[_Union[VerticalContentPosterWidget.Tag, _Mapping]]] = ..., callout_meta_tags: _Optional[_Iterable[_Union[VerticalContentPosterWidget.Tag, _Mapping]]] = ...) -> None: ...
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
    class ContentLanguageSelector(_message.Message):
        __slots__ = ("languages",)
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        languages: _containers.RepeatedCompositeFieldContainer[VerticalContentPosterWidget.ContentLanguageItem]
        def __init__(self, languages: _Optional[_Iterable[_Union[VerticalContentPosterWidget.ContentLanguageItem, _Mapping]]] = ...) -> None: ...
    class ContentLanguageItem(_message.Message):
        __slots__ = ("language", "description", "is_default", "is_selected", "actions")
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        language: _language_pb2.Language
        description: str
        is_default: bool
        is_selected: bool
        actions: _actions_pb2.Actions
        def __init__(self, language: _Optional[_Union[_language_pb2.Language, _Mapping]] = ..., description: _Optional[str] = ..., is_default: bool = ..., is_selected: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LiveBadge(_message.Message):
        __slots__ = ("text_image",)
        TEXT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        text_image: _image_pb2.Image
        def __init__(self, text_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class ContentCTAButton(_message.Message):
        __slots__ = ("cta_button", "remind_me_cta_button")
        CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        REMIND_ME_CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        cta_button: VerticalContentPosterWidget.IconLabelButton
        remind_me_cta_button: VerticalContentPosterWidget.RemindMeCTAButton
        def __init__(self, cta_button: _Optional[_Union[VerticalContentPosterWidget.IconLabelButton, _Mapping]] = ..., remind_me_cta_button: _Optional[_Union[VerticalContentPosterWidget.RemindMeCTAButton, _Mapping]] = ...) -> None: ...
    class RemindMeCTAButton(_message.Message):
        __slots__ = ("remind_me_info",)
        REMIND_ME_INFO_FIELD_NUMBER: _ClassVar[int]
        remind_me_info: _remind_me_info_pb2.ReminderInfo
        def __init__(self, remind_me_info: _Optional[_Union[_remind_me_info_pb2.ReminderInfo, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VerticalContentPosterWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VerticalContentPosterWidget.Data, _Mapping]] = ...) -> None: ...
