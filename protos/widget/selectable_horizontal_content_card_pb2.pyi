from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SelectableHorizontalContentCardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("id", "thumbnail_image", "title_image", "subtitle_text", "actions", "show_selector", "show_gradient", "lottie", "image", "is_stacked_card_ui", "card_label")
        ID_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_IMAGE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        SHOW_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        SHOW_GRADIENT_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        IS_STACKED_CARD_UI_FIELD_NUMBER: _ClassVar[int]
        CARD_LABEL_FIELD_NUMBER: _ClassVar[int]
        id: str
        thumbnail_image: _image_pb2.Image
        title_image: _image_pb2.Image
        subtitle_text: str
        actions: _actions_pb2.Actions
        show_selector: bool
        show_gradient: bool
        lottie: _lottie_pb2.Lottie
        image: _image_pb2.Image
        is_stacked_card_ui: bool
        card_label: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, id: _Optional[str] = ..., thumbnail_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., subtitle_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., show_selector: bool = ..., show_gradient: bool = ..., lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., is_stacked_card_ui: bool = ..., card_label: _Optional[_Iterable[str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SelectableHorizontalContentCardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SelectableHorizontalContentCardWidget.Data, _Mapping]] = ...) -> None: ...
