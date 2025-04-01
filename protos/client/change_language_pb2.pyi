from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeLanguageProperties(_message.Message):
    __slots__ = ("change_method", "previous_language", "new_language", "previous_language_logic", "player_orientation", "is_casting", "player_version")
    class ChangeMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHANGE_METHOD_UNSPECIFIED: _ClassVar[ChangeLanguageProperties.ChangeMethod]
        CHANGE_METHOD_PLAYER_SETTING: _ClassVar[ChangeLanguageProperties.ChangeMethod]
        CHANGE_METHOD_PLAYER_OVERLAY: _ClassVar[ChangeLanguageProperties.ChangeMethod]
        CHANGE_METHOD_PLAYER_DETAILS_AUDIO_SELECTION: _ClassVar[ChangeLanguageProperties.ChangeMethod]
    CHANGE_METHOD_UNSPECIFIED: ChangeLanguageProperties.ChangeMethod
    CHANGE_METHOD_PLAYER_SETTING: ChangeLanguageProperties.ChangeMethod
    CHANGE_METHOD_PLAYER_OVERLAY: ChangeLanguageProperties.ChangeMethod
    CHANGE_METHOD_PLAYER_DETAILS_AUDIO_SELECTION: ChangeLanguageProperties.ChangeMethod
    class LanguageLogic(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LANGUAGE_LOGIC_UNSPECIFIED: _ClassVar[ChangeLanguageProperties.LanguageLogic]
        LANGUAGE_LOGIC_LPV: _ClassVar[ChangeLanguageProperties.LanguageLogic]
        LANGUAGE_LOGIC_LAST_WATCHED_LANGUAGE: _ClassVar[ChangeLanguageProperties.LanguageLogic]
        LANGUAGE_LOGIC_USER_SELECTION_PREVIOUS_CONTENT: _ClassVar[ChangeLanguageProperties.LanguageLogic]
        LANGUAGE_LOGIC_USER_SELECTION_CURRENT_CONTENT: _ClassVar[ChangeLanguageProperties.LanguageLogic]
    LANGUAGE_LOGIC_UNSPECIFIED: ChangeLanguageProperties.LanguageLogic
    LANGUAGE_LOGIC_LPV: ChangeLanguageProperties.LanguageLogic
    LANGUAGE_LOGIC_LAST_WATCHED_LANGUAGE: ChangeLanguageProperties.LanguageLogic
    LANGUAGE_LOGIC_USER_SELECTION_PREVIOUS_CONTENT: ChangeLanguageProperties.LanguageLogic
    LANGUAGE_LOGIC_USER_SELECTION_CURRENT_CONTENT: ChangeLanguageProperties.LanguageLogic
    CHANGE_METHOD_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NEW_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_LANGUAGE_LOGIC_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    change_method: ChangeLanguageProperties.ChangeMethod
    previous_language: str
    new_language: str
    previous_language_logic: ChangeLanguageProperties.LanguageLogic
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    is_casting: bool
    player_version: str
    def __init__(self, change_method: _Optional[_Union[ChangeLanguageProperties.ChangeMethod, str]] = ..., previous_language: _Optional[str] = ..., new_language: _Optional[str] = ..., previous_language_logic: _Optional[_Union[ChangeLanguageProperties.LanguageLogic, str]] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., is_casting: bool = ..., player_version: _Optional[str] = ...) -> None: ...
