from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.search import badge_pb2 as _badge_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from feature.cw import cw_info_pb2 as _cw_info_pb2
from feature.remind_me import remind_me_info_pb2 as _remind_me_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchHeroWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class CardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERTICAL_POSTER: _ClassVar[SearchHeroWidget.CardType]
        HORIZONTAL_POSTER: _ClassVar[SearchHeroWidget.CardType]
    VERTICAL_POSTER: SearchHeroWidget.CardType
    HORIZONTAL_POSTER: SearchHeroWidget.CardType
    class Data(_message.Message):
        __slots__ = ("title", "image", "content_info", "description", "actions", "card_type", "badge", "primary_cta", "secondary_cta", "callout_tag", "background_meta", "cw_info")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_TAG_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_META_FIELD_NUMBER: _ClassVar[int]
        CW_INFO_FIELD_NUMBER: _ClassVar[int]
        title: str
        image: _image_pb2.Image
        content_info: _containers.RepeatedScalarFieldContainer[str]
        description: str
        actions: _actions_pb2.Actions
        card_type: SearchHeroWidget.CardType
        badge: _badge_pb2.Badge
        primary_cta: SearchHeroWidget.IconLabelButton
        secondary_cta: SearchHeroWidget.IconLabelButton
        callout_tag: _callout_tag_pb2.CalloutTag
        background_meta: SearchHeroWidget.HeroBackgroundMeta
        cw_info: _cw_info_pb2.CwInfo
        def __init__(self, title: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., card_type: _Optional[_Union[SearchHeroWidget.CardType, str]] = ..., badge: _Optional[_Union[_badge_pb2.Badge, _Mapping]] = ..., primary_cta: _Optional[_Union[SearchHeroWidget.IconLabelButton, _Mapping]] = ..., secondary_cta: _Optional[_Union[SearchHeroWidget.IconLabelButton, _Mapping]] = ..., callout_tag: _Optional[_Union[_callout_tag_pb2.CalloutTag, _Mapping]] = ..., background_meta: _Optional[_Union[SearchHeroWidget.HeroBackgroundMeta, _Mapping]] = ..., cw_info: _Optional[_Union[_cw_info_pb2.CwInfo, _Mapping]] = ...) -> None: ...
    class IconLabelButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions", "secondary_label", "is_coming_soon", "remind_me_info")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_COMING_SOON_FIELD_NUMBER: _ClassVar[int]
        REMIND_ME_INFO_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        secondary_label: str
        is_coming_soon: bool
        remind_me_info: _remind_me_info_pb2.ReminderInfo
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., secondary_label: _Optional[str] = ..., is_coming_soon: bool = ..., remind_me_info: _Optional[_Union[_remind_me_info_pb2.ReminderInfo, _Mapping]] = ...) -> None: ...
    class HeroBackgroundMeta(_message.Message):
        __slots__ = ("gradient_start", "gradient_middle", "gradient_end")
        GRADIENT_START_FIELD_NUMBER: _ClassVar[int]
        GRADIENT_MIDDLE_FIELD_NUMBER: _ClassVar[int]
        GRADIENT_END_FIELD_NUMBER: _ClassVar[int]
        gradient_start: str
        gradient_middle: str
        gradient_end: str
        def __init__(self, gradient_start: _Optional[str] = ..., gradient_middle: _Optional[str] = ..., gradient_end: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SearchHeroWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SearchHeroWidget.Data, _Mapping]] = ...) -> None: ...
