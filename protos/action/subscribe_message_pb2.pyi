from feature.communication import message_pb2 as _message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscribeToMessageAction(_message.Message):
    __slots__ = ["message_names"]
    MESSAGE_NAMES_FIELD_NUMBER: _ClassVar[int]
    message_names: _containers.RepeatedScalarFieldContainer[_message_pb2.Message.MessageName]
    def __init__(self, message_names: _Optional[_Iterable[_Union[_message_pb2.Message.MessageName, str]]] = ...) -> None: ...
