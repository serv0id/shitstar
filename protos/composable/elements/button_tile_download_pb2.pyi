from base import actions_pb2 as _actions_pb2
from feature.download import download_info_pb2 as _download_info_pb2
from composable.elements import button_tile_pb2 as _button_tile_pb2
from composable.elements import image_pb2 as _image_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonTileDownload(_message.Message):
    __slots__ = ("states", "info", "actions", "poster_title", "poster_image", "composable_commons")
    class DownloadButtonStates(_message.Message):
        __slots__ = ("initial", "completed", "inProgress", "paused", "failed", "fetchWidget", "waitingForWifi", "expired", "queued", "fetchWidgetCompleted", "initialToInProgress", "initialToQueued", "queuedToInProgress", "deleting")
        INITIAL_FIELD_NUMBER: _ClassVar[int]
        COMPLETED_FIELD_NUMBER: _ClassVar[int]
        INPROGRESS_FIELD_NUMBER: _ClassVar[int]
        PAUSED_FIELD_NUMBER: _ClassVar[int]
        FAILED_FIELD_NUMBER: _ClassVar[int]
        FETCHWIDGET_FIELD_NUMBER: _ClassVar[int]
        WAITINGFORWIFI_FIELD_NUMBER: _ClassVar[int]
        EXPIRED_FIELD_NUMBER: _ClassVar[int]
        QUEUED_FIELD_NUMBER: _ClassVar[int]
        FETCHWIDGETCOMPLETED_FIELD_NUMBER: _ClassVar[int]
        INITIALTOINPROGRESS_FIELD_NUMBER: _ClassVar[int]
        INITIALTOQUEUED_FIELD_NUMBER: _ClassVar[int]
        QUEUEDTOINPROGRESS_FIELD_NUMBER: _ClassVar[int]
        DELETING_FIELD_NUMBER: _ClassVar[int]
        initial: _button_tile_pb2.ButtonTileView
        completed: _button_tile_pb2.ButtonTileView
        inProgress: _button_tile_pb2.ButtonTileView
        paused: _button_tile_pb2.ButtonTileView
        failed: _button_tile_pb2.ButtonTileView
        fetchWidget: _button_tile_pb2.ButtonTileView
        waitingForWifi: _button_tile_pb2.ButtonTileView
        expired: _button_tile_pb2.ButtonTileView
        queued: _button_tile_pb2.ButtonTileView
        fetchWidgetCompleted: _button_tile_pb2.ButtonTileView
        initialToInProgress: _button_tile_pb2.ButtonTileView
        initialToQueued: _button_tile_pb2.ButtonTileView
        queuedToInProgress: _button_tile_pb2.ButtonTileView
        deleting: _button_tile_pb2.ButtonTileView
        def __init__(self, initial: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., completed: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., inProgress: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., paused: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., failed: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., fetchWidget: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., waitingForWifi: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., expired: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., queued: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., fetchWidgetCompleted: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., initialToInProgress: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., initialToQueued: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., queuedToInProgress: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., deleting: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ...) -> None: ...
    STATES_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    POSTER_TITLE_FIELD_NUMBER: _ClassVar[int]
    POSTER_IMAGE_FIELD_NUMBER: _ClassVar[int]
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    states: ButtonTileDownload.DownloadButtonStates
    info: _download_info_pb2.DownloadInfo
    actions: _actions_pb2.Actions
    poster_title: str
    poster_image: _image_pb2.Image.Source
    composable_commons: _commons_pb2.ComposableCommons
    def __init__(self, states: _Optional[_Union[ButtonTileDownload.DownloadButtonStates, _Mapping]] = ..., info: _Optional[_Union[_download_info_pb2.DownloadInfo, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., poster_title: _Optional[str] = ..., poster_image: _Optional[_Union[_image_pb2.Image.Source, _Mapping]] = ..., composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ...) -> None: ...
