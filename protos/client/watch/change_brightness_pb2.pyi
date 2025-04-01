from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeBrightnessProperties(_message.Message):
    __slots__ = ("previous_brightness_pct", "new_brightness_pct", "change_source")
    class BrightnessSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BRIGHTNESS_SOURCE_UNSPECIFIED: _ClassVar[ChangeBrightnessProperties.BrightnessSource]
        BRIGHTNESS_SOURCE_GESTURE: _ClassVar[ChangeBrightnessProperties.BrightnessSource]
        BRIGHTNESS_SOURCE_VOLUME_BAR: _ClassVar[ChangeBrightnessProperties.BrightnessSource]
        BRIGHTNESS_SOURCE_PHONE: _ClassVar[ChangeBrightnessProperties.BrightnessSource]
        BRIGHTNESS_SOURCE_BRIGHTNESS_BAR: _ClassVar[ChangeBrightnessProperties.BrightnessSource]
    BRIGHTNESS_SOURCE_UNSPECIFIED: ChangeBrightnessProperties.BrightnessSource
    BRIGHTNESS_SOURCE_GESTURE: ChangeBrightnessProperties.BrightnessSource
    BRIGHTNESS_SOURCE_VOLUME_BAR: ChangeBrightnessProperties.BrightnessSource
    BRIGHTNESS_SOURCE_PHONE: ChangeBrightnessProperties.BrightnessSource
    BRIGHTNESS_SOURCE_BRIGHTNESS_BAR: ChangeBrightnessProperties.BrightnessSource
    PREVIOUS_BRIGHTNESS_PCT_FIELD_NUMBER: _ClassVar[int]
    NEW_BRIGHTNESS_PCT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    previous_brightness_pct: int
    new_brightness_pct: int
    change_source: ChangeBrightnessProperties.BrightnessSource
    def __init__(self, previous_brightness_pct: _Optional[int] = ..., new_brightness_pct: _Optional[int] = ..., change_source: _Optional[_Union[ChangeBrightnessProperties.BrightnessSource, str]] = ...) -> None: ...
