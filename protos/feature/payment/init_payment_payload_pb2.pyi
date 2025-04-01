from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitPaymentPayload(_message.Message):
    __slots__ = ("paymentMode", "pgName", "paymentProcessor", "paymentType", "subscriptionPack", "pgParams", "city", "state", "zip", "returnUrl", "user_segments", "promoCode", "abTags", "deviceId", "phoneNumber", "userJourneyContext", "fname", "lname", "bankCode")
    class PgParams(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PAYMENTMODE_FIELD_NUMBER: _ClassVar[int]
    PGNAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENTPROCESSOR_FIELD_NUMBER: _ClassVar[int]
    PAYMENTTYPE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONPACK_FIELD_NUMBER: _ClassVar[int]
    PGPARAMS_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ZIP_FIELD_NUMBER: _ClassVar[int]
    RETURNURL_FIELD_NUMBER: _ClassVar[int]
    USER_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    PROMOCODE_FIELD_NUMBER: _ClassVar[int]
    ABTAGS_FIELD_NUMBER: _ClassVar[int]
    DEVICEID_FIELD_NUMBER: _ClassVar[int]
    PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    USERJOURNEYCONTEXT_FIELD_NUMBER: _ClassVar[int]
    FNAME_FIELD_NUMBER: _ClassVar[int]
    LNAME_FIELD_NUMBER: _ClassVar[int]
    BANKCODE_FIELD_NUMBER: _ClassVar[int]
    paymentMode: str
    pgName: str
    paymentProcessor: str
    paymentType: str
    subscriptionPack: str
    pgParams: _containers.RepeatedCompositeFieldContainer[InitPaymentPayload.PgParams]
    city: str
    state: str
    zip: str
    returnUrl: str
    user_segments: _containers.RepeatedScalarFieldContainer[str]
    promoCode: str
    abTags: _containers.RepeatedScalarFieldContainer[str]
    deviceId: str
    phoneNumber: str
    userJourneyContext: str
    fname: str
    lname: str
    bankCode: str
    def __init__(self, paymentMode: _Optional[str] = ..., pgName: _Optional[str] = ..., paymentProcessor: _Optional[str] = ..., paymentType: _Optional[str] = ..., subscriptionPack: _Optional[str] = ..., pgParams: _Optional[_Iterable[_Union[InitPaymentPayload.PgParams, _Mapping]]] = ..., city: _Optional[str] = ..., state: _Optional[str] = ..., zip: _Optional[str] = ..., returnUrl: _Optional[str] = ..., user_segments: _Optional[_Iterable[str]] = ..., promoCode: _Optional[str] = ..., abTags: _Optional[_Iterable[str]] = ..., deviceId: _Optional[str] = ..., phoneNumber: _Optional[str] = ..., userJourneyContext: _Optional[str] = ..., fname: _Optional[str] = ..., lname: _Optional[str] = ..., bankCode: _Optional[str] = ...) -> None: ...
