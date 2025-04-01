from base import widget_commons_pb2 as _widget_commons_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from feature.atom import toggle_button_pb2 as _toggle_button_pb2
from feature.atom import toggle_lottie_button_pb2 as _toggle_lottie_button_pb2
from feature.atom import event_observer_button_pb2 as _event_observer_button_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonStackWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class StackAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERTICAL: _ClassVar[ButtonStackWidget.StackAlignment]
        HORIZONTAL: _ClassVar[ButtonStackWidget.StackAlignment]
    VERTICAL: ButtonStackWidget.StackAlignment
    HORIZONTAL: ButtonStackWidget.StackAlignment
    class ButtonPadding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REGULAR: _ClassVar[ButtonStackWidget.ButtonPadding]
        LARGE: _ClassVar[ButtonStackWidget.ButtonPadding]
        NONE: _ClassVar[ButtonStackWidget.ButtonPadding]
    REGULAR: ButtonStackWidget.ButtonPadding
    LARGE: ButtonStackWidget.ButtonPadding
    NONE: ButtonStackWidget.ButtonPadding
    class HorizontalAlignmentRatio(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STANDARD: _ClassVar[ButtonStackWidget.HorizontalAlignmentRatio]
        RIGHT_CONSTRAINED: _ClassVar[ButtonStackWidget.HorizontalAlignmentRatio]
        LEFT_CONSTRAINED: _ClassVar[ButtonStackWidget.HorizontalAlignmentRatio]
    STANDARD: ButtonStackWidget.HorizontalAlignmentRatio
    RIGHT_CONSTRAINED: ButtonStackWidget.HorizontalAlignmentRatio
    LEFT_CONSTRAINED: ButtonStackWidget.HorizontalAlignmentRatio
    class Data(_message.Message):
        __slots__ = ("primary_button", "secondary_button", "aligment", "padding", "shows_loading", "primary", "secondary", "ratio", "primary_cta_button", "secondary_cta_button", "secondary_cta_watchlist_button")
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        ALIGMENT_FIELD_NUMBER: _ClassVar[int]
        PADDING_FIELD_NUMBER: _ClassVar[int]
        SHOWS_LOADING_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_FIELD_NUMBER: _ClassVar[int]
        RATIO_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_WATCHLIST_BUTTON_FIELD_NUMBER: _ClassVar[int]
        primary_button: _button_pb2.Button
        secondary_button: _button_pb2.Button
        aligment: ButtonStackWidget.StackAlignment
        padding: ButtonStackWidget.ButtonPadding
        shows_loading: bool
        primary: ButtonStackWidget.CTA
        secondary: ButtonStackWidget.CTA
        ratio: ButtonStackWidget.HorizontalAlignmentRatio
        primary_cta_button: _button_pb2.Button
        secondary_cta_button: _button_pb2.Button
        secondary_cta_watchlist_button: ButtonStackWidget.WatchlistButton
        def __init__(self, primary_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., secondary_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., aligment: _Optional[_Union[ButtonStackWidget.StackAlignment, str]] = ..., padding: _Optional[_Union[ButtonStackWidget.ButtonPadding, str]] = ..., shows_loading: bool = ..., primary: _Optional[_Union[ButtonStackWidget.CTA, _Mapping]] = ..., secondary: _Optional[_Union[ButtonStackWidget.CTA, _Mapping]] = ..., ratio: _Optional[_Union[ButtonStackWidget.HorizontalAlignmentRatio, str]] = ..., primary_cta_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., secondary_cta_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., secondary_cta_watchlist_button: _Optional[_Union[ButtonStackWidget.WatchlistButton, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("button", "watchlist_button", "toggle_button", "toggle_lottie_button", "event_observer_button")
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_BUTTON_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_LOTTIE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        EVENT_OBSERVER_BUTTON_FIELD_NUMBER: _ClassVar[int]
        button: _button_pb2.Button
        watchlist_button: ButtonStackWidget.WatchlistButton
        toggle_button: _toggle_button_pb2.ToggleButton
        toggle_lottie_button: _toggle_lottie_button_pb2.ToggleLottieButton
        event_observer_button: _event_observer_button_pb2.EventObserverButton
        def __init__(self, button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., watchlist_button: _Optional[_Union[ButtonStackWidget.WatchlistButton, _Mapping]] = ..., toggle_button: _Optional[_Union[_toggle_button_pb2.ToggleButton, _Mapping]] = ..., toggle_lottie_button: _Optional[_Union[_toggle_lottie_button_pb2.ToggleLottieButton, _Mapping]] = ..., event_observer_button: _Optional[_Union[_event_observer_button_pb2.EventObserverButton, _Mapping]] = ...) -> None: ...
    class WatchlistButton(_message.Message):
        __slots__ = ("info",)
        INFO_FIELD_NUMBER: _ClassVar[int]
        info: _watchlist_info_pb2.WatchlistInfo
        def __init__(self, info: _Optional[_Union[_watchlist_info_pb2.WatchlistInfo, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ButtonStackWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ButtonStackWidget.Data, _Mapping]] = ...) -> None: ...
