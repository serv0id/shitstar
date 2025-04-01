from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationPermission(_message.Message):
    __slots__ = ("source", "changed_to", "category_type", "category_id", "changed_from")
    class PermissionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSION_STATUS_UNSPECIFIED: _ClassVar[NotificationPermission.PermissionStatus]
        PERMISSION_STATUS_DENIED: _ClassVar[NotificationPermission.PermissionStatus]
        PERMISSION_STATUS_GRANTED: _ClassVar[NotificationPermission.PermissionStatus]
        PERMISSION_STATUS_SILENCED: _ClassVar[NotificationPermission.PermissionStatus]
    PERMISSION_STATUS_UNSPECIFIED: NotificationPermission.PermissionStatus
    PERMISSION_STATUS_DENIED: NotificationPermission.PermissionStatus
    PERMISSION_STATUS_GRANTED: NotificationPermission.PermissionStatus
    PERMISSION_STATUS_SILENCED: NotificationPermission.PermissionStatus
    class CategoryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CATEGORY_TYPE_UNSPECIFIED: _ClassVar[NotificationPermission.CategoryType]
        CATEGORY_TYPE_APP: _ClassVar[NotificationPermission.CategoryType]
        CATEGORY_TYPE_CHANNEL: _ClassVar[NotificationPermission.CategoryType]
    CATEGORY_TYPE_UNSPECIFIED: NotificationPermission.CategoryType
    CATEGORY_TYPE_APP: NotificationPermission.CategoryType
    CATEGORY_TYPE_CHANNEL: NotificationPermission.CategoryType
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CHANGED_TO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FROM_FIELD_NUMBER: _ClassVar[int]
    source: str
    changed_to: NotificationPermission.PermissionStatus
    category_type: NotificationPermission.CategoryType
    category_id: str
    changed_from: NotificationPermission.PermissionStatus
    def __init__(self, source: _Optional[str] = ..., changed_to: _Optional[_Union[NotificationPermission.PermissionStatus, str]] = ..., category_type: _Optional[_Union[NotificationPermission.CategoryType, str]] = ..., category_id: _Optional[str] = ..., changed_from: _Optional[_Union[NotificationPermission.PermissionStatus, str]] = ...) -> None: ...
