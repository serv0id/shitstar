from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CurrentPlanWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "subtitle", "description", "info", "subinfo", "usps")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        INFO_FIELD_NUMBER: _ClassVar[int]
        SUBINFO_FIELD_NUMBER: _ClassVar[int]
        USPS_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        description: str
        info: str
        subinfo: str
        usps: _containers.RepeatedCompositeFieldContainer[CurrentPlanWidget.USP]
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., description: _Optional[str] = ..., info: _Optional[str] = ..., subinfo: _Optional[str] = ..., usps: _Optional[_Iterable[_Union[CurrentPlanWidget.USP, _Mapping]]] = ...) -> None: ...
    class USP(_message.Message):
        __slots__ = ("image", "name", "description")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        name: str
        description: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CurrentPlanWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CurrentPlanWidget.Data, _Mapping]] = ...) -> None: ...
