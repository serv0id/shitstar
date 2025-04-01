from feature.tooltip import arrow_alignment_pb2 as _arrow_alignment_pb2
from feature.tooltip import content_spread_pb2 as _content_spread_pb2
from feature.tooltip import arrow_position_pb2 as _arrow_position_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowTooltipAction(_message.Message):
    __slots__ = ("message", "preferred_arrow_alignment", "content_spread", "arrow_position", "data", "tooltip_type")
    class TooltipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ShowTooltipAction.TooltipType]
        TEXT: _ClassVar[ShowTooltipAction.TooltipType]
        USER_REACTIONS: _ClassVar[ShowTooltipAction.TooltipType]
    DEFAULT: ShowTooltipAction.TooltipType
    TEXT: ShowTooltipAction.TooltipType
    USER_REACTIONS: ShowTooltipAction.TooltipType
    class Data(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_ARROW_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SPREAD_FIELD_NUMBER: _ClassVar[int]
    ARROW_POSITION_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TOOLTIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    message: str
    preferred_arrow_alignment: _arrow_alignment_pb2.ArrowAlignment
    content_spread: _content_spread_pb2.ContentSpread
    arrow_position: _arrow_position_pb2.ArrowPosition
    data: ShowTooltipAction.Data
    tooltip_type: ShowTooltipAction.TooltipType
    def __init__(self, message: _Optional[str] = ..., preferred_arrow_alignment: _Optional[_Union[_arrow_alignment_pb2.ArrowAlignment, str]] = ..., content_spread: _Optional[_Union[_content_spread_pb2.ContentSpread, str]] = ..., arrow_position: _Optional[_Union[_arrow_position_pb2.ArrowPosition, str]] = ..., data: _Optional[_Union[ShowTooltipAction.Data, _Mapping]] = ..., tooltip_type: _Optional[_Union[ShowTooltipAction.TooltipType, str]] = ...) -> None: ...
