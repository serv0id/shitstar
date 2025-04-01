from v2 import space_pb2 as _space_pb2
from v2 import refresh_page_pb2 as _refresh_page_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Page(_message.Message):
    __slots__ = ("id", "template", "version", "spaces", "data", "delivery_type", "dynamic_page_request", "deferred_page_request", "page_url", "page_slug")
    class PageDeliveryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATIC: _ClassVar[Page.PageDeliveryType]
        DYNAMIC: _ClassVar[Page.PageDeliveryType]
        DEFERRED: _ClassVar[Page.PageDeliveryType]
    STATIC: Page.PageDeliveryType
    DYNAMIC: Page.PageDeliveryType
    DEFERRED: Page.PageDeliveryType
    class SpacesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _space_pb2.Space
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_space_pb2.Space, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SPACES_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEFERRED_PAGE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SLUG_FIELD_NUMBER: _ClassVar[int]
    id: str
    template: str
    version: str
    spaces: _containers.MessageMap[str, _space_pb2.Space]
    data: _any_pb2.Any
    delivery_type: Page.PageDeliveryType
    dynamic_page_request: _refresh_page_pb2.RefreshPageRequest
    deferred_page_request: _refresh_page_pb2.DeferredPageRequest
    page_url: str
    page_slug: str
    def __init__(self, id: _Optional[str] = ..., template: _Optional[str] = ..., version: _Optional[str] = ..., spaces: _Optional[_Mapping[str, _space_pb2.Space]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., delivery_type: _Optional[_Union[Page.PageDeliveryType, str]] = ..., dynamic_page_request: _Optional[_Union[_refresh_page_pb2.RefreshPageRequest, _Mapping]] = ..., deferred_page_request: _Optional[_Union[_refresh_page_pb2.DeferredPageRequest, _Mapping]] = ..., page_url: _Optional[str] = ..., page_slug: _Optional[str] = ...) -> None: ...
