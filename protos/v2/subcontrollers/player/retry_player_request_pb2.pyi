from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RetryPlayerRequest(_message.Message):
    __slots__ = ("client_capabilities", "drm_parameters")
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    DRM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    client_capabilities: str
    drm_parameters: str
    def __init__(self, client_capabilities: _Optional[str] = ..., drm_parameters: _Optional[str] = ...) -> None: ...
