from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelSubscriptionAction(_message.Message):
    __slots__ = ("cancel_api", "sdk_navigation")
    class CancelApi(_message.Message):
        __slots__ = ("commercial_pack_id", "message")
        COMMERCIAL_PACK_ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        commercial_pack_id: str
        message: CancelSubscriptionAction.MessageOnCancel
        def __init__(self, commercial_pack_id: _Optional[str] = ..., message: _Optional[_Union[CancelSubscriptionAction.MessageOnCancel, _Mapping]] = ...) -> None: ...
    class MessageOnCancel(_message.Message):
        __slots__ = ("success_msg", "failure_msg")
        SUCCESS_MSG_FIELD_NUMBER: _ClassVar[int]
        FAILURE_MSG_FIELD_NUMBER: _ClassVar[int]
        success_msg: str
        failure_msg: str
        def __init__(self, success_msg: _Optional[str] = ..., failure_msg: _Optional[str] = ...) -> None: ...
    class SdkNavigation(_message.Message):
        __slots__ = ("commercial_pack_id",)
        COMMERCIAL_PACK_ID_FIELD_NUMBER: _ClassVar[int]
        commercial_pack_id: str
        def __init__(self, commercial_pack_id: _Optional[str] = ...) -> None: ...
    CANCEL_API_FIELD_NUMBER: _ClassVar[int]
    SDK_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
    cancel_api: CancelSubscriptionAction.CancelApi
    sdk_navigation: CancelSubscriptionAction.SdkNavigation
    def __init__(self, cancel_api: _Optional[_Union[CancelSubscriptionAction.CancelApi, _Mapping]] = ..., sdk_navigation: _Optional[_Union[CancelSubscriptionAction.SdkNavigation, _Mapping]] = ...) -> None: ...
