from feature.player import preload_pb2 as _preload_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchConfig(_message.Message):
    __slots__ = ("picture_in_picture_enabled", "starting_lag_artifact_enabled", "live_logo_enabled", "simulcast_start_point_enabled", "fan_mode_enabled", "player_gesture_control_enabled", "preload_config", "in_app_pip_enabled", "watch_page_animation_ios", "sports_whitelist_cards", "retry_pc_delay_player_enabled", "automatic_speed_test_enabled", "mux_integration_enabled", "mweb_watch_page_enabled", "maxview_improvement_enabled", "bottom_shoulder_loaded_after_playback", "preload_certificate_enabled", "network_nudge_config", "player_control_ui_type", "parallel_loading_enabled", "dns_prefetch_enabled", "show_wn_orientation_transition", "webos_watch_time_fix")
    class PlayerControlUiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAYER_CONTROL_UI_DEFAULT: _ClassVar[WatchConfig.PlayerControlUiType]
        PLAYER_CONTROL_UI_GEAR_ICON: _ClassVar[WatchConfig.PlayerControlUiType]
        PLAYER_CONTROL_UI_WITH_CONTENT_RATING: _ClassVar[WatchConfig.PlayerControlUiType]
        PLAYER_CONTROL_UI_OVERLAY_TAB: _ClassVar[WatchConfig.PlayerControlUiType]
        PLAYER_CONTROL_UI_PARTIAL_OVERLAY: _ClassVar[WatchConfig.PlayerControlUiType]
    PLAYER_CONTROL_UI_DEFAULT: WatchConfig.PlayerControlUiType
    PLAYER_CONTROL_UI_GEAR_ICON: WatchConfig.PlayerControlUiType
    PLAYER_CONTROL_UI_WITH_CONTENT_RATING: WatchConfig.PlayerControlUiType
    PLAYER_CONTROL_UI_OVERLAY_TAB: WatchConfig.PlayerControlUiType
    PLAYER_CONTROL_UI_PARTIAL_OVERLAY: WatchConfig.PlayerControlUiType
    class NetworkNudgeConfig(_message.Message):
        __slots__ = ("max_count_in_cycle", "days_count_cycle", "buffer_time_seconds", "max_count_per_day", "max_count_total")
        MAX_COUNT_IN_CYCLE_FIELD_NUMBER: _ClassVar[int]
        DAYS_COUNT_CYCLE_FIELD_NUMBER: _ClassVar[int]
        BUFFER_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
        MAX_COUNT_PER_DAY_FIELD_NUMBER: _ClassVar[int]
        MAX_COUNT_TOTAL_FIELD_NUMBER: _ClassVar[int]
        max_count_in_cycle: int
        days_count_cycle: int
        buffer_time_seconds: int
        max_count_per_day: int
        max_count_total: int
        def __init__(self, max_count_in_cycle: _Optional[int] = ..., days_count_cycle: _Optional[int] = ..., buffer_time_seconds: _Optional[int] = ..., max_count_per_day: _Optional[int] = ..., max_count_total: _Optional[int] = ...) -> None: ...
    PICTURE_IN_PICTURE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    STARTING_LAG_ARTIFACT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LIVE_LOGO_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SIMULCAST_START_POINT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    FAN_MODE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PLAYER_GESTURE_CONTROL_ENABLED_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IN_APP_PIP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    WATCH_PAGE_ANIMATION_IOS_FIELD_NUMBER: _ClassVar[int]
    SPORTS_WHITELIST_CARDS_FIELD_NUMBER: _ClassVar[int]
    RETRY_PC_DELAY_PLAYER_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTOMATIC_SPEED_TEST_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MUX_INTEGRATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MWEB_WATCH_PAGE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    MAXVIEW_IMPROVEMENT_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_SHOULDER_LOADED_AFTER_PLAYBACK_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_CERTIFICATE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    NETWORK_NUDGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CONTROL_UI_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARALLEL_LOADING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DNS_PREFETCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SHOW_WN_ORIENTATION_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    WEBOS_WATCH_TIME_FIX_FIELD_NUMBER: _ClassVar[int]
    picture_in_picture_enabled: bool
    starting_lag_artifact_enabled: bool
    live_logo_enabled: bool
    simulcast_start_point_enabled: bool
    fan_mode_enabled: bool
    player_gesture_control_enabled: bool
    preload_config: _preload_pb2.PreloadConfig
    in_app_pip_enabled: bool
    watch_page_animation_ios: bool
    sports_whitelist_cards: _containers.RepeatedScalarFieldContainer[str]
    retry_pc_delay_player_enabled: bool
    automatic_speed_test_enabled: bool
    mux_integration_enabled: bool
    mweb_watch_page_enabled: bool
    maxview_improvement_enabled: bool
    bottom_shoulder_loaded_after_playback: bool
    preload_certificate_enabled: bool
    network_nudge_config: WatchConfig.NetworkNudgeConfig
    player_control_ui_type: WatchConfig.PlayerControlUiType
    parallel_loading_enabled: bool
    dns_prefetch_enabled: bool
    show_wn_orientation_transition: bool
    webos_watch_time_fix: bool
    def __init__(self, picture_in_picture_enabled: bool = ..., starting_lag_artifact_enabled: bool = ..., live_logo_enabled: bool = ..., simulcast_start_point_enabled: bool = ..., fan_mode_enabled: bool = ..., player_gesture_control_enabled: bool = ..., preload_config: _Optional[_Union[_preload_pb2.PreloadConfig, _Mapping]] = ..., in_app_pip_enabled: bool = ..., watch_page_animation_ios: bool = ..., sports_whitelist_cards: _Optional[_Iterable[str]] = ..., retry_pc_delay_player_enabled: bool = ..., automatic_speed_test_enabled: bool = ..., mux_integration_enabled: bool = ..., mweb_watch_page_enabled: bool = ..., maxview_improvement_enabled: bool = ..., bottom_shoulder_loaded_after_playback: bool = ..., preload_certificate_enabled: bool = ..., network_nudge_config: _Optional[_Union[WatchConfig.NetworkNudgeConfig, _Mapping]] = ..., player_control_ui_type: _Optional[_Union[WatchConfig.PlayerControlUiType, str]] = ..., parallel_loading_enabled: bool = ..., dns_prefetch_enabled: bool = ..., show_wn_orientation_transition: bool = ..., webos_watch_time_fix: bool = ...) -> None: ...
