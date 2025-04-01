from feature.model import app_permission_pb2 as _app_permission_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RedirectToDeviceSettingsAction(_message.Message):
    __slots__ = ("app_permission", "trigger_source")
    APP_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    app_permission: _app_permission_pb2.AppPermission
    trigger_source: str
    def __init__(self, app_permission: _Optional[_Union[_app_permission_pb2.AppPermission, str]] = ..., trigger_source: _Optional[str] = ...) -> None: ...
