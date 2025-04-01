from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubtitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CALLOUT: _ClassVar[SubtitleType]
    ERROR: _ClassVar[SubtitleType]
    HIGHLIGHT: _ClassVar[SubtitleType]
CALLOUT: SubtitleType
ERROR: SubtitleType
HIGHLIGHT: SubtitleType

class AutoScrollGalleryWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CENTRE: _ClassVar[AutoScrollGalleryWidget.Alignment]
        LEFT: _ClassVar[AutoScrollGalleryWidget.Alignment]
    CENTRE: AutoScrollGalleryWidget.Alignment
    LEFT: AutoScrollGalleryWidget.Alignment
    class WidgetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[AutoScrollGalleryWidget.WidgetType]
        MINIFY: _ClassVar[AutoScrollGalleryWidget.WidgetType]
    DEFAULT: AutoScrollGalleryWidget.WidgetType
    MINIFY: AutoScrollGalleryWidget.WidgetType
    class ImageOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED: _ClassVar[AutoScrollGalleryWidget.ImageOrientation]
        VERTICAL: _ClassVar[AutoScrollGalleryWidget.ImageOrientation]
        HORIZONTAL: _ClassVar[AutoScrollGalleryWidget.ImageOrientation]
    UNDEFINED: AutoScrollGalleryWidget.ImageOrientation
    VERTICAL: AutoScrollGalleryWidget.ImageOrientation
    HORIZONTAL: AutoScrollGalleryWidget.ImageOrientation
    class AutoScrollDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[AutoScrollGalleryWidget.AutoScrollDirection]
        LEFT_TO_RIGHT: _ClassVar[AutoScrollGalleryWidget.AutoScrollDirection]
        RIGHT_TO_LEFT: _ClassVar[AutoScrollGalleryWidget.AutoScrollDirection]
        VERTICAL_SCROLL: _ClassVar[AutoScrollGalleryWidget.AutoScrollDirection]
    UNSPECIFIED: AutoScrollGalleryWidget.AutoScrollDirection
    LEFT_TO_RIGHT: AutoScrollGalleryWidget.AutoScrollDirection
    RIGHT_TO_LEFT: AutoScrollGalleryWidget.AutoScrollDirection
    VERTICAL_SCROLL: AutoScrollGalleryWidget.AutoScrollDirection
    class Data(_message.Message):
        __slots__ = ("bg_image_list", "title", "content_image", "sub_title", "plan_callouts", "alignment", "widget_type", "image_orientation", "auto_scroll_direction", "alt")
        BG_IMAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        PLAN_CALLOUTS_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        WIDGET_TYPE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        AUTO_SCROLL_DIRECTION_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        bg_image_list: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        title: str
        content_image: _image_pb2.Image
        sub_title: AutoScrollGalleryWidget.Subtitle
        plan_callouts: _containers.RepeatedCompositeFieldContainer[AutoScrollGalleryWidget.PlanCallouts]
        alignment: AutoScrollGalleryWidget.Alignment
        widget_type: AutoScrollGalleryWidget.WidgetType
        image_orientation: AutoScrollGalleryWidget.ImageOrientation
        auto_scroll_direction: AutoScrollGalleryWidget.AutoScrollDirection
        alt: _accessibility_pb2.Accessibility
        def __init__(self, bg_image_list: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ..., title: _Optional[str] = ..., content_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., sub_title: _Optional[_Union[AutoScrollGalleryWidget.Subtitle, _Mapping]] = ..., plan_callouts: _Optional[_Iterable[_Union[AutoScrollGalleryWidget.PlanCallouts, _Mapping]]] = ..., alignment: _Optional[_Union[AutoScrollGalleryWidget.Alignment, str]] = ..., widget_type: _Optional[_Union[AutoScrollGalleryWidget.WidgetType, str]] = ..., image_orientation: _Optional[_Union[AutoScrollGalleryWidget.ImageOrientation, str]] = ..., auto_scroll_direction: _Optional[_Union[AutoScrollGalleryWidget.AutoScrollDirection, str]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class Subtitle(_message.Message):
        __slots__ = ("type", "info_text", "rich_text", "icon_text", "bullet_text")
        class InfoText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        class RichText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        class IconText(_message.Message):
            __slots__ = ("icon_name", "value")
            ICON_NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            icon_name: str
            value: str
            def __init__(self, icon_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class BulletText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        INFO_TEXT_FIELD_NUMBER: _ClassVar[int]
        RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_TEXT_FIELD_NUMBER: _ClassVar[int]
        BULLET_TEXT_FIELD_NUMBER: _ClassVar[int]
        type: SubtitleType
        info_text: AutoScrollGalleryWidget.Subtitle.InfoText
        rich_text: AutoScrollGalleryWidget.Subtitle.RichText
        icon_text: AutoScrollGalleryWidget.Subtitle.IconText
        bullet_text: AutoScrollGalleryWidget.Subtitle.BulletText
        def __init__(self, type: _Optional[_Union[SubtitleType, str]] = ..., info_text: _Optional[_Union[AutoScrollGalleryWidget.Subtitle.InfoText, _Mapping]] = ..., rich_text: _Optional[_Union[AutoScrollGalleryWidget.Subtitle.RichText, _Mapping]] = ..., icon_text: _Optional[_Union[AutoScrollGalleryWidget.Subtitle.IconText, _Mapping]] = ..., bullet_text: _Optional[_Union[AutoScrollGalleryWidget.Subtitle.BulletText, _Mapping]] = ...) -> None: ...
    class PlanCallouts(_message.Message):
        __slots__ = ("identifier", "callout")
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_FIELD_NUMBER: _ClassVar[int]
        identifier: _containers.RepeatedScalarFieldContainer[str]
        callout: AutoScrollGalleryWidget.Subtitle
        def __init__(self, identifier: _Optional[_Iterable[str]] = ..., callout: _Optional[_Union[AutoScrollGalleryWidget.Subtitle, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AutoScrollGalleryWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AutoScrollGalleryWidget.Data, _Mapping]] = ...) -> None: ...
