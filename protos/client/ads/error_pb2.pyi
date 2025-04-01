from client.ads import info_pb2 as _info_pb2
from options import opts_pb2 as _opts_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("error_type", "error_code", "error_message", "campaign_id", "id_list", "goal_id", "info", "url", "err_code")
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    ID_LIST_FIELD_NUMBER: _ClassVar[int]
    GOAL_ID_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    error_type: str
    error_code: str
    error_message: str
    campaign_id: str
    id_list: str
    goal_id: str
    info: _info_pb2.Info
    url: str
    err_code: int
    def __init__(self, error_type: _Optional[str] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., campaign_id: _Optional[str] = ..., id_list: _Optional[str] = ..., goal_id: _Optional[str] = ..., info: _Optional[_Union[_info_pb2.Info, _Mapping]] = ..., url: _Optional[str] = ..., err_code: _Optional[int] = ...) -> None: ...
