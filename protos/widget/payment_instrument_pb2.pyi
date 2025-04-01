from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentInstrumentWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "instrument", "button")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        title: str
        instrument: PaymentInstrumentWidget.Instrument
        button: PaymentInstrumentWidget.Button
        def __init__(self, title: _Optional[str] = ..., instrument: _Optional[_Union[PaymentInstrumentWidget.Instrument, _Mapping]] = ..., button: _Optional[_Union[PaymentInstrumentWidget.Button, _Mapping]] = ...) -> None: ...
    class Instrument(_message.Message):
        __slots__ = ("name", "icon_name", "icon", "image")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        name: str
        icon_name: str
        icon: str
        image: _image_pb2.Image
        def __init__(self, name: _Optional[str] = ..., icon_name: _Optional[str] = ..., icon: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("name", "icon_name", "actions")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, name: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaymentInstrumentWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaymentInstrumentWidget.Data, _Mapping]] = ...) -> None: ...
