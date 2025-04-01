from feature.player import player_settings_type_pb2 as _player_settings_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerControlAction(_message.Message):
    __slots__ = ("params",)
    class ControlType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[PlayerControlAction.ControlType]
        MUTE: _ClassVar[PlayerControlAction.ControlType]
        UN_MUTE: _ClassVar[PlayerControlAction.ControlType]
        LANDSCAPE: _ClassVar[PlayerControlAction.ControlType]
        PORTRAIT: _ClassVar[PlayerControlAction.ControlType]
        LOCK_SCREEN: _ClassVar[PlayerControlAction.ControlType]
        UNLOCK_SCREEN: _ClassVar[PlayerControlAction.ControlType]
        PAUSE: _ClassVar[PlayerControlAction.ControlType]
        RESUME: _ClassVar[PlayerControlAction.ControlType]
    DEFAULT: PlayerControlAction.ControlType
    MUTE: PlayerControlAction.ControlType
    UN_MUTE: PlayerControlAction.ControlType
    LANDSCAPE: PlayerControlAction.ControlType
    PORTRAIT: PlayerControlAction.ControlType
    LOCK_SCREEN: PlayerControlAction.ControlType
    UNLOCK_SCREEN: PlayerControlAction.ControlType
    PAUSE: PlayerControlAction.ControlType
    RESUME: PlayerControlAction.ControlType
    class Params(_message.Message):
        __slots__ = ("change_video_quality_params", "general_player_action", "open_player_settings")
        CHANGE_VIDEO_QUALITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
        GENERAL_PLAYER_ACTION_FIELD_NUMBER: _ClassVar[int]
        OPEN_PLAYER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
        change_video_quality_params: PlayerControlAction.ChangeVideoQualityParams
        general_player_action: PlayerControlAction.GeneralControlParams
        open_player_settings: PlayerControlAction.OpenPlayerSettingsParams
        def __init__(self, change_video_quality_params: _Optional[_Union[PlayerControlAction.ChangeVideoQualityParams, _Mapping]] = ..., general_player_action: _Optional[_Union[PlayerControlAction.GeneralControlParams, _Mapping]] = ..., open_player_settings: _Optional[_Union[PlayerControlAction.OpenPlayerSettingsParams, _Mapping]] = ...) -> None: ...
    class ChangeVideoQualityParams(_message.Message):
        __slots__ = ("video_quality_code",)
        VIDEO_QUALITY_CODE_FIELD_NUMBER: _ClassVar[int]
        video_quality_code: str
        def __init__(self, video_quality_code: _Optional[str] = ...) -> None: ...
    class GeneralControlParams(_message.Message):
        __slots__ = ("type",)
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: PlayerControlAction.ControlType
        def __init__(self, type: _Optional[_Union[PlayerControlAction.ControlType, str]] = ...) -> None: ...
    class OpenPlayerSettingsParams(_message.Message):
        __slots__ = ("types",)
        TYPES_FIELD_NUMBER: _ClassVar[int]
        types: _containers.RepeatedScalarFieldContainer[_player_settings_type_pb2.PlayerSettingsType]
        def __init__(self, types: _Optional[_Iterable[_Union[_player_settings_type_pb2.PlayerSettingsType, str]]] = ...) -> None: ...
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: PlayerControlAction.Params
    def __init__(self, params: _Optional[_Union[PlayerControlAction.Params, _Mapping]] = ...) -> None: ...
