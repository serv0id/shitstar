from feature.image import image_pb2 as _image_pb2
from feature.request import http_request_commons_pb2 as _http_request_commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOURCE_UNSPECIFIED: _ClassVar[PreloadSource]
    SOURCE_NEXT_EPISODE_CTA: _ClassVar[PreloadSource]
    SOURCE_WATCH_NEXT: _ClassVar[PreloadSource]
SOURCE_UNSPECIFIED: PreloadSource
SOURCE_NEXT_EPISODE_CTA: PreloadSource
SOURCE_WATCH_NEXT: PreloadSource

class PreloadFlow(_message.Message):
    __slots__ = ("bff", "bffAndPlayback")
    class ApiCall(_message.Message):
        __slots__ = ("url", "fetch_type", "params", "client_params")
        class FetchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FETCH_PAGE: _ClassVar[PreloadFlow.ApiCall.FetchType]
            FETCH_WIDGET: _ClassVar[PreloadFlow.ApiCall.FetchType]
        FETCH_PAGE: PreloadFlow.ApiCall.FetchType
        FETCH_WIDGET: PreloadFlow.ApiCall.FetchType
        URL_FIELD_NUMBER: _ClassVar[int]
        FETCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        PARAMS_FIELD_NUMBER: _ClassVar[int]
        CLIENT_PARAMS_FIELD_NUMBER: _ClassVar[int]
        url: str
        fetch_type: PreloadFlow.ApiCall.FetchType
        params: _http_request_commons_pb2.HttpRequestCommons
        client_params: PreloadFlow.ClientParamsAdition
        def __init__(self, url: _Optional[str] = ..., fetch_type: _Optional[_Union[PreloadFlow.ApiCall.FetchType, str]] = ..., params: _Optional[_Union[_http_request_commons_pb2.HttpRequestCommons, _Mapping]] = ..., client_params: _Optional[_Union[PreloadFlow.ClientParamsAdition, _Mapping]] = ...) -> None: ...
    class ApiAndPlaybackCall(_message.Message):
        __slots__ = ("bff", "stop_stage")
        class StopStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NONE: _ClassVar[PreloadFlow.ApiAndPlaybackCall.StopStage]
            BFF: _ClassVar[PreloadFlow.ApiAndPlaybackCall.StopStage]
            MANIFEST: _ClassVar[PreloadFlow.ApiAndPlaybackCall.StopStage]
            VIDEO_SEGMENT: _ClassVar[PreloadFlow.ApiAndPlaybackCall.StopStage]
        NONE: PreloadFlow.ApiAndPlaybackCall.StopStage
        BFF: PreloadFlow.ApiAndPlaybackCall.StopStage
        MANIFEST: PreloadFlow.ApiAndPlaybackCall.StopStage
        VIDEO_SEGMENT: PreloadFlow.ApiAndPlaybackCall.StopStage
        BFF_FIELD_NUMBER: _ClassVar[int]
        STOP_STAGE_FIELD_NUMBER: _ClassVar[int]
        bff: PreloadFlow.ApiCall
        stop_stage: PreloadFlow.ApiAndPlaybackCall.StopStage
        def __init__(self, bff: _Optional[_Union[PreloadFlow.ApiCall, _Mapping]] = ..., stop_stage: _Optional[_Union[PreloadFlow.ApiAndPlaybackCall.StopStage, str]] = ...) -> None: ...
    class ClientParamsAdition(_message.Message):
        __slots__ = ("attach_playback_params",)
        ATTACH_PLAYBACK_PARAMS_FIELD_NUMBER: _ClassVar[int]
        attach_playback_params: bool
        def __init__(self, attach_playback_params: bool = ...) -> None: ...
    BFF_FIELD_NUMBER: _ClassVar[int]
    BFFANDPLAYBACK_FIELD_NUMBER: _ClassVar[int]
    bff: PreloadFlow.ApiCall
    bffAndPlayback: PreloadFlow.ApiAndPlaybackCall
    def __init__(self, bff: _Optional[_Union[PreloadFlow.ApiCall, _Mapping]] = ..., bffAndPlayback: _Optional[_Union[PreloadFlow.ApiAndPlaybackCall, _Mapping]] = ...) -> None: ...

class PreloadAction(_message.Message):
    __slots__ = ("flow", "identifier", "source")
    FLOW_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    flow: PreloadFlow
    identifier: str
    source: PreloadSource
    def __init__(self, flow: _Optional[_Union[PreloadFlow, _Mapping]] = ..., identifier: _Optional[str] = ..., source: _Optional[_Union[PreloadSource, str]] = ...) -> None: ...
