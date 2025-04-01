from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentOnboardingWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "subtitle", "subtitle_description", "minimum_selected", "submit_button", "skip_cta", "cards", "next_content_items_url")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        MINIMUM_SELECTED_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SKIP_CTA_FIELD_NUMBER: _ClassVar[int]
        CARDS_FIELD_NUMBER: _ClassVar[int]
        NEXT_CONTENT_ITEMS_URL_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        subtitle_description: str
        minimum_selected: int
        submit_button: ContentOnboardingWidget.SubmitButton
        skip_cta: ContentOnboardingWidget.SkipCTA
        cards: _containers.RepeatedCompositeFieldContainer[ContentOnboardingWidget.Card]
        next_content_items_url: str
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., subtitle_description: _Optional[str] = ..., minimum_selected: _Optional[int] = ..., submit_button: _Optional[_Union[ContentOnboardingWidget.SubmitButton, _Mapping]] = ..., skip_cta: _Optional[_Union[ContentOnboardingWidget.SkipCTA, _Mapping]] = ..., cards: _Optional[_Iterable[_Union[ContentOnboardingWidget.Card, _Mapping]]] = ..., next_content_items_url: _Optional[str] = ...) -> None: ...
    class SkipCTA(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class SubmitButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Card(_message.Message):
        __slots__ = ("content_id", "image", "actions")
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        content_id: str
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        def __init__(self, content_id: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ContentOnboardingWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ContentOnboardingWidget.Data, _Mapping]] = ...) -> None: ...
