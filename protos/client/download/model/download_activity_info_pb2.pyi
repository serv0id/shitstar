from client.download.model import download_activity_name_pb2 as _download_activity_name_pb2
from client.download.model import journey_type_pb2 as _journey_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadActivityInfo(_message.Message):
    __slots__ = ("download_activity_name", "requested_journey_type")
    DOWNLOAD_ACTIVITY_NAME_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_JOURNEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    download_activity_name: _download_activity_name_pb2.DownloadActivityName
    requested_journey_type: _journey_type_pb2.JourneyType
    def __init__(self, download_activity_name: _Optional[_Union[_download_activity_name_pb2.DownloadActivityName, str]] = ..., requested_journey_type: _Optional[_Union[_journey_type_pb2.JourneyType, str]] = ...) -> None: ...
