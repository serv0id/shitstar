from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.download import download_info_pb2 as _download_info_pb2
from feature.image import image_pb2 as _image_pb2
from feature.cw import cw_info_pb2 as _cw_info_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from feature.remind_me import remind_me_info_pb2 as _remind_me_info_pb2
from feature.community import community_info_pb2 as _community_info_pb2
from feature.language_selector import language_selector_pb2 as _language_selector_pb2
from widget import spotlight_info_pb2 as _spotlight_info_pb2
from feature.autoplay import autoplay_info_pb2 as _autoplay_info_pb2
from feature.content_language_preference import content_language_preference_pb2 as _content_language_preference_pb2
from feature.language import language_pb2 as _language_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from widget import lottie_banner_pb2 as _lottie_banner_pb2
from widget import content_rating_cta_pb2 as _content_rating_cta_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from widget import timer_pb2 as _timer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroGECWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class HeroGECUiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[HeroGECWidget.HeroGECUiType]
        BROWSE_SHEET: _ClassVar[HeroGECWidget.HeroGECUiType]
        FEED_CARD: _ClassVar[HeroGECWidget.HeroGECUiType]
        ACTION_SHEET: _ClassVar[HeroGECWidget.HeroGECUiType]
    DEFAULT: HeroGECWidget.HeroGECUiType
    BROWSE_SHEET: HeroGECWidget.HeroGECUiType
    FEED_CARD: HeroGECWidget.HeroGECUiType
    ACTION_SHEET: HeroGECWidget.HeroGECUiType
    class Data(_message.Message):
        __slots__ = ("hero_img", "content_info", "cw_info", "trailer", "primary_cta", "secondary_cta", "content_actions_row", "spotlight_info", "autoplay_info", "primary_button", "secondary_button", "animating_vertical_img", "lottie_banner", "hero_gec_ui_type")
        HERO_IMG_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        CW_INFO_FIELD_NUMBER: _ClassVar[int]
        TRAILER_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ACTIONS_ROW_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
        AUTOPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        ANIMATING_VERTICAL_IMG_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_BANNER_FIELD_NUMBER: _ClassVar[int]
        HERO_GEC_UI_TYPE_FIELD_NUMBER: _ClassVar[int]
        hero_img: _image_pb2.Image
        content_info: HeroGECWidget.HeroGECContentInfo
        cw_info: _cw_info_pb2.CwInfo
        trailer: HeroGECWidget.Trailer
        primary_cta: HeroGECWidget.CTAButton
        secondary_cta: HeroGECWidget.CTAButton
        content_actions_row: HeroGECWidget.ContentActionsRow
        spotlight_info: _spotlight_info_pb2.SpotlightInfoWidget
        autoplay_info: _autoplay_info_pb2.AutoplayInfo
        primary_button: HeroGECWidget.ContentCTAButton
        secondary_button: HeroGECWidget.ContentCTAButton
        animating_vertical_img: _image_pb2.Image
        lottie_banner: _lottie_banner_pb2.LottieBannerWidget
        hero_gec_ui_type: HeroGECWidget.HeroGECUiType
        def __init__(self, hero_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[HeroGECWidget.HeroGECContentInfo, _Mapping]] = ..., cw_info: _Optional[_Union[_cw_info_pb2.CwInfo, _Mapping]] = ..., trailer: _Optional[_Union[HeroGECWidget.Trailer, _Mapping]] = ..., primary_cta: _Optional[_Union[HeroGECWidget.CTAButton, _Mapping]] = ..., secondary_cta: _Optional[_Union[HeroGECWidget.CTAButton, _Mapping]] = ..., content_actions_row: _Optional[_Union[HeroGECWidget.ContentActionsRow, _Mapping]] = ..., spotlight_info: _Optional[_Union[_spotlight_info_pb2.SpotlightInfoWidget, _Mapping]] = ..., autoplay_info: _Optional[_Union[_autoplay_info_pb2.AutoplayInfo, _Mapping]] = ..., primary_button: _Optional[_Union[HeroGECWidget.ContentCTAButton, _Mapping]] = ..., secondary_button: _Optional[_Union[HeroGECWidget.ContentCTAButton, _Mapping]] = ..., animating_vertical_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., lottie_banner: _Optional[_Union[_lottie_banner_pb2.LottieBannerWidget, _Mapping]] = ..., hero_gec_ui_type: _Optional[_Union[HeroGECWidget.HeroGECUiType, str]] = ...) -> None: ...
    class HeroGECContentInfo(_message.Message):
        __slots__ = ("title", "title_cutout", "description", "callout_text", "subscript_tags", "superscript_tags", "language_selector", "core_meta_tags", "enriched_meta_tags", "language_preference_info", "starcast", "content_language_selector", "callout_meta_tags", "secondary_meta_tags", "alt", "core_meta_tags_alt", "enriched_meta_tags_alt", "callout_meta_tags_alt", "timer")
        class Tag(_message.Message):
            __slots__ = ("type", "value", "actions", "alt", "text_tag", "badge_tag", "image_tag", "callout_tag")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            ALT_FIELD_NUMBER: _ClassVar[int]
            TEXT_TAG_FIELD_NUMBER: _ClassVar[int]
            BADGE_TAG_FIELD_NUMBER: _ClassVar[int]
            IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
            CALLOUT_TAG_FIELD_NUMBER: _ClassVar[int]
            type: str
            value: str
            actions: _actions_pb2.Actions
            alt: _accessibility_pb2.Accessibility
            text_tag: HeroGECWidget.HeroGECContentInfo.TextTag
            badge_tag: HeroGECWidget.HeroGECContentInfo.BadgeTag
            image_tag: HeroGECWidget.HeroGECContentInfo.ImageTag
            callout_tag: _callout_tag_pb2.CalloutTag
            def __init__(self, type: _Optional[str] = ..., value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., text_tag: _Optional[_Union[HeroGECWidget.HeroGECContentInfo.TextTag, _Mapping]] = ..., badge_tag: _Optional[_Union[HeroGECWidget.HeroGECContentInfo.BadgeTag, _Mapping]] = ..., image_tag: _Optional[_Union[HeroGECWidget.HeroGECContentInfo.ImageTag, _Mapping]] = ..., callout_tag: _Optional[_Union[_callout_tag_pb2.CalloutTag, _Mapping]] = ...) -> None: ...
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
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_TEXT_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPT_TAGS_FIELD_NUMBER: _ClassVar[int]
        SUPERSCRIPT_TAGS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        CORE_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        ENRICHED_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_PREFERENCE_INFO_FIELD_NUMBER: _ClassVar[int]
        STARCAST_FIELD_NUMBER: _ClassVar[int]
        CONTENT_LANGUAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        CORE_META_TAGS_ALT_FIELD_NUMBER: _ClassVar[int]
        ENRICHED_META_TAGS_ALT_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_META_TAGS_ALT_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        title: str
        title_cutout: _image_pb2.Image
        description: str
        callout_text: str
        subscript_tags: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.HeroGECContentInfo.Tag]
        superscript_tags: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.HeroGECContentInfo.Tag]
        language_selector: _language_selector_pb2.LanguageSelector
        core_meta_tags: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.HeroGECContentInfo.Tag]
        enriched_meta_tags: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.HeroGECContentInfo.Tag]
        language_preference_info: _content_language_preference_pb2.ContentLanguagePreference
        starcast: str
        content_language_selector: HeroGECWidget.ContentLanguageSelector
        callout_meta_tags: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.HeroGECContentInfo.Tag]
        secondary_meta_tags: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.HeroGECContentInfo.Tag]
        alt: _accessibility_pb2.Accessibility
        core_meta_tags_alt: _accessibility_pb2.Accessibility
        enriched_meta_tags_alt: _accessibility_pb2.Accessibility
        callout_meta_tags_alt: _accessibility_pb2.Accessibility
        timer: _timer_pb2.TimerWidget
        def __init__(self, title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., callout_text: _Optional[str] = ..., subscript_tags: _Optional[_Iterable[_Union[HeroGECWidget.HeroGECContentInfo.Tag, _Mapping]]] = ..., superscript_tags: _Optional[_Iterable[_Union[HeroGECWidget.HeroGECContentInfo.Tag, _Mapping]]] = ..., language_selector: _Optional[_Union[_language_selector_pb2.LanguageSelector, _Mapping]] = ..., core_meta_tags: _Optional[_Iterable[_Union[HeroGECWidget.HeroGECContentInfo.Tag, _Mapping]]] = ..., enriched_meta_tags: _Optional[_Iterable[_Union[HeroGECWidget.HeroGECContentInfo.Tag, _Mapping]]] = ..., language_preference_info: _Optional[_Union[_content_language_preference_pb2.ContentLanguagePreference, _Mapping]] = ..., starcast: _Optional[str] = ..., content_language_selector: _Optional[_Union[HeroGECWidget.ContentLanguageSelector, _Mapping]] = ..., callout_meta_tags: _Optional[_Iterable[_Union[HeroGECWidget.HeroGECContentInfo.Tag, _Mapping]]] = ..., secondary_meta_tags: _Optional[_Iterable[_Union[HeroGECWidget.HeroGECContentInfo.Tag, _Mapping]]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., core_meta_tags_alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., enriched_meta_tags_alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., callout_meta_tags_alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., timer: _Optional[_Union[_timer_pb2.TimerWidget, _Mapping]] = ...) -> None: ...
    class Trailer(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ContentActionsRow(_message.Message):
        __slots__ = ("content_action_buttons",)
        class ContentActionButton(_message.Message):
            __slots__ = ("icon_label_content_action_button", "watchlist_content_action_button", "download_content_action_button", "community_content_action_button", "content_rating_cta_widget")
            ICON_LABEL_CONTENT_ACTION_BUTTON_FIELD_NUMBER: _ClassVar[int]
            WATCHLIST_CONTENT_ACTION_BUTTON_FIELD_NUMBER: _ClassVar[int]
            DOWNLOAD_CONTENT_ACTION_BUTTON_FIELD_NUMBER: _ClassVar[int]
            COMMUNITY_CONTENT_ACTION_BUTTON_FIELD_NUMBER: _ClassVar[int]
            CONTENT_RATING_CTA_WIDGET_FIELD_NUMBER: _ClassVar[int]
            icon_label_content_action_button: HeroGECWidget.IconLabelContentActionButton
            watchlist_content_action_button: HeroGECWidget.WatchlistContentActionButton
            download_content_action_button: HeroGECWidget.DownloadContentActionButton
            community_content_action_button: HeroGECWidget.CommunityJoinActionButton
            content_rating_cta_widget: _content_rating_cta_pb2.ContentRatingCtaWidget
            def __init__(self, icon_label_content_action_button: _Optional[_Union[HeroGECWidget.IconLabelContentActionButton, _Mapping]] = ..., watchlist_content_action_button: _Optional[_Union[HeroGECWidget.WatchlistContentActionButton, _Mapping]] = ..., download_content_action_button: _Optional[_Union[HeroGECWidget.DownloadContentActionButton, _Mapping]] = ..., community_content_action_button: _Optional[_Union[HeroGECWidget.CommunityJoinActionButton, _Mapping]] = ..., content_rating_cta_widget: _Optional[_Union[_content_rating_cta_pb2.ContentRatingCtaWidget, _Mapping]] = ...) -> None: ...
        CONTENT_ACTION_BUTTONS_FIELD_NUMBER: _ClassVar[int]
        content_action_buttons: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.ContentActionsRow.ContentActionButton]
        def __init__(self, content_action_buttons: _Optional[_Iterable[_Union[HeroGECWidget.ContentActionsRow.ContentActionButton, _Mapping]]] = ...) -> None: ...
    class CTAButton(_message.Message):
        __slots__ = ("label", "sublabel", "actions", "icon_name", "alt")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        SUBLABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        label: str
        sublabel: str
        actions: _actions_pb2.Actions
        icon_name: str
        alt: _accessibility_pb2.Accessibility
        def __init__(self, label: _Optional[str] = ..., sublabel: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon_name: _Optional[str] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class IconLabelContentActionButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions", "alt")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class WatchlistContentActionButton(_message.Message):
        __slots__ = ("info", "actions", "alt")
        INFO_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        info: _watchlist_info_pb2.WatchlistInfo
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        def __init__(self, info: _Optional[_Union[_watchlist_info_pb2.WatchlistInfo, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class CommunityJoinActionButton(_message.Message):
        __slots__ = ("community_info", "is_enabled", "callback_url", "actions", "alt")
        COMMUNITY_INFO_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        CALLBACK_URL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        community_info: _community_info_pb2.CommunityInfo
        is_enabled: bool
        callback_url: str
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        def __init__(self, community_info: _Optional[_Union[_community_info_pb2.CommunityInfo, _Mapping]] = ..., is_enabled: bool = ..., callback_url: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class DownloadContentActionButton(_message.Message):
        __slots__ = ("label", "download_info", "actions", "alt")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_INFO_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        label: str
        download_info: _download_info_pb2.DownloadInfo
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        def __init__(self, label: _Optional[str] = ..., download_info: _Optional[_Union[_download_info_pb2.DownloadInfo, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class ContentLanguageSelector(_message.Message):
        __slots__ = ("languages", "alt")
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        languages: _containers.RepeatedCompositeFieldContainer[HeroGECWidget.ContentLanguageItem]
        alt: _accessibility_pb2.Accessibility
        def __init__(self, languages: _Optional[_Iterable[_Union[HeroGECWidget.ContentLanguageItem, _Mapping]]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
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
    class ContentCTAButton(_message.Message):
        __slots__ = ("cta_button", "remind_me_cta_button")
        CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        REMIND_ME_CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        cta_button: HeroGECWidget.CTAButton
        remind_me_cta_button: HeroGECWidget.RemindMeCTAButton
        def __init__(self, cta_button: _Optional[_Union[HeroGECWidget.CTAButton, _Mapping]] = ..., remind_me_cta_button: _Optional[_Union[HeroGECWidget.RemindMeCTAButton, _Mapping]] = ...) -> None: ...
    class RemindMeCTAButton(_message.Message):
        __slots__ = ("remind_me_info", "alt")
        REMIND_ME_INFO_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        remind_me_info: _remind_me_info_pb2.ReminderInfo
        alt: _accessibility_pb2.Accessibility
        def __init__(self, remind_me_info: _Optional[_Union[_remind_me_info_pb2.ReminderInfo, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HeroGECWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HeroGECWidget.Data, _Mapping]] = ...) -> None: ...
