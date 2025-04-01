from component.content import cta_pb2 as _cta_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettingsOptionNudge(_message.Message):
    __slots__ = ("cta_name", "cta_type", "desired_quality")
    class NudgeDesiredQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NUDGE_DESIRED_QUALITY_UNSPECIFIED: _ClassVar[SettingsOptionNudge.NudgeDesiredQuality]
        NUDGE_DESIRED_QUALITY_4K: _ClassVar[SettingsOptionNudge.NudgeDesiredQuality]
        NUDGE_DESIRED_QUALITY_FHD: _ClassVar[SettingsOptionNudge.NudgeDesiredQuality]
        NUDGE_DESIRED_QUALITY_HD: _ClassVar[SettingsOptionNudge.NudgeDesiredQuality]
        NUDGE_DESIRED_QUALITY_DOLBY_ATMOS: _ClassVar[SettingsOptionNudge.NudgeDesiredQuality]
        NUDGE_DESIRED_QUALITY_DOLBY_51: _ClassVar[SettingsOptionNudge.NudgeDesiredQuality]
    NUDGE_DESIRED_QUALITY_UNSPECIFIED: SettingsOptionNudge.NudgeDesiredQuality
    NUDGE_DESIRED_QUALITY_4K: SettingsOptionNudge.NudgeDesiredQuality
    NUDGE_DESIRED_QUALITY_FHD: SettingsOptionNudge.NudgeDesiredQuality
    NUDGE_DESIRED_QUALITY_HD: SettingsOptionNudge.NudgeDesiredQuality
    NUDGE_DESIRED_QUALITY_DOLBY_ATMOS: SettingsOptionNudge.NudgeDesiredQuality
    NUDGE_DESIRED_QUALITY_DOLBY_51: SettingsOptionNudge.NudgeDesiredQuality
    CTA_NAME_FIELD_NUMBER: _ClassVar[int]
    CTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    DESIRED_QUALITY_FIELD_NUMBER: _ClassVar[int]
    cta_name: str
    cta_type: str
    desired_quality: SettingsOptionNudge.NudgeDesiredQuality
    def __init__(self, cta_name: _Optional[str] = ..., cta_type: _Optional[str] = ..., desired_quality: _Optional[_Union[SettingsOptionNudge.NudgeDesiredQuality, str]] = ...) -> None: ...
