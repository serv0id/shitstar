from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageLoadedCommons(_message.Message):
    __slots__ = ("time_to_first_render_ms", "response_fetch_time_ms", "request_id", "rendering_mode", "absolute_page_url", "dns_connection_time_ms", "connection_acquired_time_ms", "request_headers_time_ms", "request_body_time_ms", "response_headers_time_ms", "response_body_time_ms", "data_transfer_time_ms", "response_body_size_in_byte", "proto_parse_time_ms", "secure_connection_time_ms", "network_waiting_time_ms", "is_loaded_from_client_cache", "http_protocol", "is_retry")
    class RenderingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RENDERING_MODE_UNSPECIFIED: _ClassVar[PageLoadedCommons.RenderingMode]
        RENDERING_MODE_CSR: _ClassVar[PageLoadedCommons.RenderingMode]
        RENDERING_MODE_DW: _ClassVar[PageLoadedCommons.RenderingMode]
    RENDERING_MODE_UNSPECIFIED: PageLoadedCommons.RenderingMode
    RENDERING_MODE_CSR: PageLoadedCommons.RenderingMode
    RENDERING_MODE_DW: PageLoadedCommons.RenderingMode
    class HttpProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HTTP_PROTOCOL_UNSPECIFIED: _ClassVar[PageLoadedCommons.HttpProtocol]
        HTTP_PROTOCOL_1_1: _ClassVar[PageLoadedCommons.HttpProtocol]
        HTTP_PROTOCOL_2: _ClassVar[PageLoadedCommons.HttpProtocol]
        HTTP_PROTOCOL_3: _ClassVar[PageLoadedCommons.HttpProtocol]
    HTTP_PROTOCOL_UNSPECIFIED: PageLoadedCommons.HttpProtocol
    HTTP_PROTOCOL_1_1: PageLoadedCommons.HttpProtocol
    HTTP_PROTOCOL_2: PageLoadedCommons.HttpProtocol
    HTTP_PROTOCOL_3: PageLoadedCommons.HttpProtocol
    TIME_TO_FIRST_RENDER_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FETCH_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RENDERING_MODE_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    DNS_CONNECTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ACQUIRED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADERS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_HEADERS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DATA_TRANSFER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_SIZE_IN_BYTE_FIELD_NUMBER: _ClassVar[int]
    PROTO_PARSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SECURE_CONNECTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_WAITING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    IS_LOADED_FROM_CLIENT_CACHE_FIELD_NUMBER: _ClassVar[int]
    HTTP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    IS_RETRY_FIELD_NUMBER: _ClassVar[int]
    time_to_first_render_ms: int
    response_fetch_time_ms: int
    request_id: str
    rendering_mode: PageLoadedCommons.RenderingMode
    absolute_page_url: str
    dns_connection_time_ms: int
    connection_acquired_time_ms: int
    request_headers_time_ms: int
    request_body_time_ms: int
    response_headers_time_ms: int
    response_body_time_ms: int
    data_transfer_time_ms: int
    response_body_size_in_byte: int
    proto_parse_time_ms: int
    secure_connection_time_ms: int
    network_waiting_time_ms: int
    is_loaded_from_client_cache: bool
    http_protocol: PageLoadedCommons.HttpProtocol
    is_retry: bool
    def __init__(self, time_to_first_render_ms: _Optional[int] = ..., response_fetch_time_ms: _Optional[int] = ..., request_id: _Optional[str] = ..., rendering_mode: _Optional[_Union[PageLoadedCommons.RenderingMode, str]] = ..., absolute_page_url: _Optional[str] = ..., dns_connection_time_ms: _Optional[int] = ..., connection_acquired_time_ms: _Optional[int] = ..., request_headers_time_ms: _Optional[int] = ..., request_body_time_ms: _Optional[int] = ..., response_headers_time_ms: _Optional[int] = ..., response_body_time_ms: _Optional[int] = ..., data_transfer_time_ms: _Optional[int] = ..., response_body_size_in_byte: _Optional[int] = ..., proto_parse_time_ms: _Optional[int] = ..., secure_connection_time_ms: _Optional[int] = ..., network_waiting_time_ms: _Optional[int] = ..., is_loaded_from_client_cache: bool = ..., http_protocol: _Optional[_Union[PageLoadedCommons.HttpProtocol, str]] = ..., is_retry: bool = ...) -> None: ...
