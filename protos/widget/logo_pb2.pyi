from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.branding import brand_pb2 as _brand_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogoVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HORIZONTAL: _ClassVar[LogoVariant]
    DEFAULT: _ClassVar[LogoVariant]
HORIZONTAL: LogoVariant
DEFAULT: LogoVariant

class LogoWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("actions", "icon_name", "variant", "subs_nudge", "image_alt")
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        VARIANT_FIELD_NUMBER: _ClassVar[int]
        SUBS_NUDGE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ALT_FIELD_NUMBER: _ClassVar[int]
        actions: _actions_pb2.Actions
        icon_name: _brand_pb2.Brand
        variant: LogoVariant
        subs_nudge: LogoWidget.SubsNudge
        image_alt: str
        def __init__(self, actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon_name: _Optional[_Union[_brand_pb2.Brand, str]] = ..., variant: _Optional[_Union[LogoVariant, str]] = ..., subs_nudge: _Optional[_Union[LogoWidget.SubsNudge, _Mapping]] = ..., image_alt: _Optional[str] = ...) -> None: ...
    class SubsNudge(_message.Message):
        __slots__ = ("nudge_text", "actions")
        NUDGE_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        nudge_text: str
        actions: _actions_pb2.Actions
        def __init__(self, nudge_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LogoWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LogoWidget.Data, _Mapping]] = ...) -> None: ...
