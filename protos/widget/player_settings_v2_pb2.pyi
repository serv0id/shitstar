from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.player import player_settings_type_pb2 as _player_settings_type_pb2
from feature.language import language_pb2 as _language_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from widget import text_list_pb2 as _text_list_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerSettingsWidgetV2(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("option_list_map", "landscape_option_list_groups", "portrait_option_list_groups", "text_list")
        class OptionListMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: PlayerSettingsWidgetV2.PlayerSettingsList
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PlayerSettingsWidgetV2.PlayerSettingsList, _Mapping]] = ...) -> None: ...
        OPTION_LIST_MAP_FIELD_NUMBER: _ClassVar[int]
        LANDSCAPE_OPTION_LIST_GROUPS_FIELD_NUMBER: _ClassVar[int]
        PORTRAIT_OPTION_LIST_GROUPS_FIELD_NUMBER: _ClassVar[int]
        TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
        option_list_map: _containers.MessageMap[str, PlayerSettingsWidgetV2.PlayerSettingsList]
        landscape_option_list_groups: _containers.RepeatedCompositeFieldContainer[PlayerSettingsWidgetV2.PlayerSettingsOptionListGroup]
        portrait_option_list_groups: _containers.RepeatedCompositeFieldContainer[PlayerSettingsWidgetV2.PlayerSettingsOptionListGroup]
        text_list: _text_list_pb2.TextListWidget
        def __init__(self, option_list_map: _Optional[_Mapping[str, PlayerSettingsWidgetV2.PlayerSettingsList]] = ..., landscape_option_list_groups: _Optional[_Iterable[_Union[PlayerSettingsWidgetV2.PlayerSettingsOptionListGroup, _Mapping]]] = ..., portrait_option_list_groups: _Optional[_Iterable[_Union[PlayerSettingsWidgetV2.PlayerSettingsOptionListGroup, _Mapping]]] = ..., text_list: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ...) -> None: ...
    class PlayerSettingsOptionListGroup(_message.Message):
        __slots__ = ("title", "option_list_keys")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        OPTION_LIST_KEYS_FIELD_NUMBER: _ClassVar[int]
        title: str
        option_list_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, title: _Optional[str] = ..., option_list_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class PlayerSettingsVideoQualityList(_message.Message):
        __slots__ = ("title", "type", "video_quality_option")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_QUALITY_OPTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        type: _player_settings_type_pb2.PlayerSettingsType
        video_quality_option: _containers.RepeatedCompositeFieldContainer[PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption]
        def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[_player_settings_type_pb2.PlayerSettingsType, str]] = ..., video_quality_option: _Optional[_Iterable[_Union[PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption, _Mapping]]] = ...) -> None: ...
    class PlayerSettingsAudioLanguageList(_message.Message):
        __slots__ = ("title", "type", "audio_nudge", "audio_filer", "audio_language_action")
        class AudioNudgeEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: PlayerSettingsWidgetV2.SettingsOptionAccessory
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PlayerSettingsWidgetV2.SettingsOptionAccessory, _Mapping]] = ...) -> None: ...
        class AudioLanguageActionEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _actions_pb2.Actions
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_NUDGE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FILER_FIELD_NUMBER: _ClassVar[int]
        AUDIO_LANGUAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        type: _player_settings_type_pb2.PlayerSettingsType
        audio_nudge: _containers.MessageMap[str, PlayerSettingsWidgetV2.SettingsOptionAccessory]
        audio_filer: _containers.RepeatedCompositeFieldContainer[_language_pb2.Language]
        audio_language_action: _containers.MessageMap[str, _actions_pb2.Actions]
        def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[_player_settings_type_pb2.PlayerSettingsType, str]] = ..., audio_nudge: _Optional[_Mapping[str, PlayerSettingsWidgetV2.SettingsOptionAccessory]] = ..., audio_filer: _Optional[_Iterable[_Union[_language_pb2.Language, _Mapping]]] = ..., audio_language_action: _Optional[_Mapping[str, _actions_pb2.Actions]] = ...) -> None: ...
    class PlayerSettingsSubtitleList(_message.Message):
        __slots__ = ("title", "type", "subtitle_filer")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FILER_FIELD_NUMBER: _ClassVar[int]
        title: str
        type: _player_settings_type_pb2.PlayerSettingsType
        subtitle_filer: _containers.RepeatedCompositeFieldContainer[_language_pb2.Language]
        def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[_player_settings_type_pb2.PlayerSettingsType, str]] = ..., subtitle_filer: _Optional[_Iterable[_Union[_language_pb2.Language, _Mapping]]] = ...) -> None: ...
    class PlayerSettingsPlaybackSpeedList(_message.Message):
        __slots__ = ("title", "type", "playback_speed_option")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_SPEED_OPTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        type: _player_settings_type_pb2.PlayerSettingsType
        playback_speed_option: _containers.RepeatedCompositeFieldContainer[PlayerSettingsWidgetV2.PlayerPlaybackSpeedOption]
        def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[_player_settings_type_pb2.PlayerSettingsType, str]] = ..., playback_speed_option: _Optional[_Iterable[_Union[PlayerSettingsWidgetV2.PlayerPlaybackSpeedOption, _Mapping]]] = ...) -> None: ...
    class PlayerSettingsList(_message.Message):
        __slots__ = ("video_quality_list", "audio_language_list", "subtitle_list", "playback_speed_list")
        VIDEO_QUALITY_LIST_FIELD_NUMBER: _ClassVar[int]
        AUDIO_LANGUAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_LIST_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_SPEED_LIST_FIELD_NUMBER: _ClassVar[int]
        video_quality_list: PlayerSettingsWidgetV2.PlayerSettingsVideoQualityList
        audio_language_list: PlayerSettingsWidgetV2.PlayerSettingsAudioLanguageList
        subtitle_list: PlayerSettingsWidgetV2.PlayerSettingsSubtitleList
        playback_speed_list: PlayerSettingsWidgetV2.PlayerSettingsPlaybackSpeedList
        def __init__(self, video_quality_list: _Optional[_Union[PlayerSettingsWidgetV2.PlayerSettingsVideoQualityList, _Mapping]] = ..., audio_language_list: _Optional[_Union[PlayerSettingsWidgetV2.PlayerSettingsAudioLanguageList, _Mapping]] = ..., subtitle_list: _Optional[_Union[PlayerSettingsWidgetV2.PlayerSettingsSubtitleList, _Mapping]] = ..., playback_speed_list: _Optional[_Union[PlayerSettingsWidgetV2.PlayerSettingsPlaybackSpeedList, _Mapping]] = ...) -> None: ...
    class PlayerSettingsVideoQualityOption(_message.Message):
        __slots__ = ("title", "subtitle", "description", "badge_type", "is_selected", "bitrate", "width", "height", "min_height", "max_height", "min_bandwidth", "max_bandwidth", "code", "analytics_index", "analytics_code", "accessory")
        class BadgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption.BadgeType]
            NEED_UPGRADE: _ClassVar[PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption.BadgeType]
        UNKNOWN: PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption.BadgeType
        NEED_UPGRADE: PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption.BadgeType
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BADGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        BITRATE_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        MIN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
        MAX_HEIGHT_FIELD_NUMBER: _ClassVar[int]
        MIN_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
        MAX_BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
        CODE_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_INDEX_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_CODE_FIELD_NUMBER: _ClassVar[int]
        ACCESSORY_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        description: str
        badge_type: PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption.BadgeType
        is_selected: bool
        bitrate: int
        width: int
        height: int
        min_height: int
        max_height: int
        min_bandwidth: int
        max_bandwidth: int
        code: str
        analytics_index: int
        analytics_code: str
        accessory: PlayerSettingsWidgetV2.SettingsOptionAccessory
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., description: _Optional[str] = ..., badge_type: _Optional[_Union[PlayerSettingsWidgetV2.PlayerSettingsVideoQualityOption.BadgeType, str]] = ..., is_selected: bool = ..., bitrate: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., min_height: _Optional[int] = ..., max_height: _Optional[int] = ..., min_bandwidth: _Optional[int] = ..., max_bandwidth: _Optional[int] = ..., code: _Optional[str] = ..., analytics_index: _Optional[int] = ..., analytics_code: _Optional[str] = ..., accessory: _Optional[_Union[PlayerSettingsWidgetV2.SettingsOptionAccessory, _Mapping]] = ...) -> None: ...
    class SettingsOptionAccessory(_message.Message):
        __slots__ = ("tag", "action")
        TAG_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        tag: PlayerSettingsWidgetV2.SettingsOptionAccessoryTag
        action: _actions_pb2.Actions
        def __init__(self, tag: _Optional[_Union[PlayerSettingsWidgetV2.SettingsOptionAccessoryTag, _Mapping]] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class SettingsOptionAccessoryTag(_message.Message):
        __slots__ = ("text", "icon")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon: _image_pb2.Image
        def __init__(self, text: _Optional[str] = ..., icon: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class PlayerPlaybackSpeedOption(_message.Message):
        __slots__ = ("title", "subtitle", "is_selected", "speed")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        SPEED_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        is_selected: bool
        speed: float
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., is_selected: bool = ..., speed: _Optional[float] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerSettingsWidgetV2.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerSettingsWidgetV2.Data, _Mapping]] = ...) -> None: ...
