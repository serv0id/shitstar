from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerOnboardingWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("rating", "brand", "on_boarding_overlay_duration_in_seconds", "player_onboarding_languages")
        RATING_FIELD_NUMBER: _ClassVar[int]
        BRAND_FIELD_NUMBER: _ClassVar[int]
        ON_BOARDING_OVERLAY_DURATION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
        PLAYER_ONBOARDING_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        rating: PlayerOnboardingWidget.Rating
        brand: _brand_pb2.Brand
        on_boarding_overlay_duration_in_seconds: int
        player_onboarding_languages: PlayerOnboardingWidget.PlayerOnboardingLanguages
        def __init__(self, rating: _Optional[_Union[PlayerOnboardingWidget.Rating, _Mapping]] = ..., brand: _Optional[_Union[_brand_pb2.Brand, str]] = ..., on_boarding_overlay_duration_in_seconds: _Optional[int] = ..., player_onboarding_languages: _Optional[_Union[PlayerOnboardingWidget.PlayerOnboardingLanguages, _Mapping]] = ...) -> None: ...
    class Rating(_message.Message):
        __slots__ = ("title", "subtitle")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ...) -> None: ...
    class PlayerOnboardingLanguages(_message.Message):
        __slots__ = ("icon", "languages", "subtitle_map")
        class SubtitleMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        ICON_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_MAP_FIELD_NUMBER: _ClassVar[int]
        icon: str
        languages: _containers.RepeatedCompositeFieldContainer[PlayerOnboardingWidget.PlayerOnboardingLanguageTab]
        subtitle_map: _containers.ScalarMap[str, str]
        def __init__(self, icon: _Optional[str] = ..., languages: _Optional[_Iterable[_Union[PlayerOnboardingWidget.PlayerOnboardingLanguageTab, _Mapping]]] = ..., subtitle_map: _Optional[_Mapping[str, str]] = ...) -> None: ...
    class PlayerOnboardingLanguageTab(_message.Message):
        __slots__ = ("name", "display_name", "description", "is_selected", "iso2code", "iso3code")
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ISO2CODE_FIELD_NUMBER: _ClassVar[int]
        ISO3CODE_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str
        description: str
        is_selected: bool
        iso2code: str
        iso3code: str
        def __init__(self, name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., is_selected: bool = ..., iso2code: _Optional[str] = ..., iso3code: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerOnboardingWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerOnboardingWidget.Data, _Mapping]] = ...) -> None: ...
