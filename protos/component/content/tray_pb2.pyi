from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TraySource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRAY_SOURCE_UNSPECIFIED: _ClassVar[TraySource]
    TRAY_SOURCE_PERSONA: _ClassVar[TraySource]
    TRAY_SOURCE_CMS: _ClassVar[TraySource]
TRAY_SOURCE_UNSPECIFIED: TraySource
TRAY_SOURCE_PERSONA: TraySource
TRAY_SOURCE_CMS: TraySource

class Tray(_message.Message):
    __slots__ = ("tray_id", "tray_name", "tray_position", "localised_tray_name", "source", "logic", "display_language", "initiation_source")
    TRAY_ID_FIELD_NUMBER: _ClassVar[int]
    TRAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TRAY_POSITION_FIELD_NUMBER: _ClassVar[int]
    LOCALISED_TRAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    INITIATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    tray_id: str
    tray_name: str
    tray_position: int
    localised_tray_name: str
    source: TraySource
    logic: str
    display_language: str
    initiation_source: str
    def __init__(self, tray_id: _Optional[str] = ..., tray_name: _Optional[str] = ..., tray_position: _Optional[int] = ..., localised_tray_name: _Optional[str] = ..., source: _Optional[_Union[TraySource, str]] = ..., logic: _Optional[str] = ..., display_language: _Optional[str] = ..., initiation_source: _Optional[str] = ...) -> None: ...
