from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.player import player_settings_type_pb2 as _player_settings_type_pb2
from widget import playable_content_pb2 as _playable_content_pb2
from widget import content_rating_cta_pb2 as _content_rating_cta_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerControlMenuWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("items", "landscape_items", "portrait_items")
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        LANDSCAPE_ITEMS_FIELD_NUMBER: _ClassVar[int]
        PORTRAIT_ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[PlayerControlMenuWidget.PlayerControlMenuItem]
        landscape_items: _containers.RepeatedCompositeFieldContainer[PlayerControlMenuWidget.PlayerControlMenuItem]
        portrait_items: _containers.RepeatedCompositeFieldContainer[PlayerControlMenuWidget.PlayerControlMenuItem]
        def __init__(self, items: _Optional[_Iterable[_Union[PlayerControlMenuWidget.PlayerControlMenuItem, _Mapping]]] = ..., landscape_items: _Optional[_Iterable[_Union[PlayerControlMenuWidget.PlayerControlMenuItem, _Mapping]]] = ..., portrait_items: _Optional[_Iterable[_Union[PlayerControlMenuWidget.PlayerControlMenuItem, _Mapping]]] = ...) -> None: ...
    class OpenPlayerSettingsActionItem(_message.Message):
        __slots__ = ("title", "subtitle", "icon", "types", "actions", "alt")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        TYPES_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        icon: str
        types: _containers.RepeatedScalarFieldContainer[_player_settings_type_pb2.PlayerSettingsType]
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., icon: _Optional[str] = ..., types: _Optional[_Iterable[_Union[_player_settings_type_pb2.PlayerSettingsType, str]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class GeneralActionItem(_message.Message):
        __slots__ = ("title", "subtitle", "icon", "type", "actions", "playable_content")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        PLAYABLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        icon: str
        type: str
        actions: _actions_pb2.Actions
        playable_content: _playable_content_pb2.PlayableContentWidget
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., icon: _Optional[str] = ..., type: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., playable_content: _Optional[_Union[_playable_content_pb2.PlayableContentWidget, _Mapping]] = ...) -> None: ...
    class FanModeActionItem(_message.Message):
        __slots__ = ("title", "icon", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        icon: str
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class OpenPlaybackSpeedActionItem(_message.Message):
        __slots__ = ("icon", "title", "subtitle", "overlay_duration_in_seconds")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        OVERLAY_DURATION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
        icon: str
        title: str
        subtitle: str
        overlay_duration_in_seconds: int
        def __init__(self, icon: _Optional[str] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., overlay_duration_in_seconds: _Optional[int] = ...) -> None: ...
    class PlayInThreeSixtyModeActionItem(_message.Message):
        __slots__ = ("icon", "title", "subtitle", "page_title", "page_subtitle", "content_id", "watch_in_vr_headset_enabled", "motion_tracking_enabled", "actions", "motion_tracking_toggle_label", "watch_in_vr_cta_label", "vr_swipe_gesture_label", "error_title", "error_subtitle", "error_retry_cta_label", "brand_icon", "live_label", "live_badge")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        PAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
        PAGE_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        WATCH_IN_VR_HEADSET_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MOTION_TRACKING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        MOTION_TRACKING_TOGGLE_LABEL_FIELD_NUMBER: _ClassVar[int]
        WATCH_IN_VR_CTA_LABEL_FIELD_NUMBER: _ClassVar[int]
        VR_SWIPE_GESTURE_LABEL_FIELD_NUMBER: _ClassVar[int]
        ERROR_TITLE_FIELD_NUMBER: _ClassVar[int]
        ERROR_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        ERROR_RETRY_CTA_LABEL_FIELD_NUMBER: _ClassVar[int]
        BRAND_ICON_FIELD_NUMBER: _ClassVar[int]
        LIVE_LABEL_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        icon: str
        title: str
        subtitle: str
        page_title: str
        page_subtitle: str
        content_id: str
        watch_in_vr_headset_enabled: bool
        motion_tracking_enabled: bool
        actions: _actions_pb2.Actions
        motion_tracking_toggle_label: str
        watch_in_vr_cta_label: str
        vr_swipe_gesture_label: str
        error_title: str
        error_subtitle: str
        error_retry_cta_label: str
        brand_icon: _brand_pb2.Brand
        live_label: str
        live_badge: _illustration_pb2.Illustration
        def __init__(self, icon: _Optional[str] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., page_title: _Optional[str] = ..., page_subtitle: _Optional[str] = ..., content_id: _Optional[str] = ..., watch_in_vr_headset_enabled: bool = ..., motion_tracking_enabled: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., motion_tracking_toggle_label: _Optional[str] = ..., watch_in_vr_cta_label: _Optional[str] = ..., vr_swipe_gesture_label: _Optional[str] = ..., error_title: _Optional[str] = ..., error_subtitle: _Optional[str] = ..., error_retry_cta_label: _Optional[str] = ..., brand_icon: _Optional[_Union[_brand_pb2.Brand, str]] = ..., live_label: _Optional[str] = ..., live_badge: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
    class PlayerControlMenuItem(_message.Message):
        __slots__ = ("open_settings_item", "general_action_item", "fan_mode_action_item", "playback_speed_item", "content_rating_cta_widget", "play_three_sixty_mode_action_item")
        OPEN_SETTINGS_ITEM_FIELD_NUMBER: _ClassVar[int]
        GENERAL_ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
        FAN_MODE_ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_SPEED_ITEM_FIELD_NUMBER: _ClassVar[int]
        CONTENT_RATING_CTA_WIDGET_FIELD_NUMBER: _ClassVar[int]
        PLAY_THREE_SIXTY_MODE_ACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
        open_settings_item: PlayerControlMenuWidget.OpenPlayerSettingsActionItem
        general_action_item: PlayerControlMenuWidget.GeneralActionItem
        fan_mode_action_item: PlayerControlMenuWidget.FanModeActionItem
        playback_speed_item: PlayerControlMenuWidget.OpenPlaybackSpeedActionItem
        content_rating_cta_widget: _content_rating_cta_pb2.ContentRatingCtaWidget
        play_three_sixty_mode_action_item: PlayerControlMenuWidget.PlayInThreeSixtyModeActionItem
        def __init__(self, open_settings_item: _Optional[_Union[PlayerControlMenuWidget.OpenPlayerSettingsActionItem, _Mapping]] = ..., general_action_item: _Optional[_Union[PlayerControlMenuWidget.GeneralActionItem, _Mapping]] = ..., fan_mode_action_item: _Optional[_Union[PlayerControlMenuWidget.FanModeActionItem, _Mapping]] = ..., playback_speed_item: _Optional[_Union[PlayerControlMenuWidget.OpenPlaybackSpeedActionItem, _Mapping]] = ..., content_rating_cta_widget: _Optional[_Union[_content_rating_cta_pb2.ContentRatingCtaWidget, _Mapping]] = ..., play_three_sixty_mode_action_item: _Optional[_Union[PlayerControlMenuWidget.PlayInThreeSixtyModeActionItem, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerControlMenuWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerControlMenuWidget.Data, _Mapping]] = ...) -> None: ...
