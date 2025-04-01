# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/communication/message.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'feature/communication/message.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.communication.data import kids_profile_toggle_pb2 as feature_dot_communication_dot_data_dot_kids__profile__toggle__pb2
from feature.communication.data import form_event_pb2 as feature_dot_communication_dot_data_dot_form__event__pb2
from feature.communication.data import search_zero_filter_data_pb2 as feature_dot_communication_dot_data_dot_search__zero__filter__data__pb2
from feature.communication.data import toggle_widget_visibility_pb2 as feature_dot_communication_dot_data_dot_toggle__widget__visibility__pb2
from feature.share import share_info_pb2 as feature_dot_share_dot_share__info__pb2
from feature.communication.data import payment_initiated_pb2 as feature_dot_communication_dot_data_dot_payment__initiated__pb2
from feature.communication.data import show_tooltip_event_data_pb2 as feature_dot_communication_dot_data_dot_show__tooltip__event__data__pb2
from feature.communication.data import player_content_rating_nudge_event_data_pb2 as feature_dot_communication_dot_data_dot_player__content__rating__nudge__event__data__pb2
from feature.communication.data import refresh_payment_status_pb2 as feature_dot_communication_dot_data_dot_refresh__payment__status__pb2
from feature.communication.data import select_tab_pb2 as feature_dot_communication_dot_data_dot_select__tab__pb2
from feature.communication.data import toggle_watchlist_pb2 as feature_dot_communication_dot_data_dot_toggle__watchlist__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#feature/communication/message.proto\x12\x15\x66\x65\x61ture.communication\x1a\x34\x66\x65\x61ture/communication/data/kids_profile_toggle.proto\x1a+feature/communication/data/form_event.proto\x1a\x38\x66\x65\x61ture/communication/data/search_zero_filter_data.proto\x1a\x39\x66\x65\x61ture/communication/data/toggle_widget_visibility.proto\x1a\x1e\x66\x65\x61ture/share/share_info.proto\x1a\x32\x66\x65\x61ture/communication/data/payment_initiated.proto\x1a\x38\x66\x65\x61ture/communication/data/show_tooltip_event_data.proto\x1aGfeature/communication/data/player_content_rating_nudge_event_data.proto\x1a\x37\x66\x65\x61ture/communication/data/refresh_payment_status.proto\x1a+feature/communication/data/select_tab.proto\x1a\x31\x66\x65\x61ture/communication/data/toggle_watchlist.proto\"\xd4\n\n\x07Message\x12@\n\x0cmessage_name\x18\x01 \x01(\x0e\x32*.feature.communication.Message.MessageName\x12\x31\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32#.feature.communication.Message.Data\x1a\x87\x07\n\x04\x44\x61ta\x12\x1d\n\x15\x64isableMessageCaching\x18\x04 \x01(\x08\x12L\n\x13kids_profile_toggle\x18\x01 \x01(\x0b\x32-.feature.communication.data.KidsProfileToggleH\x00\x12;\n\nform_event\x18\x02 \x01(\x0b\x32%.feature.communication.data.FormEventH\x00\x12S\n\x17search_zero_filter_data\x18\x03 \x01(\x0b\x32\x30.feature.communication.data.SearchZeroFilterDataH\x00\x12.\n\nshare_info\x18\x05 \x01(\x0b\x32\x18.feature.share.ShareInfoH\x00\x12I\n\x11payment_initiated\x18\x06 \x01(\x0b\x32,.feature.communication.data.PaymentInitiatedH\x00\x12V\n\x18toggle_widget_visibility\x18\x07 \x01(\x0b\x32\x32.feature.communication.data.ToggleWidgetVisibilityH\x00\x12S\n\x17show_tooltip_event_data\x18\x08 \x01(\x0b\x32\x30.feature.communication.data.ShowTooltipEventDataH\x00\x12o\n&player_content_rating_nudge_event_data\x18\t \x01(\x0b\x32=.feature.communication.data.PlayerContentRatingNudgeEventDataH\x00\x12R\n\x16refresh_payment_status\x18\n \x01(\x0b\x32\x30.feature.communication.data.RefreshPaymentStatusH\x00\x12;\n\nselect_tab\x18\x0b \x01(\x0b\x32%.feature.communication.data.SelectTabH\x00\x12G\n\x10toggle_watchlist\x18\x0c \x01(\x0b\x32+.feature.communication.data.ToggleWatchlistH\x00\x42\r\n\x0bMessageData\"\xc9\x02\n\x0bMessageName\x12\x1f\n\x1bKIDS_PROFILE_TOGGLE_MESSAGE\x10\x00\x12\x16\n\x12\x46ORM_EVENT_MESSAGE\x10\x01\x12\x1f\n\x1bSEARCH_ZERO_FILTERS_MESSAGE\x10\x02\x12\x1c\n\x18SHARE_SCREENSHOT_MESSAGE\x10\x03\x12\x15\n\x11PAYMENT_INITIATED\x10\x04\x12\x1c\n\x18TOGGLE_WIDGET_VISIBILITY\x10\x05\x12\x1e\n\x1aSHOW_TOOLTIP_NEW_HOT_EVENT\x10\x06\x12%\n!PLAYER_CONTENT_RATING_NUDGE_EVENT\x10\x07\x12\x1a\n\x16REFRESH_PAYMENT_STATUS\x10\x08\x12\x0e\n\nSELECT_TAB\x10\t\x12\x1a\n\x16TOGGLE_WATCHLIST_EVENT\x10\nBm\n*com.hotstar.ui.model.feature.communicationP\x01Z=github.com/hotstar/hs-core-ui-models-go/feature/communicationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.communication.message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.hotstar.ui.model.feature.communicationP\001Z=github.com/hotstar/hs-core-ui-models-go/feature/communication'
  _globals['_MESSAGE']._serialized_start=647
  _globals['_MESSAGE']._serialized_end=2011
  _globals['_MESSAGE_DATA']._serialized_start=776
  _globals['_MESSAGE_DATA']._serialized_end=1679
  _globals['_MESSAGE_MESSAGENAME']._serialized_start=1682
  _globals['_MESSAGE_MESSAGENAME']._serialized_end=2011
# @@protoc_insertion_point(module_scope)
