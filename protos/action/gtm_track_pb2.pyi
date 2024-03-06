from feature.payment import payment_status_track_meta_pb2 as _payment_status_track_meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GTMTrackAction(_message.Message):
    __slots__ = ["event_name", "payment_status_gtm_meta"]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_STATUS_GTM_META_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    payment_status_gtm_meta: _payment_status_track_meta_pb2.PaymentStatusTrackMeta
    def __init__(self, event_name: _Optional[str] = ..., payment_status_gtm_meta: _Optional[_Union[_payment_status_track_meta_pb2.PaymentStatusTrackMeta, _Mapping]] = ...) -> None: ...
