from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.quiz import title_icon_combo_pb2 as _title_icon_combo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanCTAWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("is_expandable", "plan_map", "defaultPlanIdentifier", "checkbox", "secondary_cta")
        class PlanMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: PlanCTAWidget.PlanDetails
            def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[PlanCTAWidget.PlanDetails, _Mapping]] = ...) -> None: ...
        IS_EXPANDABLE_FIELD_NUMBER: _ClassVar[int]
        PLAN_MAP_FIELD_NUMBER: _ClassVar[int]
        DEFAULTPLANIDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        CHECKBOX_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        is_expandable: bool
        plan_map: _containers.MessageMap[str, PlanCTAWidget.PlanDetails]
        defaultPlanIdentifier: str
        checkbox: PlanCTAWidget.PaytmCheckbox
        secondary_cta: PlanCTAWidget.CTA
        def __init__(self, is_expandable: bool = ..., plan_map: _Optional[_Mapping[str, PlanCTAWidget.PlanDetails]] = ..., defaultPlanIdentifier: _Optional[str] = ..., checkbox: _Optional[_Union[PlanCTAWidget.PaytmCheckbox, _Mapping]] = ..., secondary_cta: _Optional[_Union[PlanCTAWidget.CTA, _Mapping]] = ...) -> None: ...
    class PlanDetails(_message.Message):
        __slots__ = ("price_details", "callout", "price_info", "cta", "offers")
        PRICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_FIELD_NUMBER: _ClassVar[int]
        PRICE_INFO_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        OFFERS_FIELD_NUMBER: _ClassVar[int]
        price_details: PlanCTAWidget.PriceDetails
        callout: PlanCTAWidget.Callout
        price_info: PlanCTAWidget.PriceInfo
        cta: PlanCTAWidget.CTA
        offers: PlanCTAWidget.Offers
        def __init__(self, price_details: _Optional[_Union[PlanCTAWidget.PriceDetails, _Mapping]] = ..., callout: _Optional[_Union[PlanCTAWidget.Callout, _Mapping]] = ..., price_info: _Optional[_Union[PlanCTAWidget.PriceInfo, _Mapping]] = ..., cta: _Optional[_Union[PlanCTAWidget.CTA, _Mapping]] = ..., offers: _Optional[_Union[PlanCTAWidget.Offers, _Mapping]] = ...) -> None: ...
    class Offers(_message.Message):
        __slots__ = ("header", "collapsed_state_data", "expanded_state_data", "backgroundColor", "actions")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        COLLAPSED_STATE_DATA_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_STATE_DATA_FIELD_NUMBER: _ClassVar[int]
        BACKGROUNDCOLOR_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        header: _title_icon_combo_pb2.TitleIconCombo
        collapsed_state_data: PlanCTAWidget.StateData
        expanded_state_data: PlanCTAWidget.StateData
        backgroundColor: PlanCTAWidget.Color
        actions: _actions_pb2.Actions
        def __init__(self, header: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ..., collapsed_state_data: _Optional[_Union[PlanCTAWidget.StateData, _Mapping]] = ..., expanded_state_data: _Optional[_Union[PlanCTAWidget.StateData, _Mapping]] = ..., backgroundColor: _Optional[_Union[PlanCTAWidget.Color, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class StateData(_message.Message):
        __slots__ = ("text_list", "icon")
        TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        text_list: _containers.RepeatedCompositeFieldContainer[_title_icon_combo_pb2.TitleIconCombo]
        icon: str
        def __init__(self, text_list: _Optional[_Iterable[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]]] = ..., icon: _Optional[str] = ...) -> None: ...
    class PriceDetails(_message.Message):
        __slots__ = ("price_description",)
        PRICE_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        price_description: _containers.RepeatedCompositeFieldContainer[PlanCTAWidget.PriceDescription]
        def __init__(self, price_description: _Optional[_Iterable[_Union[PlanCTAWidget.PriceDescription, _Mapping]]] = ...) -> None: ...
    class PriceDescription(_message.Message):
        __slots__ = ("text", "value")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        text: str
        value: str
        def __init__(self, text: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PriceInfo(_message.Message):
        __slots__ = ("value", "strikethrough_text", "callout")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        STRIKETHROUGH_TEXT_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_FIELD_NUMBER: _ClassVar[int]
        value: str
        strikethrough_text: str
        callout: PlanCTAWidget.Callout
        def __init__(self, value: _Optional[str] = ..., strikethrough_text: _Optional[str] = ..., callout: _Optional[_Union[PlanCTAWidget.Callout, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("text", "icon", "actions", "alt")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon: str
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        def __init__(self, text: _Optional[str] = ..., icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class PaytmCheckbox(_message.Message):
        __slots__ = ("icon", "text")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        icon: str
        text: str
        def __init__(self, icon: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    class Callout(_message.Message):
        __slots__ = ("text", "color")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        text: str
        color: str
        def __init__(self, text: _Optional[str] = ..., color: _Optional[str] = ...) -> None: ...
    class Color(_message.Message):
        __slots__ = ("primary_color", "secondary_color")
        PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        primary_color: str
        secondary_color: str
        def __init__(self, primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlanCTAWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlanCTAWidget.Data, _Mapping]] = ...) -> None: ...
