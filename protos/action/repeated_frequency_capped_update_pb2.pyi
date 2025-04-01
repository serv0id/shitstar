from action import frequency_capped_update_pb2 as _frequency_capped_update_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RepeatedFrequencyCappedUpdateAction(_message.Message):
    __slots__ = ("frequencyCappedUpdateAction",)
    FREQUENCYCAPPEDUPDATEACTION_FIELD_NUMBER: _ClassVar[int]
    frequencyCappedUpdateAction: _containers.RepeatedCompositeFieldContainer[_frequency_capped_update_pb2.FrequencyCappedUpdateAction]
    def __init__(self, frequencyCappedUpdateAction: _Optional[_Iterable[_Union[_frequency_capped_update_pb2.FrequencyCappedUpdateAction, _Mapping]]] = ...) -> None: ...
