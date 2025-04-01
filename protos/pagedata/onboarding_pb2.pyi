from base import page_data_commons_pb2 as _page_data_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnboardingPageData(_message.Message):
    __slots__ = ("page_data_commons", "hero_backdrop", "page_event_actions", "should_replace_page_url")
    class HeroBackdrop(_message.Message):
        __slots__ = ("backdrop_img", "backdrop_video", "onboarding_video_enabled", "bg_image_list")
        BACKDROP_IMG_FIELD_NUMBER: _ClassVar[int]
        BACKDROP_VIDEO_FIELD_NUMBER: _ClassVar[int]
        ONBOARDING_VIDEO_ENABLED_FIELD_NUMBER: _ClassVar[int]
        BG_IMAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        backdrop_img: _image_pb2.Image
        backdrop_video: _image_pb2.Image
        onboarding_video_enabled: bool
        bg_image_list: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        def __init__(self, backdrop_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., backdrop_video: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., onboarding_video_enabled: bool = ..., bg_image_list: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ...) -> None: ...
    class PageEventActionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _actions_pb2.Actions.Action
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_actions_pb2.Actions.Action, _Mapping]] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    HERO_BACKDROP_FIELD_NUMBER: _ClassVar[int]
    PAGE_EVENT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SHOULD_REPLACE_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    hero_backdrop: OnboardingPageData.HeroBackdrop
    page_event_actions: _containers.MessageMap[str, _actions_pb2.Actions.Action]
    should_replace_page_url: bool
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., hero_backdrop: _Optional[_Union[OnboardingPageData.HeroBackdrop, _Mapping]] = ..., page_event_actions: _Optional[_Mapping[str, _actions_pb2.Actions.Action]] = ..., should_replace_page_url: bool = ...) -> None: ...
