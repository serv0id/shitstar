from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MaturitySelectionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("desc", "first_profile_label", "ratings", "selected_rating_id", "highest_kids_rating", "non_kids_rating_selection_message", "kids_mode_auto_toggle_message")
        DESC_FIELD_NUMBER: _ClassVar[int]
        FIRST_PROFILE_LABEL_FIELD_NUMBER: _ClassVar[int]
        RATINGS_FIELD_NUMBER: _ClassVar[int]
        SELECTED_RATING_ID_FIELD_NUMBER: _ClassVar[int]
        HIGHEST_KIDS_RATING_FIELD_NUMBER: _ClassVar[int]
        NON_KIDS_RATING_SELECTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        KIDS_MODE_AUTO_TOGGLE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        desc: str
        first_profile_label: str
        ratings: _containers.RepeatedCompositeFieldContainer[MaturitySelectionWidget.Rating]
        selected_rating_id: str
        highest_kids_rating: str
        non_kids_rating_selection_message: str
        kids_mode_auto_toggle_message: str
        def __init__(self, desc: _Optional[str] = ..., first_profile_label: _Optional[str] = ..., ratings: _Optional[_Iterable[_Union[MaturitySelectionWidget.Rating, _Mapping]]] = ..., selected_rating_id: _Optional[str] = ..., highest_kids_rating: _Optional[str] = ..., non_kids_rating_selection_message: _Optional[str] = ..., kids_mode_auto_toggle_message: _Optional[str] = ...) -> None: ...
    class Rating(_message.Message):
        __slots__ = ("id", "title", "desc", "display_text", "title_text")
        ID_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
        TITLE_TEXT_FIELD_NUMBER: _ClassVar[int]
        id: str
        title: str
        desc: str
        display_text: str
        title_text: str
        def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., display_text: _Optional[str] = ..., title_text: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MaturitySelectionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MaturitySelectionWidget.Data, _Mapping]] = ...) -> None: ...
