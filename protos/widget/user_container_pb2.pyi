from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import profiles_pb2 as _profiles_pb2
from widget import subscriptions_header_pb2 as _subscriptions_header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserContainerWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("widgets",)
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        widgets: _containers.RepeatedCompositeFieldContainer[UserContainerWidget.UserContainerWidgets]
        def __init__(self, widgets: _Optional[_Iterable[_Union[UserContainerWidget.UserContainerWidgets, _Mapping]]] = ...) -> None: ...
    class UserContainerWidgets(_message.Message):
        __slots__ = ("subscriptions_header", "profiles")
        SUBSCRIPTIONS_HEADER_FIELD_NUMBER: _ClassVar[int]
        PROFILES_FIELD_NUMBER: _ClassVar[int]
        subscriptions_header: _subscriptions_header_pb2.SubscriptionsHeaderWidget
        profiles: _profiles_pb2.ProfilesWidget
        def __init__(self, subscriptions_header: _Optional[_Union[_subscriptions_header_pb2.SubscriptionsHeaderWidget, _Mapping]] = ..., profiles: _Optional[_Union[_profiles_pb2.ProfilesWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: UserContainerWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[UserContainerWidget.Data, _Mapping]] = ...) -> None: ...
