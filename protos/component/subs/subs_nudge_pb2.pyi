from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubsNudgeProperties(_message.Message):
    __slots__ = ("nudge_layout", "nudge_type")
    class NudgeLayout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NUDGE_LAYOUT_UNSPECIFIED: _ClassVar[SubsNudgeProperties.NudgeLayout]
        NUDGE_LAYOUT_NONE: _ClassVar[SubsNudgeProperties.NudgeLayout]
        NUDGE_LAYOUT_DECOUPLED: _ClassVar[SubsNudgeProperties.NudgeLayout]
        NUDGE_LAYOUT_NESTED: _ClassVar[SubsNudgeProperties.NudgeLayout]
    NUDGE_LAYOUT_UNSPECIFIED: SubsNudgeProperties.NudgeLayout
    NUDGE_LAYOUT_NONE: SubsNudgeProperties.NudgeLayout
    NUDGE_LAYOUT_DECOUPLED: SubsNudgeProperties.NudgeLayout
    NUDGE_LAYOUT_NESTED: SubsNudgeProperties.NudgeLayout
    class NudgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NUDGE_TYPE_UNSPECIFIED: _ClassVar[SubsNudgeProperties.NudgeType]
        NUDGE_TYPE_SUBSCRIBE: _ClassVar[SubsNudgeProperties.NudgeType]
        NUDGE_TYPE_UPGRADE: _ClassVar[SubsNudgeProperties.NudgeType]
    NUDGE_TYPE_UNSPECIFIED: SubsNudgeProperties.NudgeType
    NUDGE_TYPE_SUBSCRIBE: SubsNudgeProperties.NudgeType
    NUDGE_TYPE_UPGRADE: SubsNudgeProperties.NudgeType
    NUDGE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    NUDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    nudge_layout: SubsNudgeProperties.NudgeLayout
    nudge_type: SubsNudgeProperties.NudgeType
    def __init__(self, nudge_layout: _Optional[_Union[SubsNudgeProperties.NudgeLayout, str]] = ..., nudge_type: _Optional[_Union[SubsNudgeProperties.NudgeType, str]] = ...) -> None: ...
