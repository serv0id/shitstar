from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.cw import cw_info_pb2 as _cw_info_pb2
from feature.download import download_info_pb2 as _download_info_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from widget import spotlight_info_pb2 as _spotlight_info_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CWCardWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED: _ClassVar[CWCardWidget.ContentType]
        MOVIE: _ClassVar[CWCardWidget.ContentType]
        EPISODE: _ClassVar[CWCardWidget.ContentType]
    UNDEFINED: CWCardWidget.ContentType
    MOVIE: CWCardWidget.ContentType
    EPISODE: CWCardWidget.ContentType
    class ContinueWatchingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[CWCardWidget.ContinueWatchingType]
        CONTINUE: _ClassVar[CWCardWidget.ContinueWatchingType]
        NEW: _ClassVar[CWCardWidget.ContinueWatchingType]
        NEXT: _ClassVar[CWCardWidget.ContinueWatchingType]
    DEFAULT: CWCardWidget.ContinueWatchingType
    CONTINUE: CWCardWidget.ContinueWatchingType
    NEW: CWCardWidget.ContinueWatchingType
    NEXT: CWCardWidget.ContinueWatchingType
    class Data(_message.Message):
        __slots__ = ("image", "actions", "cw_info", "footer", "expanded_content_poster", "spotlight_info", "meta_info", "alt", "play")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CW_INFO_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
        META_INFO_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        PLAY_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        cw_info: _cw_info_pb2.CwInfo
        footer: CWCardWidget.Footer
        expanded_content_poster: CWCardWidget.ExpandedContentPoster
        spotlight_info: _spotlight_info_pb2.SpotlightInfoWidget
        meta_info: CWCardWidget.MetaInfo
        alt: _accessibility_pb2.Accessibility
        play: _illustration_pb2.Illustration
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cw_info: _Optional[_Union[_cw_info_pb2.CwInfo, _Mapping]] = ..., footer: _Optional[_Union[CWCardWidget.Footer, _Mapping]] = ..., expanded_content_poster: _Optional[_Union[CWCardWidget.ExpandedContentPoster, _Mapping]] = ..., spotlight_info: _Optional[_Union[_spotlight_info_pb2.SpotlightInfoWidget, _Mapping]] = ..., meta_info: _Optional[_Union[CWCardWidget.MetaInfo, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., play: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
    class ExpandedContentPoster(_message.Message):
        __slots__ = ("title", "tag", "primary_cta", "remove_cw_cta", "see_more_cta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        REMOVE_CW_CTA_FIELD_NUMBER: _ClassVar[int]
        SEE_MORE_CTA_FIELD_NUMBER: _ClassVar[int]
        title: str
        tag: CWCardWidget.Tag
        primary_cta: CWCardWidget.IconLabelButton
        remove_cw_cta: CWCardWidget.RemoveCWButton
        see_more_cta: CWCardWidget.IconLabelButton
        def __init__(self, title: _Optional[str] = ..., tag: _Optional[_Union[CWCardWidget.Tag, _Mapping]] = ..., primary_cta: _Optional[_Union[CWCardWidget.IconLabelButton, _Mapping]] = ..., remove_cw_cta: _Optional[_Union[CWCardWidget.RemoveCWButton, _Mapping]] = ..., see_more_cta: _Optional[_Union[CWCardWidget.IconLabelButton, _Mapping]] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("title", "tag", "kebab_menu")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        KEBAB_MENU_FIELD_NUMBER: _ClassVar[int]
        title: str
        tag: CWCardWidget.Tag
        kebab_menu: CWCardWidget.KebabMenu
        def __init__(self, title: _Optional[str] = ..., tag: _Optional[_Union[CWCardWidget.Tag, _Mapping]] = ..., kebab_menu: _Optional[_Union[CWCardWidget.KebabMenu, _Mapping]] = ...) -> None: ...
    class KebabMenu(_message.Message):
        __slots__ = ("kebab_menu_title", "items", "alt", "actions")
        class Item(_message.Message):
            __slots__ = ("kebab_menu_option", "download_kebab_menu_option", "cw_remove_from_row_kebab_menu_option")
            KEBAB_MENU_OPTION_FIELD_NUMBER: _ClassVar[int]
            DOWNLOAD_KEBAB_MENU_OPTION_FIELD_NUMBER: _ClassVar[int]
            CW_REMOVE_FROM_ROW_KEBAB_MENU_OPTION_FIELD_NUMBER: _ClassVar[int]
            kebab_menu_option: CWCardWidget.KebabMenuOption
            download_kebab_menu_option: CWCardWidget.DownloadKebabMenuOption
            cw_remove_from_row_kebab_menu_option: CWCardWidget.CWRemovefromRowKebabMenuOption
            def __init__(self, kebab_menu_option: _Optional[_Union[CWCardWidget.KebabMenuOption, _Mapping]] = ..., download_kebab_menu_option: _Optional[_Union[CWCardWidget.DownloadKebabMenuOption, _Mapping]] = ..., cw_remove_from_row_kebab_menu_option: _Optional[_Union[CWCardWidget.CWRemovefromRowKebabMenuOption, _Mapping]] = ...) -> None: ...
        KEBAB_MENU_TITLE_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        kebab_menu_title: str
        items: _containers.RepeatedCompositeFieldContainer[CWCardWidget.KebabMenu.Item]
        alt: _accessibility_pb2.Accessibility
        actions: _actions_pb2.Actions
        def __init__(self, kebab_menu_title: _Optional[str] = ..., items: _Optional[_Iterable[_Union[CWCardWidget.KebabMenu.Item, _Mapping]]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
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
    class CWRemovefromRowKebabMenuOption(_message.Message):
        __slots__ = ("content_id", "icon_name", "label", "actions")
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        content_id: str
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, content_id: _Optional[str] = ..., icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class IconLabelButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class RemoveCWButton(_message.Message):
        __slots__ = ("icon_name", "label", "sublabel", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        SUBLABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        sublabel: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., sublabel: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("text", "is_highlighted")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_HIGHLIGHTED_FIELD_NUMBER: _ClassVar[int]
        text: str
        is_highlighted: bool
        def __init__(self, text: _Optional[str] = ..., is_highlighted: bool = ...) -> None: ...
    class MetaInfo(_message.Message):
        __slots__ = ("content_type", "continue_watching_type", "episode_number", "season_number", "content_key", "release_year", "age_rating", "content_release_year")
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_WATCHING_TYPE_FIELD_NUMBER: _ClassVar[int]
        EPISODE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SEASON_NUMBER_FIELD_NUMBER: _ClassVar[int]
        CONTENT_KEY_FIELD_NUMBER: _ClassVar[int]
        RELEASE_YEAR_FIELD_NUMBER: _ClassVar[int]
        AGE_RATING_FIELD_NUMBER: _ClassVar[int]
        CONTENT_RELEASE_YEAR_FIELD_NUMBER: _ClassVar[int]
        content_type: CWCardWidget.ContentType
        continue_watching_type: CWCardWidget.ContinueWatchingType
        episode_number: int
        season_number: int
        content_key: str
        release_year: int
        age_rating: str
        content_release_year: int
        def __init__(self, content_type: _Optional[_Union[CWCardWidget.ContentType, str]] = ..., continue_watching_type: _Optional[_Union[CWCardWidget.ContinueWatchingType, str]] = ..., episode_number: _Optional[int] = ..., season_number: _Optional[int] = ..., content_key: _Optional[str] = ..., release_year: _Optional[int] = ..., age_rating: _Optional[str] = ..., content_release_year: _Optional[int] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CWCardWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CWCardWidget.Data, _Mapping]] = ...) -> None: ...
