from feature.download import download_content_state_pb2 as _download_content_state_pb2
from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadStatusWidget(_message.Message):
    __slots__ = ("widget_commons", "user_facing_action", "contentState")
    class UserFacingActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BFF_ACTION: _ClassVar[DownloadStatusWidget.UserFacingActionType]
        SHOW_TOAST: _ClassVar[DownloadStatusWidget.UserFacingActionType]
        SHOW_SHEET: _ClassVar[DownloadStatusWidget.UserFacingActionType]
    BFF_ACTION: DownloadStatusWidget.UserFacingActionType
    SHOW_TOAST: DownloadStatusWidget.UserFacingActionType
    SHOW_SHEET: DownloadStatusWidget.UserFacingActionType
    class CTAType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISMISS: _ClassVar[DownloadStatusWidget.CTAType]
        DELETE: _ClassVar[DownloadStatusWidget.CTAType]
    DISMISS: DownloadStatusWidget.CTAType
    DELETE: DownloadStatusWidget.CTAType
    class UserFacingAction(_message.Message):
        __slots__ = ("type", "value")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        type: DownloadStatusWidget.UserFacingActionType
        value: DownloadStatusWidget.UserFacingActionValue
        def __init__(self, type: _Optional[_Union[DownloadStatusWidget.UserFacingActionType, str]] = ..., value: _Optional[_Union[DownloadStatusWidget.UserFacingActionValue, _Mapping]] = ...) -> None: ...
    class UserFacingActionValue(_message.Message):
        __slots__ = ("actions", "toast", "alert")
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TOAST_FIELD_NUMBER: _ClassVar[int]
        ALERT_FIELD_NUMBER: _ClassVar[int]
        actions: _actions_pb2.Actions
        toast: DownloadStatusWidget.ShowToast
        alert: DownloadStatusWidget.ShowActionSheet
        def __init__(self, actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., toast: _Optional[_Union[DownloadStatusWidget.ShowToast, _Mapping]] = ..., alert: _Optional[_Union[DownloadStatusWidget.ShowActionSheet, _Mapping]] = ...) -> None: ...
    class ShowToast(_message.Message):
        __slots__ = ("text",)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    class ShowActionSheet(_message.Message):
        __slots__ = ("text", "desc", "primary_cta", "secondary_cta")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        text: str
        desc: str
        primary_cta: DownloadStatusWidget.CTA
        secondary_cta: DownloadStatusWidget.CTA
        def __init__(self, text: _Optional[str] = ..., desc: _Optional[str] = ..., primary_cta: _Optional[_Union[DownloadStatusWidget.CTA, _Mapping]] = ..., secondary_cta: _Optional[_Union[DownloadStatusWidget.CTA, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("title", "type", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        type: DownloadStatusWidget.CTAType
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., type: _Optional[_Union[DownloadStatusWidget.CTAType, str]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    USER_FACING_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTENTSTATE_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    user_facing_action: DownloadStatusWidget.UserFacingAction
    contentState: _download_content_state_pb2.DownloadContentState
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., user_facing_action: _Optional[_Union[DownloadStatusWidget.UserFacingAction, _Mapping]] = ..., contentState: _Optional[_Union[_download_content_state_pb2.DownloadContentState, _Mapping]] = ...) -> None: ...
