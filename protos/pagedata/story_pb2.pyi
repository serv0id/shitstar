from base import page_data_commons_pb2 as _page_data_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoryPageData(_message.Message):
    __slots__ = ("page_data_commons", "audio_url", "auto_close_config")
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_URL_FIELD_NUMBER: _ClassVar[int]
    AUTO_CLOSE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    audio_url: str
    auto_close_config: AutoCloseConfig
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., audio_url: _Optional[str] = ..., auto_close_config: _Optional[_Union[AutoCloseConfig, _Mapping]] = ...) -> None: ...

class AutoCloseConfig(_message.Message):
    __slots__ = ("is_auto_close_enabled", "delay_in_ms", "actions")
    IS_AUTO_CLOSE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    DELAY_IN_MS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    is_auto_close_enabled: bool
    delay_in_ms: int
    actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    def __init__(self, is_auto_close_enabled: bool = ..., delay_in_ms: _Optional[int] = ..., actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
