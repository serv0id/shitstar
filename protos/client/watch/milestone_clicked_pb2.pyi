from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MilestoneClickedProperties(_message.Message):
    __slots__ = ("button_type", "milestone_appeared_secs", "is_casting", "milestone_length_ms", "start_pos_sec", "clicked_pos_sec", "click_type", "is_download", "is_downloaded", "player_version")
    class MilestoneButtonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MILESTONE_BUTTON_TYPE_UNSPECIFIED: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_SKIP_INTRO: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_SKIP_RECAP: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_WATCH_CREDITS: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_NEXT_CONTENT: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_GO_LIVE: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_GO_BACK: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_NEXT_KEY_MOMENT: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_WATCH_INTRO: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
        MILESTONE_BUTTON_TYPE_WATCH_RECAP: _ClassVar[MilestoneClickedProperties.MilestoneButtonType]
    MILESTONE_BUTTON_TYPE_UNSPECIFIED: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_SKIP_INTRO: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_SKIP_RECAP: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_WATCH_CREDITS: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_NEXT_CONTENT: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_GO_LIVE: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_GO_BACK: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_NEXT_KEY_MOMENT: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_WATCH_INTRO: MilestoneClickedProperties.MilestoneButtonType
    MILESTONE_BUTTON_TYPE_WATCH_RECAP: MilestoneClickedProperties.MilestoneButtonType
    class ClickType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLICK_TYPE_UNSPECIFIED: _ClassVar[MilestoneClickedProperties.ClickType]
        CLICK_TYPE_MANUAL: _ClassVar[MilestoneClickedProperties.ClickType]
        CLICK_TYPE_AUTO: _ClassVar[MilestoneClickedProperties.ClickType]
    CLICK_TYPE_UNSPECIFIED: MilestoneClickedProperties.ClickType
    CLICK_TYPE_MANUAL: MilestoneClickedProperties.ClickType
    CLICK_TYPE_AUTO: MilestoneClickedProperties.ClickType
    BUTTON_TYPE_FIELD_NUMBER: _ClassVar[int]
    MILESTONE_APPEARED_SECS_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    MILESTONE_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    START_POS_SEC_FIELD_NUMBER: _ClassVar[int]
    CLICKED_POS_SEC_FIELD_NUMBER: _ClassVar[int]
    CLICK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    button_type: MilestoneClickedProperties.MilestoneButtonType
    milestone_appeared_secs: int
    is_casting: bool
    milestone_length_ms: int
    start_pos_sec: int
    clicked_pos_sec: int
    click_type: MilestoneClickedProperties.ClickType
    is_download: bool
    is_downloaded: bool
    player_version: str
    def __init__(self, button_type: _Optional[_Union[MilestoneClickedProperties.MilestoneButtonType, str]] = ..., milestone_appeared_secs: _Optional[int] = ..., is_casting: bool = ..., milestone_length_ms: _Optional[int] = ..., start_pos_sec: _Optional[int] = ..., clicked_pos_sec: _Optional[int] = ..., click_type: _Optional[_Union[MilestoneClickedProperties.ClickType, str]] = ..., is_download: bool = ..., is_downloaded: bool = ..., player_version: _Optional[str] = ...) -> None: ...
