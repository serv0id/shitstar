from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import screen_size_image_pb2 as _screen_size_image_pb2
from feature.ad import badge_pb2 as _badge_pb2
from feature.image import aspect_ratio_pb2 as _aspect_ratio_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppStoryWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class AudioState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[AppStoryWidget.AudioState]
        MUTE: _ClassVar[AppStoryWidget.AudioState]
        UNMUTE: _ClassVar[AppStoryWidget.AudioState]
    UNKNOWN: AppStoryWidget.AudioState
    MUTE: AppStoryWidget.AudioState
    UNMUTE: AppStoryWidget.AudioState
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[AppStoryWidget.Type]
        INTERSTITIAL_AD: _ClassVar[AppStoryWidget.Type]
        CONTENT_STORY: _ClassVar[AppStoryWidget.Type]
    DEFAULT: AppStoryWidget.Type
    INTERSTITIAL_AD: AppStoryWidget.Type
    CONTENT_STORY: AppStoryWidget.Type
    class Data(_message.Message):
        __slots__ = ("video_meta", "story", "story_type")
        VIDEO_META_FIELD_NUMBER: _ClassVar[int]
        STORY_FIELD_NUMBER: _ClassVar[int]
        STORY_TYPE_FIELD_NUMBER: _ClassVar[int]
        video_meta: AppStoryWidget.VideoMeta
        story: _containers.RepeatedCompositeFieldContainer[AppStoryWidget.Story]
        story_type: AppStoryWidget.Type
        def __init__(self, video_meta: _Optional[_Union[AppStoryWidget.VideoMeta, _Mapping]] = ..., story: _Optional[_Iterable[_Union[AppStoryWidget.Story, _Mapping]]] = ..., story_type: _Optional[_Union[AppStoryWidget.Type, str]] = ...) -> None: ...
    class VideoMeta(_message.Message):
        __slots__ = ("url", "duration_sec", "url_medium_size", "on_video_start", "load_timeout_sec", "duration_ms", "disable_audio", "aspect_ratio", "audio_control")
        URL_FIELD_NUMBER: _ClassVar[int]
        DURATION_SEC_FIELD_NUMBER: _ClassVar[int]
        URL_MEDIUM_SIZE_FIELD_NUMBER: _ClassVar[int]
        ON_VIDEO_START_FIELD_NUMBER: _ClassVar[int]
        LOAD_TIMEOUT_SEC_FIELD_NUMBER: _ClassVar[int]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_AUDIO_FIELD_NUMBER: _ClassVar[int]
        ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
        AUDIO_CONTROL_FIELD_NUMBER: _ClassVar[int]
        url: str
        duration_sec: int
        url_medium_size: str
        on_video_start: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        load_timeout_sec: int
        duration_ms: int
        disable_audio: bool
        aspect_ratio: _aspect_ratio_pb2.AspectRatio
        audio_control: AppStoryWidget.AudioControl
        def __init__(self, url: _Optional[str] = ..., duration_sec: _Optional[int] = ..., url_medium_size: _Optional[str] = ..., on_video_start: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., load_timeout_sec: _Optional[int] = ..., duration_ms: _Optional[int] = ..., disable_audio: bool = ..., aspect_ratio: _Optional[_Union[_aspect_ratio_pb2.AspectRatio, _Mapping]] = ..., audio_control: _Optional[_Union[AppStoryWidget.AudioControl, _Mapping]] = ...) -> None: ...
    class Story(_message.Message):
        __slots__ = ("cta", "duration_sec", "start_time", "fallback_image", "fallback_images", "on_story_finish_actions", "badge", "video_placeholder_images", "duration_ms", "start_time_ms", "disable_gestures")
        CTA_FIELD_NUMBER: _ClassVar[int]
        DURATION_SEC_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_IMAGE_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_IMAGES_FIELD_NUMBER: _ClassVar[int]
        ON_STORY_FINISH_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_PLACEHOLDER_IMAGES_FIELD_NUMBER: _ClassVar[int]
        DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        DISABLE_GESTURES_FIELD_NUMBER: _ClassVar[int]
        cta: AppStoryWidget.CTA
        duration_sec: int
        start_time: int
        fallback_image: _image_pb2.Image
        fallback_images: _screen_size_image_pb2.ScreenSizeImage
        on_story_finish_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        badge: AppStoryWidget.Badge
        video_placeholder_images: _screen_size_image_pb2.ScreenSizeImage
        duration_ms: int
        start_time_ms: int
        disable_gestures: bool
        def __init__(self, cta: _Optional[_Union[AppStoryWidget.CTA, _Mapping]] = ..., duration_sec: _Optional[int] = ..., start_time: _Optional[int] = ..., fallback_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., fallback_images: _Optional[_Union[_screen_size_image_pb2.ScreenSizeImage, _Mapping]] = ..., on_story_finish_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., badge: _Optional[_Union[AppStoryWidget.Badge, _Mapping]] = ..., video_placeholder_images: _Optional[_Union[_screen_size_image_pb2.ScreenSizeImage, _Mapping]] = ..., duration_ms: _Optional[int] = ..., start_time_ms: _Optional[int] = ..., disable_gestures: bool = ...) -> None: ...
    class AudioControl(_message.Message):
        __slots__ = ("audio_state", "toggle_button")
        AUDIO_STATE_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        audio_state: AppStoryWidget.AudioState
        toggle_button: AppStoryWidget.Toggle
        def __init__(self, audio_state: _Optional[_Union[AppStoryWidget.AudioState, str]] = ..., toggle_button: _Optional[_Union[AppStoryWidget.Toggle, _Mapping]] = ...) -> None: ...
    class Toggle(_message.Message):
        __slots__ = ("mute", "unmute")
        MUTE_FIELD_NUMBER: _ClassVar[int]
        UNMUTE_FIELD_NUMBER: _ClassVar[int]
        mute: _illustration_pb2.Illustration
        unmute: _illustration_pb2.Illustration
        def __init__(self, mute: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., unmute: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("text", "action")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        text: str
        action: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, text: _Optional[str] = ..., action: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class Badge(_message.Message):
        __slots__ = ("ad_badge",)
        AD_BADGE_FIELD_NUMBER: _ClassVar[int]
        ad_badge: _badge_pb2.AdBadge
        def __init__(self, ad_badge: _Optional[_Union[_badge_pb2.AdBadge, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AppStoryWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AppStoryWidget.Data, _Mapping]] = ...) -> None: ...
