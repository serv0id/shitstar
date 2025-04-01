from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.branding import brand_pb2 as _brand_pb2
from widget import logo_pb2 as _logo_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrelaunchHeroWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("hero_img", "hero_info", "tnc", "language_selector")
        HERO_IMG_FIELD_NUMBER: _ClassVar[int]
        HERO_INFO_FIELD_NUMBER: _ClassVar[int]
        TNC_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        hero_img: _image_pb2.Image
        hero_info: PrelaunchHeroWidget.HeroInfo
        tnc: str
        language_selector: PrelaunchHeroWidget.LanguageSelector
        def __init__(self, hero_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., hero_info: _Optional[_Union[PrelaunchHeroWidget.HeroInfo, _Mapping]] = ..., tnc: _Optional[str] = ..., language_selector: _Optional[_Union[PrelaunchHeroWidget.LanguageSelector, _Mapping]] = ...) -> None: ...
    class HeroInfo(_message.Message):
        __slots__ = ("logo", "title", "subtitle", "info_msg", "register_btn", "launch_time", "brand_details")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        INFO_MSG_FIELD_NUMBER: _ClassVar[int]
        REGISTER_BTN_FIELD_NUMBER: _ClassVar[int]
        LAUNCH_TIME_FIELD_NUMBER: _ClassVar[int]
        BRAND_DETAILS_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        title: PrelaunchHeroWidget.RichTextTitle
        subtitle: str
        info_msg: str
        register_btn: PrelaunchHeroWidget.RegisterBtn
        launch_time: PrelaunchHeroWidget.Countdown
        brand_details: _logo_pb2.LogoWidget
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title: _Optional[_Union[PrelaunchHeroWidget.RichTextTitle, _Mapping]] = ..., subtitle: _Optional[str] = ..., info_msg: _Optional[str] = ..., register_btn: _Optional[_Union[PrelaunchHeroWidget.RegisterBtn, _Mapping]] = ..., launch_time: _Optional[_Union[PrelaunchHeroWidget.Countdown, _Mapping]] = ..., brand_details: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ...) -> None: ...
    class RichTextTitle(_message.Message):
        __slots__ = ("highlighted_text", "text", "highlight_color")
        HIGHLIGHTED_TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        HIGHLIGHT_COLOR_FIELD_NUMBER: _ClassVar[int]
        highlighted_text: str
        text: str
        highlight_color: str
        def __init__(self, highlighted_text: _Optional[str] = ..., text: _Optional[str] = ..., highlight_color: _Optional[str] = ...) -> None: ...
    class RegisterBtn(_message.Message):
        __slots__ = ("icon_name", "label", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Countdown(_message.Message):
        __slots__ = ("launch_date", "count_down", "current_server_time")
        LAUNCH_DATE_FIELD_NUMBER: _ClassVar[int]
        COUNT_DOWN_FIELD_NUMBER: _ClassVar[int]
        CURRENT_SERVER_TIME_FIELD_NUMBER: _ClassVar[int]
        launch_date: int
        count_down: PrelaunchHeroWidget.Intervals
        current_server_time: int
        def __init__(self, launch_date: _Optional[int] = ..., count_down: _Optional[_Union[PrelaunchHeroWidget.Intervals, _Mapping]] = ..., current_server_time: _Optional[int] = ...) -> None: ...
    class Intervals(_message.Message):
        __slots__ = ("day", "hrs", "mins", "seconds")
        DAY_FIELD_NUMBER: _ClassVar[int]
        HRS_FIELD_NUMBER: _ClassVar[int]
        MINS_FIELD_NUMBER: _ClassVar[int]
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        day: str
        hrs: str
        mins: str
        seconds: str
        def __init__(self, day: _Optional[str] = ..., hrs: _Optional[str] = ..., mins: _Optional[str] = ..., seconds: _Optional[str] = ...) -> None: ...
    class LanguageSelector(_message.Message):
        __slots__ = ("choose_language_text", "languages")
        CHOOSE_LANGUAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        choose_language_text: str
        languages: _containers.RepeatedCompositeFieldContainer[PrelaunchHeroWidget.LanguageOption]
        def __init__(self, choose_language_text: _Optional[str] = ..., languages: _Optional[_Iterable[_Union[PrelaunchHeroWidget.LanguageOption, _Mapping]]] = ...) -> None: ...
    class LanguageOption(_message.Message):
        __slots__ = ("iso", "flag", "label", "is_selected", "change_lang_action")
        ISO_FIELD_NUMBER: _ClassVar[int]
        FLAG_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        CHANGE_LANG_ACTION_FIELD_NUMBER: _ClassVar[int]
        iso: str
        flag: _image_pb2.Image
        label: str
        is_selected: bool
        change_lang_action: _actions_pb2.Actions
        def __init__(self, iso: _Optional[str] = ..., flag: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., label: _Optional[str] = ..., is_selected: bool = ..., change_lang_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PrelaunchHeroWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PrelaunchHeroWidget.Data, _Mapping]] = ...) -> None: ...
