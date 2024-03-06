from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerControlAction(_message.Message):
    __slots__ = ["params"]
    class Params(_message.Message):
        __slots__ = ["change_video_quality_params"]
        CHANGE_VIDEO_QUALITY_PARAMS_FIELD_NUMBER: _ClassVar[int]
        change_video_quality_params: PlayerControlAction.ChangeVideoQualityParams
        def __init__(self, change_video_quality_params: _Optional[_Union[PlayerControlAction.ChangeVideoQualityParams, _Mapping]] = ...) -> None: ...
    class ChangeVideoQualityParams(_message.Message):
        __slots__ = ["video_quality_code"]
        VIDEO_QUALITY_CODE_FIELD_NUMBER: _ClassVar[int]
        video_quality_code: str
        def __init__(self, video_quality_code: _Optional[str] = ...) -> None: ...
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    params: PlayerControlAction.Params
    def __init__(self, params: _Optional[_Union[PlayerControlAction.Params, _Mapping]] = ...) -> None: ...
