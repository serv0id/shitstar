from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipActionsClickDetails(_message.Message):
    __slots__ = ("action_type", "plan_name")
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    action_type: str
    plan_name: str
    def __init__(self, action_type: _Optional[str] = ..., plan_name: _Optional[str] = ...) -> None: ...
