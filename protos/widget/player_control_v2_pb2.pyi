from base import widget_commons_pb2 as _widget_commons_pb2
from base import orientation_pb2 as _orientation_pb2
from feature.commons import alignment_pb2 as _alignment_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.atom import toggle_button_pb2 as _toggle_button_pb2
from feature.atom import toggle_lottie_button_pb2 as _toggle_lottie_button_pb2
from feature.atom import event_observer_button_pb2 as _event_observer_button_pb2
from feature.text import text_pb2 as _text_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerControlV2Widget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("content_header", "settings", "sticky_header")
        CONTENT_HEADER_FIELD_NUMBER: _ClassVar[int]
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        STICKY_HEADER_FIELD_NUMBER: _ClassVar[int]
        content_header: PlayerControlV2Widget.ContentHeader
        settings: PlayerControlV2Widget.Settings
        sticky_header: PlayerControlV2Widget.ContentHeader
        def __init__(self, content_header: _Optional[_Union[PlayerControlV2Widget.ContentHeader, _Mapping]] = ..., settings: _Optional[_Union[PlayerControlV2Widget.Settings, _Mapping]] = ..., sticky_header: _Optional[_Union[PlayerControlV2Widget.ContentHeader, _Mapping]] = ...) -> None: ...
    class ContentHeader(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[PlayerControlV2Widget.HeaderItem]
        def __init__(self, items: _Optional[_Iterable[_Union[PlayerControlV2Widget.HeaderItem, _Mapping]]] = ...) -> None: ...
    class Settings(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[PlayerControlV2Widget.SettingItem]
        def __init__(self, items: _Optional[_Iterable[_Union[PlayerControlV2Widget.SettingItem, _Mapping]]] = ...) -> None: ...
    class TextHeaderItem(_message.Message):
        __slots__ = ("title", "subtitle")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        title: _text_pb2.Text
        subtitle: _text_pb2.Text
        def __init__(self, title: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., subtitle: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    class HeaderItem(_message.Message):
        __slots__ = ("orientation", "alignment", "button", "toggle_button", "toggle_lottie_button", "event_observer_button", "text_header_item")
        ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_LOTTIE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        EVENT_OBSERVER_BUTTON_FIELD_NUMBER: _ClassVar[int]
        TEXT_HEADER_ITEM_FIELD_NUMBER: _ClassVar[int]
        orientation: _orientation_pb2.Orientation
        alignment: _alignment_pb2.Alignment
        button: _button_pb2.Button
        toggle_button: _toggle_button_pb2.ToggleButton
        toggle_lottie_button: _toggle_lottie_button_pb2.ToggleLottieButton
        event_observer_button: _event_observer_button_pb2.EventObserverButton
        text_header_item: PlayerControlV2Widget.TextHeaderItem
        def __init__(self, orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ..., alignment: _Optional[_Union[_alignment_pb2.Alignment, str]] = ..., button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., toggle_button: _Optional[_Union[_toggle_button_pb2.ToggleButton, _Mapping]] = ..., toggle_lottie_button: _Optional[_Union[_toggle_lottie_button_pb2.ToggleLottieButton, _Mapping]] = ..., event_observer_button: _Optional[_Union[_event_observer_button_pb2.EventObserverButton, _Mapping]] = ..., text_header_item: _Optional[_Union[PlayerControlV2Widget.TextHeaderItem, _Mapping]] = ...) -> None: ...
    class SettingItem(_message.Message):
        __slots__ = ("orientation", "button", "toggle_button", "toggle_lottie_button", "event_observer_button")
        ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_LOTTIE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        EVENT_OBSERVER_BUTTON_FIELD_NUMBER: _ClassVar[int]
        orientation: _orientation_pb2.Orientation
        button: _button_pb2.Button
        toggle_button: _toggle_button_pb2.ToggleButton
        toggle_lottie_button: _toggle_lottie_button_pb2.ToggleLottieButton
        event_observer_button: _event_observer_button_pb2.EventObserverButton
        def __init__(self, orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ..., button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., toggle_button: _Optional[_Union[_toggle_button_pb2.ToggleButton, _Mapping]] = ..., toggle_lottie_button: _Optional[_Union[_toggle_lottie_button_pb2.ToggleLottieButton, _Mapping]] = ..., event_observer_button: _Optional[_Union[_event_observer_button_pb2.EventObserverButton, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerControlV2Widget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerControlV2Widget.Data, _Mapping]] = ...) -> None: ...
