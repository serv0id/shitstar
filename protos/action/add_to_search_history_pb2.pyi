from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddToSearchHistoryAction(_message.Message):
    __slots__ = ("history_record_name", "page_url", "is_content", "image", "page_type", "instrumentation_url", "instrumentation_value", "expiry_config")
    class ExpiryConfig(_message.Message):
        __slots__ = ("duration", "unit")
        DURATION_FIELD_NUMBER: _ClassVar[int]
        UNIT_FIELD_NUMBER: _ClassVar[int]
        duration: int
        unit: str
        def __init__(self, duration: _Optional[int] = ..., unit: _Optional[str] = ...) -> None: ...
    HISTORY_RECORD_NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    IS_CONTENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_URL_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    history_record_name: str
    page_url: str
    is_content: bool
    image: _image_pb2.Image
    page_type: str
    instrumentation_url: str
    instrumentation_value: bytes
    expiry_config: AddToSearchHistoryAction.ExpiryConfig
    def __init__(self, history_record_name: _Optional[str] = ..., page_url: _Optional[str] = ..., is_content: bool = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., page_type: _Optional[str] = ..., instrumentation_url: _Optional[str] = ..., instrumentation_value: _Optional[bytes] = ..., expiry_config: _Optional[_Union[AddToSearchHistoryAction.ExpiryConfig, _Mapping]] = ...) -> None: ...
