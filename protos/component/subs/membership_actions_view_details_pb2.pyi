from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipActionsViewDetails(_message.Message):
    __slots__ = ("plan_names", "membership_actions_view_details")
    PLAN_NAMES_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_ACTIONS_VIEW_DETAILS_FIELD_NUMBER: _ClassVar[int]
    plan_names: _containers.RepeatedScalarFieldContainer[str]
    membership_actions_view_details: _containers.RepeatedCompositeFieldContainer[MembershipActionsViewDetail]
    def __init__(self, plan_names: _Optional[_Iterable[str]] = ..., membership_actions_view_details: _Optional[_Iterable[_Union[MembershipActionsViewDetail, _Mapping]]] = ...) -> None: ...

class MembershipActionsViewDetail(_message.Message):
    __slots__ = ("plan_name", "actions_types")
    PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_TYPES_FIELD_NUMBER: _ClassVar[int]
    plan_name: str
    actions_types: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, plan_name: _Optional[str] = ..., actions_types: _Optional[_Iterable[str]] = ...) -> None: ...
