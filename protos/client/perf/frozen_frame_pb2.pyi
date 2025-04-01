from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MoreInfoKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MORE_INFO_KEY_UNSPECIFIED: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_PAGE_URL: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_IS_SCROLLING_VERTICALLY: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_INTERACTED_PAGE: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_INTERACTED_SPACE: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_INTERACTED_WIDGET: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_SUB_TYPE: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_LAST_ACTION: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_LAST_INTERACTED_ELEMENT: _ClassVar[MoreInfoKey]
    MORE_INFO_KEY_WEB_LOAD_STATE: _ClassVar[MoreInfoKey]
MORE_INFO_KEY_UNSPECIFIED: MoreInfoKey
MORE_INFO_KEY_PAGE_URL: MoreInfoKey
MORE_INFO_KEY_IS_SCROLLING_VERTICALLY: MoreInfoKey
MORE_INFO_KEY_INTERACTED_PAGE: MoreInfoKey
MORE_INFO_KEY_INTERACTED_SPACE: MoreInfoKey
MORE_INFO_KEY_INTERACTED_WIDGET: MoreInfoKey
MORE_INFO_KEY_SUB_TYPE: MoreInfoKey
MORE_INFO_KEY_LAST_ACTION: MoreInfoKey
MORE_INFO_KEY_LAST_INTERACTED_ELEMENT: MoreInfoKey
MORE_INFO_KEY_WEB_LOAD_STATE: MoreInfoKey

class FrozenFrame(_message.Message):
    __slots__ = ("page_name", "duration_ms", "more_infos", "is_scrolling_vertically", "last_action", "last_interacted_element", "web_sub_type", "web_load_state", "heap_memory_used_bytes", "heap_memory_available_bytes")
    PAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    MORE_INFOS_FIELD_NUMBER: _ClassVar[int]
    IS_SCROLLING_VERTICALLY_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTION_FIELD_NUMBER: _ClassVar[int]
    LAST_INTERACTED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    WEB_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    WEB_LOAD_STATE_FIELD_NUMBER: _ClassVar[int]
    HEAP_MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    HEAP_MEMORY_AVAILABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    page_name: str
    duration_ms: int
    more_infos: _containers.RepeatedCompositeFieldContainer[MoreInfo]
    is_scrolling_vertically: bool
    last_action: str
    last_interacted_element: str
    web_sub_type: str
    web_load_state: str
    heap_memory_used_bytes: float
    heap_memory_available_bytes: float
    def __init__(self, page_name: _Optional[str] = ..., duration_ms: _Optional[int] = ..., more_infos: _Optional[_Iterable[_Union[MoreInfo, _Mapping]]] = ..., is_scrolling_vertically: bool = ..., last_action: _Optional[str] = ..., last_interacted_element: _Optional[str] = ..., web_sub_type: _Optional[str] = ..., web_load_state: _Optional[str] = ..., heap_memory_used_bytes: _Optional[float] = ..., heap_memory_available_bytes: _Optional[float] = ...) -> None: ...

class MoreInfo(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: MoreInfoKey
    value: str
    def __init__(self, key: _Optional[_Union[MoreInfoKey, str]] = ..., value: _Optional[str] = ...) -> None: ...
