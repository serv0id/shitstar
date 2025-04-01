from client import orientation_pb2 as _orientation_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppState(_message.Message):
    __slots__ = ("battery_is_charging", "is_device_rooted", "permission_os", "step", "step_status", "start_type", "app_state_when_app_closed", "referral", "time", "heap_memory_used_bytes", "heap_memory_available_bytes", "app_orientation")
    class StartType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        START_TYPE_UNSPECIFIED: _ClassVar[AppState.StartType]
        START_TYPE_COLD: _ClassVar[AppState.StartType]
        START_TYPE_WARM: _ClassVar[AppState.StartType]
        START_TYPE_HOT: _ClassVar[AppState.StartType]
    START_TYPE_UNSPECIFIED: AppState.StartType
    START_TYPE_COLD: AppState.StartType
    START_TYPE_WARM: AppState.StartType
    START_TYPE_HOT: AppState.StartType
    BATTERY_IS_CHARGING_FIELD_NUMBER: _ClassVar[int]
    IS_DEVICE_ROOTED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_OS_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    STEP_STATUS_FIELD_NUMBER: _ClassVar[int]
    START_TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_STATE_WHEN_APP_CLOSED_FIELD_NUMBER: _ClassVar[int]
    REFERRAL_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    HEAP_MEMORY_USED_BYTES_FIELD_NUMBER: _ClassVar[int]
    HEAP_MEMORY_AVAILABLE_BYTES_FIELD_NUMBER: _ClassVar[int]
    APP_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    battery_is_charging: bool
    is_device_rooted: bool
    permission_os: bool
    step: str
    step_status: str
    start_type: AppState.StartType
    app_state_when_app_closed: str
    referral: str
    time: int
    heap_memory_used_bytes: float
    heap_memory_available_bytes: float
    app_orientation: _orientation_pb2.Orientation
    def __init__(self, battery_is_charging: bool = ..., is_device_rooted: bool = ..., permission_os: bool = ..., step: _Optional[str] = ..., step_status: _Optional[str] = ..., start_type: _Optional[_Union[AppState.StartType, str]] = ..., app_state_when_app_closed: _Optional[str] = ..., referral: _Optional[str] = ..., time: _Optional[int] = ..., heap_memory_used_bytes: _Optional[float] = ..., heap_memory_available_bytes: _Optional[float] = ..., app_orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ...) -> None: ...
