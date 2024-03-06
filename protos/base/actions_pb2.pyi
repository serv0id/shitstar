from protos.action import page_navigation_pb2 as _page_navigation_pb2
from protos.action import share_pb2 as _share_pb2
from protos.action import widget_navigation_pb2 as _widget_navigation_pb2
from protos.action import fetch_widget_pb2 as _fetch_widget_pb2
from protos.action import purchase_pb2 as _purchase_pb2
from protos.action import web_view_navigation_pb2 as _web_view_navigation_pb2
from protos.action import external_navigation_pb2 as _external_navigation_pb2
from protos.action import login_action_pb2 as _login_action_pb2
from protos.action import subscribe_action_pb2 as _subscribe_action_pb2
from protos.action import mail_to_pb2 as _mail_to_pb2
from protos.action import go_back_pb2 as _go_back_pb2
from protos.action import hs_track_pb2 as _hs_track_pb2
from protos.action import appsflyer_track_pb2 as _appsflyer_track_pb2
from protos.action import logout_action_pb2 as _logout_action_pb2
from protos.action import page_event_pb2 as _page_event_pb2
from protos.action import cancel_subscription_pb2 as _cancel_subscription_pb2
from protos.action import open_widget_overlay_pb2 as _open_widget_overlay_pb2
from protos.action import open_page_overlay_pb2 as _open_page_overlay_pb2
from protos.action import add_to_search_history_pb2 as _add_to_search_history_pb2
from protos.action import change_language_pb2 as _change_language_pb2
from protos.action import fetch_start_pb2 as _fetch_start_pb2
from protos.action import change_privacy_preferences_pb2 as _change_privacy_preferences_pb2
from protos.action import close_overlay_pb2 as _close_overlay_pb2
from protos.action import reinitiate_last_payment_pb2 as _reinitiate_last_payment_pb2
from protos.action import gtm_track_pb2 as _gtm_track_pb2
from protos.action import rate_app_pb2 as _rate_app_pb2
from protos.action import load_pg_form_pb2 as _load_pg_form_pb2
from protos.action import post_payment_navigation_pb2 as _post_payment_navigation_pb2
from protos.action import show_toast_pb2 as _show_toast_pb2
from protos.action import bridge_event_pb2 as _bridge_event_pb2
from protos.action import generate_recaptcha_token_pb2 as _generate_recaptcha_token_pb2
from protos.action import reload_pb2 as _reload_pb2
from protos.action import dismiss_notification_pb2 as _dismiss_notification_pb2
from protos.action import deeplink_pb2 as _deeplink_pb2
from protos.action import form_input_pb2 as _form_input_pb2
from protos.action import form_validation_pb2 as _form_validation_pb2
from protos.action import fetch_page_pb2 as _fetch_page_pb2
from protos.action import invoke_http_url_action_pb2 as _invoke_http_url_action_pb2
from protos.action import invoke_sna_url_action_pb2 as _invoke_sna_url_action_pb2
from protos.action import invalidate_proxy_state_pb2 as _invalidate_proxy_state_pb2
from protos.action import upsert_routing_table_query_param_pb2 as _upsert_routing_table_query_param_pb2
from protos.action import verify_sna_pb2 as _verify_sna_pb2
from protos.action import delete_list_item_pb2 as _delete_list_item_pb2
from protos.action import login_via_encrypted_id_pb2 as _login_via_encrypted_id_pb2
from protos.action import app_restart_pb2 as _app_restart_pb2
from protos.action import watchlist_pb2 as _watchlist_pb2
from protos.action import subscribe_message_pb2 as _subscribe_message_pb2
from protos.action import publish_message_pb2 as _publish_message_pb2
from protos.action import form_input_reset_pb2 as _form_input_reset_pb2
from protos.action import form_reset_pb2 as _form_reset_pb2
from protos.action import show_tooltip_pb2 as _show_tooltip_pb2
from protos.action import frequency_capped_status_pb2 as _frequency_capped_status_pb2
from protos.action import frequency_capped_update_pb2 as _frequency_capped_update_pb2
from protos.action import check_permission_status_pb2 as _check_permission_status_pb2
from protos.action import redirect_to_device_settings_pb2 as _redirect_to_device_settings_pb2
from protos.action import player_control_action_pb2 as _player_control_action_pb2
from protos.action import initiate_payment_pb2 as _initiate_payment_pb2
from protos.action import form_submit_pb2 as _form_submit_pb2
from protos.action import remind_me_pb2 as _remind_me_pb2
from protos.action import preload_pb2 as _preload_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Actions(_message.Message):
    __slots__ = ["on_click", "on_long_click", "on_re_focus", "on_dismiss", "on_load", "on_reset", "on_appear"]
    class Action(_message.Message):
        __slots__ = ["page_navigation", "share", "widget_navigation", "fetch_widget", "purchase_action", "web_view_navigation", "external_navigation", "mail_to", "init_login", "init_subscribe", "page_back", "hs_track", "appsflyer_track", "logout", "cancel_subscription", "page_event", "open_widget_overlay", "add_to_search_history", "change_language", "fetch_start", "change_privacy_preferences", "open_page_overlay", "close_overlay", "reinitiate_last_payment", "gtm_track", "rate_app", "load_pg_form", "post_payment_navigation", "show_toast_action", "bridge_event", "generate_recaptcha_token_action", "reload_action", "dismiss_notification_action", "deeplink_action", "invoke_url_action", "form_validation_action", "wrapper_action", "form_input_action", "fetch_page", "invoke_sna_url_action", "update_proxy_state_action", "upsert_routing_table_query_param_action", "verify_sna", "delete_list_item_action", "login_via_encrypted_id_action", "app_restart_action", "watchlist_action", "subscribe_to_message_action", "publish_message_action", "form_input_reset_action", "form_reset_action", "show_tooltip_action", "frequency_capped_status_action", "frequency_capped_update_action", "check_permission_status_action", "redirect_to_device_settings_action", "player_control_action", "initiate_payment_action", "form_submit_action", "remind_me_action", "preload_action"]
        PAGE_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        SHARE_FIELD_NUMBER: _ClassVar[int]
        WIDGET_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        FETCH_WIDGET_FIELD_NUMBER: _ClassVar[int]
        PURCHASE_ACTION_FIELD_NUMBER: _ClassVar[int]
        WEB_VIEW_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        MAIL_TO_FIELD_NUMBER: _ClassVar[int]
        INIT_LOGIN_FIELD_NUMBER: _ClassVar[int]
        INIT_SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
        PAGE_BACK_FIELD_NUMBER: _ClassVar[int]
        HS_TRACK_FIELD_NUMBER: _ClassVar[int]
        APPSFLYER_TRACK_FIELD_NUMBER: _ClassVar[int]
        LOGOUT_FIELD_NUMBER: _ClassVar[int]
        CANCEL_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PAGE_EVENT_FIELD_NUMBER: _ClassVar[int]
        OPEN_WIDGET_OVERLAY_FIELD_NUMBER: _ClassVar[int]
        ADD_TO_SEARCH_HISTORY_FIELD_NUMBER: _ClassVar[int]
        CHANGE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        FETCH_START_FIELD_NUMBER: _ClassVar[int]
        CHANGE_PRIVACY_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
        OPEN_PAGE_OVERLAY_FIELD_NUMBER: _ClassVar[int]
        CLOSE_OVERLAY_FIELD_NUMBER: _ClassVar[int]
        REINITIATE_LAST_PAYMENT_FIELD_NUMBER: _ClassVar[int]
        GTM_TRACK_FIELD_NUMBER: _ClassVar[int]
        RATE_APP_FIELD_NUMBER: _ClassVar[int]
        LOAD_PG_FORM_FIELD_NUMBER: _ClassVar[int]
        POST_PAYMENT_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        SHOW_TOAST_ACTION_FIELD_NUMBER: _ClassVar[int]
        BRIDGE_EVENT_FIELD_NUMBER: _ClassVar[int]
        GENERATE_RECAPTCHA_TOKEN_ACTION_FIELD_NUMBER: _ClassVar[int]
        RELOAD_ACTION_FIELD_NUMBER: _ClassVar[int]
        DISMISS_NOTIFICATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        DEEPLINK_ACTION_FIELD_NUMBER: _ClassVar[int]
        INVOKE_URL_ACTION_FIELD_NUMBER: _ClassVar[int]
        FORM_VALIDATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        WRAPPER_ACTION_FIELD_NUMBER: _ClassVar[int]
        FORM_INPUT_ACTION_FIELD_NUMBER: _ClassVar[int]
        FETCH_PAGE_FIELD_NUMBER: _ClassVar[int]
        INVOKE_SNA_URL_ACTION_FIELD_NUMBER: _ClassVar[int]
        UPDATE_PROXY_STATE_ACTION_FIELD_NUMBER: _ClassVar[int]
        UPSERT_ROUTING_TABLE_QUERY_PARAM_ACTION_FIELD_NUMBER: _ClassVar[int]
        VERIFY_SNA_FIELD_NUMBER: _ClassVar[int]
        DELETE_LIST_ITEM_ACTION_FIELD_NUMBER: _ClassVar[int]
        LOGIN_VIA_ENCRYPTED_ID_ACTION_FIELD_NUMBER: _ClassVar[int]
        APP_RESTART_ACTION_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_ACTION_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIBE_TO_MESSAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
        PUBLISH_MESSAGE_ACTION_FIELD_NUMBER: _ClassVar[int]
        FORM_INPUT_RESET_ACTION_FIELD_NUMBER: _ClassVar[int]
        FORM_RESET_ACTION_FIELD_NUMBER: _ClassVar[int]
        SHOW_TOOLTIP_ACTION_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_CAPPED_STATUS_ACTION_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_CAPPED_UPDATE_ACTION_FIELD_NUMBER: _ClassVar[int]
        CHECK_PERMISSION_STATUS_ACTION_FIELD_NUMBER: _ClassVar[int]
        REDIRECT_TO_DEVICE_SETTINGS_ACTION_FIELD_NUMBER: _ClassVar[int]
        PLAYER_CONTROL_ACTION_FIELD_NUMBER: _ClassVar[int]
        INITIATE_PAYMENT_ACTION_FIELD_NUMBER: _ClassVar[int]
        FORM_SUBMIT_ACTION_FIELD_NUMBER: _ClassVar[int]
        REMIND_ME_ACTION_FIELD_NUMBER: _ClassVar[int]
        PRELOAD_ACTION_FIELD_NUMBER: _ClassVar[int]
        page_navigation: _page_navigation_pb2.PageNavigationAction
        share: _share_pb2.Share
        widget_navigation: _widget_navigation_pb2.WidgetNavigationAction
        fetch_widget: _fetch_widget_pb2.FetchWidgetAction
        purchase_action: _purchase_pb2.PurchaseAction
        web_view_navigation: _web_view_navigation_pb2.WebViewNavigationAction
        external_navigation: _external_navigation_pb2.ExternalNavigationAction
        mail_to: _mail_to_pb2.MailtoAction
        init_login: _login_action_pb2.LoginAction
        init_subscribe: _subscribe_action_pb2.SubscribeAction
        page_back: _go_back_pb2.GoBackAction
        hs_track: _hs_track_pb2.HSTrackAction
        appsflyer_track: _appsflyer_track_pb2.AppsflyerTrackAction
        logout: _logout_action_pb2.LogoutAction
        cancel_subscription: _cancel_subscription_pb2.CancelSubscriptionAction
        page_event: _page_event_pb2.PageEventAction
        open_widget_overlay: _open_widget_overlay_pb2.OpenWidgetOverlayAction
        add_to_search_history: _add_to_search_history_pb2.AddToSearchHistoryAction
        change_language: _change_language_pb2.ChangeLanguageAction
        fetch_start: _fetch_start_pb2.FetchStartAction
        change_privacy_preferences: _change_privacy_preferences_pb2.ChangePrivacyPreferencesAction
        open_page_overlay: _open_page_overlay_pb2.OpenPageOverlayAction
        close_overlay: _close_overlay_pb2.CloseOverlayAction
        reinitiate_last_payment: _reinitiate_last_payment_pb2.ReinitiateLastPaymentAction
        gtm_track: _gtm_track_pb2.GTMTrackAction
        rate_app: _rate_app_pb2.RateAppAction
        load_pg_form: _load_pg_form_pb2.LoadPgForm
        post_payment_navigation: _post_payment_navigation_pb2.PostPaymentNavigationAction
        show_toast_action: _show_toast_pb2.ShowToastAction
        bridge_event: _bridge_event_pb2.BridgeEventAction
        generate_recaptcha_token_action: _generate_recaptcha_token_pb2.GenerateRecaptchaTokenAction
        reload_action: _reload_pb2.ReloadAction
        dismiss_notification_action: _dismiss_notification_pb2.DismissNotificationAction
        deeplink_action: _deeplink_pb2.DeeplinkAction
        invoke_url_action: _invoke_http_url_action_pb2.InvokeHttpUrlAction
        form_validation_action: _form_validation_pb2.FormValidationAction
        wrapper_action: WrapperAction
        form_input_action: _form_input_pb2.FormInputAction
        fetch_page: _fetch_page_pb2.FetchPageAction
        invoke_sna_url_action: _invoke_sna_url_action_pb2.InvokeSnaUrlAction
        update_proxy_state_action: _invalidate_proxy_state_pb2.UpdateProxyStateTTLAction
        upsert_routing_table_query_param_action: _upsert_routing_table_query_param_pb2.UpsertRoutingTableQueryParamAction
        verify_sna: _verify_sna_pb2.VerifySnaAction
        delete_list_item_action: _delete_list_item_pb2.DeleteListItemAction
        login_via_encrypted_id_action: _login_via_encrypted_id_pb2.LoginViaEncryptedIdAction
        app_restart_action: _app_restart_pb2.AppRestartAction
        watchlist_action: _watchlist_pb2.WatchlistAction
        subscribe_to_message_action: _subscribe_message_pb2.SubscribeToMessageAction
        publish_message_action: _publish_message_pb2.PublishMessageAction
        form_input_reset_action: _form_input_reset_pb2.FormInputResetAction
        form_reset_action: _form_reset_pb2.FormResetAction
        show_tooltip_action: _show_tooltip_pb2.ShowTooltipAction
        frequency_capped_status_action: _frequency_capped_status_pb2.FrequencyCappedStatusAction
        frequency_capped_update_action: _frequency_capped_update_pb2.FrequencyCappedUpdateAction
        check_permission_status_action: _check_permission_status_pb2.CheckPermissionStatusAction
        redirect_to_device_settings_action: _redirect_to_device_settings_pb2.RedirectToDeviceSettingsAction
        player_control_action: _player_control_action_pb2.PlayerControlAction
        initiate_payment_action: _initiate_payment_pb2.InitiatePaymentAction
        form_submit_action: _form_submit_pb2.FormSubmitAction
        remind_me_action: _remind_me_pb2.RemindMeAction
        preload_action: _preload_pb2.PreloadAction
        def __init__(self, page_navigation: _Optional[_Union[_page_navigation_pb2.PageNavigationAction, _Mapping]] = ..., share: _Optional[_Union[_share_pb2.Share, _Mapping]] = ..., widget_navigation: _Optional[_Union[_widget_navigation_pb2.WidgetNavigationAction, _Mapping]] = ..., fetch_widget: _Optional[_Union[_fetch_widget_pb2.FetchWidgetAction, _Mapping]] = ..., purchase_action: _Optional[_Union[_purchase_pb2.PurchaseAction, _Mapping]] = ..., web_view_navigation: _Optional[_Union[_web_view_navigation_pb2.WebViewNavigationAction, _Mapping]] = ..., external_navigation: _Optional[_Union[_external_navigation_pb2.ExternalNavigationAction, _Mapping]] = ..., mail_to: _Optional[_Union[_mail_to_pb2.MailtoAction, _Mapping]] = ..., init_login: _Optional[_Union[_login_action_pb2.LoginAction, _Mapping]] = ..., init_subscribe: _Optional[_Union[_subscribe_action_pb2.SubscribeAction, _Mapping]] = ..., page_back: _Optional[_Union[_go_back_pb2.GoBackAction, _Mapping]] = ..., hs_track: _Optional[_Union[_hs_track_pb2.HSTrackAction, _Mapping]] = ..., appsflyer_track: _Optional[_Union[_appsflyer_track_pb2.AppsflyerTrackAction, _Mapping]] = ..., logout: _Optional[_Union[_logout_action_pb2.LogoutAction, _Mapping]] = ..., cancel_subscription: _Optional[_Union[_cancel_subscription_pb2.CancelSubscriptionAction, _Mapping]] = ..., page_event: _Optional[_Union[_page_event_pb2.PageEventAction, _Mapping]] = ..., open_widget_overlay: _Optional[_Union[_open_widget_overlay_pb2.OpenWidgetOverlayAction, _Mapping]] = ..., add_to_search_history: _Optional[_Union[_add_to_search_history_pb2.AddToSearchHistoryAction, _Mapping]] = ..., change_language: _Optional[_Union[_change_language_pb2.ChangeLanguageAction, _Mapping]] = ..., fetch_start: _Optional[_Union[_fetch_start_pb2.FetchStartAction, _Mapping]] = ..., change_privacy_preferences: _Optional[_Union[_change_privacy_preferences_pb2.ChangePrivacyPreferencesAction, _Mapping]] = ..., open_page_overlay: _Optional[_Union[_open_page_overlay_pb2.OpenPageOverlayAction, _Mapping]] = ..., close_overlay: _Optional[_Union[_close_overlay_pb2.CloseOverlayAction, _Mapping]] = ..., reinitiate_last_payment: _Optional[_Union[_reinitiate_last_payment_pb2.ReinitiateLastPaymentAction, _Mapping]] = ..., gtm_track: _Optional[_Union[_gtm_track_pb2.GTMTrackAction, _Mapping]] = ..., rate_app: _Optional[_Union[_rate_app_pb2.RateAppAction, _Mapping]] = ..., load_pg_form: _Optional[_Union[_load_pg_form_pb2.LoadPgForm, _Mapping]] = ..., post_payment_navigation: _Optional[_Union[_post_payment_navigation_pb2.PostPaymentNavigationAction, _Mapping]] = ..., show_toast_action: _Optional[_Union[_show_toast_pb2.ShowToastAction, _Mapping]] = ..., bridge_event: _Optional[_Union[_bridge_event_pb2.BridgeEventAction, _Mapping]] = ..., generate_recaptcha_token_action: _Optional[_Union[_generate_recaptcha_token_pb2.GenerateRecaptchaTokenAction, _Mapping]] = ..., reload_action: _Optional[_Union[_reload_pb2.ReloadAction, _Mapping]] = ..., dismiss_notification_action: _Optional[_Union[_dismiss_notification_pb2.DismissNotificationAction, _Mapping]] = ..., deeplink_action: _Optional[_Union[_deeplink_pb2.DeeplinkAction, _Mapping]] = ..., invoke_url_action: _Optional[_Union[_invoke_http_url_action_pb2.InvokeHttpUrlAction, _Mapping]] = ..., form_validation_action: _Optional[_Union[_form_validation_pb2.FormValidationAction, _Mapping]] = ..., wrapper_action: _Optional[_Union[WrapperAction, _Mapping]] = ..., form_input_action: _Optional[_Union[_form_input_pb2.FormInputAction, _Mapping]] = ..., fetch_page: _Optional[_Union[_fetch_page_pb2.FetchPageAction, _Mapping]] = ..., invoke_sna_url_action: _Optional[_Union[_invoke_sna_url_action_pb2.InvokeSnaUrlAction, _Mapping]] = ..., update_proxy_state_action: _Optional[_Union[_invalidate_proxy_state_pb2.UpdateProxyStateTTLAction, _Mapping]] = ..., upsert_routing_table_query_param_action: _Optional[_Union[_upsert_routing_table_query_param_pb2.UpsertRoutingTableQueryParamAction, _Mapping]] = ..., verify_sna: _Optional[_Union[_verify_sna_pb2.VerifySnaAction, _Mapping]] = ..., delete_list_item_action: _Optional[_Union[_delete_list_item_pb2.DeleteListItemAction, _Mapping]] = ..., login_via_encrypted_id_action: _Optional[_Union[_login_via_encrypted_id_pb2.LoginViaEncryptedIdAction, _Mapping]] = ..., app_restart_action: _Optional[_Union[_app_restart_pb2.AppRestartAction, _Mapping]] = ..., watchlist_action: _Optional[_Union[_watchlist_pb2.WatchlistAction, _Mapping]] = ..., subscribe_to_message_action: _Optional[_Union[_subscribe_message_pb2.SubscribeToMessageAction, _Mapping]] = ..., publish_message_action: _Optional[_Union[_publish_message_pb2.PublishMessageAction, _Mapping]] = ..., form_input_reset_action: _Optional[_Union[_form_input_reset_pb2.FormInputResetAction, _Mapping]] = ..., form_reset_action: _Optional[_Union[_form_reset_pb2.FormResetAction, _Mapping]] = ..., show_tooltip_action: _Optional[_Union[_show_tooltip_pb2.ShowTooltipAction, _Mapping]] = ..., frequency_capped_status_action: _Optional[_Union[_frequency_capped_status_pb2.FrequencyCappedStatusAction, _Mapping]] = ..., frequency_capped_update_action: _Optional[_Union[_frequency_capped_update_pb2.FrequencyCappedUpdateAction, _Mapping]] = ..., check_permission_status_action: _Optional[_Union[_check_permission_status_pb2.CheckPermissionStatusAction, _Mapping]] = ..., redirect_to_device_settings_action: _Optional[_Union[_redirect_to_device_settings_pb2.RedirectToDeviceSettingsAction, _Mapping]] = ..., player_control_action: _Optional[_Union[_player_control_action_pb2.PlayerControlAction, _Mapping]] = ..., initiate_payment_action: _Optional[_Union[_initiate_payment_pb2.InitiatePaymentAction, _Mapping]] = ..., form_submit_action: _Optional[_Union[_form_submit_pb2.FormSubmitAction, _Mapping]] = ..., remind_me_action: _Optional[_Union[_remind_me_pb2.RemindMeAction, _Mapping]] = ..., preload_action: _Optional[_Union[_preload_pb2.PreloadAction, _Mapping]] = ...) -> None: ...
    ON_CLICK_FIELD_NUMBER: _ClassVar[int]
    ON_LONG_CLICK_FIELD_NUMBER: _ClassVar[int]
    ON_RE_FOCUS_FIELD_NUMBER: _ClassVar[int]
    ON_DISMISS_FIELD_NUMBER: _ClassVar[int]
    ON_LOAD_FIELD_NUMBER: _ClassVar[int]
    ON_RESET_FIELD_NUMBER: _ClassVar[int]
    ON_APPEAR_FIELD_NUMBER: _ClassVar[int]
    on_click: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    on_long_click: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    on_re_focus: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    on_dismiss: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    on_load: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    on_reset: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    on_appear: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    def __init__(self, on_click: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ..., on_long_click: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ..., on_re_focus: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ..., on_dismiss: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ..., on_load: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ..., on_reset: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ..., on_appear: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ...) -> None: ...

class WrapperAction(_message.Message):
    __slots__ = ["action", "on_success", "on_failure"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ON_SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ON_FAILURE_FIELD_NUMBER: _ClassVar[int]
    action: Actions.Action
    on_success: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    on_failure: _containers.RepeatedCompositeFieldContainer[Actions.Action]
    def __init__(self, action: _Optional[_Union[Actions.Action, _Mapping]] = ..., on_success: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ..., on_failure: _Optional[_Iterable[_Union[Actions.Action, _Mapping]]] = ...) -> None: ...
