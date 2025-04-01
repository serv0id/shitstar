from client.download.model import journey_type_pb2 as _journey_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadAttemptProperties(_message.Message):
    __slots__ = ("requested_journey_type", "download_uuid")
    REQUESTED_JOURNEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_UUID_FIELD_NUMBER: _ClassVar[int]
    requested_journey_type: _journey_type_pb2.JourneyType
    download_uuid: str
    def __init__(self, requested_journey_type: _Optional[_Union[_journey_type_pb2.JourneyType, str]] = ..., download_uuid: _Optional[str] = ...) -> None: ...
