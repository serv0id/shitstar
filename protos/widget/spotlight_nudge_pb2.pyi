from base import template_pb2 as _template_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.trackers import tracker_pb2 as _tracker_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpotlightNudgeWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ImageSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE: _ClassVar[SpotlightNudgeWidget.ImageSourceType]
        ICON: _ClassVar[SpotlightNudgeWidget.ImageSourceType]
        LOTTIE: _ClassVar[SpotlightNudgeWidget.ImageSourceType]
    IMAGE: SpotlightNudgeWidget.ImageSourceType
    ICON: SpotlightNudgeWidget.ImageSourceType
    LOTTIE: SpotlightNudgeWidget.ImageSourceType
    class Data(_message.Message):
        __slots__ = ("image_source_type", "title", "sub_title", "primary_cta", "dismiss_icon", "impression_tracker", "nudge_img", "nudge_lottie", "nudge_icon_name")
        IMAGE_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        DISMISS_ICON_FIELD_NUMBER: _ClassVar[int]
        IMPRESSION_TRACKER_FIELD_NUMBER: _ClassVar[int]
        NUDGE_IMG_FIELD_NUMBER: _ClassVar[int]
        NUDGE_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        NUDGE_ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        image_source_type: SpotlightNudgeWidget.ImageSourceType
        title: str
        sub_title: str
        primary_cta: SpotlightNudgeWidget.PrimaryCTA
        dismiss_icon: SpotlightNudgeWidget.DismissIcon
        impression_tracker: _tracker_pb2.Tracker
        nudge_img: _image_pb2.Image
        nudge_lottie: str
        nudge_icon_name: str
        def __init__(self, image_source_type: _Optional[_Union[SpotlightNudgeWidget.ImageSourceType, str]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., primary_cta: _Optional[_Union[SpotlightNudgeWidget.PrimaryCTA, _Mapping]] = ..., dismiss_icon: _Optional[_Union[SpotlightNudgeWidget.DismissIcon, _Mapping]] = ..., impression_tracker: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ..., nudge_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., nudge_lottie: _Optional[str] = ..., nudge_icon_name: _Optional[str] = ...) -> None: ...
    class PrimaryCTA(_message.Message):
        __slots__ = ("text", "actions", "click_tracker")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CLICK_TRACKER_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        click_tracker: _tracker_pb2.Tracker
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., click_tracker: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ...) -> None: ...
    class DismissIcon(_message.Message):
        __slots__ = ("icon_name", "click_tracker")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        CLICK_TRACKER_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        click_tracker: _tracker_pb2.Tracker
        def __init__(self, icon_name: _Optional[str] = ..., click_tracker: _Optional[_Union[_tracker_pb2.Tracker, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SpotlightNudgeWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SpotlightNudgeWidget.Data, _Mapping]] = ...) -> None: ...
