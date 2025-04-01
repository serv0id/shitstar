from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.autoplay import autoplay_info_pb2 as _autoplay_info_pb2
from feature.image import image_pb2 as _image_pb2
from widget import unified_attention_tray_content_info_pb2 as _unified_attention_tray_content_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UatVerticalContentPosterWidget(_message.Message):
    __slots__ = ("widget_commons", "data", "expanded_state_metadata")
    class Data(_message.Message):
        __slots__ = ("default_image", "content_info", "autoplay_info", "alt")
        DEFAULT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        AUTOPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        default_image: _image_pb2.Image
        content_info: _unified_attention_tray_content_info_pb2.UnifiedAttentionTrayContentInfoWidget
        autoplay_info: _autoplay_info_pb2.AutoplayInfo
        alt: _accessibility_pb2.Accessibility
        def __init__(self, default_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[_unified_attention_tray_content_info_pb2.UnifiedAttentionTrayContentInfoWidget, _Mapping]] = ..., autoplay_info: _Optional[_Union[_autoplay_info_pb2.AutoplayInfo, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class ExpandedStateMetaData(_message.Message):
        __slots__ = ("expanded_image", "title_cutout_image", "title", "expand_delay_in_ms", "on_expanded_actions")
        EXPANDED_IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        EXPAND_DELAY_IN_MS_FIELD_NUMBER: _ClassVar[int]
        ON_EXPANDED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        expanded_image: _image_pb2.Image
        title_cutout_image: _image_pb2.Image
        title: str
        expand_delay_in_ms: int
        on_expanded_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, expanded_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title_cutout_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., expand_delay_in_ms: _Optional[int] = ..., on_expanded_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    EXPANDED_STATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: UatVerticalContentPosterWidget.Data
    expanded_state_metadata: UatVerticalContentPosterWidget.ExpandedStateMetaData
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[UatVerticalContentPosterWidget.Data, _Mapping]] = ..., expanded_state_metadata: _Optional[_Union[UatVerticalContentPosterWidget.ExpandedStateMetaData, _Mapping]] = ...) -> None: ...
