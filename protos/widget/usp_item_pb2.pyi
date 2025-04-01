from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UspItemWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class TypographyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        H5: _ClassVar[UspItemWidget.TypographyType]
        H1: _ClassVar[UspItemWidget.TypographyType]
        TITLE1: _ClassVar[UspItemWidget.TypographyType]
        TITLE2: _ClassVar[UspItemWidget.TypographyType]
        BODY1_MEDIUM: _ClassVar[UspItemWidget.TypographyType]
        BODY2_REGULAR: _ClassVar[UspItemWidget.TypographyType]
        BODY3_REGULAR: _ClassVar[UspItemWidget.TypographyType]
        BODY2_MEDIUM: _ClassVar[UspItemWidget.TypographyType]
    H5: UspItemWidget.TypographyType
    H1: UspItemWidget.TypographyType
    TITLE1: UspItemWidget.TypographyType
    TITLE2: UspItemWidget.TypographyType
    BODY1_MEDIUM: UspItemWidget.TypographyType
    BODY2_REGULAR: UspItemWidget.TypographyType
    BODY3_REGULAR: UspItemWidget.TypographyType
    BODY2_MEDIUM: UspItemWidget.TypographyType
    class Data(_message.Message):
        __slots__ = ("usp_image", "label", "item")
        USP_IMAGE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        usp_image: _image_pb2.Image
        label: UspItemWidget.TextInfo
        item: UspItemWidget.Item
        def __init__(self, usp_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., label: _Optional[_Union[UspItemWidget.TextInfo, _Mapping]] = ..., item: _Optional[_Union[UspItemWidget.Item, _Mapping]] = ...) -> None: ...
    class TextInfo(_message.Message):
        __slots__ = ("text", "typographyType")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TYPOGRAPHYTYPE_FIELD_NUMBER: _ClassVar[int]
        text: str
        typographyType: UspItemWidget.TypographyType
        def __init__(self, text: _Optional[str] = ..., typographyType: _Optional[_Union[UspItemWidget.TypographyType, str]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("description", "desc_list")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DESC_LIST_FIELD_NUMBER: _ClassVar[int]
        description: UspItemWidget.TextInfo
        desc_list: UspItemWidget.DescTextList
        def __init__(self, description: _Optional[_Union[UspItemWidget.TextInfo, _Mapping]] = ..., desc_list: _Optional[_Union[UspItemWidget.DescTextList, _Mapping]] = ...) -> None: ...
    class DescTextList(_message.Message):
        __slots__ = ("desc_text_list",)
        DESC_TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
        desc_text_list: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, desc_text_list: _Optional[_Iterable[str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: UspItemWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[UspItemWidget.Data, _Mapping]] = ...) -> None: ...
