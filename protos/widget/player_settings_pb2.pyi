from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.player import player_settings_type_pb2 as _player_settings_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerSettingsWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("option_list_map", "landscape_option_list_groups", "portrait_option_list_groups")
        class OptionListMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: PlayerSettingsWidget.PlayerSettingsOptionList
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PlayerSettingsWidget.PlayerSettingsOptionList, _Mapping]] = ...) -> None: ...
        OPTION_LIST_MAP_FIELD_NUMBER: _ClassVar[int]
        LANDSCAPE_OPTION_LIST_GROUPS_FIELD_NUMBER: _ClassVar[int]
        PORTRAIT_OPTION_LIST_GROUPS_FIELD_NUMBER: _ClassVar[int]
        option_list_map: _containers.MessageMap[str, PlayerSettingsWidget.PlayerSettingsOptionList]
        landscape_option_list_groups: _containers.RepeatedCompositeFieldContainer[PlayerSettingsWidget.PlayerSettingsOptionListGroup]
        portrait_option_list_groups: _containers.RepeatedCompositeFieldContainer[PlayerSettingsWidget.PlayerSettingsOptionListGroup]
        def __init__(self, option_list_map: _Optional[_Mapping[str, PlayerSettingsWidget.PlayerSettingsOptionList]] = ..., landscape_option_list_groups: _Optional[_Iterable[_Union[PlayerSettingsWidget.PlayerSettingsOptionListGroup, _Mapping]]] = ..., portrait_option_list_groups: _Optional[_Iterable[_Union[PlayerSettingsWidget.PlayerSettingsOptionListGroup, _Mapping]]] = ...) -> None: ...
    class PlayerSettingsOptionListGroup(_message.Message):
        __slots__ = ("title", "option_list_keys")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        OPTION_LIST_KEYS_FIELD_NUMBER: _ClassVar[int]
        title: str
        option_list_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, title: _Optional[str] = ..., option_list_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class PlayerSettingsOptionList(_message.Message):
        __slots__ = ("title", "type", "options")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        type: _player_settings_type_pb2.PlayerSettingsType
        options: _containers.RepeatedCompositeFieldContainer[PlayerSettingsWidget.SettingsOption]
        def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[_player_settings_type_pb2.PlayerSettingsType, str]] = ..., options: _Optional[_Iterable[_Union[PlayerSettingsWidget.SettingsOption, _Mapping]]] = ...) -> None: ...
    class SettingsOption(_message.Message):
        __slots__ = ("video_quality_option", "audio_option", "subtitle_option")
        VIDEO_QUALITY_OPTION_FIELD_NUMBER: _ClassVar[int]
        AUDIO_OPTION_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_OPTION_FIELD_NUMBER: _ClassVar[int]
        video_quality_option: PlayerSettingsWidget.PlayerSettingsVideoQualityOption
        audio_option: PlayerSettingsWidget.PlayerSettingsAudioOption
        subtitle_option: PlayerSettingsWidget.PlayerSettingsSubtitleOption
        def __init__(self, video_quality_option: _Optional[_Union[PlayerSettingsWidget.PlayerSettingsVideoQualityOption, _Mapping]] = ..., audio_option: _Optional[_Union[PlayerSettingsWidget.PlayerSettingsAudioOption, _Mapping]] = ..., subtitle_option: _Optional[_Union[PlayerSettingsWidget.PlayerSettingsSubtitleOption, _Mapping]] = ...) -> None: ...
    class PlayerSettingsVideoQualityOption(_message.Message):
        __slots__ = ("title", "subtitle", "description", "badge_type", "is_selected", "bitrate", "width", "height", "min_height", "max_height", "min_bandwidth", "max_bandwidth")
        class BadgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[PlayerSettingsWidget.PlayerSettingsVideoQualityOption.BadgeType]
            NEED_UPGRADE: _ClassVar[PlayerSettingsWidget.PlayerSettingsVideoQualityOption.BadgeType]
        UNKNOWN: PlayerSettingsWidget.PlayerSettingsVideoQualityOption.BadgeType
        NEED_UPGRADE: PlayerSettingsWidget.PlayerSettingsVideoQualityOption.BadgeType
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
        title: str
        subtitle: str
        description: str
        badge_type: PlayerSettingsWidget.PlayerSettingsVideoQualityOption.BadgeType
        is_selected: bool
        bitrate: int
        width: int
        height: int
        min_height: int
        max_height: int
        min_bandwidth: int
        max_bandwidth: int
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., description: _Optional[str] = ..., badge_type: _Optional[_Union[PlayerSettingsWidget.PlayerSettingsVideoQualityOption.BadgeType, str]] = ..., is_selected: bool = ..., bitrate: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., min_height: _Optional[int] = ..., max_height: _Optional[int] = ..., min_bandwidth: _Optional[int] = ..., max_bandwidth: _Optional[int] = ...) -> None: ...
    class PlayerSettingsAudioOption(_message.Message):
        __slots__ = ("title", "is_selected", "iso2code", "iso3code", "name_in_english", "language_tag", "channel_count")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ISO2CODE_FIELD_NUMBER: _ClassVar[int]
        ISO3CODE_FIELD_NUMBER: _ClassVar[int]
        NAME_IN_ENGLISH_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        title: str
        is_selected: bool
        iso2code: str
        iso3code: str
        name_in_english: str
        language_tag: str
        channel_count: int
        def __init__(self, title: _Optional[str] = ..., is_selected: bool = ..., iso2code: _Optional[str] = ..., iso3code: _Optional[str] = ..., name_in_english: _Optional[str] = ..., language_tag: _Optional[str] = ..., channel_count: _Optional[int] = ...) -> None: ...
    class PlayerSettingsSubtitleOption(_message.Message):
        __slots__ = ("title", "is_selected", "iso2code", "iso3code", "name_in_english", "language_tag")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ISO2CODE_FIELD_NUMBER: _ClassVar[int]
        ISO3CODE_FIELD_NUMBER: _ClassVar[int]
        NAME_IN_ENGLISH_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
        title: str
        is_selected: bool
        iso2code: str
        iso3code: str
        name_in_english: str
        language_tag: str
        def __init__(self, title: _Optional[str] = ..., is_selected: bool = ..., iso2code: _Optional[str] = ..., iso3code: _Optional[str] = ..., name_in_english: _Optional[str] = ..., language_tag: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerSettingsWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerSettingsWidget.Data, _Mapping]] = ...) -> None: ...
