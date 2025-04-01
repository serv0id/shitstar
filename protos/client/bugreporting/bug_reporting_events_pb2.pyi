from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BugReportEvent(_message.Message):
    __slots__ = ("brt_event_type", "cpu_usage", "memory_usage", "brt_sdk_version")
    class BugReportEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUG_REPORT_EVENT_TYPE_BRT_UNSPECIFIED: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_INVOKED: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_DB_INITIALIZATION_FAILED: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_DB_INITIALIZED: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_BUG_SCREEN_INVOKED: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_BUG_REPORT_DROP_OFF: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_BUG_REPORT_SAVED: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_NO_INTERNET: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_NON_REPORTED_BUGS_COUNT: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_REPORT_SUCCESS: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_REPORT_FAILURE: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_REPORT_DELETE: _ClassVar[BugReportEvent.BugReportEventType]
        BUG_REPORT_EVENT_TYPE_BRT_INITIALIZED: _ClassVar[BugReportEvent.BugReportEventType]
    BUG_REPORT_EVENT_TYPE_BRT_UNSPECIFIED: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_INVOKED: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_DB_INITIALIZATION_FAILED: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_DB_INITIALIZED: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_BUG_SCREEN_INVOKED: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_BUG_REPORT_DROP_OFF: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_BUG_REPORT_SAVED: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_NO_INTERNET: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_NON_REPORTED_BUGS_COUNT: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_REPORT_SUCCESS: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_REPORT_FAILURE: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_REPORT_DELETE: BugReportEvent.BugReportEventType
    BUG_REPORT_EVENT_TYPE_BRT_INITIALIZED: BugReportEvent.BugReportEventType
    BRT_EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CPU_USAGE_FIELD_NUMBER: _ClassVar[int]
    MEMORY_USAGE_FIELD_NUMBER: _ClassVar[int]
    BRT_SDK_VERSION_FIELD_NUMBER: _ClassVar[int]
    brt_event_type: BugReportEvent.BugReportEventType
    cpu_usage: int
    memory_usage: float
    brt_sdk_version: str
    def __init__(self, brt_event_type: _Optional[_Union[BugReportEvent.BugReportEventType, str]] = ..., cpu_usage: _Optional[int] = ..., memory_usage: _Optional[float] = ..., brt_sdk_version: _Optional[str] = ...) -> None: ...
