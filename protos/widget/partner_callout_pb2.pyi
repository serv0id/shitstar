from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PartnerCalloutWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("top_text", "partner_image", "bottom_text")
        TOP_TEXT_FIELD_NUMBER: _ClassVar[int]
        PARTNER_IMAGE_FIELD_NUMBER: _ClassVar[int]
        BOTTOM_TEXT_FIELD_NUMBER: _ClassVar[int]
        top_text: str
        partner_image: _image_pb2.Image
        bottom_text: str
        def __init__(self, top_text: _Optional[str] = ..., partner_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., bottom_text: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PartnerCalloutWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PartnerCalloutWidget.Data, _Mapping]] = ...) -> None: ...
