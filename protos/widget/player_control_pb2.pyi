from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import player_control_menu_pb2 as _player_control_menu_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.player import heatmap_pb2 as _heatmap_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerControlWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("content_name", "live_info", "player_seekbar_heading", "player_control_menu", "live_position_tag", "live_logo", "heatmap", "cast_button", "player_top_control_items")
        CONTENT_NAME_FIELD_NUMBER: _ClassVar[int]
        LIVE_INFO_FIELD_NUMBER: _ClassVar[int]
        PLAYER_SEEKBAR_HEADING_FIELD_NUMBER: _ClassVar[int]
        PLAYER_CONTROL_MENU_FIELD_NUMBER: _ClassVar[int]
        LIVE_POSITION_TAG_FIELD_NUMBER: _ClassVar[int]
        LIVE_LOGO_FIELD_NUMBER: _ClassVar[int]
        HEATMAP_FIELD_NUMBER: _ClassVar[int]
        CAST_BUTTON_FIELD_NUMBER: _ClassVar[int]
        PLAYER_TOP_CONTROL_ITEMS_FIELD_NUMBER: _ClassVar[int]
        content_name: PlayerControlWidget.ContentName
        live_info: PlayerControlWidget.LiveInfo
        player_seekbar_heading: PlayerControlWidget.ContentName
        player_control_menu: _player_control_menu_pb2.PlayerControlMenuWidget
        live_position_tag: str
        live_logo: _brand_pb2.Brand
        heatmap: _heatmap_pb2.Heatmap
        cast_button: _button_pb2.Button
        player_top_control_items: _containers.RepeatedCompositeFieldContainer[PlayerControlWidget.PlayerTopControlItems]
        def __init__(self, content_name: _Optional[_Union[PlayerControlWidget.ContentName, _Mapping]] = ..., live_info: _Optional[_Union[PlayerControlWidget.LiveInfo, _Mapping]] = ..., player_seekbar_heading: _Optional[_Union[PlayerControlWidget.ContentName, _Mapping]] = ..., player_control_menu: _Optional[_Union[_player_control_menu_pb2.PlayerControlMenuWidget, _Mapping]] = ..., live_position_tag: _Optional[str] = ..., live_logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., heatmap: _Optional[_Union[_heatmap_pb2.Heatmap, _Mapping]] = ..., cast_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., player_top_control_items: _Optional[_Iterable[_Union[PlayerControlWidget.PlayerTopControlItems, _Mapping]]] = ...) -> None: ...
    class PlayerTopControlItems(_message.Message):
        __slots__ = ("vr360",)
        VR360_FIELD_NUMBER: _ClassVar[int]
        vr360: PlayerControlWidget.ThreeSixtyControlItem
        def __init__(self, vr360: _Optional[_Union[PlayerControlWidget.ThreeSixtyControlItem, _Mapping]] = ...) -> None: ...
    class ThreeSixtyControlItem(_message.Message):
        __slots__ = ("icon", "actions", "page_metadata")
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        PAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
        icon: str
        actions: _actions_pb2.Actions
        page_metadata: PlayerControlWidget.ThreeSixtyPageMetadata
        def __init__(self, icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., page_metadata: _Optional[_Union[PlayerControlWidget.ThreeSixtyPageMetadata, _Mapping]] = ...) -> None: ...
    class ThreeSixtyPageMetadata(_message.Message):
        __slots__ = ("page_title", "page_subtitle", "content_id", "motion_tracking_toggle_label", "watch_in_vr_cta_label", "vr_swipe_gesture_label", "live_label", "error_title", "error_subtitle", "error_retry_cta_label", "watch_in_vr_headset_enabled", "motion_tracking_enabled", "brand_icon", "live_badge", "dismiss_action")
        PAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
        PAGE_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        MOTION_TRACKING_TOGGLE_LABEL_FIELD_NUMBER: _ClassVar[int]
        WATCH_IN_VR_CTA_LABEL_FIELD_NUMBER: _ClassVar[int]
        VR_SWIPE_GESTURE_LABEL_FIELD_NUMBER: _ClassVar[int]
        LIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
        ERROR_TITLE_FIELD_NUMBER: _ClassVar[int]
        ERROR_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        ERROR_RETRY_CTA_LABEL_FIELD_NUMBER: _ClassVar[int]
        WATCH_IN_VR_HEADSET_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MOTION_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        BRAND_ICON_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        DISMISS_ACTION_FIELD_NUMBER: _ClassVar[int]
        page_title: str
        page_subtitle: str
        content_id: str
        motion_tracking_toggle_label: str
        watch_in_vr_cta_label: str
        vr_swipe_gesture_label: str
        live_label: str
        error_title: str
        error_subtitle: str
        error_retry_cta_label: str
        watch_in_vr_headset_enabled: bool
        motion_tracking_enabled: bool
        brand_icon: _brand_pb2.Brand
        live_badge: _illustration_pb2.Illustration
        dismiss_action: _actions_pb2.Actions
        def __init__(self, page_title: _Optional[str] = ..., page_subtitle: _Optional[str] = ..., content_id: _Optional[str] = ..., motion_tracking_toggle_label: _Optional[str] = ..., watch_in_vr_cta_label: _Optional[str] = ..., vr_swipe_gesture_label: _Optional[str] = ..., live_label: _Optional[str] = ..., error_title: _Optional[str] = ..., error_subtitle: _Optional[str] = ..., error_retry_cta_label: _Optional[str] = ..., watch_in_vr_headset_enabled: bool = ..., motion_tracking_enabled: bool = ..., brand_icon: _Optional[_Union[_brand_pb2.Brand, str]] = ..., live_badge: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., dismiss_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class ContentName(_message.Message):
        __slots__ = ("title", "subtitle", "season_episode", "alt")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        SEASON_EPISODE_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        season_episode: str
        alt: _accessibility_pb2.Accessibility
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., season_episode: _Optional[str] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class LiveInfo(_message.Message):
        __slots__ = ("concurrency",)
        CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
        concurrency: str
        def __init__(self, concurrency: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerControlWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerControlWidget.Data, _Mapping]] = ...) -> None: ...
