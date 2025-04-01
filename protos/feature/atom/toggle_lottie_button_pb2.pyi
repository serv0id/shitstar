from feature.image import lottie_pb2 as _lottie_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToggleLottieButton(_message.Message):
    __slots__ = ("lottie", "initial_actions", "final_actions", "is_final_state", "reverse_lottie")
    LOTTIE_FIELD_NUMBER: _ClassVar[int]
    INITIAL_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    FINAL_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_FINAL_STATE_FIELD_NUMBER: _ClassVar[int]
    REVERSE_LOTTIE_FIELD_NUMBER: _ClassVar[int]
    lottie: _lottie_pb2.Lottie
    initial_actions: _actions_pb2.Actions
    final_actions: _actions_pb2.Actions
    is_final_state: bool
    reverse_lottie: _lottie_pb2.Lottie
    def __init__(self, lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., initial_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., final_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., is_final_state: bool = ..., reverse_lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ...) -> None: ...
