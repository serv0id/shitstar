from options import opts_pb2 as _opts_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ("session_id", "campaign", "ts_session_start_ms", "appsuite_id", "appsuite_type", "seo_referrer")
    class SessionIdentifier(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Campaign(_message.Message):
        __slots__ = ("name", "source", "medium", "term", "content")
        NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        MEDIUM_FIELD_NUMBER: _ClassVar[int]
        TERM_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        name: str
        source: str
        medium: str
        term: str
        content: str
        def __init__(self, name: _Optional[str] = ..., source: _Optional[str] = ..., medium: _Optional[str] = ..., term: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CAMPAIGN_FIELD_NUMBER: _ClassVar[int]
    TS_SESSION_START_MS_FIELD_NUMBER: _ClassVar[int]
    APPSUITE_ID_FIELD_NUMBER: _ClassVar[int]
    APPSUITE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEO_REFERRER_FIELD_NUMBER: _ClassVar[int]
    session_id: Session.SessionIdentifier
    campaign: Session.Campaign
    ts_session_start_ms: int
    appsuite_id: str
    appsuite_type: str
    seo_referrer: str
    def __init__(self, session_id: _Optional[_Union[Session.SessionIdentifier, _Mapping]] = ..., campaign: _Optional[_Union[Session.Campaign, _Mapping]] = ..., ts_session_start_ms: _Optional[int] = ..., appsuite_id: _Optional[str] = ..., appsuite_type: _Optional[str] = ..., seo_referrer: _Optional[str] = ...) -> None: ...
