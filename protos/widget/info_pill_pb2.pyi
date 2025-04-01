from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InfoPillWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class PinState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InfoPillWidget.PinState]
        HIDDEN: _ClassVar[InfoPillWidget.PinState]
        PINNED: _ClassVar[InfoPillWidget.PinState]
        UNPINNED: _ClassVar[InfoPillWidget.PinState]
    UNSPECIFIED: InfoPillWidget.PinState
    HIDDEN: InfoPillWidget.PinState
    PINNED: InfoPillWidget.PinState
    UNPINNED: InfoPillWidget.PinState
    class Data(_message.Message):
        __slots__ = ("pill_summary", "pin_summary", "actions")
        PILL_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        PIN_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        pill_summary: InfoPillWidget.PillSummary
        pin_summary: InfoPillWidget.PinSummary
        actions: _actions_pb2.Actions
        def __init__(self, pill_summary: _Optional[_Union[InfoPillWidget.PillSummary, _Mapping]] = ..., pin_summary: _Optional[_Union[InfoPillWidget.PinSummary, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PillSummary(_message.Message):
        __slots__ = ("primary_item", "secondary_item", "start_time")
        PRIMARY_ITEM_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_ITEM_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        primary_item: InfoPillWidget.Item
        secondary_item: InfoPillWidget.Item
        start_time: str
        def __init__(self, primary_item: _Optional[_Union[InfoPillWidget.Item, _Mapping]] = ..., secondary_item: _Optional[_Union[InfoPillWidget.Item, _Mapping]] = ..., start_time: _Optional[str] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("title", "active_icon", "primary_sub_title", "secondary_sub_title", "is_active", "active_soul_icon_name")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ICON_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_SOUL_ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        title: str
        active_icon: _image_pb2.Image
        primary_sub_title: str
        secondary_sub_title: str
        is_active: bool
        active_soul_icon_name: str
        def __init__(self, title: _Optional[str] = ..., active_icon: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., primary_sub_title: _Optional[str] = ..., secondary_sub_title: _Optional[str] = ..., is_active: bool = ..., active_soul_icon_name: _Optional[str] = ...) -> None: ...
    class PinSummary(_message.Message):
        __slots__ = ("pin_state", "pin_icon_active", "pin_icon_inactive", "force_pin_state", "pill_persistence_key", "active_pin_lottie", "inactive_pin_lottie")
        PIN_STATE_FIELD_NUMBER: _ClassVar[int]
        PIN_ICON_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        PIN_ICON_INACTIVE_FIELD_NUMBER: _ClassVar[int]
        FORCE_PIN_STATE_FIELD_NUMBER: _ClassVar[int]
        PILL_PERSISTENCE_KEY_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_PIN_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        INACTIVE_PIN_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        pin_state: InfoPillWidget.PinState
        pin_icon_active: _image_pb2.Image
        pin_icon_inactive: _image_pb2.Image
        force_pin_state: bool
        pill_persistence_key: str
        active_pin_lottie: _lottie_pb2.Lottie
        inactive_pin_lottie: _lottie_pb2.Lottie
        def __init__(self, pin_state: _Optional[_Union[InfoPillWidget.PinState, str]] = ..., pin_icon_active: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., pin_icon_inactive: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., force_pin_state: bool = ..., pill_persistence_key: _Optional[str] = ..., active_pin_lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., inactive_pin_lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: InfoPillWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[InfoPillWidget.Data, _Mapping]] = ...) -> None: ...
