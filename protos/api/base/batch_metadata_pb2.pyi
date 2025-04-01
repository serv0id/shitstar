from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatchMetadata(_message.Message):
    __slots__ = ("batch_id", "batch_size_bytes", "common_size_bytes", "event_size_bytes", "batch_num_events", "request_payload_size_bytes", "is_request_payload_compressed")
    BATCH_ID_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    COMMON_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    EVENT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    BATCH_NUM_EVENTS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_PAYLOAD_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_REQUEST_PAYLOAD_COMPRESSED_FIELD_NUMBER: _ClassVar[int]
    batch_id: str
    batch_size_bytes: int
    common_size_bytes: int
    event_size_bytes: int
    batch_num_events: int
    request_payload_size_bytes: int
    is_request_payload_compressed: bool
    def __init__(self, batch_id: _Optional[str] = ..., batch_size_bytes: _Optional[int] = ..., common_size_bytes: _Optional[int] = ..., event_size_bytes: _Optional[int] = ..., batch_num_events: _Optional[int] = ..., request_payload_size_bytes: _Optional[int] = ..., is_request_payload_compressed: bool = ...) -> None: ...
