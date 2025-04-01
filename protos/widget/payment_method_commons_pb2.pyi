from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.payment import payment_gateway_pb2 as _payment_gateway_pb2
from widget import text_list_pb2 as _text_list_pb2
from widget import refreshable_status_pb2 as _refreshable_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodCommonsWidget(_message.Message):
    __slots__ = ("widget_commons", "method_name", "method_image", "method_features", "method_info", "gateways", "is_expanded", "selected_method_meta", "payment_method_loading_state", "payment_method_error_state", "tab_open_actions")
    class SelectedMethodMeta(_message.Message):
        __slots__ = ("title", "method_warning_text", "method_item_warning_text")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        METHOD_WARNING_TEXT_FIELD_NUMBER: _ClassVar[int]
        METHOD_ITEM_WARNING_TEXT_FIELD_NUMBER: _ClassVar[int]
        title: str
        method_warning_text: str
        method_item_warning_text: str
        def __init__(self, title: _Optional[str] = ..., method_warning_text: _Optional[str] = ..., method_item_warning_text: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_IMAGE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FEATURES_FIELD_NUMBER: _ClassVar[int]
    METHOD_INFO_FIELD_NUMBER: _ClassVar[int]
    GATEWAYS_FIELD_NUMBER: _ClassVar[int]
    IS_EXPANDED_FIELD_NUMBER: _ClassVar[int]
    SELECTED_METHOD_META_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_LOADING_STATE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_ERROR_STATE_FIELD_NUMBER: _ClassVar[int]
    TAB_OPEN_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    method_name: str
    method_image: _image_pb2.Image
    method_features: _text_list_pb2.TextListWidget
    method_info: _text_list_pb2.TextListWidget
    gateways: _containers.RepeatedCompositeFieldContainer[_payment_gateway_pb2.PaymentGateway]
    is_expanded: bool
    selected_method_meta: PaymentMethodCommonsWidget.SelectedMethodMeta
    payment_method_loading_state: _refreshable_status_pb2.RefreshableStatusWidget
    payment_method_error_state: _refreshable_status_pb2.RefreshableStatusWidget
    tab_open_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., method_name: _Optional[str] = ..., method_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., method_features: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., method_info: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., gateways: _Optional[_Iterable[_Union[_payment_gateway_pb2.PaymentGateway, _Mapping]]] = ..., is_expanded: bool = ..., selected_method_meta: _Optional[_Union[PaymentMethodCommonsWidget.SelectedMethodMeta, _Mapping]] = ..., payment_method_loading_state: _Optional[_Union[_refreshable_status_pb2.RefreshableStatusWidget, _Mapping]] = ..., payment_method_error_state: _Optional[_Union[_refreshable_status_pb2.RefreshableStatusWidget, _Mapping]] = ..., tab_open_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
