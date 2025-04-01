from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionAction(_message.Message):
    __slots__ = ("action_type",)
    class SubscriptionActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUBSCRIPTION_ACTION_TYPE_UNSPECIFIED: _ClassVar[SubscriptionAction.SubscriptionActionType]
        SUBSCRIPTION_ACTION_TYPE_SUBSCRIBE: _ClassVar[SubscriptionAction.SubscriptionActionType]
        SUBSCRIPTION_ACTION_TYPE_UNSUBSCRIBE: _ClassVar[SubscriptionAction.SubscriptionActionType]
    SUBSCRIPTION_ACTION_TYPE_UNSPECIFIED: SubscriptionAction.SubscriptionActionType
    SUBSCRIPTION_ACTION_TYPE_SUBSCRIBE: SubscriptionAction.SubscriptionActionType
    SUBSCRIPTION_ACTION_TYPE_UNSUBSCRIBE: SubscriptionAction.SubscriptionActionType
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    action_type: SubscriptionAction.SubscriptionActionType
    def __init__(self, action_type: _Optional[_Union[SubscriptionAction.SubscriptionActionType, str]] = ...) -> None: ...
