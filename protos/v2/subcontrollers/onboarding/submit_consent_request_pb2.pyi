from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmitConsentRequest(_message.Message):
    __slots__ = ("consent_details", "device_ids", "device_meta")
    class ConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPT_IN: _ClassVar[SubmitConsentRequest.ConsentStatus]
        OPT_OUT: _ClassVar[SubmitConsentRequest.ConsentStatus]
    OPT_IN: SubmitConsentRequest.ConsentStatus
    OPT_OUT: SubmitConsentRequest.ConsentStatus
    class DeviceIdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AD_ID: _ClassVar[SubmitConsentRequest.DeviceIdType]
        ANDROID_ID: _ClassVar[SubmitConsentRequest.DeviceIdType]
        UUID: _ClassVar[SubmitConsentRequest.DeviceIdType]
        DEVICE_ID: _ClassVar[SubmitConsentRequest.DeviceIdType]
    AD_ID: SubmitConsentRequest.DeviceIdType
    ANDROID_ID: SubmitConsentRequest.DeviceIdType
    UUID: SubmitConsentRequest.DeviceIdType
    DEVICE_ID: SubmitConsentRequest.DeviceIdType
    class ConsentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[SubmitConsentRequest.ConsentType]
        PPTOU: _ClassVar[SubmitConsentRequest.ConsentType]
        NOTIFICATION: _ClassVar[SubmitConsentRequest.ConsentType]
        SMS: _ClassVar[SubmitConsentRequest.ConsentType]
        WHATSAPP: _ClassVar[SubmitConsentRequest.ConsentType]
        EMAIL: _ClassVar[SubmitConsentRequest.ConsentType]
        DIRECT_MARKETING: _ClassVar[SubmitConsentRequest.ConsentType]
    UNKNOWN: SubmitConsentRequest.ConsentType
    PPTOU: SubmitConsentRequest.ConsentType
    NOTIFICATION: SubmitConsentRequest.ConsentType
    SMS: SubmitConsentRequest.ConsentType
    WHATSAPP: SubmitConsentRequest.ConsentType
    EMAIL: SubmitConsentRequest.ConsentType
    DIRECT_MARKETING: SubmitConsentRequest.ConsentType
    class ConsentDetails(_message.Message):
        __slots__ = ("consent_id", "consent_type", "status", "consent_version")
        CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
        CONSENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CONSENT_VERSION_FIELD_NUMBER: _ClassVar[int]
        consent_id: str
        consent_type: SubmitConsentRequest.ConsentType
        status: SubmitConsentRequest.ConsentStatus
        consent_version: int
        def __init__(self, consent_id: _Optional[str] = ..., consent_type: _Optional[_Union[SubmitConsentRequest.ConsentType, str]] = ..., status: _Optional[_Union[SubmitConsentRequest.ConsentStatus, str]] = ..., consent_version: _Optional[int] = ...) -> None: ...
    class DeviceId(_message.Message):
        __slots__ = ("id", "type")
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: SubmitConsentRequest.DeviceIdType
        def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[SubmitConsentRequest.DeviceIdType, str]] = ...) -> None: ...
    class DeviceMeta(_message.Message):
        __slots__ = ("network_operator", "os_name", "os_version")
        NETWORK_OPERATOR_FIELD_NUMBER: _ClassVar[int]
        OS_NAME_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        network_operator: str
        os_name: str
        os_version: str
        def __init__(self, network_operator: _Optional[str] = ..., os_name: _Optional[str] = ..., os_version: _Optional[str] = ...) -> None: ...
    CONSENT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
    DEVICE_META_FIELD_NUMBER: _ClassVar[int]
    consent_details: SubmitConsentRequest.ConsentDetails
    device_ids: _containers.RepeatedCompositeFieldContainer[SubmitConsentRequest.DeviceId]
    device_meta: SubmitConsentRequest.DeviceMeta
    def __init__(self, consent_details: _Optional[_Union[SubmitConsentRequest.ConsentDetails, _Mapping]] = ..., device_ids: _Optional[_Iterable[_Union[SubmitConsentRequest.DeviceId, _Mapping]]] = ..., device_meta: _Optional[_Union[SubmitConsentRequest.DeviceMeta, _Mapping]] = ...) -> None: ...
