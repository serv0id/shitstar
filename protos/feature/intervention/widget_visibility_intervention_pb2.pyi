from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetVisibilityIntervention(_message.Message):
    __slots__ = ("duration_time_s", "identifier")
    class WidgetIdentifier(_message.Message):
        __slots__ = ("template",)
        TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        template: str
        def __init__(self, template: _Optional[str] = ...) -> None: ...
    DURATION_TIME_S_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    duration_time_s: int
    identifier: WidgetVisibilityIntervention.WidgetIdentifier
    def __init__(self, duration_time_s: _Optional[int] = ..., identifier: _Optional[_Union[WidgetVisibilityIntervention.WidgetIdentifier, _Mapping]] = ...) -> None: ...
