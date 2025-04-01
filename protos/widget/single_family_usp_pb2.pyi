from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SingleFamilyUSPWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("usp_list", "usp_grid")
        USP_LIST_FIELD_NUMBER: _ClassVar[int]
        USP_GRID_FIELD_NUMBER: _ClassVar[int]
        usp_list: _containers.RepeatedCompositeFieldContainer[SingleFamilyUSPWidget.IconText]
        usp_grid: _containers.RepeatedCompositeFieldContainer[SingleFamilyUSPWidget.USPGrid]
        def __init__(self, usp_list: _Optional[_Iterable[_Union[SingleFamilyUSPWidget.IconText, _Mapping]]] = ..., usp_grid: _Optional[_Iterable[_Union[SingleFamilyUSPWidget.USPGrid, _Mapping]]] = ...) -> None: ...
    class USPGrid(_message.Message):
        __slots__ = ("image", "label")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        label: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., label: _Optional[str] = ...) -> None: ...
    class IconText(_message.Message):
        __slots__ = ("icon_name", "value")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        value: str
        def __init__(self, icon_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SingleFamilyUSPWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SingleFamilyUSPWidget.Data, _Mapping]] = ...) -> None: ...
