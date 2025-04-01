from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayAdWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class TypeOfAd(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FirstParty: _ClassVar[DisplayAdWidget.TypeOfAd]
        ThirdParty: _ClassVar[DisplayAdWidget.TypeOfAd]
    FirstParty: DisplayAdWidget.TypeOfAd
    ThirdParty: DisplayAdWidget.TypeOfAd
    class PlacementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IMAGE: _ClassVar[DisplayAdWidget.PlacementType]
        VIDEO: _ClassVar[DisplayAdWidget.PlacementType]
        SKINNY: _ClassVar[DisplayAdWidget.PlacementType]
    IMAGE: DisplayAdWidget.PlacementType
    VIDEO: DisplayAdWidget.PlacementType
    SKINNY: DisplayAdWidget.PlacementType
    class Data(_message.Message):
        __slots__ = ("type", "placement", "refresh_url", "refresh_info", "actions", "server_url", "payload")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PLACEMENT_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        SERVER_URL_FIELD_NUMBER: _ClassVar[int]
        PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        type: DisplayAdWidget.TypeOfAd
        placement: DisplayAdWidget.PlacementType
        refresh_url: str
        refresh_info: DisplayAdWidget.RefreshInfo
        actions: _actions_pb2.Actions
        server_url: str
        payload: str
        def __init__(self, type: _Optional[_Union[DisplayAdWidget.TypeOfAd, str]] = ..., placement: _Optional[_Union[DisplayAdWidget.PlacementType, str]] = ..., refresh_url: _Optional[str] = ..., refresh_info: _Optional[_Union[DisplayAdWidget.RefreshInfo, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., server_url: _Optional[str] = ..., payload: _Optional[str] = ...) -> None: ...
    class RefreshInfo(_message.Message):
        __slots__ = ("max_age_ms", "refresh_url")
        MAX_AGE_MS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        max_age_ms: int
        refresh_url: str
        def __init__(self, max_age_ms: _Optional[int] = ..., refresh_url: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DisplayAdWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DisplayAdWidget.Data, _Mapping]] = ...) -> None: ...
