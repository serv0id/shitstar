from base import page_data_commons_pb2 as _page_data_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BGOverlayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[BGOverlayType]
    CLEAR: _ClassVar[BGOverlayType]
DEFAULT: BGOverlayType
CLEAR: BGOverlayType

class ActionsheetData(_message.Message):
    __slots__ = ("page_data_commons", "actionsheet_config", "page_event_actions")
    class PageEventActionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _actions_pb2.Actions.Action
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_actions_pb2.Actions.Action, _Mapping]] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    ACTIONSHEET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PAGE_EVENT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    actionsheet_config: ActionsheetConfig
    page_event_actions: _containers.MessageMap[str, _actions_pb2.Actions.Action]
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., actionsheet_config: _Optional[_Union[ActionsheetConfig, _Mapping]] = ..., page_event_actions: _Optional[_Mapping[str, _actions_pb2.Actions.Action]] = ...) -> None: ...

class ActionsheetConfig(_message.Message):
    __slots__ = ("max_height_ratio", "is_closeable", "not_skippable", "bg_overlay_type", "action_sheet_top_padding", "action_sheet_bottom_padding")
    class ActionSheetPadding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ActionsheetConfig.ActionSheetPadding]
        ZERO: _ClassVar[ActionsheetConfig.ActionSheetPadding]
        HEAVY: _ClassVar[ActionsheetConfig.ActionSheetPadding]
    DEFAULT: ActionsheetConfig.ActionSheetPadding
    ZERO: ActionsheetConfig.ActionSheetPadding
    HEAVY: ActionsheetConfig.ActionSheetPadding
    MAX_HEIGHT_RATIO_FIELD_NUMBER: _ClassVar[int]
    IS_CLOSEABLE_FIELD_NUMBER: _ClassVar[int]
    NOT_SKIPPABLE_FIELD_NUMBER: _ClassVar[int]
    BG_OVERLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_SHEET_TOP_PADDING_FIELD_NUMBER: _ClassVar[int]
    ACTION_SHEET_BOTTOM_PADDING_FIELD_NUMBER: _ClassVar[int]
    max_height_ratio: float
    is_closeable: bool
    not_skippable: bool
    bg_overlay_type: BGOverlayType
    action_sheet_top_padding: ActionsheetConfig.ActionSheetPadding
    action_sheet_bottom_padding: ActionsheetConfig.ActionSheetPadding
    def __init__(self, max_height_ratio: _Optional[float] = ..., is_closeable: bool = ..., not_skippable: bool = ..., bg_overlay_type: _Optional[_Union[BGOverlayType, str]] = ..., action_sheet_top_padding: _Optional[_Union[ActionsheetConfig.ActionSheetPadding, str]] = ..., action_sheet_bottom_padding: _Optional[_Union[ActionsheetConfig.ActionSheetPadding, str]] = ...) -> None: ...
