from base import page_data_commons_pb2 as _page_data_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.watch import watch_ab_config_pb2 as _watch_ab_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchPageData(_message.Message):
    __slots__ = ("page_data_commons", "report_data", "watch_config", "page_event_actions", "player_config")
    class PlayerReportItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[WatchPageData.PlayerReportItemType]
        BUFFERING_CONNECTION: _ClassVar[WatchPageData.PlayerReportItemType]
        VIDEO_QUALITY: _ClassVar[WatchPageData.PlayerReportItemType]
        AUDIO_QUALITY: _ClassVar[WatchPageData.PlayerReportItemType]
        SUBTITLES_CAPTIONS: _ClassVar[WatchPageData.PlayerReportItemType]
    UNKNOWN: WatchPageData.PlayerReportItemType
    BUFFERING_CONNECTION: WatchPageData.PlayerReportItemType
    VIDEO_QUALITY: WatchPageData.PlayerReportItemType
    AUDIO_QUALITY: WatchPageData.PlayerReportItemType
    SUBTITLES_CAPTIONS: WatchPageData.PlayerReportItemType
    class PlayerReportMenuData(_message.Message):
        __slots__ = ("title", "report_options")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        REPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        report_options: _containers.RepeatedCompositeFieldContainer[WatchPageData.PlayerReportMenuItem]
        def __init__(self, title: _Optional[str] = ..., report_options: _Optional[_Iterable[_Union[WatchPageData.PlayerReportMenuItem, _Mapping]]] = ...) -> None: ...
    class PageEventActionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _actions_pb2.Actions.Action
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_actions_pb2.Actions.Action, _Mapping]] = ...) -> None: ...
    class PlayerConfig(_message.Message):
        __slots__ = ("av1_decoder", "hsdav1d_thread_count_percentage")
        AV1_DECODER_FIELD_NUMBER: _ClassVar[int]
        HSDAV1D_THREAD_COUNT_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        av1_decoder: str
        hsdav1d_thread_count_percentage: int
        def __init__(self, av1_decoder: _Optional[str] = ..., hsdav1d_thread_count_percentage: _Optional[int] = ...) -> None: ...
    class PlayerReportMenuItem(_message.Message):
        __slots__ = ("icon_name", "title", "description", "result", "type")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        title: str
        description: str
        result: str
        type: WatchPageData.PlayerReportItemType
        def __init__(self, icon_name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., result: _Optional[str] = ..., type: _Optional[_Union[WatchPageData.PlayerReportItemType, str]] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    REPORT_DATA_FIELD_NUMBER: _ClassVar[int]
    WATCH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PAGE_EVENT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    report_data: WatchPageData.PlayerReportMenuData
    watch_config: _watch_ab_config_pb2.WatchConfig
    page_event_actions: _containers.MessageMap[str, _actions_pb2.Actions.Action]
    player_config: WatchPageData.PlayerConfig
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., report_data: _Optional[_Union[WatchPageData.PlayerReportMenuData, _Mapping]] = ..., watch_config: _Optional[_Union[_watch_ab_config_pb2.WatchConfig, _Mapping]] = ..., page_event_actions: _Optional[_Mapping[str, _actions_pb2.Actions.Action]] = ..., player_config: _Optional[_Union[WatchPageData.PlayerConfig, _Mapping]] = ...) -> None: ...
