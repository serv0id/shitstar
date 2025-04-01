from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.subscription import restore_pb2 as _restore_pb2
from feature.image import image_pb2 as _image_pb2
from feature.atom import button_pb2 as _button_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MembershipActionsWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class TitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[MembershipActionsWidget.TitleType]
        HIGHLIGHTED: _ClassVar[MembershipActionsWidget.TitleType]
    DEFAULT: MembershipActionsWidget.TitleType
    HIGHLIGHTED: MembershipActionsWidget.TitleType
    class SubtextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[MembershipActionsWidget.SubtextType]
        HIGHLIGHTED_SUBTEXT: _ClassVar[MembershipActionsWidget.SubtextType]
        ERROR_SUBTEXT: _ClassVar[MembershipActionsWidget.SubtextType]
    UNKNOWN: MembershipActionsWidget.SubtextType
    HIGHLIGHTED_SUBTEXT: MembershipActionsWidget.SubtextType
    ERROR_SUBTEXT: MembershipActionsWidget.SubtextType
    class CtaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_CTA: _ClassVar[MembershipActionsWidget.CtaType]
        DEFAULT_CTA: _ClassVar[MembershipActionsWidget.CtaType]
        SUBTLE_CTA: _ClassVar[MembershipActionsWidget.CtaType]
    UNKNOWN_CTA: MembershipActionsWidget.CtaType
    DEFAULT_CTA: MembershipActionsWidget.CtaType
    SUBTLE_CTA: MembershipActionsWidget.CtaType
    class Theme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DARK: _ClassVar[MembershipActionsWidget.Theme]
        LIGHT: _ClassVar[MembershipActionsWidget.Theme]
    DARK: MembershipActionsWidget.Theme
    LIGHT: MembershipActionsWidget.Theme
    class Data(_message.Message):
        __slots__ = ("membership", "refresh_url", "theme")
        MEMBERSHIP_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        THEME_FIELD_NUMBER: _ClassVar[int]
        membership: _containers.RepeatedCompositeFieldContainer[MembershipActionsWidget.Membership]
        refresh_url: str
        theme: MembershipActionsWidget.Theme
        def __init__(self, membership: _Optional[_Iterable[_Union[MembershipActionsWidget.Membership, _Mapping]]] = ..., refresh_url: _Optional[str] = ..., theme: _Optional[_Union[MembershipActionsWidget.Theme, str]] = ...) -> None: ...
    class Membership(_message.Message):
        __slots__ = ("title", "cta", "operations", "icon")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        title: MembershipActionsWidget.Title
        cta: MembershipActionsWidget.Cta
        operations: _containers.RepeatedCompositeFieldContainer[MembershipActionsWidget.MembershipOperation]
        icon: _button_pb2.Button
        def __init__(self, title: _Optional[_Union[MembershipActionsWidget.Title, _Mapping]] = ..., cta: _Optional[_Union[MembershipActionsWidget.Cta, _Mapping]] = ..., operations: _Optional[_Iterable[_Union[MembershipActionsWidget.MembershipOperation, _Mapping]]] = ..., icon: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    class Title(_message.Message):
        __slots__ = ("value", "type", "sub_title", "subtext")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTEXT_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: MembershipActionsWidget.TitleType
        sub_title: str
        subtext: MembershipActionsWidget.Subtext
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[MembershipActionsWidget.TitleType, str]] = ..., sub_title: _Optional[str] = ..., subtext: _Optional[_Union[MembershipActionsWidget.Subtext, _Mapping]] = ...) -> None: ...
    class Subtext(_message.Message):
        __slots__ = ("value", "type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: MembershipActionsWidget.SubtextType
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[MembershipActionsWidget.SubtextType, str]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("value", "action", "type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        action: _actions_pb2.Actions
        type: MembershipActionsWidget.CtaType
        def __init__(self, value: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., type: _Optional[_Union[MembershipActionsWidget.CtaType, str]] = ...) -> None: ...
    class MembershipOperation(_message.Message):
        __slots__ = ("label", "icon_name", "badge_value", "action", "actions", "type", "img", "restore")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        BADGE_VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        IMG_FIELD_NUMBER: _ClassVar[int]
        RESTORE_FIELD_NUMBER: _ClassVar[int]
        label: str
        icon_name: str
        badge_value: str
        action: _actions_pb2.Actions
        actions: _actions_pb2.Actions
        type: MembershipActionsWidget.CtaType
        img: _image_pb2.Image
        restore: MembershipActionsWidget.RestoreOperation
        def __init__(self, label: _Optional[str] = ..., icon_name: _Optional[str] = ..., badge_value: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., type: _Optional[_Union[MembershipActionsWidget.CtaType, str]] = ..., img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., restore: _Optional[_Union[MembershipActionsWidget.RestoreOperation, _Mapping]] = ...) -> None: ...
    class RestoreOperation(_message.Message):
        __slots__ = ("info", "on_success_actions", "on_failure_actions")
        INFO_FIELD_NUMBER: _ClassVar[int]
        ON_SUCCESS_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ON_FAILURE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        info: _restore_pb2.Restore
        on_success_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        on_failure_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, info: _Optional[_Union[_restore_pb2.Restore, _Mapping]] = ..., on_success_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., on_failure_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MembershipActionsWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MembershipActionsWidget.Data, _Mapping]] = ...) -> None: ...
