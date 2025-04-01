import feedback_pb2 as _feedback_pb2
import metadata_pb2 as _metadata_pb2
import log_pb2 as _log_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoggingPayload(_message.Message):
    __slots__ = ("feedback", "metadata", "log")
    FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    LOG_FIELD_NUMBER: _ClassVar[int]
    feedback: _feedback_pb2.Feedback
    metadata: _metadata_pb2.Metadata
    log: _log_pb2.Log
    def __init__(self, feedback: _Optional[_Union[_feedback_pb2.Feedback, _Mapping]] = ..., metadata: _Optional[_Union[_metadata_pb2.Metadata, _Mapping]] = ..., log: _Optional[_Union[_log_pb2.Log, _Mapping]] = ...) -> None: ...
