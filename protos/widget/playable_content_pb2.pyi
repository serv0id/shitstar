from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.download import download_info_pb2 as _download_info_pb2
from feature.image import image_pb2 as _image_pb2
from feature.cw import cw_info_pb2 as _cw_info_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayableContentWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("poster", "title", "tags", "description", "download_option", "cw_info", "live_tag", "content_id", "actions", "is_focused", "play", "static_badge", "play_badge", "identifier")
        POSTER_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_OPTION_FIELD_NUMBER: _ClassVar[int]
        CW_INFO_FIELD_NUMBER: _ClassVar[int]
        LIVE_TAG_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        IS_FOCUSED_FIELD_NUMBER: _ClassVar[int]
        PLAY_FIELD_NUMBER: _ClassVar[int]
        STATIC_BADGE_FIELD_NUMBER: _ClassVar[int]
        PLAY_BADGE_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        poster: _image_pb2.Image
        title: str
        tags: _containers.RepeatedCompositeFieldContainer[PlayableContentWidget.Tag]
        description: str
        download_option: PlayableContentWidget.DownloadOption
        cw_info: _cw_info_pb2.CwInfo
        live_tag: str
        content_id: str
        actions: _actions_pb2.Actions
        is_focused: bool
        play: _illustration_pb2.Illustration
        static_badge: str
        play_badge: str
        identifier: str
        def __init__(self, poster: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[PlayableContentWidget.Tag, _Mapping]]] = ..., description: _Optional[str] = ..., download_option: _Optional[_Union[PlayableContentWidget.DownloadOption, _Mapping]] = ..., cw_info: _Optional[_Union[_cw_info_pb2.CwInfo, _Mapping]] = ..., live_tag: _Optional[str] = ..., content_id: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., is_focused: bool = ..., play: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., static_badge: _Optional[str] = ..., play_badge: _Optional[str] = ..., identifier: _Optional[str] = ...) -> None: ...
    class DownloadOption(_message.Message):
        __slots__ = ("title", "items", "selected_id", "footer", "download_info", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        SELECTED_ID_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_INFO_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        items: _containers.RepeatedCompositeFieldContainer[PlayableContentWidget.DownloadOptionItem]
        selected_id: str
        footer: PlayableContentWidget.Footer
        download_info: _download_info_pb2.DownloadInfo
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., items: _Optional[_Iterable[_Union[PlayableContentWidget.DownloadOptionItem, _Mapping]]] = ..., selected_id: _Optional[str] = ..., footer: _Optional[_Union[PlayableContentWidget.Footer, _Mapping]] = ..., download_info: _Optional[_Union[_download_info_pb2.DownloadInfo, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class DownloadOptionItem(_message.Message):
        __slots__ = ("id", "resolution", "size")
        ID_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        id: str
        resolution: str
        size: str
        def __init__(self, id: _Optional[str] = ..., resolution: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("description", "button_text", "actions")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BUTTON_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        description: str
        button_text: str
        actions: _actions_pb2.Actions
        def __init__(self, description: _Optional[str] = ..., button_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("value", "actions")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        value: str
        actions: _actions_pb2.Actions
        def __init__(self, value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayableContentWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayableContentWidget.Data, _Mapping]] = ...) -> None: ...
