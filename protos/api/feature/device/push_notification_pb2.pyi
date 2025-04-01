from api.feature.device import platform_pb2 as _platform_pb2
from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PushNotification(_message.Message):
    __slots__ = ("device_token", "permission_status")
    class PermissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSION_STATUS_UNSPECIFIED: _ClassVar[PushNotification.PermissionStatus]
        PERMISSION_STATUS_DENIED: _ClassVar[PushNotification.PermissionStatus]
        PERMISSION_STATUS_GRANTED: _ClassVar[PushNotification.PermissionStatus]
        PERMISSION_STATUS_SILENCED: _ClassVar[PushNotification.PermissionStatus]
    PERMISSION_STATUS_UNSPECIFIED: PushNotification.PermissionStatus
    PERMISSION_STATUS_DENIED: PushNotification.PermissionStatus
    PERMISSION_STATUS_GRANTED: PushNotification.PermissionStatus
    PERMISSION_STATUS_SILENCED: PushNotification.PermissionStatus
    DEVICE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_STATUS_FIELD_NUMBER: _ClassVar[int]
    device_token: str
    permission_status: PushNotification.PermissionStatus
    def __init__(self, device_token: _Optional[str] = ..., permission_status: _Optional[_Union[PushNotification.PermissionStatus, str]] = ...) -> None: ...
