from v2 import page_pb2 as _page_pb2
from v2 import error_pb2 as _error_pb2
from v2 import widget_pb2 as _widget_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartResponse(_message.Message):
    __slots__ = ("success", "error")
    class Success(_message.Message):
        __slots__ = ("menu", "page", "is_child", "is_pre_launch", "is_deeplink_resolved", "overlay_data", "is_onboarding", "overlay_widget", "widget_url", "widget_wrapper")
        class Overlay(_message.Message):
            __slots__ = ("config", "auto_dismiss_config", "widget_wrapper", "page")
            CONFIG_FIELD_NUMBER: _ClassVar[int]
            AUTO_DISMISS_CONFIG_FIELD_NUMBER: _ClassVar[int]
            WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
            PAGE_FIELD_NUMBER: _ClassVar[int]
            config: StartResponse.Success.autoDismissConfig
            auto_dismiss_config: StartResponse.Success.AutoDismissConfig
            widget_wrapper: _widget_pb2.WidgetWrapper
            page: _page_pb2.Page
            def __init__(self, config: _Optional[_Union[StartResponse.Success.autoDismissConfig, _Mapping]] = ..., auto_dismiss_config: _Optional[_Union[StartResponse.Success.AutoDismissConfig, _Mapping]] = ..., widget_wrapper: _Optional[_Union[_widget_pb2.WidgetWrapper, _Mapping]] = ..., page: _Optional[_Union[_page_pb2.Page, _Mapping]] = ...) -> None: ...
        class OverlayWidget(_message.Message):
            __slots__ = ("widget_url", "widget_wrapper")
            WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
            WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
            widget_url: str
            widget_wrapper: _widget_pb2.WidgetWrapper
            def __init__(self, widget_url: _Optional[str] = ..., widget_wrapper: _Optional[_Union[_widget_pb2.WidgetWrapper, _Mapping]] = ...) -> None: ...
        class autoDismissConfig(_message.Message):
            __slots__ = ("dismissTimeInMillis",)
            DISMISSTIMEINMILLIS_FIELD_NUMBER: _ClassVar[int]
            dismissTimeInMillis: int
            def __init__(self, dismissTimeInMillis: _Optional[int] = ...) -> None: ...
        class AutoDismissConfig(_message.Message):
            __slots__ = ("dismiss_time_in_sec",)
            DISMISS_TIME_IN_SEC_FIELD_NUMBER: _ClassVar[int]
            dismiss_time_in_sec: int
            def __init__(self, dismiss_time_in_sec: _Optional[int] = ...) -> None: ...
        MENU_FIELD_NUMBER: _ClassVar[int]
        PAGE_FIELD_NUMBER: _ClassVar[int]
        IS_CHILD_FIELD_NUMBER: _ClassVar[int]
        IS_PRE_LAUNCH_FIELD_NUMBER: _ClassVar[int]
        IS_DEEPLINK_RESOLVED_FIELD_NUMBER: _ClassVar[int]
        OVERLAY_DATA_FIELD_NUMBER: _ClassVar[int]
        IS_ONBOARDING_FIELD_NUMBER: _ClassVar[int]
        OVERLAY_WIDGET_FIELD_NUMBER: _ClassVar[int]
        WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        menu: _widget_pb2.WidgetWrapper
        page: _page_pb2.Page
        is_child: bool
        is_pre_launch: bool
        is_deeplink_resolved: bool
        overlay_data: StartResponse.Success.Overlay
        is_onboarding: bool
        overlay_widget: StartResponse.Success.OverlayWidget
        widget_url: str
        widget_wrapper: _widget_pb2.WidgetWrapper
        def __init__(self, menu: _Optional[_Union[_widget_pb2.WidgetWrapper, _Mapping]] = ..., page: _Optional[_Union[_page_pb2.Page, _Mapping]] = ..., is_child: bool = ..., is_pre_launch: bool = ..., is_deeplink_resolved: bool = ..., overlay_data: _Optional[_Union[StartResponse.Success.Overlay, _Mapping]] = ..., is_onboarding: bool = ..., overlay_widget: _Optional[_Union[StartResponse.Success.OverlayWidget, _Mapping]] = ..., widget_url: _Optional[str] = ..., widget_wrapper: _Optional[_Union[_widget_pb2.WidgetWrapper, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: StartResponse.Success
    error: _error_pb2.Error
    def __init__(self, success: _Optional[_Union[StartResponse.Success, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
