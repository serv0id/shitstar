from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommsPrefUpdateRequest(_message.Message):
    __slots__ = ("preference_id", "preference_type", "status", "preference_version")
    class PreferenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CommsPrefUpdateRequest.PreferenceType]
        PPTOU: _ClassVar[CommsPrefUpdateRequest.PreferenceType]
        NOTIFICATION: _ClassVar[CommsPrefUpdateRequest.PreferenceType]
        SMS: _ClassVar[CommsPrefUpdateRequest.PreferenceType]
        WHATSAPP: _ClassVar[CommsPrefUpdateRequest.PreferenceType]
        EMAIL: _ClassVar[CommsPrefUpdateRequest.PreferenceType]
    UNKNOWN: CommsPrefUpdateRequest.PreferenceType
    PPTOU: CommsPrefUpdateRequest.PreferenceType
    NOTIFICATION: CommsPrefUpdateRequest.PreferenceType
    SMS: CommsPrefUpdateRequest.PreferenceType
    WHATSAPP: CommsPrefUpdateRequest.PreferenceType
    EMAIL: CommsPrefUpdateRequest.PreferenceType
    class PreferenceStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPT_IN: _ClassVar[CommsPrefUpdateRequest.PreferenceStatus]
        OPT_OUT: _ClassVar[CommsPrefUpdateRequest.PreferenceStatus]
    OPT_IN: CommsPrefUpdateRequest.PreferenceStatus
    OPT_OUT: CommsPrefUpdateRequest.PreferenceStatus
    PREFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PREFERENCE_VERSION_FIELD_NUMBER: _ClassVar[int]
    preference_id: str
    preference_type: CommsPrefUpdateRequest.PreferenceType
    status: CommsPrefUpdateRequest.PreferenceStatus
    preference_version: int
    def __init__(self, preference_id: _Optional[str] = ..., preference_type: _Optional[_Union[CommsPrefUpdateRequest.PreferenceType, str]] = ..., status: _Optional[_Union[CommsPrefUpdateRequest.PreferenceStatus, str]] = ..., preference_version: _Optional[int] = ...) -> None: ...
