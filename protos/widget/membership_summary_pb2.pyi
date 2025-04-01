from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipSummaryWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class SubtextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BASE: _ClassVar[MembershipSummaryWidget.SubtextType]
        HIGHLIGHTED: _ClassVar[MembershipSummaryWidget.SubtextType]
        ERROR_SUBTEXT: _ClassVar[MembershipSummaryWidget.SubtextType]
    BASE: MembershipSummaryWidget.SubtextType
    HIGHLIGHTED: MembershipSummaryWidget.SubtextType
    ERROR_SUBTEXT: MembershipSummaryWidget.SubtextType
    class TitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[MembershipSummaryWidget.TitleType]
        ERROR: _ClassVar[MembershipSummaryWidget.TitleType]
        HIGHLIGHTED_TITLE: _ClassVar[MembershipSummaryWidget.TitleType]
    DEFAULT: MembershipSummaryWidget.TitleType
    ERROR: MembershipSummaryWidget.TitleType
    HIGHLIGHTED_TITLE: MembershipSummaryWidget.TitleType
    class Data(_message.Message):
        __slots__ = ("title", "primary_sub_title", "secondary_sub_title", "cta", "subtext", "help_settings_cta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        SUBTEXT_FIELD_NUMBER: _ClassVar[int]
        HELP_SETTINGS_CTA_FIELD_NUMBER: _ClassVar[int]
        title: MembershipSummaryWidget.Title
        primary_sub_title: str
        secondary_sub_title: str
        cta: MembershipSummaryWidget.Cta
        subtext: MembershipSummaryWidget.Subtext
        help_settings_cta: MembershipSummaryWidget.HelpSettings
        def __init__(self, title: _Optional[_Union[MembershipSummaryWidget.Title, _Mapping]] = ..., primary_sub_title: _Optional[str] = ..., secondary_sub_title: _Optional[str] = ..., cta: _Optional[_Union[MembershipSummaryWidget.Cta, _Mapping]] = ..., subtext: _Optional[_Union[MembershipSummaryWidget.Subtext, _Mapping]] = ..., help_settings_cta: _Optional[_Union[MembershipSummaryWidget.HelpSettings, _Mapping]] = ...) -> None: ...
    class Title(_message.Message):
        __slots__ = ("value", "type", "action")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: MembershipSummaryWidget.TitleType
        action: _actions_pb2.Actions
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[MembershipSummaryWidget.TitleType, str]] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("value", "action", "strikethrough_text")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        STRIKETHROUGH_TEXT_FIELD_NUMBER: _ClassVar[int]
        value: str
        action: _actions_pb2.Actions
        strikethrough_text: str
        def __init__(self, value: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., strikethrough_text: _Optional[str] = ...) -> None: ...
    class Subtext(_message.Message):
        __slots__ = ("value", "type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: MembershipSummaryWidget.SubtextType
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[MembershipSummaryWidget.SubtextType, str]] = ...) -> None: ...
    class HelpSettings(_message.Message):
        __slots__ = ("icon_name", "value", "action")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        value: str
        action: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., value: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MembershipSummaryWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MembershipSummaryWidget.Data, _Mapping]] = ...) -> None: ...
