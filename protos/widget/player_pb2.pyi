from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import player_onboarding_pb2 as _player_onboarding_pb2
from widget import player_control_pb2 as _player_control_pb2
from widget import player_error_pb2 as _player_error_pb2
from feature.videoads import preroll_pb2 as _preroll_pb2
from feature.videoads import midroll_pb2 as _midroll_pb2
from feature.cw import cw_info_pb2 as _cw_info_pb2
from feature.player import media_asset_pb2 as _media_asset_pb2
from feature.player import stream_type_pb2 as _stream_type_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from feature.content_language_preference import content_language_preference_pb2 as _content_language_preference_pb2
from feature.live import live_info_pb2 as _live_info_pb2
from feature.intervention import interventions_pb2 as _interventions_pb2
from feature.intervention import intervention_source_pb2 as _intervention_source_pb2
from feature.intervention import event_interventions_pb2 as _event_interventions_pb2
from feature.player import preload_pb2 as _preload_pb2
from widget import info_pill_pb2 as _info_pill_pb2
from base import orientation_pb2 as _orientation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class AudioSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_SOURCE_MANIFEST: _ClassVar[PlayerWidget.AudioSource]
        AUDIO_SOURCE_BACKEND: _ClassVar[PlayerWidget.AudioSource]
    AUDIO_SOURCE_MANIFEST: PlayerWidget.AudioSource
    AUDIO_SOURCE_BACKEND: PlayerWidget.AudioSource
    class SubWidgetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LIVE: _ClassVar[PlayerWidget.SubWidgetType]
        VOD: _ClassVar[PlayerWidget.SubWidgetType]
    LIVE: PlayerWidget.SubWidgetType
    VOD: PlayerWidget.SubWidgetType
    class TimerSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TIMER_SOURCE_SELF: _ClassVar[PlayerWidget.TimerSource]
        TIMER_SOURCE_EXTERNAL: _ClassVar[PlayerWidget.TimerSource]
        TIMER_SOURCE_PREF_EXTERNAL: _ClassVar[PlayerWidget.TimerSource]
    TIMER_SOURCE_SELF: PlayerWidget.TimerSource
    TIMER_SOURCE_EXTERNAL: PlayerWidget.TimerSource
    TIMER_SOURCE_PREF_EXTERNAL: PlayerWidget.TimerSource
    class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KEY_MOMENT: _ClassVar[PlayerWidget.ContentType]
        SPORT_LIVE: _ClassVar[PlayerWidget.ContentType]
    KEY_MOMENT: PlayerWidget.ContentType
    SPORT_LIVE: PlayerWidget.ContentType
    class Data(_message.Message):
        __slots__ = ("player_config", "milestone_config", "player_onboarding", "player_control", "sub_widgets", "play_finish_actions", "player_retry_widget_url", "player_error_widget", "sleep_state_config", "video_meta", "free_timer", "subs_error_widget", "surround_content_config", "live_stream_ad", "intervention_data", "ads_free_button", "preload_config", "info_pill", "entitlement_error_widget")
        PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
        MILESTONE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ONBOARDING_FIELD_NUMBER: _ClassVar[int]
        PLAYER_CONTROL_FIELD_NUMBER: _ClassVar[int]
        SUB_WIDGETS_FIELD_NUMBER: _ClassVar[int]
        PLAY_FINISH_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_RETRY_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ERROR_WIDGET_FIELD_NUMBER: _ClassVar[int]
        SLEEP_STATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        VIDEO_META_FIELD_NUMBER: _ClassVar[int]
        FREE_TIMER_FIELD_NUMBER: _ClassVar[int]
        SUBS_ERROR_WIDGET_FIELD_NUMBER: _ClassVar[int]
        SURROUND_CONTENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        LIVE_STREAM_AD_FIELD_NUMBER: _ClassVar[int]
        INTERVENTION_DATA_FIELD_NUMBER: _ClassVar[int]
        ADS_FREE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        PRELOAD_CONFIG_FIELD_NUMBER: _ClassVar[int]
        INFO_PILL_FIELD_NUMBER: _ClassVar[int]
        ENTITLEMENT_ERROR_WIDGET_FIELD_NUMBER: _ClassVar[int]
        player_config: PlayerWidget.PlayerConfig
        milestone_config: PlayerWidget.MilestoneConfig
        player_onboarding: _player_onboarding_pb2.PlayerOnboardingWidget
        player_control: _player_control_pb2.PlayerControlWidget
        sub_widgets: PlayerWidget.SubWidgets
        play_finish_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        player_retry_widget_url: str
        player_error_widget: _player_error_pb2.PlayerErrorWidget
        sleep_state_config: PlayerWidget.SleepStateConfig
        video_meta: PlayerWidget.VideoMetaConfig
        free_timer: PlayerWidget.FreeTimer
        subs_error_widget: PlayerWidget.SubscriptionErrorWidget
        surround_content_config: PlayerWidget.SurroundContentConfig
        live_stream_ad: PlayerWidget.LiveStreamAdData
        intervention_data: PlayerWidget.InterventionData
        ads_free_button: PlayerWidget.AdsFreeButton
        preload_config: _preload_pb2.PreloadConfig
        info_pill: _info_pill_pb2.InfoPillWidget
        entitlement_error_widget: PlayerWidget.EntitlementErrorWidget
        def __init__(self, player_config: _Optional[_Union[PlayerWidget.PlayerConfig, _Mapping]] = ..., milestone_config: _Optional[_Union[PlayerWidget.MilestoneConfig, _Mapping]] = ..., player_onboarding: _Optional[_Union[_player_onboarding_pb2.PlayerOnboardingWidget, _Mapping]] = ..., player_control: _Optional[_Union[_player_control_pb2.PlayerControlWidget, _Mapping]] = ..., sub_widgets: _Optional[_Union[PlayerWidget.SubWidgets, _Mapping]] = ..., play_finish_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., player_retry_widget_url: _Optional[str] = ..., player_error_widget: _Optional[_Union[_player_error_pb2.PlayerErrorWidget, _Mapping]] = ..., sleep_state_config: _Optional[_Union[PlayerWidget.SleepStateConfig, _Mapping]] = ..., video_meta: _Optional[_Union[PlayerWidget.VideoMetaConfig, _Mapping]] = ..., free_timer: _Optional[_Union[PlayerWidget.FreeTimer, _Mapping]] = ..., subs_error_widget: _Optional[_Union[PlayerWidget.SubscriptionErrorWidget, _Mapping]] = ..., surround_content_config: _Optional[_Union[PlayerWidget.SurroundContentConfig, _Mapping]] = ..., live_stream_ad: _Optional[_Union[PlayerWidget.LiveStreamAdData, _Mapping]] = ..., intervention_data: _Optional[_Union[PlayerWidget.InterventionData, _Mapping]] = ..., ads_free_button: _Optional[_Union[PlayerWidget.AdsFreeButton, _Mapping]] = ..., preload_config: _Optional[_Union[_preload_pb2.PreloadConfig, _Mapping]] = ..., info_pill: _Optional[_Union[_info_pill_pb2.InfoPillWidget, _Mapping]] = ..., entitlement_error_widget: _Optional[_Union[PlayerWidget.EntitlementErrorWidget, _Mapping]] = ...) -> None: ...
    class InterventionData(_message.Message):
        __slots__ = ("interventions", "sources", "absolute_interventions", "event_interventions")
        INTERVENTIONS_FIELD_NUMBER: _ClassVar[int]
        SOURCES_FIELD_NUMBER: _ClassVar[int]
        ABSOLUTE_INTERVENTIONS_FIELD_NUMBER: _ClassVar[int]
        EVENT_INTERVENTIONS_FIELD_NUMBER: _ClassVar[int]
        interventions: _containers.RepeatedCompositeFieldContainer[_interventions_pb2.Intervention]
        sources: _containers.RepeatedCompositeFieldContainer[_intervention_source_pb2.InterventionSource]
        absolute_interventions: _containers.RepeatedCompositeFieldContainer[_interventions_pb2.Intervention]
        event_interventions: _containers.RepeatedCompositeFieldContainer[_event_interventions_pb2.EventIntervention]
        def __init__(self, interventions: _Optional[_Iterable[_Union[_interventions_pb2.Intervention, _Mapping]]] = ..., sources: _Optional[_Iterable[_Union[_intervention_source_pb2.InterventionSource, _Mapping]]] = ..., absolute_interventions: _Optional[_Iterable[_Union[_interventions_pb2.Intervention, _Mapping]]] = ..., event_interventions: _Optional[_Iterable[_Union[_event_interventions_pb2.EventIntervention, _Mapping]]] = ...) -> None: ...
    class AdsFreeButton(_message.Message):
        __slots__ = ("label", "action")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        label: str
        action: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LiveStreamAdData(_message.Message):
        __slots__ = ("ssai_tag", "ad_server_url", "macro_tags")
        class MacroTagsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        SSAI_TAG_FIELD_NUMBER: _ClassVar[int]
        AD_SERVER_URL_FIELD_NUMBER: _ClassVar[int]
        MACRO_TAGS_FIELD_NUMBER: _ClassVar[int]
        ssai_tag: str
        ad_server_url: str
        macro_tags: _containers.ScalarMap[str, str]
        def __init__(self, ssai_tag: _Optional[str] = ..., ad_server_url: _Optional[str] = ..., macro_tags: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class PlayerConfig(_message.Message):
        __slots__ = ("content_metadata", "media_asset", "media_asset_v2", "cast_image", "high_buffering_rate_config", "background_image", "av1_config", "av1_config_v2")
        CONTENT_METADATA_FIELD_NUMBER: _ClassVar[int]
        MEDIA_ASSET_FIELD_NUMBER: _ClassVar[int]
        MEDIA_ASSET_V2_FIELD_NUMBER: _ClassVar[int]
        CAST_IMAGE_FIELD_NUMBER: _ClassVar[int]
        HIGH_BUFFERING_RATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_IMAGE_FIELD_NUMBER: _ClassVar[int]
        AV1_CONFIG_FIELD_NUMBER: _ClassVar[int]
        AV1_CONFIG_V2_FIELD_NUMBER: _ClassVar[int]
        content_metadata: PlayerWidget.ContentMetadata
        media_asset: PlayerWidget.MediaAsset
        media_asset_v2: _media_asset_pb2.MediaAsset
        cast_image: _image_pb2.Image
        high_buffering_rate_config: PlayerWidget.HighBufferingRateConfig
        background_image: _image_pb2.Image
        av1_config: PlayerWidget.Av1Config
        av1_config_v2: _containers.RepeatedCompositeFieldContainer[PlayerWidget.Av1ConfigV2]
        def __init__(self, content_metadata: _Optional[_Union[PlayerWidget.ContentMetadata, _Mapping]] = ..., media_asset: _Optional[_Union[PlayerWidget.MediaAsset, _Mapping]] = ..., media_asset_v2: _Optional[_Union[_media_asset_pb2.MediaAsset, _Mapping]] = ..., cast_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., high_buffering_rate_config: _Optional[_Union[PlayerWidget.HighBufferingRateConfig, _Mapping]] = ..., background_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., av1_config: _Optional[_Union[PlayerWidget.Av1Config, _Mapping]] = ..., av1_config_v2: _Optional[_Iterable[_Union[PlayerWidget.Av1ConfigV2, _Mapping]]] = ...) -> None: ...
    class ContentMetadata(_message.Message):
        __slots__ = ("live", "bookmark", "content_id", "cw_info", "audio_languages", "original_audio_language", "track_languages", "user_language_preference_id", "language_preference_info", "subtitle_languages", "live_data", "audio_source", "stream_type", "content_start_point_seconds", "audio_language_action", "title_cutout", "identifier")
        class AudioLanguageActionEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: _actions_pb2.Actions
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        LIVE_FIELD_NUMBER: _ClassVar[int]
        BOOKMARK_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        CW_INFO_FIELD_NUMBER: _ClassVar[int]
        AUDIO_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_AUDIO_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        TRACK_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        USER_LANGUAGE_PREFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_PREFERENCE_INFO_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        LIVE_DATA_FIELD_NUMBER: _ClassVar[int]
        AUDIO_SOURCE_FIELD_NUMBER: _ClassVar[int]
        STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_START_POINT_SECONDS_FIELD_NUMBER: _ClassVar[int]
        AUDIO_LANGUAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        live: bool
        bookmark: int
        content_id: str
        cw_info: _cw_info_pb2.CwInfo
        audio_languages: _containers.RepeatedCompositeFieldContainer[PlayerWidget.AudioLanguage]
        original_audio_language: PlayerWidget.AudioLanguage
        track_languages: _containers.RepeatedCompositeFieldContainer[PlayerWidget.TrackLanguage]
        user_language_preference_id: str
        language_preference_info: _content_language_preference_pb2.ContentLanguagePreference
        subtitle_languages: _containers.RepeatedCompositeFieldContainer[PlayerWidget.TrackLanguage]
        live_data: _live_info_pb2.LiveInfo
        audio_source: PlayerWidget.AudioSource
        stream_type: _stream_type_pb2.StreamType
        content_start_point_seconds: int
        audio_language_action: _containers.MessageMap[str, _actions_pb2.Actions]
        title_cutout: _image_pb2.Image
        identifier: str
        def __init__(self, live: bool = ..., bookmark: _Optional[int] = ..., content_id: _Optional[str] = ..., cw_info: _Optional[_Union[_cw_info_pb2.CwInfo, _Mapping]] = ..., audio_languages: _Optional[_Iterable[_Union[PlayerWidget.AudioLanguage, _Mapping]]] = ..., original_audio_language: _Optional[_Union[PlayerWidget.AudioLanguage, _Mapping]] = ..., track_languages: _Optional[_Iterable[_Union[PlayerWidget.TrackLanguage, _Mapping]]] = ..., user_language_preference_id: _Optional[str] = ..., language_preference_info: _Optional[_Union[_content_language_preference_pb2.ContentLanguagePreference, _Mapping]] = ..., subtitle_languages: _Optional[_Iterable[_Union[PlayerWidget.TrackLanguage, _Mapping]]] = ..., live_data: _Optional[_Union[_live_info_pb2.LiveInfo, _Mapping]] = ..., audio_source: _Optional[_Union[PlayerWidget.AudioSource, str]] = ..., stream_type: _Optional[_Union[_stream_type_pb2.StreamType, str]] = ..., content_start_point_seconds: _Optional[int] = ..., audio_language_action: _Optional[_Mapping[str, _actions_pb2.Actions]] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., identifier: _Optional[str] = ...) -> None: ...
    class MediaAsset(_message.Message):
        __slots__ = ("content_urls", "licence_urls", "repeat_mode", "default_audio_language", "default_text_language", "certificate_urls", "primary", "fallback", "session_id")
        CONTENT_URLS_FIELD_NUMBER: _ClassVar[int]
        LICENCE_URLS_FIELD_NUMBER: _ClassVar[int]
        REPEAT_MODE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_AUDIO_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_TEXT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_URLS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        content_urls: _containers.RepeatedScalarFieldContainer[str]
        licence_urls: _containers.RepeatedScalarFieldContainer[str]
        repeat_mode: bool
        default_audio_language: str
        default_text_language: str
        certificate_urls: _containers.RepeatedScalarFieldContainer[str]
        primary: PlayerWidget.PlaybackParams
        fallback: PlayerWidget.PlaybackParams
        session_id: str
        def __init__(self, content_urls: _Optional[_Iterable[str]] = ..., licence_urls: _Optional[_Iterable[str]] = ..., repeat_mode: bool = ..., default_audio_language: _Optional[str] = ..., default_text_language: _Optional[str] = ..., certificate_urls: _Optional[_Iterable[str]] = ..., primary: _Optional[_Union[PlayerWidget.PlaybackParams, _Mapping]] = ..., fallback: _Optional[_Union[PlayerWidget.PlaybackParams, _Mapping]] = ..., session_id: _Optional[str] = ...) -> None: ...
    class PlaybackParams(_message.Message):
        __slots__ = ("content_url", "license_url", "certificate_url", "playback_tags")
        CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        LICENSE_URL_FIELD_NUMBER: _ClassVar[int]
        CERTIFICATE_URL_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_TAGS_FIELD_NUMBER: _ClassVar[int]
        content_url: str
        license_url: str
        certificate_url: str
        playback_tags: str
        def __init__(self, content_url: _Optional[str] = ..., license_url: _Optional[str] = ..., certificate_url: _Optional[str] = ..., playback_tags: _Optional[str] = ...) -> None: ...
    class AudioLanguage(_message.Message):
        __slots__ = ("iso2code", "iso3code", "name", "description", "is_selected", "tag", "accessory_icon", "disable_remembrance")
        ISO2CODE_FIELD_NUMBER: _ClassVar[int]
        ISO3CODE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        ACCESSORY_ICON_FIELD_NUMBER: _ClassVar[int]
        DISABLE_REMEMBRANCE_FIELD_NUMBER: _ClassVar[int]
        iso2code: str
        iso3code: str
        name: str
        description: str
        is_selected: bool
        tag: str
        accessory_icon: _illustration_pb2.Illustration
        disable_remembrance: bool
        def __init__(self, iso2code: _Optional[str] = ..., iso3code: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., is_selected: bool = ..., tag: _Optional[str] = ..., accessory_icon: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., disable_remembrance: bool = ...) -> None: ...
    class TrackLanguage(_message.Message):
        __slots__ = ("iso2code", "iso3code", "name", "description")
        ISO2CODE_FIELD_NUMBER: _ClassVar[int]
        ISO3CODE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        iso2code: str
        iso3code: str
        name: str
        description: str
        def __init__(self, iso2code: _Optional[str] = ..., iso3code: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    class SubWidgets(_message.Message):
        __slots__ = ("type", "preroll", "midroll")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PREROLL_FIELD_NUMBER: _ClassVar[int]
        MIDROLL_FIELD_NUMBER: _ClassVar[int]
        type: PlayerWidget.SubWidgetType
        preroll: _preroll_pb2.Preroll
        midroll: _midroll_pb2.Midroll
        def __init__(self, type: _Optional[_Union[PlayerWidget.SubWidgetType, str]] = ..., preroll: _Optional[_Union[_preroll_pb2.Preroll, _Mapping]] = ..., midroll: _Optional[_Union[_midroll_pb2.Midroll, _Mapping]] = ...) -> None: ...
    class MilestoneConfig(_message.Message):
        __slots__ = ("button_show_time_ms", "autoplay_timer_ms", "auto_skip", "milestone_element", "next_content_element", "next_element")
        BUTTON_SHOW_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        AUTOPLAY_TIMER_MS_FIELD_NUMBER: _ClassVar[int]
        AUTO_SKIP_FIELD_NUMBER: _ClassVar[int]
        MILESTONE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
        NEXT_CONTENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
        NEXT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
        button_show_time_ms: int
        autoplay_timer_ms: int
        auto_skip: bool
        milestone_element: _containers.RepeatedCompositeFieldContainer[PlayerWidget.MilestoneElement]
        next_content_element: PlayerWidget.NextContentElement
        next_element: PlayerWidget.NextElement
        def __init__(self, button_show_time_ms: _Optional[int] = ..., autoplay_timer_ms: _Optional[int] = ..., auto_skip: bool = ..., milestone_element: _Optional[_Iterable[_Union[PlayerWidget.MilestoneElement, _Mapping]]] = ..., next_content_element: _Optional[_Union[PlayerWidget.NextContentElement, _Mapping]] = ..., next_element: _Optional[_Union[PlayerWidget.NextElement, _Mapping]] = ...) -> None: ...
    class MilestoneElement(_message.Message):
        __slots__ = ("element_type", "start_time_ms", "end_time_ms", "threshold_ms", "title", "auto_skip", "auto_skip_timer_ms", "sub_title")
        class ElementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[PlayerWidget.MilestoneElement.ElementType]
            INTRO: _ClassVar[PlayerWidget.MilestoneElement.ElementType]
            RECAP: _ClassVar[PlayerWidget.MilestoneElement.ElementType]
            CREDITS: _ClassVar[PlayerWidget.MilestoneElement.ElementType]
            UPNEXT: _ClassVar[PlayerWidget.MilestoneElement.ElementType]
        UNKNOWN: PlayerWidget.MilestoneElement.ElementType
        INTRO: PlayerWidget.MilestoneElement.ElementType
        RECAP: PlayerWidget.MilestoneElement.ElementType
        CREDITS: PlayerWidget.MilestoneElement.ElementType
        UPNEXT: PlayerWidget.MilestoneElement.ElementType
        ELEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        THRESHOLD_MS_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        AUTO_SKIP_FIELD_NUMBER: _ClassVar[int]
        AUTO_SKIP_TIMER_MS_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        element_type: PlayerWidget.MilestoneElement.ElementType
        start_time_ms: int
        end_time_ms: int
        threshold_ms: int
        title: str
        auto_skip: bool
        auto_skip_timer_ms: int
        sub_title: str
        def __init__(self, element_type: _Optional[_Union[PlayerWidget.MilestoneElement.ElementType, str]] = ..., start_time_ms: _Optional[int] = ..., end_time_ms: _Optional[int] = ..., threshold_ms: _Optional[int] = ..., title: _Optional[str] = ..., auto_skip: bool = ..., auto_skip_timer_ms: _Optional[int] = ..., sub_title: _Optional[str] = ...) -> None: ...
    class NextContentElement(_message.Message):
        __slots__ = ("title", "last_show_time_ms", "action", "icon", "content_id")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        LAST_SHOW_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        title: str
        last_show_time_ms: int
        action: _actions_pb2.Actions
        icon: str
        content_id: str
        def __init__(self, title: _Optional[str] = ..., last_show_time_ms: _Optional[int] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon: _Optional[str] = ..., content_id: _Optional[str] = ...) -> None: ...
    class NextElement(_message.Message):
        __slots__ = ("next_episode_element", "watch_next_element")
        NEXT_EPISODE_ELEMENT_FIELD_NUMBER: _ClassVar[int]
        WATCH_NEXT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
        next_episode_element: PlayerWidget.NextContentElement
        watch_next_element: PlayerWidget.WatchNextElement
        def __init__(self, next_episode_element: _Optional[_Union[PlayerWidget.NextContentElement, _Mapping]] = ..., watch_next_element: _Optional[_Union[PlayerWidget.WatchNextElement, _Mapping]] = ...) -> None: ...
    class WatchNextElement(_message.Message):
        __slots__ = ("start_time_ms", "waiting_time_after_end_ms")
        START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        WAITING_TIME_AFTER_END_MS_FIELD_NUMBER: _ClassVar[int]
        start_time_ms: int
        waiting_time_after_end_ms: int
        def __init__(self, start_time_ms: _Optional[int] = ..., waiting_time_after_end_ms: _Optional[int] = ...) -> None: ...
    class SleepStateConfig(_message.Message):
        __slots__ = ("sleep_threshold_ms", "title_cutout", "subtitle")
        SLEEP_THRESHOLD_MS_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        sleep_threshold_ms: int
        title_cutout: _image_pb2.Image
        subtitle: str
        def __init__(self, sleep_threshold_ms: _Optional[int] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., subtitle: _Optional[str] = ...) -> None: ...
    class VideoMetaConfig(_message.Message):
        __slots__ = ("url",)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str
        def __init__(self, url: _Optional[str] = ...) -> None: ...
    class FreeTimer(_message.Message):
        __slots__ = ("widget_commons", "timer_duration_ms", "timer_label", "timer_desc", "cta", "actions", "timedEvents", "supported_orientation", "timer_source", "min_visibility_threshold_ms", "timer_extension_desc")
        class TimedEventsEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: PlayerWidget.FreeTimerEvents
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[PlayerWidget.FreeTimerEvents, _Mapping]] = ...) -> None: ...
        WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
        TIMER_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        TIMER_LABEL_FIELD_NUMBER: _ClassVar[int]
        TIMER_DESC_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TIMEDEVENTS_FIELD_NUMBER: _ClassVar[int]
        SUPPORTED_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        TIMER_SOURCE_FIELD_NUMBER: _ClassVar[int]
        MIN_VISIBILITY_THRESHOLD_MS_FIELD_NUMBER: _ClassVar[int]
        TIMER_EXTENSION_DESC_FIELD_NUMBER: _ClassVar[int]
        widget_commons: _widget_commons_pb2.WidgetCommons
        timer_duration_ms: int
        timer_label: str
        timer_desc: str
        cta: PlayerWidget.ConfigurableAction
        actions: _actions_pb2.Actions
        timedEvents: _containers.MessageMap[int, PlayerWidget.FreeTimerEvents]
        supported_orientation: _orientation_pb2.Orientation
        timer_source: PlayerWidget.TimerSource
        min_visibility_threshold_ms: int
        timer_extension_desc: str
        def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., timer_duration_ms: _Optional[int] = ..., timer_label: _Optional[str] = ..., timer_desc: _Optional[str] = ..., cta: _Optional[_Union[PlayerWidget.ConfigurableAction, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., timedEvents: _Optional[_Mapping[int, PlayerWidget.FreeTimerEvents]] = ..., supported_orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ..., timer_source: _Optional[_Union[PlayerWidget.TimerSource, str]] = ..., min_visibility_threshold_ms: _Optional[int] = ..., timer_extension_desc: _Optional[str] = ...) -> None: ...
    class FreeTimerEvents(_message.Message):
        __slots__ = ("events",)
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        events: _containers.RepeatedCompositeFieldContainer[PlayerWidget.FreeTimerIntervention]
        def __init__(self, events: _Optional[_Iterable[_Union[PlayerWidget.FreeTimerIntervention, _Mapping]]] = ...) -> None: ...
    class FreeTimerIntervention(_message.Message):
        __slots__ = ("action", "intervention")
        ACTION_FIELD_NUMBER: _ClassVar[int]
        INTERVENTION_FIELD_NUMBER: _ClassVar[int]
        action: _actions_pb2.Actions.Action
        intervention: _interventions_pb2.Intervention
        def __init__(self, action: _Optional[_Union[_actions_pb2.Actions.Action, _Mapping]] = ..., intervention: _Optional[_Union[_interventions_pb2.Intervention, _Mapping]] = ...) -> None: ...
    class ConfigurableAction(_message.Message):
        __slots__ = ("label", "icon", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        icon: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class SubscriptionErrorWidget(_message.Message):
        __slots__ = ("title", "sub_title", "cta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: PlayerWidget.Subtitle
        cta: PlayerWidget.ConfigurableAction
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[_Union[PlayerWidget.Subtitle, _Mapping]] = ..., cta: _Optional[_Union[PlayerWidget.ConfigurableAction, _Mapping]] = ...) -> None: ...
    class EntitlementErrorWidget(_message.Message):
        __slots__ = ("title", "sub_title", "cta", "secondaryCta", "errorInfo", "primaryCta", "widget_commons")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARYCTA_FIELD_NUMBER: _ClassVar[int]
        ERRORINFO_FIELD_NUMBER: _ClassVar[int]
        PRIMARYCTA_FIELD_NUMBER: _ClassVar[int]
        WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: PlayerWidget.Subtitle
        cta: PlayerWidget.ConfigurableAction
        secondaryCta: _player_error_pb2.ErrorHandleButton
        errorInfo: _player_error_pb2.ErrorInfo
        primaryCta: _player_error_pb2.ErrorHandleButton
        widget_commons: _widget_commons_pb2.WidgetCommons
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[_Union[PlayerWidget.Subtitle, _Mapping]] = ..., cta: _Optional[_Union[PlayerWidget.ConfigurableAction, _Mapping]] = ..., secondaryCta: _Optional[_Union[_player_error_pb2.ErrorHandleButton, _Mapping]] = ..., errorInfo: _Optional[_Union[_player_error_pb2.ErrorInfo, _Mapping]] = ..., primaryCta: _Optional[_Union[_player_error_pb2.ErrorHandleButton, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ...) -> None: ...
    class Subtitle(_message.Message):
        __slots__ = ("text", "placeholders")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDERS_FIELD_NUMBER: _ClassVar[int]
        text: str
        placeholders: _containers.RepeatedCompositeFieldContainer[PlayerWidget.Placeholder]
        def __init__(self, text: _Optional[str] = ..., placeholders: _Optional[_Iterable[_Union[PlayerWidget.Placeholder, _Mapping]]] = ...) -> None: ...
    class Placeholder(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SurroundContentConfig(_message.Message):
        __slots__ = ("content_type", "underlying_content_url", "next_surround_content_element", "cta")
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        UNDERLYING_CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        NEXT_SURROUND_CONTENT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        content_type: PlayerWidget.ContentType
        underlying_content_url: str
        next_surround_content_element: PlayerWidget.NextContentElement
        cta: PlayerWidget.CTA
        def __init__(self, content_type: _Optional[_Union[PlayerWidget.ContentType, str]] = ..., underlying_content_url: _Optional[str] = ..., next_surround_content_element: _Optional[_Union[PlayerWidget.NextContentElement, _Mapping]] = ..., cta: _Optional[_Union[PlayerWidget.CTA, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("title", "icon", "action", "cta_type")
        class CTAType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[PlayerWidget.CTA.CTAType]
            GO_LIVE: _ClassVar[PlayerWidget.CTA.CTAType]
            GO_BACK: _ClassVar[PlayerWidget.CTA.CTAType]
            GO_DEFAULT: _ClassVar[PlayerWidget.CTA.CTAType]
        UNKNOWN: PlayerWidget.CTA.CTAType
        GO_LIVE: PlayerWidget.CTA.CTAType
        GO_BACK: PlayerWidget.CTA.CTAType
        GO_DEFAULT: PlayerWidget.CTA.CTAType
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        CTA_TYPE_FIELD_NUMBER: _ClassVar[int]
        title: str
        icon: str
        action: _actions_pb2.Actions
        cta_type: PlayerWidget.CTA.CTAType
        def __init__(self, title: _Optional[str] = ..., icon: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta_type: _Optional[_Union[PlayerWidget.CTA.CTAType, str]] = ...) -> None: ...
    class HighBufferingRateConfig(_message.Message):
        __slots__ = ("buffer_threshold_seconds", "buffer_window_seconds")
        BUFFER_THRESHOLD_SECONDS_FIELD_NUMBER: _ClassVar[int]
        BUFFER_WINDOW_SECONDS_FIELD_NUMBER: _ClassVar[int]
        buffer_threshold_seconds: int
        buffer_window_seconds: int
        def __init__(self, buffer_threshold_seconds: _Optional[int] = ..., buffer_window_seconds: _Optional[int] = ...) -> None: ...
    class Av1Config(_message.Message):
        __slots__ = ("av1_decoder", "hsdav1d_thread_count_percentage")
        AV1_DECODER_FIELD_NUMBER: _ClassVar[int]
        HSDAV1D_THREAD_COUNT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        av1_decoder: str
        hsdav1d_thread_count_percentage: int
        def __init__(self, av1_decoder: _Optional[str] = ..., hsdav1d_thread_count_percentage: _Optional[int] = ...) -> None: ...
    class Av1ConfigV2(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerWidget.Data, _Mapping]] = ...) -> None: ...
