from base import widget_commons_pb2 as _widget_commons_pb2
from widget import media_container_pb2 as _media_container_pb2
from widget import hero_gec_pb2 as _hero_gec_pb2
from widget import media_callout_pb2 as _media_callout_pb2
from widget import media_collection_pb2 as _media_collection_pb2
from widget import top3_template_pb2 as _top3_template_pb2
from widget import text_prompt_pb2 as _text_prompt_pb2
from widget import hero_pb2 as _hero_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoryWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("common_elements", "background_elements", "foreground_elements")
        class CommonElements(_message.Message):
            __slots__ = ("number_of_templates", "intro_lottie_duration_in_ms", "story_templates_duration_in_ms")
            NUMBER_OF_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
            INTRO_LOTTIE_DURATION_IN_MS_FIELD_NUMBER: _ClassVar[int]
            STORY_TEMPLATES_DURATION_IN_MS_FIELD_NUMBER: _ClassVar[int]
            number_of_templates: int
            intro_lottie_duration_in_ms: int
            story_templates_duration_in_ms: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, number_of_templates: _Optional[int] = ..., intro_lottie_duration_in_ms: _Optional[int] = ..., story_templates_duration_in_ms: _Optional[_Iterable[int]] = ...) -> None: ...
        class BackgroundElements(_message.Message):
            __slots__ = ("background_element", "static_background_fallback_image")
            BACKGROUND_ELEMENT_FIELD_NUMBER: _ClassVar[int]
            STATIC_BACKGROUND_FALLBACK_IMAGE_FIELD_NUMBER: _ClassVar[int]
            background_element: _media_container_pb2.MediaContainerWidget
            static_background_fallback_image: _media_container_pb2.MediaContainerWidget
            def __init__(self, background_element: _Optional[_Union[_media_container_pb2.MediaContainerWidget, _Mapping]] = ..., static_background_fallback_image: _Optional[_Union[_media_container_pb2.MediaContainerWidget, _Mapping]] = ...) -> None: ...
        class ForegroundElements(_message.Message):
            __slots__ = ("templates",)
            TEMPLATES_FIELD_NUMBER: _ClassVar[int]
            templates: _containers.RepeatedCompositeFieldContainer[StoryWidget.Data.Templates]
            def __init__(self, templates: _Optional[_Iterable[_Union[StoryWidget.Data.Templates, _Mapping]]] = ...) -> None: ...
        class Templates(_message.Message):
            __slots__ = ("prompt_template", "callout_template", "collection_template", "top3_template", "text_prompt_template", "hero_template")
            PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            CALLOUT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            COLLECTION_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            TOP3_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            TEXT_PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            HERO_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
            prompt_template: _hero_gec_pb2.HeroGECWidget
            callout_template: _media_callout_pb2.MediaCalloutWidget
            collection_template: _media_collection_pb2.MediaCollectionWidget
            top3_template: _top3_template_pb2.Top3TemplateWidget
            text_prompt_template: _text_prompt_pb2.TextPromptWidget
            hero_template: _hero_pb2.HeroWidget
            def __init__(self, prompt_template: _Optional[_Union[_hero_gec_pb2.HeroGECWidget, _Mapping]] = ..., callout_template: _Optional[_Union[_media_callout_pb2.MediaCalloutWidget, _Mapping]] = ..., collection_template: _Optional[_Union[_media_collection_pb2.MediaCollectionWidget, _Mapping]] = ..., top3_template: _Optional[_Union[_top3_template_pb2.Top3TemplateWidget, _Mapping]] = ..., text_prompt_template: _Optional[_Union[_text_prompt_pb2.TextPromptWidget, _Mapping]] = ..., hero_template: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ...) -> None: ...
        COMMON_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        FOREGROUND_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        common_elements: StoryWidget.Data.CommonElements
        background_elements: StoryWidget.Data.BackgroundElements
        foreground_elements: StoryWidget.Data.ForegroundElements
        def __init__(self, common_elements: _Optional[_Union[StoryWidget.Data.CommonElements, _Mapping]] = ..., background_elements: _Optional[_Union[StoryWidget.Data.BackgroundElements, _Mapping]] = ..., foreground_elements: _Optional[_Union[StoryWidget.Data.ForegroundElements, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: StoryWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[StoryWidget.Data, _Mapping]] = ...) -> None: ...
