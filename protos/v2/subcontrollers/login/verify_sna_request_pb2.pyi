from v2.subcontrollers.login import login_device_meta_pb2 as _login_device_meta_pb2
from v2.subcontrollers.login import login_source_pb2 as _login_source_pb2
from v2.subcontrollers.login import consent_status_pb2 as _consent_status_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifySnaRequest(_message.Message):
    __slots__ = ("login_device_meta", "phone_number", "association_key", "country_prefix", "source", "consent_status")
    LOGIN_DEVICE_META_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ASSOCIATION_KEY_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    login_device_meta: _login_device_meta_pb2.LoginDeviceMeta
    phone_number: str
    association_key: str
    country_prefix: str
    source: _login_source_pb2.Source
    consent_status: _consent_status_pb2.ConsentStatus
    def __init__(self, login_device_meta: _Optional[_Union[_login_device_meta_pb2.LoginDeviceMeta, _Mapping]] = ..., phone_number: _Optional[str] = ..., association_key: _Optional[str] = ..., country_prefix: _Optional[str] = ..., source: _Optional[_Union[_login_source_pb2.Source, str]] = ..., consent_status: _Optional[_Union[_consent_status_pb2.ConsentStatus, str]] = ...) -> None: ...
