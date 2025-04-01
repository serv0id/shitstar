from action import frequency_capped_status_pb2 as _frequency_capped_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RepeatedFrequencyCappedStatusAction(_message.Message):
    __slots__ = ("frequencyCappedStatusAction",)
    FREQUENCYCAPPEDSTATUSACTION_FIELD_NUMBER: _ClassVar[int]
    frequencyCappedStatusAction: _containers.RepeatedCompositeFieldContainer[_frequency_capped_status_pb2.FrequencyCappedStatusAction]
    def __init__(self, frequencyCappedStatusAction: _Optional[_Iterable[_Union[_frequency_capped_status_pb2.FrequencyCappedStatusAction, _Mapping]]] = ...) -> None: ...
