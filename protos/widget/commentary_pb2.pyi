from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommentaryWidget(_message.Message):
    __slots__ = ("text_commentary", "lottie_commentary")
    TEXT_COMMENTARY_FIELD_NUMBER: _ClassVar[int]
    LOTTIE_COMMENTARY_FIELD_NUMBER: _ClassVar[int]
    text_commentary: TextCommentaryWidget
    lottie_commentary: LottieCommentaryWidget
    def __init__(self, text_commentary: _Optional[_Union[TextCommentaryWidget, _Mapping]] = ..., lottie_commentary: _Optional[_Union[LottieCommentaryWidget, _Mapping]] = ...) -> None: ...

class TextCommentaryWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("commentary", "actions")
        COMMENTARY_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        commentary: str
        actions: _actions_pb2.Actions
        def __init__(self, commentary: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TextCommentaryWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TextCommentaryWidget.Data, _Mapping]] = ...) -> None: ...

class LottieCommentaryWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("placeholder_text", "lottie", "actions")
        PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        placeholder_text: str
        lottie: _lottie_pb2.Lottie
        actions: _actions_pb2.Actions
        def __init__(self, placeholder_text: _Optional[str] = ..., lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LottieCommentaryWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LottieCommentaryWidget.Data, _Mapping]] = ...) -> None: ...
