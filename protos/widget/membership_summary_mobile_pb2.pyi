from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.quiz import title_icon_combo_pb2 as _title_icon_combo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipSummaryMobileWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class SubtextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BASE: _ClassVar[MembershipSummaryMobileWidget.SubtextType]
        ERROR_SUBTEXT: _ClassVar[MembershipSummaryMobileWidget.SubtextType]
    BASE: MembershipSummaryMobileWidget.SubtextType
    ERROR_SUBTEXT: MembershipSummaryMobileWidget.SubtextType
    class TitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[MembershipSummaryMobileWidget.TitleType]
        HIGHLIGHTED_TITLE: _ClassVar[MembershipSummaryMobileWidget.TitleType]
    DEFAULT: MembershipSummaryMobileWidget.TitleType
    HIGHLIGHTED_TITLE: MembershipSummaryMobileWidget.TitleType
    class Data(_message.Message):
        __slots__ = ("title", "primary_sub_title", "secondary_sub_title", "cta", "subtext", "showDivider", "animatableList")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        SUBTEXT_FIELD_NUMBER: _ClassVar[int]
        SHOWDIVIDER_FIELD_NUMBER: _ClassVar[int]
        ANIMATABLELIST_FIELD_NUMBER: _ClassVar[int]
        title: MembershipSummaryMobileWidget.Title
        primary_sub_title: str
        secondary_sub_title: str
        cta: MembershipSummaryMobileWidget.Cta
        subtext: MembershipSummaryMobileWidget.Subtext
        showDivider: bool
        animatableList: _containers.RepeatedCompositeFieldContainer[_title_icon_combo_pb2.TitleIconCombo]
        def __init__(self, title: _Optional[_Union[MembershipSummaryMobileWidget.Title, _Mapping]] = ..., primary_sub_title: _Optional[str] = ..., secondary_sub_title: _Optional[str] = ..., cta: _Optional[_Union[MembershipSummaryMobileWidget.Cta, _Mapping]] = ..., subtext: _Optional[_Union[MembershipSummaryMobileWidget.Subtext, _Mapping]] = ..., showDivider: bool = ..., animatableList: _Optional[_Iterable[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]]] = ...) -> None: ...
    class Title(_message.Message):
        __slots__ = ("value", "type", "action")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: MembershipSummaryMobileWidget.TitleType
        action: _actions_pb2.Actions
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[MembershipSummaryMobileWidget.TitleType, str]] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("value", "action", "strikethrough_text", "text", "animation")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        STRIKETHROUGH_TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_FIELD_NUMBER: _ClassVar[int]
        value: str
        action: _actions_pb2.Actions
        strikethrough_text: str
        text: str
        animation: MembershipSummaryMobileWidget.ButtonAnimation
        def __init__(self, value: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., strikethrough_text: _Optional[str] = ..., text: _Optional[str] = ..., animation: _Optional[_Union[MembershipSummaryMobileWidget.ButtonAnimation, _Mapping]] = ...) -> None: ...
    class ButtonAnimation(_message.Message):
        __slots__ = ("slide_up",)
        SLIDE_UP_FIELD_NUMBER: _ClassVar[int]
        slide_up: _containers.RepeatedCompositeFieldContainer[_title_icon_combo_pb2.TitleIconCombo]
        def __init__(self, slide_up: _Optional[_Iterable[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]]] = ...) -> None: ...
    class Subtext(_message.Message):
        __slots__ = ("value", "type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: MembershipSummaryMobileWidget.SubtextType
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[MembershipSummaryMobileWidget.SubtextType, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MembershipSummaryMobileWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MembershipSummaryMobileWidget.Data, _Mapping]] = ...) -> None: ...
