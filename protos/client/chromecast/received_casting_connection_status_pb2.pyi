from client.chromecast import casting_connection_state_pb2 as _casting_connection_state_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReceivedCastingConnectionStatusProperties(_message.Message):
    __slots__ = ("casting_connection_state", "additional_details")
    CASTING_CONNECTION_STATE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    casting_connection_state: _casting_connection_state_pb2.CastingConnectionState
    additional_details: str
    def __init__(self, casting_connection_state: _Optional[_Union[_casting_connection_state_pb2.CastingConnectionState, str]] = ..., additional_details: _Optional[str] = ...) -> None: ...
