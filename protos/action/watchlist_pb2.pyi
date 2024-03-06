from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchlistAction(_message.Message):
    __slots__ = ["info"]
    INFO_FIELD_NUMBER: _ClassVar[int]
    info: _watchlist_info_pb2.WatchlistInfo
    def __init__(self, info: _Optional[_Union[_watchlist_info_pb2.WatchlistInfo, _Mapping]] = ...) -> None: ...
