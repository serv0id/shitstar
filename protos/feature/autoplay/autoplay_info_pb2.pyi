from base import actions_pb2 as _actions_pb2
from feature.content_language_preference import content_language_preference_pb2 as _content_language_preference_pb2
from feature.image import image_pb2 as _image_pb2
from feature.language import language_pb2 as _language_pb2
from feature.player import media_asset_pb2 as _media_asset_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AutoplayInfo(_message.Message):
    __slots__ = ("widget_url", "delay_in_ms", "language_preference_info", "optional_language", "autoplay_widget_url", "media_asset", "cover_image")
    WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    DELAY_IN_MS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_PREFERENCE_INFO_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    AUTOPLAY_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    MEDIA_ASSET_FIELD_NUMBER: _ClassVar[int]
    COVER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    widget_url: str
    delay_in_ms: int
    language_preference_info: _content_language_preference_pb2.ContentLanguagePreference
    optional_language: _containers.RepeatedCompositeFieldContainer[ContentLanguageItem]
    autoplay_widget_url: str
    media_asset: _media_asset_pb2.MediaAsset
    cover_image: _image_pb2.Image
    def __init__(self, widget_url: _Optional[str] = ..., delay_in_ms: _Optional[int] = ..., language_preference_info: _Optional[_Union[_content_language_preference_pb2.ContentLanguagePreference, _Mapping]] = ..., optional_language: _Optional[_Iterable[_Union[ContentLanguageItem, _Mapping]]] = ..., autoplay_widget_url: _Optional[str] = ..., media_asset: _Optional[_Union[_media_asset_pb2.MediaAsset, _Mapping]] = ..., cover_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...

class ContentLanguageItem(_message.Message):
    __slots__ = ("language", "description", "is_default", "is_selected", "actions")
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    language: _language_pb2.Language
    description: str
    is_default: bool
    is_selected: bool
    actions: _actions_pb2.Actions
    def __init__(self, language: _Optional[_Union[_language_pb2.Language, _Mapping]] = ..., description: _Optional[str] = ..., is_default: bool = ..., is_selected: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
