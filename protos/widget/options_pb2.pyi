from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OptionsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("id", "type", "size", "input_options")
        class SelectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SINGLE: _ClassVar[OptionsWidget.Data.SelectionType]
            MULTIPLE: _ClassVar[OptionsWidget.Data.SelectionType]
        SINGLE: OptionsWidget.Data.SelectionType
        MULTIPLE: OptionsWidget.Data.SelectionType
        class Size(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FLUID: _ClassVar[OptionsWidget.Data.Size]
            FULLWIDTH: _ClassVar[OptionsWidget.Data.Size]
        FLUID: OptionsWidget.Data.Size
        FULLWIDTH: OptionsWidget.Data.Size
        ID_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        INPUT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        id: str
        type: OptionsWidget.Data.SelectionType
        size: OptionsWidget.Data.Size
        input_options: _containers.RepeatedCompositeFieldContainer[OptionsWidget.InputOption]
        def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[OptionsWidget.Data.SelectionType, str]] = ..., size: _Optional[_Union[OptionsWidget.Data.Size, str]] = ..., input_options: _Optional[_Iterable[_Union[OptionsWidget.InputOption, _Mapping]]] = ...) -> None: ...
    class InputOption(_message.Message):
        __slots__ = ("id", "label")
        ID_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        id: str
        label: str
        def __init__(self, id: _Optional[str] = ..., label: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: OptionsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[OptionsWidget.Data, _Mapping]] = ...) -> None: ...
