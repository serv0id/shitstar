from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaywallImpressionPayload(_message.Message):
    __slots__ = ("journey", "source", "packId", "params", "meta")
    JOURNEY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PACKID_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    journey: str
    source: str
    packId: str
    params: Params
    meta: Meta
    def __init__(self, journey: _Optional[str] = ..., source: _Optional[str] = ..., packId: _Optional[str] = ..., params: _Optional[_Union[Params, _Mapping]] = ..., meta: _Optional[_Union[Meta, _Mapping]] = ...) -> None: ...

class Params(_message.Message):
    __slots__ = ("journey", "pack_id")
    JOURNEY_FIELD_NUMBER: _ClassVar[int]
    PACK_ID_FIELD_NUMBER: _ClassVar[int]
    journey: str
    pack_id: str
    def __init__(self, journey: _Optional[str] = ..., pack_id: _Optional[str] = ...) -> None: ...

class Meta(_message.Message):
    __slots__ = ("source", "use_case")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    USE_CASE_FIELD_NUMBER: _ClassVar[int]
    source: str
    use_case: str
    def __init__(self, source: _Optional[str] = ..., use_case: _Optional[str] = ...) -> None: ...
