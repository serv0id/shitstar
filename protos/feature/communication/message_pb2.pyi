from feature.communication.data import kids_profile_toggle_pb2 as _kids_profile_toggle_pb2
from feature.communication.data import form_event_pb2 as _form_event_pb2
from feature.communication.data import search_zero_filter_data_pb2 as _search_zero_filter_data_pb2
from feature.share import share_info_pb2 as _share_info_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ["message_name", "data"]
    class MessageName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        KIDS_PROFILE_TOGGLE_MESSAGE: _ClassVar[Message.MessageName]
        FORM_EVENT_MESSAGE: _ClassVar[Message.MessageName]
        SEARCH_ZERO_FILTERS_MESSAGE: _ClassVar[Message.MessageName]
        SHARE_SCREENSHOT_MESSAGE: _ClassVar[Message.MessageName]
    KIDS_PROFILE_TOGGLE_MESSAGE: Message.MessageName
    FORM_EVENT_MESSAGE: Message.MessageName
    SEARCH_ZERO_FILTERS_MESSAGE: Message.MessageName
    SHARE_SCREENSHOT_MESSAGE: Message.MessageName
    class Data(_message.Message):
        __slots__ = ["disableMessageCaching", "kids_profile_toggle", "form_event", "search_zero_filter_data", "share_info"]
        DISABLEMESSAGECACHING_FIELD_NUMBER: _ClassVar[int]
        KIDS_PROFILE_TOGGLE_FIELD_NUMBER: _ClassVar[int]
        FORM_EVENT_FIELD_NUMBER: _ClassVar[int]
        SEARCH_ZERO_FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
        SHARE_INFO_FIELD_NUMBER: _ClassVar[int]
        disableMessageCaching: bool
        kids_profile_toggle: _kids_profile_toggle_pb2.KidsProfileToggle
        form_event: _form_event_pb2.FormEvent
        search_zero_filter_data: _search_zero_filter_data_pb2.SearchZeroFilterData
        share_info: _share_info_pb2.ShareInfo
        def __init__(self, disableMessageCaching: bool = ..., kids_profile_toggle: _Optional[_Union[_kids_profile_toggle_pb2.KidsProfileToggle, _Mapping]] = ..., form_event: _Optional[_Union[_form_event_pb2.FormEvent, _Mapping]] = ..., search_zero_filter_data: _Optional[_Union[_search_zero_filter_data_pb2.SearchZeroFilterData, _Mapping]] = ..., share_info: _Optional[_Union[_share_info_pb2.ShareInfo, _Mapping]] = ...) -> None: ...
    MESSAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    message_name: Message.MessageName
    data: Message.Data
    def __init__(self, message_name: _Optional[_Union[Message.MessageName, str]] = ..., data: _Optional[_Union[Message.Data, _Mapping]] = ...) -> None: ...
