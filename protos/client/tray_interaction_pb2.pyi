from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrayInteractionProperties(_message.Message):
    __slots__ = ("tray_interaction_effect", "tray_interaction_trigger_type")
    class TrayInteractionEffect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRAY_INTERACTION_EFFECT_UNSPECIFIED: _ClassVar[TrayInteractionProperties.TrayInteractionEffect]
        TRAY_INTERACTION_EFFECT_COLLAPSED: _ClassVar[TrayInteractionProperties.TrayInteractionEffect]
        TRAY_INTERACTION_EFFECT_UNCOLLAPSED: _ClassVar[TrayInteractionProperties.TrayInteractionEffect]
    TRAY_INTERACTION_EFFECT_UNSPECIFIED: TrayInteractionProperties.TrayInteractionEffect
    TRAY_INTERACTION_EFFECT_COLLAPSED: TrayInteractionProperties.TrayInteractionEffect
    TRAY_INTERACTION_EFFECT_UNCOLLAPSED: TrayInteractionProperties.TrayInteractionEffect
    class TrayInteractionTriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRAY_INTERACTION_TRIGGER_TYPE_UNSPECIFIED: _ClassVar[TrayInteractionProperties.TrayInteractionTriggerType]
        TRAY_INTERACTION_TRIGGER_TYPE_CLICK_CARET: _ClassVar[TrayInteractionProperties.TrayInteractionTriggerType]
        TRAY_INTERACTION_TRIGGER_TYPE_TAP_OUTSIDE: _ClassVar[TrayInteractionProperties.TrayInteractionTriggerType]
    TRAY_INTERACTION_TRIGGER_TYPE_UNSPECIFIED: TrayInteractionProperties.TrayInteractionTriggerType
    TRAY_INTERACTION_TRIGGER_TYPE_CLICK_CARET: TrayInteractionProperties.TrayInteractionTriggerType
    TRAY_INTERACTION_TRIGGER_TYPE_TAP_OUTSIDE: TrayInteractionProperties.TrayInteractionTriggerType
    TRAY_INTERACTION_EFFECT_FIELD_NUMBER: _ClassVar[int]
    TRAY_INTERACTION_TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    tray_interaction_effect: TrayInteractionProperties.TrayInteractionEffect
    tray_interaction_trigger_type: TrayInteractionProperties.TrayInteractionTriggerType
    def __init__(self, tray_interaction_effect: _Optional[_Union[TrayInteractionProperties.TrayInteractionEffect, str]] = ..., tray_interaction_trigger_type: _Optional[_Union[TrayInteractionProperties.TrayInteractionTriggerType, str]] = ...) -> None: ...
