from base import page_data_commons_pb2 as _page_data_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MobilePaywallV2PageData(_message.Message):
    __slots__ = ("page_data_commons", "page_event_actions")
    class PageEventActionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _actions_pb2.Actions.Action
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_actions_pb2.Actions.Action, _Mapping]] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    PAGE_EVENT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    page_event_actions: _containers.MessageMap[str, _actions_pb2.Actions.Action]
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., page_event_actions: _Optional[_Mapping[str, _actions_pb2.Actions.Action]] = ...) -> None: ...
