from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadFlow(_message.Message):
    __slots__ = ["bff"]
    class ApiCall(_message.Message):
        __slots__ = ["url", "fetch_type"]
        class FetchType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            FETCH_PAGE: _ClassVar[PreloadFlow.ApiCall.FetchType]
            FETCH_WIDGET: _ClassVar[PreloadFlow.ApiCall.FetchType]
        FETCH_PAGE: PreloadFlow.ApiCall.FetchType
        FETCH_WIDGET: PreloadFlow.ApiCall.FetchType
        URL_FIELD_NUMBER: _ClassVar[int]
        FETCH_TYPE_FIELD_NUMBER: _ClassVar[int]
        url: str
        fetch_type: PreloadFlow.ApiCall.FetchType
        def __init__(self, url: _Optional[str] = ..., fetch_type: _Optional[_Union[PreloadFlow.ApiCall.FetchType, str]] = ...) -> None: ...
    BFF_FIELD_NUMBER: _ClassVar[int]
    bff: PreloadFlow.ApiCall
    def __init__(self, bff: _Optional[_Union[PreloadFlow.ApiCall, _Mapping]] = ...) -> None: ...

class PreloadAction(_message.Message):
    __slots__ = ["flow"]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    flow: PreloadFlow
    def __init__(self, flow: _Optional[_Union[PreloadFlow, _Mapping]] = ...) -> None: ...
