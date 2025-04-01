from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SupportedOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALL: _ClassVar[SupportedOrientation]
    PORTRAIT: _ClassVar[SupportedOrientation]
    LANDSCAPE: _ClassVar[SupportedOrientation]

class DurationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHORT: _ClassVar[DurationType]
    MEDIUM: _ClassVar[DurationType]
    LONG: _ClassVar[DurationType]

class ToastType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[ToastType]
    SUCCESS: _ClassVar[ToastType]
    ERROR: _ClassVar[ToastType]
    WARNING: _ClassVar[ToastType]
ALL: SupportedOrientation
PORTRAIT: SupportedOrientation
LANDSCAPE: SupportedOrientation
SHORT: DurationType
MEDIUM: DurationType
LONG: DurationType
UNSPECIFIED: ToastType
SUCCESS: ToastType
ERROR: ToastType
WARNING: ToastType

class ShowToastAction(_message.Message):
    __slots__ = ("message", "duration_type", "cta_label", "supported_orientation", "icon", "toast_type", "local_image")
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DURATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CTA_LABEL_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TOAST_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOCAL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    duration_type: DurationType
    cta_label: str
    supported_orientation: SupportedOrientation
    icon: str
    toast_type: ToastType
    local_image: str
    def __init__(self, message: _Optional[str] = ..., duration_type: _Optional[_Union[DurationType, str]] = ..., cta_label: _Optional[str] = ..., supported_orientation: _Optional[_Union[SupportedOrientation, str]] = ..., icon: _Optional[str] = ..., toast_type: _Optional[_Union[ToastType, str]] = ..., local_image: _Optional[str] = ...) -> None: ...
