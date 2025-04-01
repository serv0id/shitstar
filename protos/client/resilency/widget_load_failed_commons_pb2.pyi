from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetLoadFailedCommons(_message.Message):
    __slots__ = ("error_code", "error_message", "failure_view_type", "request_id", "url", "retry_count")
    class ErrorViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_VIEW_TYPE_UNSPECIFIED: _ClassVar[WidgetLoadFailedCommons.ErrorViewType]
        ERROR_VIEW_TYPE_OVERLAY: _ClassVar[WidgetLoadFailedCommons.ErrorViewType]
        ERROR_VIEW_TYPE_FULL_SCREEN: _ClassVar[WidgetLoadFailedCommons.ErrorViewType]
        ERROR_VIEW_TYPE_IGNORED: _ClassVar[WidgetLoadFailedCommons.ErrorViewType]
    ERROR_VIEW_TYPE_UNSPECIFIED: WidgetLoadFailedCommons.ErrorViewType
    ERROR_VIEW_TYPE_OVERLAY: WidgetLoadFailedCommons.ErrorViewType
    ERROR_VIEW_TYPE_FULL_SCREEN: WidgetLoadFailedCommons.ErrorViewType
    ERROR_VIEW_TYPE_IGNORED: WidgetLoadFailedCommons.ErrorViewType
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    error_message: str
    failure_view_type: WidgetLoadFailedCommons.ErrorViewType
    request_id: str
    url: str
    retry_count: int
    def __init__(self, error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., failure_view_type: _Optional[_Union[WidgetLoadFailedCommons.ErrorViewType, str]] = ..., request_id: _Optional[str] = ..., url: _Optional[str] = ..., retry_count: _Optional[int] = ...) -> None: ...
