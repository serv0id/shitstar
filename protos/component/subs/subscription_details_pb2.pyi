from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionDetails(_message.Message):
    __slots__ = ("plan_name", "plan_ctx")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAN_CTX_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    plan_ctx: str
    def __init__(self, plan_name: _Optional[str] = ..., plan_ctx: _Optional[str] = ...) -> None: ...
