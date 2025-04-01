from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExploreFiltersWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class FilterStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ExploreFiltersWidget.FilterStatus]
        SELECTED: _ClassVar[ExploreFiltersWidget.FilterStatus]
        NON_CLICKABLE: _ClassVar[ExploreFiltersWidget.FilterStatus]
    DEFAULT: ExploreFiltersWidget.FilterStatus
    SELECTED: ExploreFiltersWidget.FilterStatus
    NON_CLICKABLE: ExploreFiltersWidget.FilterStatus
    class Data(_message.Message):
        __slots__ = ("filter_tags", "filter_names", "filters_url", "fetch_content_url")
        FILTER_TAGS_FIELD_NUMBER: _ClassVar[int]
        FILTER_NAMES_FIELD_NUMBER: _ClassVar[int]
        FILTERS_URL_FIELD_NUMBER: _ClassVar[int]
        FETCH_CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
        filter_tags: _containers.RepeatedCompositeFieldContainer[ExploreFiltersWidget.Filter]
        filter_names: _containers.RepeatedScalarFieldContainer[str]
        filters_url: str
        fetch_content_url: str
        def __init__(self, filter_tags: _Optional[_Iterable[_Union[ExploreFiltersWidget.Filter, _Mapping]]] = ..., filter_names: _Optional[_Iterable[str]] = ..., filters_url: _Optional[str] = ..., fetch_content_url: _Optional[str] = ...) -> None: ...
    class Filter(_message.Message):
        __slots__ = ("boolean_filter", "single_choice_filter", "multiple_choice_filter")
        BOOLEAN_FILTER_FIELD_NUMBER: _ClassVar[int]
        SINGLE_CHOICE_FILTER_FIELD_NUMBER: _ClassVar[int]
        MULTIPLE_CHOICE_FILTER_FIELD_NUMBER: _ClassVar[int]
        boolean_filter: ExploreFiltersWidget.BooleanFilter
        single_choice_filter: ExploreFiltersWidget.SingleChoiceFilter
        multiple_choice_filter: ExploreFiltersWidget.MultipleChoiceFilter
        def __init__(self, boolean_filter: _Optional[_Union[ExploreFiltersWidget.BooleanFilter, _Mapping]] = ..., single_choice_filter: _Optional[_Union[ExploreFiltersWidget.SingleChoiceFilter, _Mapping]] = ..., multiple_choice_filter: _Optional[_Union[ExploreFiltersWidget.MultipleChoiceFilter, _Mapping]] = ...) -> None: ...
    class BooleanFilter(_message.Message):
        __slots__ = ("filter_name", "display_name", "selected", "group_title", "use_toggle", "image")
        FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        SELECTED_FIELD_NUMBER: _ClassVar[int]
        GROUP_TITLE_FIELD_NUMBER: _ClassVar[int]
        USE_TOGGLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        filter_name: str
        display_name: str
        selected: bool
        group_title: str
        use_toggle: bool
        image: _image_pb2.Image
        def __init__(self, filter_name: _Optional[str] = ..., display_name: _Optional[str] = ..., selected: bool = ..., group_title: _Optional[str] = ..., use_toggle: bool = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class SingleChoiceFilter(_message.Message):
        __slots__ = ("filter_name", "display_name", "filter_items", "image", "actions")
        FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        FILTER_ITEMS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        filter_name: str
        display_name: str
        filter_items: _containers.RepeatedCompositeFieldContainer[ExploreFiltersWidget.FilterItem]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        def __init__(self, filter_name: _Optional[str] = ..., display_name: _Optional[str] = ..., filter_items: _Optional[_Iterable[_Union[ExploreFiltersWidget.FilterItem, _Mapping]]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class MultipleChoiceFilter(_message.Message):
        __slots__ = ("filter_name", "display_name", "filter_items", "image", "actions")
        FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        FILTER_ITEMS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        filter_name: str
        display_name: str
        filter_items: _containers.RepeatedCompositeFieldContainer[ExploreFiltersWidget.FilterItem]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        def __init__(self, filter_name: _Optional[str] = ..., display_name: _Optional[str] = ..., filter_items: _Optional[_Iterable[_Union[ExploreFiltersWidget.FilterItem, _Mapping]]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class FilterItem(_message.Message):
        __slots__ = ("filter_name", "filter_status", "hide_in_collapse_mode")
        FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
        FILTER_STATUS_FIELD_NUMBER: _ClassVar[int]
        HIDE_IN_COLLAPSE_MODE_FIELD_NUMBER: _ClassVar[int]
        filter_name: str
        filter_status: ExploreFiltersWidget.FilterStatus
        hide_in_collapse_mode: bool
        def __init__(self, filter_name: _Optional[str] = ..., filter_status: _Optional[_Union[ExploreFiltersWidget.FilterStatus, str]] = ..., hide_in_collapse_mode: bool = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ExploreFiltersWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ExploreFiltersWidget.Data, _Mapping]] = ...) -> None: ...
