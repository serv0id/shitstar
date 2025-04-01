from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BatteryInfo(_message.Message):
    __slots__ = ("battery_strength_percent", "is_battery_charging", "battery_capacity_mah_current")
    BATTERY_STRENGTH_PERCENT_FIELD_NUMBER: _ClassVar[int]
    IS_BATTERY_CHARGING_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CAPACITY_MAH_CURRENT_FIELD_NUMBER: _ClassVar[int]
    battery_strength_percent: int
    is_battery_charging: bool
    battery_capacity_mah_current: int
    def __init__(self, battery_strength_percent: _Optional[int] = ..., is_battery_charging: bool = ..., battery_capacity_mah_current: _Optional[int] = ...) -> None: ...
