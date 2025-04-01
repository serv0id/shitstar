from feature.image import image_pb2 as _image_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshableStatusWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("refresh_info", "title", "details", "primary_cta", "secondary_cta", "is_closable", "on_load_actions", "use_force_refresh", "is_plan_active", "polling_timeout_in_ms", "img", "animation")
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        IS_CLOSABLE_FIELD_NUMBER: _ClassVar[int]
        ON_LOAD_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        USE_FORCE_REFRESH_FIELD_NUMBER: _ClassVar[int]
        IS_PLAN_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        POLLING_TIMEOUT_IN_MS_FIELD_NUMBER: _ClassVar[int]
        IMG_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_FIELD_NUMBER: _ClassVar[int]
        refresh_info: _refresh_info_pb2.RefreshInfo
        title: RefreshableStatusWidget.Title
        details: _containers.RepeatedCompositeFieldContainer[RefreshableStatusWidget.Detail]
        primary_cta: RefreshableStatusWidget.Cta
        secondary_cta: RefreshableStatusWidget.Cta
        is_closable: bool
        on_load_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        use_force_refresh: bool
        is_plan_active: bool
        polling_timeout_in_ms: int
        img: _image_pb2.Image
        animation: RefreshableStatusWidget.Animation
        def __init__(self, refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ..., title: _Optional[_Union[RefreshableStatusWidget.Title, _Mapping]] = ..., details: _Optional[_Iterable[_Union[RefreshableStatusWidget.Detail, _Mapping]]] = ..., primary_cta: _Optional[_Union[RefreshableStatusWidget.Cta, _Mapping]] = ..., secondary_cta: _Optional[_Union[RefreshableStatusWidget.Cta, _Mapping]] = ..., is_closable: bool = ..., on_load_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., use_force_refresh: bool = ..., is_plan_active: bool = ..., polling_timeout_in_ms: _Optional[int] = ..., img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., animation: _Optional[_Union[RefreshableStatusWidget.Animation, _Mapping]] = ...) -> None: ...
    class Animation(_message.Message):
        __slots__ = ("type", "animation_type", "url", "animatation_meta")
        class AnimationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[RefreshableStatusWidget.Animation.AnimationType]
            LOADING: _ClassVar[RefreshableStatusWidget.Animation.AnimationType]
            SUCCESS: _ClassVar[RefreshableStatusWidget.Animation.AnimationType]
            TRANSFORM: _ClassVar[RefreshableStatusWidget.Animation.AnimationType]
        UNSPECIFIED: RefreshableStatusWidget.Animation.AnimationType
        LOADING: RefreshableStatusWidget.Animation.AnimationType
        SUCCESS: RefreshableStatusWidget.Animation.AnimationType
        TRANSFORM: RefreshableStatusWidget.Animation.AnimationType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        ANIMATATION_META_FIELD_NUMBER: _ClassVar[int]
        type: str
        animation_type: RefreshableStatusWidget.Animation.AnimationType
        url: str
        animatation_meta: RefreshableStatusWidget.AnimatationMeta
        def __init__(self, type: _Optional[str] = ..., animation_type: _Optional[_Union[RefreshableStatusWidget.Animation.AnimationType, str]] = ..., url: _Optional[str] = ..., animatation_meta: _Optional[_Union[RefreshableStatusWidget.AnimatationMeta, _Mapping]] = ...) -> None: ...
    class AnimatationMeta(_message.Message):
        __slots__ = ("from_img", "to_img", "animation_duration_ms")
        FROM_IMG_FIELD_NUMBER: _ClassVar[int]
        TO_IMG_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
        from_img: _image_pb2.Image
        to_img: _image_pb2.Image
        animation_duration_ms: int
        def __init__(self, from_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., to_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., animation_duration_ms: _Optional[int] = ...) -> None: ...
    class Detail(_message.Message):
        __slots__ = ("description", "links")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        description: str
        links: _containers.RepeatedCompositeFieldContainer[RefreshableStatusWidget.Link]
        def __init__(self, description: _Optional[str] = ..., links: _Optional[_Iterable[_Union[RefreshableStatusWidget.Link, _Mapping]]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("key", "label", "url")
        KEY_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        key: str
        label: str
        url: str
        def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Title(_message.Message):
        __slots__ = ("text", "type")
        class TitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[RefreshableStatusWidget.Title.TitleType]
            DEFAULT: _ClassVar[RefreshableStatusWidget.Title.TitleType]
            ERROR: _ClassVar[RefreshableStatusWidget.Title.TitleType]
        UNSPECIFIED: RefreshableStatusWidget.Title.TitleType
        DEFAULT: RefreshableStatusWidget.Title.TitleType
        ERROR: RefreshableStatusWidget.Title.TitleType
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        text: str
        type: RefreshableStatusWidget.Title.TitleType
        def __init__(self, text: _Optional[str] = ..., type: _Optional[_Union[RefreshableStatusWidget.Title.TitleType, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: RefreshableStatusWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[RefreshableStatusWidget.Data, _Mapping]] = ...) -> None: ...
