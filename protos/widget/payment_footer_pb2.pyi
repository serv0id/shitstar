from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentFooterWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("icon", "text", "sub_text", "details")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        icon: str
        text: str
        sub_text: str
        details: _containers.RepeatedCompositeFieldContainer[PaymentFooterWidget.Detail]
        def __init__(self, icon: _Optional[str] = ..., text: _Optional[str] = ..., sub_text: _Optional[str] = ..., details: _Optional[_Iterable[_Union[PaymentFooterWidget.Detail, _Mapping]]] = ...) -> None: ...
    class Detail(_message.Message):
        __slots__ = ("description", "links")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        description: str
        links: _containers.RepeatedCompositeFieldContainer[PaymentFooterWidget.Link]
        def __init__(self, description: _Optional[str] = ..., links: _Optional[_Iterable[_Union[PaymentFooterWidget.Link, _Mapping]]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("key", "label", "url")
        KEY_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        key: str
        label: str
        url: str
        def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaymentFooterWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaymentFooterWidget.Data, _Mapping]] = ...) -> None: ...
