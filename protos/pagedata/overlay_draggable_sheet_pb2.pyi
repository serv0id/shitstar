from base import page_data_commons_pb2 as _page_data_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OverlayDraggableSheetData(_message.Message):
    __slots__ = ("page_data_commons", "overlay_draggable_sheet_config")
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    OVERLAY_DRAGGABLE_SHEET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    overlay_draggable_sheet_config: OverlayDraggableSheetConfig
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., overlay_draggable_sheet_config: _Optional[_Union[OverlayDraggableSheetConfig, _Mapping]] = ...) -> None: ...

class OverlayDraggableSheetConfig(_message.Message):
    __slots__ = ("show_bottom_nav_on_scroll", "bottom_nav_visibility_scroll_ratio", "is_overlay_dismissible", "height_ratio", "snap_dismissal_ratio")
    SHOW_BOTTOM_NAV_ON_SCROLL_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_NAV_VISIBILITY_SCROLL_RATIO_FIELD_NUMBER: _ClassVar[int]
    IS_OVERLAY_DISMISSIBLE_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_RATIO_FIELD_NUMBER: _ClassVar[int]
    SNAP_DISMISSAL_RATIO_FIELD_NUMBER: _ClassVar[int]
    show_bottom_nav_on_scroll: bool
    bottom_nav_visibility_scroll_ratio: float
    is_overlay_dismissible: bool
    height_ratio: float
    snap_dismissal_ratio: float
    def __init__(self, show_bottom_nav_on_scroll: bool = ..., bottom_nav_visibility_scroll_ratio: _Optional[float] = ..., is_overlay_dismissible: bool = ..., height_ratio: _Optional[float] = ..., snap_dismissal_ratio: _Optional[float] = ...) -> None: ...
