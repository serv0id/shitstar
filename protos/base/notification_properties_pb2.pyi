from base import referrer_properties_pb2 as _referrer_properties_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PushNotificationDialogProperties(_message.Message):
    __slots__ = ("cta_type", "push_type", "referrer_properties")
    class CtaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CTA_UNSPECIFIED: _ClassVar[PushNotificationDialogProperties.CtaType]
        CTA_POSITIVE_CTA: _ClassVar[PushNotificationDialogProperties.CtaType]
        CTA_NEGATIVE_CTA: _ClassVar[PushNotificationDialogProperties.CtaType]
    CTA_UNSPECIFIED: PushNotificationDialogProperties.CtaType
    CTA_POSITIVE_CTA: PushNotificationDialogProperties.CtaType
    CTA_NEGATIVE_CTA: PushNotificationDialogProperties.CtaType
    class PushType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PUSH_UNSPECIFIED: _ClassVar[PushNotificationDialogProperties.PushType]
        PUSH_NOTIFICATION: _ClassVar[PushNotificationDialogProperties.PushType]
        PUSH_SMS: _ClassVar[PushNotificationDialogProperties.PushType]
        PUSH_WHATSAPP: _ClassVar[PushNotificationDialogProperties.PushType]
    PUSH_UNSPECIFIED: PushNotificationDialogProperties.PushType
    PUSH_NOTIFICATION: PushNotificationDialogProperties.PushType
    PUSH_SMS: PushNotificationDialogProperties.PushType
    PUSH_WHATSAPP: PushNotificationDialogProperties.PushType
    CTA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PUSH_TYPE_FIELD_NUMBER: _ClassVar[int]
    REFERRER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    cta_type: PushNotificationDialogProperties.CtaType
    push_type: PushNotificationDialogProperties.PushType
    referrer_properties: _referrer_properties_pb2.ReferrerProperties
    def __init__(self, cta_type: _Optional[_Union[PushNotificationDialogProperties.CtaType, str]] = ..., push_type: _Optional[_Union[PushNotificationDialogProperties.PushType, str]] = ..., referrer_properties: _Optional[_Union[_referrer_properties_pb2.ReferrerProperties, _Mapping]] = ...) -> None: ...
