from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import device_manager_pb2 as _device_manager_pb2
from widget import membership_actions_pb2 as _membership_actions_pb2
from widget import mobile_detail_pb2 as _mobile_detail_pb2
from widget import payment_instrument_pb2 as _payment_instrument_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountSettingsContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("widget_content", "actions")
        WIDGET_CONTENT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        widget_content: _containers.RepeatedCompositeFieldContainer[AccountSettingsContainerWidget.WidgetContent]
        actions: _actions_pb2.Actions
        def __init__(self, widget_content: _Optional[_Iterable[_Union[AccountSettingsContainerWidget.WidgetContent, _Mapping]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class WidgetContent(_message.Message):
        __slots__ = ("membership_actions", "mobile_detail", "device_manager", "payment_instrument")
        MEMBERSHIP_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        MOBILE_DETAIL_FIELD_NUMBER: _ClassVar[int]
        DEVICE_MANAGER_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_INSTRUMENT_FIELD_NUMBER: _ClassVar[int]
        membership_actions: _membership_actions_pb2.MembershipActionsWidget
        mobile_detail: _mobile_detail_pb2.MobileDetailWidget
        device_manager: _device_manager_pb2.DeviceManagerWidget
        payment_instrument: _payment_instrument_pb2.PaymentInstrumentWidget
        def __init__(self, membership_actions: _Optional[_Union[_membership_actions_pb2.MembershipActionsWidget, _Mapping]] = ..., mobile_detail: _Optional[_Union[_mobile_detail_pb2.MobileDetailWidget, _Mapping]] = ..., device_manager: _Optional[_Union[_device_manager_pb2.DeviceManagerWidget, _Mapping]] = ..., payment_instrument: _Optional[_Union[_payment_instrument_pb2.PaymentInstrumentWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AccountSettingsContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AccountSettingsContainerWidget.Data, _Mapping]] = ...) -> None: ...
