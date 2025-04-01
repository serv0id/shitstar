from base import widget_commons_pb2 as _widget_commons_pb2
from widget import text_list_pb2 as _text_list_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentHistoryTableWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class CellType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PaymentHistoryTableWidget.CellType]
        DETAILS: _ClassVar[PaymentHistoryTableWidget.CellType]
        ACTION: _ClassVar[PaymentHistoryTableWidget.CellType]
    UNSPECIFIED: PaymentHistoryTableWidget.CellType
    DETAILS: PaymentHistoryTableWidget.CellType
    ACTION: PaymentHistoryTableWidget.CellType
    class Data(_message.Message):
        __slots__ = ("rows", "columns", "disclaimer")
        ROWS_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        DISCLAIMER_FIELD_NUMBER: _ClassVar[int]
        rows: _containers.RepeatedCompositeFieldContainer[PaymentHistoryTableWidget.Row]
        columns: _containers.RepeatedCompositeFieldContainer[PaymentHistoryTableWidget.Column]
        disclaimer: PaymentHistoryTableWidget.Disclaimer
        def __init__(self, rows: _Optional[_Iterable[_Union[PaymentHistoryTableWidget.Row, _Mapping]]] = ..., columns: _Optional[_Iterable[_Union[PaymentHistoryTableWidget.Column, _Mapping]]] = ..., disclaimer: _Optional[_Union[PaymentHistoryTableWidget.Disclaimer, _Mapping]] = ...) -> None: ...
    class Row(_message.Message):
        __slots__ = ("title", "desc", "link", "status", "button")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        title: _containers.RepeatedScalarFieldContainer[str]
        desc: _containers.RepeatedScalarFieldContainer[str]
        link: PaymentHistoryTableWidget.Link
        status: _text_list_pb2.TextListWidget
        button: PaymentHistoryTableWidget.Button
        def __init__(self, title: _Optional[_Iterable[str]] = ..., desc: _Optional[_Iterable[str]] = ..., link: _Optional[_Union[PaymentHistoryTableWidget.Link, _Mapping]] = ..., status: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., button: _Optional[_Union[PaymentHistoryTableWidget.Button, _Mapping]] = ...) -> None: ...
    class Column(_message.Message):
        __slots__ = ("name", "type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        type: PaymentHistoryTableWidget.CellType
        def __init__(self, name: _Optional[str] = ..., type: _Optional[_Union[PaymentHistoryTableWidget.CellType, str]] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("icon", "label", "action")
        ICON_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        icon: str
        label: str
        action: _actions_pb2.Actions
        def __init__(self, icon: _Optional[str] = ..., label: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("label", "url", "key")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        label: str
        url: str
        key: str
        def __init__(self, label: _Optional[str] = ..., url: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...
    class Disclaimer(_message.Message):
        __slots__ = ("message", "links")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        message: str
        links: _containers.RepeatedCompositeFieldContainer[PaymentHistoryTableWidget.Link]
        def __init__(self, message: _Optional[str] = ..., links: _Optional[_Iterable[_Union[PaymentHistoryTableWidget.Link, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaymentHistoryTableWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaymentHistoryTableWidget.Data, _Mapping]] = ...) -> None: ...
