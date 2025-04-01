from feature.communication.data import kids_profile_toggle_pb2 as _kids_profile_toggle_pb2
from feature.communication.data import form_event_pb2 as _form_event_pb2
from feature.communication.data import search_zero_filter_data_pb2 as _search_zero_filter_data_pb2
from feature.communication.data import toggle_widget_visibility_pb2 as _toggle_widget_visibility_pb2
from feature.share import share_info_pb2 as _share_info_pb2
from feature.communication.data import payment_initiated_pb2 as _payment_initiated_pb2
from feature.communication.data import show_tooltip_event_data_pb2 as _show_tooltip_event_data_pb2
from feature.communication.data import player_content_rating_nudge_event_data_pb2 as _player_content_rating_nudge_event_data_pb2
from feature.communication.data import refresh_payment_status_pb2 as _refresh_payment_status_pb2
from feature.communication.data import select_tab_pb2 as _select_tab_pb2
from feature.communication.data import toggle_watchlist_pb2 as _toggle_watchlist_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
    __slots__ = ("message_name", "data")
    class MessageName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        KIDS_PROFILE_TOGGLE_MESSAGE: _ClassVar[Message.MessageName]
        FORM_EVENT_MESSAGE: _ClassVar[Message.MessageName]
        SEARCH_ZERO_FILTERS_MESSAGE: _ClassVar[Message.MessageName]
        SHARE_SCREENSHOT_MESSAGE: _ClassVar[Message.MessageName]
        PAYMENT_INITIATED: _ClassVar[Message.MessageName]
        TOGGLE_WIDGET_VISIBILITY: _ClassVar[Message.MessageName]
        SHOW_TOOLTIP_NEW_HOT_EVENT: _ClassVar[Message.MessageName]
        PLAYER_CONTENT_RATING_NUDGE_EVENT: _ClassVar[Message.MessageName]
        REFRESH_PAYMENT_STATUS: _ClassVar[Message.MessageName]
        SELECT_TAB: _ClassVar[Message.MessageName]
        TOGGLE_WATCHLIST_EVENT: _ClassVar[Message.MessageName]
    KIDS_PROFILE_TOGGLE_MESSAGE: Message.MessageName
    FORM_EVENT_MESSAGE: Message.MessageName
    SEARCH_ZERO_FILTERS_MESSAGE: Message.MessageName
    SHARE_SCREENSHOT_MESSAGE: Message.MessageName
    PAYMENT_INITIATED: Message.MessageName
    TOGGLE_WIDGET_VISIBILITY: Message.MessageName
    SHOW_TOOLTIP_NEW_HOT_EVENT: Message.MessageName
    PLAYER_CONTENT_RATING_NUDGE_EVENT: Message.MessageName
    REFRESH_PAYMENT_STATUS: Message.MessageName
    SELECT_TAB: Message.MessageName
    TOGGLE_WATCHLIST_EVENT: Message.MessageName
    class Data(_message.Message):
        __slots__ = ("disableMessageCaching", "kids_profile_toggle", "form_event", "search_zero_filter_data", "share_info", "payment_initiated", "toggle_widget_visibility", "show_tooltip_event_data", "player_content_rating_nudge_event_data", "refresh_payment_status", "select_tab", "toggle_watchlist")
        DISABLEMESSAGECACHING_FIELD_NUMBER: _ClassVar[int]
        KIDS_PROFILE_TOGGLE_FIELD_NUMBER: _ClassVar[int]
        FORM_EVENT_FIELD_NUMBER: _ClassVar[int]
        SEARCH_ZERO_FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
        SHARE_INFO_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_INITIATED_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_WIDGET_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        SHOW_TOOLTIP_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
        PLAYER_CONTENT_RATING_NUDGE_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
        REFRESH_PAYMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
        SELECT_TAB_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_WATCHLIST_FIELD_NUMBER: _ClassVar[int]
        disableMessageCaching: bool
        kids_profile_toggle: _kids_profile_toggle_pb2.KidsProfileToggle
        form_event: _form_event_pb2.FormEvent
        search_zero_filter_data: _search_zero_filter_data_pb2.SearchZeroFilterData
        share_info: _share_info_pb2.ShareInfo
        payment_initiated: _payment_initiated_pb2.PaymentInitiated
        toggle_widget_visibility: _toggle_widget_visibility_pb2.ToggleWidgetVisibility
        show_tooltip_event_data: _show_tooltip_event_data_pb2.ShowTooltipEventData
        player_content_rating_nudge_event_data: _player_content_rating_nudge_event_data_pb2.PlayerContentRatingNudgeEventData
        refresh_payment_status: _refresh_payment_status_pb2.RefreshPaymentStatus
        select_tab: _select_tab_pb2.SelectTab
        toggle_watchlist: _toggle_watchlist_pb2.ToggleWatchlist
        def __init__(self, disableMessageCaching: bool = ..., kids_profile_toggle: _Optional[_Union[_kids_profile_toggle_pb2.KidsProfileToggle, _Mapping]] = ..., form_event: _Optional[_Union[_form_event_pb2.FormEvent, _Mapping]] = ..., search_zero_filter_data: _Optional[_Union[_search_zero_filter_data_pb2.SearchZeroFilterData, _Mapping]] = ..., share_info: _Optional[_Union[_share_info_pb2.ShareInfo, _Mapping]] = ..., payment_initiated: _Optional[_Union[_payment_initiated_pb2.PaymentInitiated, _Mapping]] = ..., toggle_widget_visibility: _Optional[_Union[_toggle_widget_visibility_pb2.ToggleWidgetVisibility, _Mapping]] = ..., show_tooltip_event_data: _Optional[_Union[_show_tooltip_event_data_pb2.ShowTooltipEventData, _Mapping]] = ..., player_content_rating_nudge_event_data: _Optional[_Union[_player_content_rating_nudge_event_data_pb2.PlayerContentRatingNudgeEventData, _Mapping]] = ..., refresh_payment_status: _Optional[_Union[_refresh_payment_status_pb2.RefreshPaymentStatus, _Mapping]] = ..., select_tab: _Optional[_Union[_select_tab_pb2.SelectTab, _Mapping]] = ..., toggle_watchlist: _Optional[_Union[_toggle_watchlist_pb2.ToggleWatchlist, _Mapping]] = ...) -> None: ...
    MESSAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    message_name: Message.MessageName
    data: Message.Data
    def __init__(self, message_name: _Optional[_Union[Message.MessageName, str]] = ..., data: _Optional[_Union[Message.Data, _Mapping]] = ...) -> None: ...
