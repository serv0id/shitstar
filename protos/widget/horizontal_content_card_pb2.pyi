from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.download import download_info_pb2 as _download_info_pb2
from base import actions_pb2 as _actions_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from widget import spotlight_info_pb2 as _spotlight_info_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from feature.remind_me import remind_me_info_pb2 as _remind_me_info_pb2
from feature.tag import tag_pb2 as _tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HorizontalContentCardWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("duration", "image", "footer", "actions", "expanded_content_poster", "spotlight_info", "live_badge", "alt", "play", "watchlist_button", "content_id")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        PLAY_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_BUTTON_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        duration: str
        image: _image_pb2.Image
        footer: HorizontalContentCardWidget.Footer
        actions: _actions_pb2.Actions
        expanded_content_poster: HorizontalContentCardWidget.ExpandedContentPoster
        spotlight_info: _spotlight_info_pb2.SpotlightInfoWidget
        live_badge: HorizontalContentCardWidget.LiveBadge
        alt: _accessibility_pb2.Accessibility
        play: _illustration_pb2.Illustration
        watchlist_button: HorizontalContentCardWidget.WatchlistButton
        content_id: str
        def __init__(self, duration: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., footer: _Optional[_Union[HorizontalContentCardWidget.Footer, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., expanded_content_poster: _Optional[_Union[HorizontalContentCardWidget.ExpandedContentPoster, _Mapping]] = ..., spotlight_info: _Optional[_Union[_spotlight_info_pb2.SpotlightInfoWidget, _Mapping]] = ..., live_badge: _Optional[_Union[HorizontalContentCardWidget.LiveBadge, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., play: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., watchlist_button: _Optional[_Union[HorizontalContentCardWidget.WatchlistButton, _Mapping]] = ..., content_id: _Optional[str] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("title", "sub_title", "kebab_menu", "tags")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        KEBAB_MENU_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        kebab_menu: HorizontalContentCardWidget.KebabMenu
        tags: _containers.RepeatedCompositeFieldContainer[_tag_pb2.Tag]
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., kebab_menu: _Optional[_Union[HorizontalContentCardWidget.KebabMenu, _Mapping]] = ..., tags: _Optional[_Iterable[_Union[_tag_pb2.Tag, _Mapping]]] = ...) -> None: ...
    class ExpandedContentPoster(_message.Message):
        __slots__ = ("image", "content_info")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        content_info: HorizontalContentCardWidget.ContentInfo
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[HorizontalContentCardWidget.ContentInfo, _Mapping]] = ...) -> None: ...
    class ContentInfo(_message.Message):
        __slots__ = ("title", "title_cutout", "description", "tags", "languages", "progress", "primary_cta", "watchlist_cta", "see_more_cta", "primary_button")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        PROGRESS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_CTA_FIELD_NUMBER: _ClassVar[int]
        SEE_MORE_CTA_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        title: str
        title_cutout: _image_pb2.Image
        description: str
        tags: _containers.RepeatedCompositeFieldContainer[HorizontalContentCardWidget.Tag]
        languages: _containers.RepeatedCompositeFieldContainer[HorizontalContentCardWidget.Language]
        progress: int
        primary_cta: HorizontalContentCardWidget.IconLabelButton
        watchlist_cta: HorizontalContentCardWidget.WatchlistButton
        see_more_cta: HorizontalContentCardWidget.IconLabelButton
        primary_button: HorizontalContentCardWidget.ContentCTAButton
        def __init__(self, title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[HorizontalContentCardWidget.Tag, _Mapping]]] = ..., languages: _Optional[_Iterable[_Union[HorizontalContentCardWidget.Language, _Mapping]]] = ..., progress: _Optional[int] = ..., primary_cta: _Optional[_Union[HorizontalContentCardWidget.IconLabelButton, _Mapping]] = ..., watchlist_cta: _Optional[_Union[HorizontalContentCardWidget.WatchlistButton, _Mapping]] = ..., see_more_cta: _Optional[_Union[HorizontalContentCardWidget.IconLabelButton, _Mapping]] = ..., primary_button: _Optional[_Union[HorizontalContentCardWidget.ContentCTAButton, _Mapping]] = ...) -> None: ...
    class ContentCTAButton(_message.Message):
        __slots__ = ("cta_button", "remind_me_cta_button")
        CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        REMIND_ME_CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        cta_button: HorizontalContentCardWidget.IconLabelButton
        remind_me_cta_button: HorizontalContentCardWidget.RemindMeCTAButton
        def __init__(self, cta_button: _Optional[_Union[HorizontalContentCardWidget.IconLabelButton, _Mapping]] = ..., remind_me_cta_button: _Optional[_Union[HorizontalContentCardWidget.RemindMeCTAButton, _Mapping]] = ...) -> None: ...
    class RemindMeCTAButton(_message.Message):
        __slots__ = ("remind_me_info",)
        REMIND_ME_INFO_FIELD_NUMBER: _ClassVar[int]
        remind_me_info: _remind_me_info_pb2.ReminderInfo
        def __init__(self, remind_me_info: _Optional[_Union[_remind_me_info_pb2.ReminderInfo, _Mapping]] = ...) -> None: ...
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
    class KebabMenu(_message.Message):
        __slots__ = ("kebab_menu_title", "items", "alt")
        class Item(_message.Message):
            __slots__ = ("kebab_menu_option", "download_kebab_menu_option", "watchlist_kebab_menu_option")
            KEBAB_MENU_OPTION_FIELD_NUMBER: _ClassVar[int]
            DOWNLOAD_KEBAB_MENU_OPTION_FIELD_NUMBER: _ClassVar[int]
            WATCHLIST_KEBAB_MENU_OPTION_FIELD_NUMBER: _ClassVar[int]
            kebab_menu_option: HorizontalContentCardWidget.KebabMenuOption
            download_kebab_menu_option: HorizontalContentCardWidget.DownloadKebabMenuOption
            watchlist_kebab_menu_option: HorizontalContentCardWidget.WatchlistKebabMenuOption
            def __init__(self, kebab_menu_option: _Optional[_Union[HorizontalContentCardWidget.KebabMenuOption, _Mapping]] = ..., download_kebab_menu_option: _Optional[_Union[HorizontalContentCardWidget.DownloadKebabMenuOption, _Mapping]] = ..., watchlist_kebab_menu_option: _Optional[_Union[HorizontalContentCardWidget.WatchlistKebabMenuOption, _Mapping]] = ...) -> None: ...
        KEBAB_MENU_TITLE_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        kebab_menu_title: str
        items: _containers.RepeatedCompositeFieldContainer[HorizontalContentCardWidget.KebabMenu.Item]
        alt: _accessibility_pb2.Accessibility
        def __init__(self, kebab_menu_title: _Optional[str] = ..., items: _Optional[_Iterable[_Union[HorizontalContentCardWidget.KebabMenu.Item, _Mapping]]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class KebabMenuOption(_message.Message):
        __slots__ = ("icon_name", "label", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class DownloadKebabMenuOption(_message.Message):
        __slots__ = ("downloadInfo", "download_info_option", "actions")
        DOWNLOADINFO_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_INFO_OPTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        downloadInfo: _download_info_pb2.DownloadInfo
        download_info_option: _download_info_pb2.DownloadInfo
        actions: _actions_pb2.Actions
        def __init__(self, downloadInfo: _Optional[_Union[_download_info_pb2.DownloadInfo, _Mapping]] = ..., download_info_option: _Optional[_Union[_download_info_pb2.DownloadInfo, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class WatchlistKebabMenuOption(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _watchlist_info_pb2.WatchlistInfo
        def __init__(self, info: _Optional[_Union[_watchlist_info_pb2.WatchlistInfo, _Mapping]] = ...) -> None: ...
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
    data: HorizontalContentCardWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HorizontalContentCardWidget.Data, _Mapping]] = ...) -> None: ...
