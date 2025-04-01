from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DividerWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class DividerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WIDGET_DIVIDER: _ClassVar[DividerWidget.DividerType]
        PAGE_DIVIDER: _ClassVar[DividerWidget.DividerType]
    WIDGET_DIVIDER: DividerWidget.DividerType
    PAGE_DIVIDER: DividerWidget.DividerType
    class DividerVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[DividerWidget.DividerVariant]
        THICK: _ClassVar[DividerWidget.DividerVariant]
        THICK_WITH_BOTTOM_MARGIN: _ClassVar[DividerWidget.DividerVariant]
        SPLIT_WITH_TEXT_STYLE_1: _ClassVar[DividerWidget.DividerVariant]
    NONE: DividerWidget.DividerVariant
    THICK: DividerWidget.DividerVariant
    THICK_WITH_BOTTOM_MARGIN: DividerWidget.DividerVariant
    SPLIT_WITH_TEXT_STYLE_1: DividerWidget.DividerVariant
    class DividerOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[DividerWidget.DividerOrientation]
        HORIZONTAL: _ClassVar[DividerWidget.DividerOrientation]
        VERTICAL: _ClassVar[DividerWidget.DividerOrientation]
    UNSPECIFIED: DividerWidget.DividerOrientation
    HORIZONTAL: DividerWidget.DividerOrientation
    VERTICAL: DividerWidget.DividerOrientation
    class Data(_message.Message):
        __slots__ = ("node", "divider_type", "variant", "text", "divider_orientation")
        NODE_FIELD_NUMBER: _ClassVar[int]
        DIVIDER_TYPE_FIELD_NUMBER: _ClassVar[int]
        VARIANT_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        DIVIDER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        node: str
        divider_type: DividerWidget.DividerType
        variant: DividerWidget.DividerVariant
        text: str
        divider_orientation: DividerWidget.DividerOrientation
        def __init__(self, node: _Optional[str] = ..., divider_type: _Optional[_Union[DividerWidget.DividerType, str]] = ..., variant: _Optional[_Union[DividerWidget.DividerVariant, str]] = ..., text: _Optional[str] = ..., divider_orientation: _Optional[_Union[DividerWidget.DividerOrientation, str]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DividerWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DividerWidget.Data, _Mapping]] = ...) -> None: ...
