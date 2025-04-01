from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from widget import avatar_pb2 as _avatar_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedCaptionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("caption",)
        CAPTION_FIELD_NUMBER: _ClassVar[int]
        caption: CaptionData
        def __init__(self, caption: _Optional[_Union[CaptionData, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: FeedCaptionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[FeedCaptionWidget.Data, _Mapping]] = ...) -> None: ...

class CaptionData(_message.Message):
    __slots__ = ("profile", "cricket_stat", "avatar")
    PROFILE_FIELD_NUMBER: _ClassVar[int]
    CRICKET_STAT_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    profile: FeedProfile
    cricket_stat: FeedCricketStatistics
    avatar: _avatar_pb2.AvatarWidget
    def __init__(self, profile: _Optional[_Union[FeedProfile, _Mapping]] = ..., cricket_stat: _Optional[_Union[FeedCricketStatistics, _Mapping]] = ..., avatar: _Optional[_Union[_avatar_pb2.AvatarWidget, _Mapping]] = ...) -> None: ...

class FeedProfile(_message.Message):
    __slots__ = ("image", "actions")
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    image: _image_pb2.Image
    actions: _actions_pb2.Actions
    def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...

class FeedCricketStatistics(_message.Message):
    __slots__ = ("over_ball", "score_image", "score_text", "actions")
    OVER_BALL_FIELD_NUMBER: _ClassVar[int]
    SCORE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    SCORE_TEXT_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    over_ball: str
    score_image: _image_pb2.Image
    score_text: str
    actions: _actions_pb2.Actions
    def __init__(self, over_ball: _Optional[str] = ..., score_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., score_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
