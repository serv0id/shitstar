from feature.payment import payment_status_track_meta_pb2 as _payment_status_track_meta_pb2
from feature.gtm_event import login_success_track_meta_pb2 as _login_success_track_meta_pb2
from feature.gtm_event import ecommerce_events_track_meta_pb2 as _ecommerce_events_track_meta_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GTMTrackAction(_message.Message):
    __slots__ = ("event_name", "payment_status_gtm_meta", "login_success_gtm_meta", "ecommerce_events_gtm_meta")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_STATUS_GTM_META_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SUCCESS_GTM_META_FIELD_NUMBER: _ClassVar[int]
    ECOMMERCE_EVENTS_GTM_META_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    payment_status_gtm_meta: _payment_status_track_meta_pb2.PaymentStatusTrackMeta
    login_success_gtm_meta: _login_success_track_meta_pb2.LoginSuccessTrackMeta
    ecommerce_events_gtm_meta: _ecommerce_events_track_meta_pb2.EcommerceEventsTrackMeta
    def __init__(self, event_name: _Optional[str] = ..., payment_status_gtm_meta: _Optional[_Union[_payment_status_track_meta_pb2.PaymentStatusTrackMeta, _Mapping]] = ..., login_success_gtm_meta: _Optional[_Union[_login_success_track_meta_pb2.LoginSuccessTrackMeta, _Mapping]] = ..., ecommerce_events_gtm_meta: _Optional[_Union[_ecommerce_events_track_meta_pb2.EcommerceEventsTrackMeta, _Mapping]] = ...) -> None: ...
