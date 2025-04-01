from feature.request import http_request_commons_pb2 as _http_request_commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DataBindMechanism(_message.Message):
    __slots__ = ("centralStore",)
    class NameSpace(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[DataBindMechanism.NameSpace]
        CRICKET_SCORE_CARD: _ClassVar[DataBindMechanism.NameSpace]
        TV_CHANNEL: _ClassVar[DataBindMechanism.NameSpace]
        LOGIN_WITH_QR: _ClassVar[DataBindMechanism.NameSpace]
        FENCE_AD: _ClassVar[DataBindMechanism.NameSpace]
    UNKNOWN: DataBindMechanism.NameSpace
    CRICKET_SCORE_CARD: DataBindMechanism.NameSpace
    TV_CHANNEL: DataBindMechanism.NameSpace
    LOGIN_WITH_QR: DataBindMechanism.NameSpace
    FENCE_AD: DataBindMechanism.NameSpace
    class SubscribeToCentralStore(_message.Message):
        __slots__ = ("url", "namespace", "polling_frequency_millisec", "max_retry_count", "http_request_commons", "poll_config", "delay_ms", "initial_poll_config")
        URL_FIELD_NUMBER: _ClassVar[int]
        NAMESPACE_FIELD_NUMBER: _ClassVar[int]
        POLLING_FREQUENCY_MILLISEC_FIELD_NUMBER: _ClassVar[int]
        MAX_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
        HTTP_REQUEST_COMMONS_FIELD_NUMBER: _ClassVar[int]
        POLL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        DELAY_MS_FIELD_NUMBER: _ClassVar[int]
        INITIAL_POLL_CONFIG_FIELD_NUMBER: _ClassVar[int]
        url: str
        namespace: DataBindMechanism.NameSpace
        polling_frequency_millisec: int
        max_retry_count: int
        http_request_commons: _http_request_commons_pb2.HttpRequestCommons
        poll_config: DataBindMechanism.PollConfiguration
        delay_ms: int
        initial_poll_config: DataBindMechanism.PollConfiguration
        def __init__(self, url: _Optional[str] = ..., namespace: _Optional[_Union[DataBindMechanism.NameSpace, str]] = ..., polling_frequency_millisec: _Optional[int] = ..., max_retry_count: _Optional[int] = ..., http_request_commons: _Optional[_Union[_http_request_commons_pb2.HttpRequestCommons, _Mapping]] = ..., poll_config: _Optional[_Union[DataBindMechanism.PollConfiguration, _Mapping]] = ..., delay_ms: _Optional[int] = ..., initial_poll_config: _Optional[_Union[DataBindMechanism.PollConfiguration, _Mapping]] = ...) -> None: ...
    class PollConfiguration(_message.Message):
        __slots__ = ("fixed_interval", "jittered_interval")
        FIXED_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        JITTERED_INTERVAL_FIELD_NUMBER: _ClassVar[int]
        fixed_interval: DataBindMechanism.FixedIntervalPoll
        jittered_interval: DataBindMechanism.JitteredIntervalPoll
        def __init__(self, fixed_interval: _Optional[_Union[DataBindMechanism.FixedIntervalPoll, _Mapping]] = ..., jittered_interval: _Optional[_Union[DataBindMechanism.JitteredIntervalPoll, _Mapping]] = ...) -> None: ...
    class FixedIntervalPoll(_message.Message):
        __slots__ = ("interval_ms",)
        INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
        interval_ms: int
        def __init__(self, interval_ms: _Optional[int] = ...) -> None: ...
    class JitteredIntervalPoll(_message.Message):
        __slots__ = ("min_interval_ms", "max_interval_ms")
        MIN_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
        MAX_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
        min_interval_ms: int
        max_interval_ms: int
        def __init__(self, min_interval_ms: _Optional[int] = ..., max_interval_ms: _Optional[int] = ...) -> None: ...
    CENTRALSTORE_FIELD_NUMBER: _ClassVar[int]
    centralStore: DataBindMechanism.SubscribeToCentralStore
    def __init__(self, centralStore: _Optional[_Union[DataBindMechanism.SubscribeToCentralStore, _Mapping]] = ...) -> None: ...
