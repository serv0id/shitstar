from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OptionActionProperties(_message.Message):
    __slots__ = ("action_type", "action_component_id", "action_component_position")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_COMPONENT_ID_FIELD_NUMBER: _ClassVar[int]
    ACTION_COMPONENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    action_type: str
    action_component_id: str
    action_component_position: int
    def __init__(self, action_type: _Optional[str] = ..., action_component_id: _Optional[str] = ..., action_component_position: _Optional[int] = ...) -> None: ...
