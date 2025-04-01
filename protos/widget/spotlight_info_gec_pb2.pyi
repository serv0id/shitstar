from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.live import live_info_pb2 as _live_info_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from widget import timer_pb2 as _timer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpotlightInfoGecWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class TagType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TEXT: _ClassVar[SpotlightInfoGecWidget.TagType]
        BADGE: _ClassVar[SpotlightInfoGecWidget.TagType]
        IMAGE: _ClassVar[SpotlightInfoGecWidget.TagType]
    TEXT: SpotlightInfoGecWidget.TagType
    BADGE: SpotlightInfoGecWidget.TagType
    IMAGE: SpotlightInfoGecWidget.TagType
    class Data(_message.Message):
        __slots__ = ("title", "title_cutout", "description", "callout_text", "superscript_tags", "subscript_tags", "subscript_usp", "core_meta_tags", "enriched_meta_tags", "live_info", "callout_meta_tags", "timer", "secondary_meta_tags")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_TEXT_FIELD_NUMBER: _ClassVar[int]
        SUPERSCRIPT_TAGS_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPT_TAGS_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPT_USP_FIELD_NUMBER: _ClassVar[int]
        CORE_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        ENRICHED_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        LIVE_INFO_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        title: str
        title_cutout: _image_pb2.Image
        description: str
        callout_text: str
        superscript_tags: _containers.RepeatedCompositeFieldContainer[SpotlightInfoGecWidget.Tag]
        subscript_tags: _containers.RepeatedCompositeFieldContainer[SpotlightInfoGecWidget.Tag]
        subscript_usp: SpotlightInfoGecWidget.Tag
        core_meta_tags: _containers.RepeatedCompositeFieldContainer[SpotlightInfoGecWidget.Tag]
        enriched_meta_tags: _containers.RepeatedCompositeFieldContainer[SpotlightInfoGecWidget.Tag]
        live_info: _live_info_pb2.LiveInfo
        callout_meta_tags: _containers.RepeatedCompositeFieldContainer[SpotlightInfoGecWidget.Tag]
        timer: _timer_pb2.TimerWidget
        secondary_meta_tags: _containers.RepeatedCompositeFieldContainer[SpotlightInfoGecWidget.Tag]
        def __init__(self, title: _Optional[str] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., callout_text: _Optional[str] = ..., superscript_tags: _Optional[_Iterable[_Union[SpotlightInfoGecWidget.Tag, _Mapping]]] = ..., subscript_tags: _Optional[_Iterable[_Union[SpotlightInfoGecWidget.Tag, _Mapping]]] = ..., subscript_usp: _Optional[_Union[SpotlightInfoGecWidget.Tag, _Mapping]] = ..., core_meta_tags: _Optional[_Iterable[_Union[SpotlightInfoGecWidget.Tag, _Mapping]]] = ..., enriched_meta_tags: _Optional[_Iterable[_Union[SpotlightInfoGecWidget.Tag, _Mapping]]] = ..., live_info: _Optional[_Union[_live_info_pb2.LiveInfo, _Mapping]] = ..., callout_meta_tags: _Optional[_Iterable[_Union[SpotlightInfoGecWidget.Tag, _Mapping]]] = ..., timer: _Optional[_Union[_timer_pb2.TimerWidget, _Mapping]] = ..., secondary_meta_tags: _Optional[_Iterable[_Union[SpotlightInfoGecWidget.Tag, _Mapping]]] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("type", "value", "fallback_value", "text_tag", "badge_tag", "image_tag", "callout_tag")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_VALUE_FIELD_NUMBER: _ClassVar[int]
        TEXT_TAG_FIELD_NUMBER: _ClassVar[int]
        BADGE_TAG_FIELD_NUMBER: _ClassVar[int]
        IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_TAG_FIELD_NUMBER: _ClassVar[int]
        type: SpotlightInfoGecWidget.TagType
        value: str
        fallback_value: str
        text_tag: SpotlightInfoGecWidget.TextTag
        badge_tag: SpotlightInfoGecWidget.BadgeTag
        image_tag: SpotlightInfoGecWidget.ImageTag
        callout_tag: _callout_tag_pb2.CalloutTag
        def __init__(self, type: _Optional[_Union[SpotlightInfoGecWidget.TagType, str]] = ..., value: _Optional[str] = ..., fallback_value: _Optional[str] = ..., text_tag: _Optional[_Union[SpotlightInfoGecWidget.TextTag, _Mapping]] = ..., badge_tag: _Optional[_Union[SpotlightInfoGecWidget.BadgeTag, _Mapping]] = ..., image_tag: _Optional[_Union[SpotlightInfoGecWidget.ImageTag, _Mapping]] = ..., callout_tag: _Optional[_Union[_callout_tag_pb2.CalloutTag, _Mapping]] = ...) -> None: ...
    class TextTag(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class BadgeTag(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class ImageTag(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _image_pb2.Image
        def __init__(self, value: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SpotlightInfoGecWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SpotlightInfoGecWidget.Data, _Mapping]] = ...) -> None: ...
