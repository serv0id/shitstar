from base import widget_commons_pb2 as _widget_commons_pb2
from feature.payment import validations_pb2 as _validations_pb2
from feature.image import image_pb2 as _image_pb2
from feature.payment import restrictions_pb2 as _restrictions_pb2
from base import actions_pb2 as _actions_pb2
from widget import text_list_pb2 as _text_list_pb2
from widget import hero_pb2 as _hero_pb2
from widget import refreshable_status_pb2 as _refreshable_status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RedeemCouponWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("hero_widget", "input", "cta", "text_list", "success_response")
        HERO_WIDGET_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
        hero_widget: _hero_pb2.HeroWidget
        input: RedeemCouponWidget.Input
        cta: RedeemCouponWidget.Cta
        text_list: _text_list_pb2.TextListWidget
        success_response: _refreshable_status_pb2.RefreshableStatusWidget
        def __init__(self, hero_widget: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ..., input: _Optional[_Union[RedeemCouponWidget.Input, _Mapping]] = ..., cta: _Optional[_Union[RedeemCouponWidget.Cta, _Mapping]] = ..., text_list: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., success_response: _Optional[_Union[_refreshable_status_pb2.RefreshableStatusWidget, _Mapping]] = ...) -> None: ...
    class Input(_message.Message):
        __slots__ = ("title", "placeholder", "default_value", "validations", "restrictions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
        RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        placeholder: str
        default_value: str
        validations: _containers.RepeatedCompositeFieldContainer[_validations_pb2.Validation]
        restrictions: _containers.RepeatedCompositeFieldContainer[_restrictions_pb2.Restriction]
        def __init__(self, title: _Optional[str] = ..., placeholder: _Optional[str] = ..., default_value: _Optional[str] = ..., validations: _Optional[_Iterable[_Union[_validations_pb2.Validation, _Mapping]]] = ..., restrictions: _Optional[_Iterable[_Union[_restrictions_pb2.Restriction, _Mapping]]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: RedeemCouponWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[RedeemCouponWidget.Data, _Mapping]] = ...) -> None: ...
