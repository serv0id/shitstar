from feature.share import share_info_pb2 as _share_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Share(_message.Message):
    __slots__ = ("share_url", "share_info")
    SHARE_URL_FIELD_NUMBER: _ClassVar[int]
    SHARE_INFO_FIELD_NUMBER: _ClassVar[int]
    share_url: str
    share_info: _share_info_pb2.ShareInfo
    def __init__(self, share_url: _Optional[str] = ..., share_info: _Optional[_Union[_share_info_pb2.ShareInfo, _Mapping]] = ...) -> None: ...
