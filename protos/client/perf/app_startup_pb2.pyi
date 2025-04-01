from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppStart(_message.Message):
    __slots__ = ("total_load_time_ms", "start_type", "splash_screen_time_ms", "first_frame_time_ms", "rendering_mode", "app_startup_time_ms", "data_processing_time_ms", "api_response_time_ms", "fetch_fp_key_time_ms", "page_rendering_time_ms", "app_init_time_ms", "activity_init_time_ms", "splash_init_time_ms", "startup_init_time_ms", "start_api_init_time_ms", "proto_parsing_time_ms", "splash_page_time_ms", "start_api_domain_connection_time_ms", "start_api_connection_time_ms", "start_api_secure_connection_time_ms", "start_api_response_time_ms", "start_api_response_body_size_kb", "start_api_response_time_event_listener_ms", "processing_time_before_start_api_call_ms", "processing_time_after_start_api_response_ms", "mandatory_task_time_for_start_operation_ms", "firebase_configuration_time_ms", "config_lib_init_time_ms", "is_pre_warm_launch", "start_api_response_time_response_interceptor_ms", "processing_time_response_header_interceptor_ms", "runblocking_time_response_header_interceptor_ms", "ops_time_oncreate_main_activity_ms", "start_up_initialiser_initialise_method_time_ms", "start_api_connection_acquired_time_ms", "start_api_request_headers_time_ms", "start_api_request_body_time_ms", "start_api_response_headers_time_ms", "splash_setup_process_time_ms", "navigation_from_splash_time_ms", "send_splash_viewed_analytics_time_ms", "mandatory_task_in_splash_time_ms", "start_api_retry_count", "document_fetch_n_load_time_ms", "absolute_page_url", "start_up_initializer_injection_time_ms", "processing_time_before_bff_startup_repo_ms", "bff_start_up_repo_injection_time_ms", "context_switching_bff_start_up_repo_time_ms", "bff_startup_repo_end_to_initializer_end_time_ms", "analytics_lib_operation_time_ms", "app_suite_setup_operation_time_ms", "logging_lib_setup_operation_time_ms", "download_service_setup_operation_time_ms", "dns_resolver_type", "is_loaded_from_client_cache", "http_protocol")
    class StartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        START_TYPE_UNSPECIFIED: _ClassVar[AppStart.StartType]
        START_TYPE_COLD: _ClassVar[AppStart.StartType]
        START_TYPE_WARM: _ClassVar[AppStart.StartType]
    START_TYPE_UNSPECIFIED: AppStart.StartType
    START_TYPE_COLD: AppStart.StartType
    START_TYPE_WARM: AppStart.StartType
    class RenderingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RENDERING_MODE_UNSPECIFIED: _ClassVar[AppStart.RenderingMode]
        RENDERING_MODE_SSR: _ClassVar[AppStart.RenderingMode]
        RENDERING_MODE_CSR: _ClassVar[AppStart.RenderingMode]
        RENDERING_MODE_DW: _ClassVar[AppStart.RenderingMode]
    RENDERING_MODE_UNSPECIFIED: AppStart.RenderingMode
    RENDERING_MODE_SSR: AppStart.RenderingMode
    RENDERING_MODE_CSR: AppStart.RenderingMode
    RENDERING_MODE_DW: AppStart.RenderingMode
    class DnsResolverType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DNS_RESOLVER_TYPE_UNSPECIFIED: _ClassVar[AppStart.DnsResolverType]
        DNS_RESOLVER_TYPE_SYSTEM: _ClassVar[AppStart.DnsResolverType]
        DNS_RESOLVER_TYPE_GOOGLE: _ClassVar[AppStart.DnsResolverType]
        DNS_RESOLVER_TYPE_CLOUDFLARE: _ClassVar[AppStart.DnsResolverType]
    DNS_RESOLVER_TYPE_UNSPECIFIED: AppStart.DnsResolverType
    DNS_RESOLVER_TYPE_SYSTEM: AppStart.DnsResolverType
    DNS_RESOLVER_TYPE_GOOGLE: AppStart.DnsResolverType
    DNS_RESOLVER_TYPE_CLOUDFLARE: AppStart.DnsResolverType
    class HttpProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HTTP_PROTOCOL_UNSPECIFIED: _ClassVar[AppStart.HttpProtocol]
        HTTP_PROTOCOL_1_1: _ClassVar[AppStart.HttpProtocol]
        HTTP_PROTOCOL_2: _ClassVar[AppStart.HttpProtocol]
        HTTP_PROTOCOL_3: _ClassVar[AppStart.HttpProtocol]
    HTTP_PROTOCOL_UNSPECIFIED: AppStart.HttpProtocol
    HTTP_PROTOCOL_1_1: AppStart.HttpProtocol
    HTTP_PROTOCOL_2: AppStart.HttpProtocol
    HTTP_PROTOCOL_3: AppStart.HttpProtocol
    TOTAL_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPLASH_SCREEN_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FIRST_FRAME_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RENDERING_MODE_FIELD_NUMBER: _ClassVar[int]
    APP_STARTUP_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DATA_PROCESSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    API_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FETCH_FP_KEY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PAGE_RENDERING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    APP_INIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_INIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SPLASH_INIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    STARTUP_INIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_INIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PROTO_PARSING_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SPLASH_PAGE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_DOMAIN_CONNECTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_CONNECTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_SECURE_CONNECTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_RESPONSE_BODY_SIZE_KB_FIELD_NUMBER: _ClassVar[int]
    START_API_RESPONSE_TIME_EVENT_LISTENER_MS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_BEFORE_START_API_CALL_MS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_AFTER_START_API_RESPONSE_MS_FIELD_NUMBER: _ClassVar[int]
    MANDATORY_TASK_TIME_FOR_START_OPERATION_MS_FIELD_NUMBER: _ClassVar[int]
    FIREBASE_CONFIGURATION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CONFIG_LIB_INIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    IS_PRE_WARM_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    START_API_RESPONSE_TIME_RESPONSE_INTERCEPTOR_MS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_RESPONSE_HEADER_INTERCEPTOR_MS_FIELD_NUMBER: _ClassVar[int]
    RUNBLOCKING_TIME_RESPONSE_HEADER_INTERCEPTOR_MS_FIELD_NUMBER: _ClassVar[int]
    OPS_TIME_ONCREATE_MAIN_ACTIVITY_MS_FIELD_NUMBER: _ClassVar[int]
    START_UP_INITIALISER_INITIALISE_METHOD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_CONNECTION_ACQUIRED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_REQUEST_HEADERS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_REQUEST_BODY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_RESPONSE_HEADERS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SPLASH_SETUP_PROCESS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    NAVIGATION_FROM_SPLASH_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SEND_SPLASH_VIEWED_ANALYTICS_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    MANDATORY_TASK_IN_SPLASH_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FETCH_N_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    START_UP_INITIALIZER_INJECTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PROCESSING_TIME_BEFORE_BFF_STARTUP_REPO_MS_FIELD_NUMBER: _ClassVar[int]
    BFF_START_UP_REPO_INJECTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_SWITCHING_BFF_START_UP_REPO_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    BFF_STARTUP_REPO_END_TO_INITIALIZER_END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_LIB_OPERATION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    APP_SUITE_SETUP_OPERATION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    LOGGING_LIB_SETUP_OPERATION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SERVICE_SETUP_OPERATION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DNS_RESOLVER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_LOADED_FROM_CLIENT_CACHE_FIELD_NUMBER: _ClassVar[int]
    HTTP_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    total_load_time_ms: int
    start_type: AppStart.StartType
    splash_screen_time_ms: int
    first_frame_time_ms: int
    rendering_mode: AppStart.RenderingMode
    app_startup_time_ms: int
    data_processing_time_ms: int
    api_response_time_ms: int
    fetch_fp_key_time_ms: int
    page_rendering_time_ms: int
    app_init_time_ms: int
    activity_init_time_ms: int
    splash_init_time_ms: int
    startup_init_time_ms: int
    start_api_init_time_ms: int
    proto_parsing_time_ms: int
    splash_page_time_ms: int
    start_api_domain_connection_time_ms: int
    start_api_connection_time_ms: int
    start_api_secure_connection_time_ms: int
    start_api_response_time_ms: int
    start_api_response_body_size_kb: int
    start_api_response_time_event_listener_ms: int
    processing_time_before_start_api_call_ms: int
    processing_time_after_start_api_response_ms: int
    mandatory_task_time_for_start_operation_ms: int
    firebase_configuration_time_ms: int
    config_lib_init_time_ms: int
    is_pre_warm_launch: bool
    start_api_response_time_response_interceptor_ms: int
    processing_time_response_header_interceptor_ms: int
    runblocking_time_response_header_interceptor_ms: int
    ops_time_oncreate_main_activity_ms: int
    start_up_initialiser_initialise_method_time_ms: int
    start_api_connection_acquired_time_ms: int
    start_api_request_headers_time_ms: int
    start_api_request_body_time_ms: int
    start_api_response_headers_time_ms: int
    splash_setup_process_time_ms: int
    navigation_from_splash_time_ms: int
    send_splash_viewed_analytics_time_ms: int
    mandatory_task_in_splash_time_ms: int
    start_api_retry_count: int
    document_fetch_n_load_time_ms: int
    absolute_page_url: str
    start_up_initializer_injection_time_ms: int
    processing_time_before_bff_startup_repo_ms: int
    bff_start_up_repo_injection_time_ms: int
    context_switching_bff_start_up_repo_time_ms: int
    bff_startup_repo_end_to_initializer_end_time_ms: int
    analytics_lib_operation_time_ms: int
    app_suite_setup_operation_time_ms: int
    logging_lib_setup_operation_time_ms: int
    download_service_setup_operation_time_ms: int
    dns_resolver_type: AppStart.DnsResolverType
    is_loaded_from_client_cache: bool
    http_protocol: AppStart.HttpProtocol
    def __init__(self, total_load_time_ms: _Optional[int] = ..., start_type: _Optional[_Union[AppStart.StartType, str]] = ..., splash_screen_time_ms: _Optional[int] = ..., first_frame_time_ms: _Optional[int] = ..., rendering_mode: _Optional[_Union[AppStart.RenderingMode, str]] = ..., app_startup_time_ms: _Optional[int] = ..., data_processing_time_ms: _Optional[int] = ..., api_response_time_ms: _Optional[int] = ..., fetch_fp_key_time_ms: _Optional[int] = ..., page_rendering_time_ms: _Optional[int] = ..., app_init_time_ms: _Optional[int] = ..., activity_init_time_ms: _Optional[int] = ..., splash_init_time_ms: _Optional[int] = ..., startup_init_time_ms: _Optional[int] = ..., start_api_init_time_ms: _Optional[int] = ..., proto_parsing_time_ms: _Optional[int] = ..., splash_page_time_ms: _Optional[int] = ..., start_api_domain_connection_time_ms: _Optional[int] = ..., start_api_connection_time_ms: _Optional[int] = ..., start_api_secure_connection_time_ms: _Optional[int] = ..., start_api_response_time_ms: _Optional[int] = ..., start_api_response_body_size_kb: _Optional[int] = ..., start_api_response_time_event_listener_ms: _Optional[int] = ..., processing_time_before_start_api_call_ms: _Optional[int] = ..., processing_time_after_start_api_response_ms: _Optional[int] = ..., mandatory_task_time_for_start_operation_ms: _Optional[int] = ..., firebase_configuration_time_ms: _Optional[int] = ..., config_lib_init_time_ms: _Optional[int] = ..., is_pre_warm_launch: bool = ..., start_api_response_time_response_interceptor_ms: _Optional[int] = ..., processing_time_response_header_interceptor_ms: _Optional[int] = ..., runblocking_time_response_header_interceptor_ms: _Optional[int] = ..., ops_time_oncreate_main_activity_ms: _Optional[int] = ..., start_up_initialiser_initialise_method_time_ms: _Optional[int] = ..., start_api_connection_acquired_time_ms: _Optional[int] = ..., start_api_request_headers_time_ms: _Optional[int] = ..., start_api_request_body_time_ms: _Optional[int] = ..., start_api_response_headers_time_ms: _Optional[int] = ..., splash_setup_process_time_ms: _Optional[int] = ..., navigation_from_splash_time_ms: _Optional[int] = ..., send_splash_viewed_analytics_time_ms: _Optional[int] = ..., mandatory_task_in_splash_time_ms: _Optional[int] = ..., start_api_retry_count: _Optional[int] = ..., document_fetch_n_load_time_ms: _Optional[int] = ..., absolute_page_url: _Optional[str] = ..., start_up_initializer_injection_time_ms: _Optional[int] = ..., processing_time_before_bff_startup_repo_ms: _Optional[int] = ..., bff_start_up_repo_injection_time_ms: _Optional[int] = ..., context_switching_bff_start_up_repo_time_ms: _Optional[int] = ..., bff_startup_repo_end_to_initializer_end_time_ms: _Optional[int] = ..., analytics_lib_operation_time_ms: _Optional[int] = ..., app_suite_setup_operation_time_ms: _Optional[int] = ..., logging_lib_setup_operation_time_ms: _Optional[int] = ..., download_service_setup_operation_time_ms: _Optional[int] = ..., dns_resolver_type: _Optional[_Union[AppStart.DnsResolverType, str]] = ..., is_loaded_from_client_cache: bool = ..., http_protocol: _Optional[_Union[AppStart.HttpProtocol, str]] = ...) -> None: ...
