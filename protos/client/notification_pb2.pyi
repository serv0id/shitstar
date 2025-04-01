from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationRenderState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOTIFICATION_RENDER_STATE_UNSPECIFIED: _ClassVar[NotificationRenderState]
    NOTIFICATION_RENDER_STATE_SUCCESS: _ClassVar[NotificationRenderState]
    NOTIFICATION_RENDER_STATE_DISCARD_DUPLICATE_PN_SENT_TIME: _ClassVar[NotificationRenderState]
    NOTIFICATION_RENDER_STATE_DISCARD_PID_MIS_MATCH: _ClassVar[NotificationRenderState]
    NOTIFICATION_RENDER_STATE_DISCARD_SAME_CONTENT_IS_PLAYING: _ClassVar[NotificationRenderState]
    NOTIFICATION_RENDER_STATE_DISCARD_APP_PN_PERMISSION_DENIED: _ClassVar[NotificationRenderState]
    NOTIFICATION_RENDER_STATE_DISCARD_PN_CHANNEL_PERMISSION_DENIED: _ClassVar[NotificationRenderState]
NOTIFICATION_RENDER_STATE_UNSPECIFIED: NotificationRenderState
NOTIFICATION_RENDER_STATE_SUCCESS: NotificationRenderState
NOTIFICATION_RENDER_STATE_DISCARD_DUPLICATE_PN_SENT_TIME: NotificationRenderState
NOTIFICATION_RENDER_STATE_DISCARD_PID_MIS_MATCH: NotificationRenderState
NOTIFICATION_RENDER_STATE_DISCARD_SAME_CONTENT_IS_PLAYING: NotificationRenderState
NOTIFICATION_RENDER_STATE_DISCARD_APP_PN_PERMISSION_DENIED: NotificationRenderState
NOTIFICATION_RENDER_STATE_DISCARD_PN_CHANNEL_PERMISSION_DENIED: NotificationRenderState

class Notification(_message.Message):
    __slots__ = ("uri", "campaign_id", "notification_render_state", "ts_pt_timer_end_ms", "is_staggered")
    URI_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    NOTIFICATION_RENDER_STATE_FIELD_NUMBER: _ClassVar[int]
    TS_PT_TIMER_END_MS_FIELD_NUMBER: _ClassVar[int]
    IS_STAGGERED_FIELD_NUMBER: _ClassVar[int]
    uri: str
    campaign_id: str
    notification_render_state: NotificationRenderState
    ts_pt_timer_end_ms: int
    is_staggered: bool
    def __init__(self, uri: _Optional[str] = ..., campaign_id: _Optional[str] = ..., notification_render_state: _Optional[_Union[NotificationRenderState, str]] = ..., ts_pt_timer_end_ms: _Optional[int] = ..., is_staggered: bool = ...) -> None: ...
