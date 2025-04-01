from client.chromecast import casting_disconnection_reason_pb2 as _casting_disconnection_reason_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisconnectedCastingProperties(_message.Message):
    __slots__ = ("disconnect_reason",)
    DISCONNECT_REASON_FIELD_NUMBER: _ClassVar[int]
    disconnect_reason: _casting_disconnection_reason_pb2.CastingDisconnectionReason
    def __init__(self, disconnect_reason: _Optional[_Union[_casting_disconnection_reason_pb2.CastingDisconnectionReason, str]] = ...) -> None: ...
