from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OpenWidgetOverlayAction(_message.Message):
    __slots__ = ("config", "auto_dismiss_config", "is_non_cancelable", "url", "widget_url", "widget_wrapper")
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
    class WidgetWrapper(_message.Message):
        __slots__ = ("template", "widget")
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        WIDGET_FIELD_NUMBER: _ClassVar[int]
        template: str
        widget: _any_pb2.Any
        def __init__(self, template: _Optional[str] = ..., widget: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTO_DISMISS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    IS_NON_CANCELABLE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    config: OpenWidgetOverlayAction.autoDismissConfig
    auto_dismiss_config: OpenWidgetOverlayAction.AutoDismissConfig
    is_non_cancelable: bool
    url: str
    widget_url: str
    widget_wrapper: OpenWidgetOverlayAction.WidgetWrapper
    def __init__(self, config: _Optional[_Union[OpenWidgetOverlayAction.autoDismissConfig, _Mapping]] = ..., auto_dismiss_config: _Optional[_Union[OpenWidgetOverlayAction.AutoDismissConfig, _Mapping]] = ..., is_non_cancelable: bool = ..., url: _Optional[str] = ..., widget_url: _Optional[str] = ..., widget_wrapper: _Optional[_Union[OpenWidgetOverlayAction.WidgetWrapper, _Mapping]] = ...) -> None: ...
