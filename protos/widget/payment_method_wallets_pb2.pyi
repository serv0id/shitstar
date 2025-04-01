from feature.payment import validations_pb2 as _validations_pb2
from feature.payment import restrictions_pb2 as _restrictions_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import payment_method_commons_pb2 as _payment_method_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodWalletsWidget(_message.Message):
    __slots__ = ("widget_commons", "wallet_arr", "payment_method_meta")
    class Wallet(_message.Message):
        __slots__ = ("paytm", "other_wallet")
        class Paytm(_message.Message):
            __slots__ = ("verify_phone_number", "verify_otp", "payment_failed", "payment_method_meta", "sufficient_balance", "actions", "prefixNode")
            class VerifyPhoneNumer(_message.Message):
                __slots__ = ("title", "input_phone", "cta", "auto_triggered_actions")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                INPUT_PHONE_FIELD_NUMBER: _ClassVar[int]
                CTA_FIELD_NUMBER: _ClassVar[int]
                AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
                title: str
                input_phone: PaymentMethodWalletsWidget.Input
                cta: PaymentMethodWalletsWidget.Cta
                auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
                def __init__(self, title: _Optional[str] = ..., input_phone: _Optional[_Union[PaymentMethodWalletsWidget.Input, _Mapping]] = ..., cta: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
            class VerifyOtp(_message.Message):
                __slots__ = ("title", "otp_length", "edit_btn", "resend_btn", "verify_via_call", "timer", "submit", "auto_triggered_actions")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                OTP_LENGTH_FIELD_NUMBER: _ClassVar[int]
                EDIT_BTN_FIELD_NUMBER: _ClassVar[int]
                RESEND_BTN_FIELD_NUMBER: _ClassVar[int]
                VERIFY_VIA_CALL_FIELD_NUMBER: _ClassVar[int]
                TIMER_FIELD_NUMBER: _ClassVar[int]
                SUBMIT_FIELD_NUMBER: _ClassVar[int]
                AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
                title: str
                otp_length: int
                edit_btn: PaymentMethodWalletsWidget.Cta
                resend_btn: PaymentMethodWalletsWidget.Cta
                verify_via_call: PaymentMethodWalletsWidget.Cta
                timer: PaymentMethodWalletsWidget.Timer
                submit: PaymentMethodWalletsWidget.Cta
                auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
                def __init__(self, title: _Optional[str] = ..., otp_length: _Optional[int] = ..., edit_btn: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., resend_btn: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., verify_via_call: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., timer: _Optional[_Union[PaymentMethodWalletsWidget.Timer, _Mapping]] = ..., submit: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
            class PaytmError(_message.Message):
                __slots__ = ("title", "primary_cta", "secondary_cta", "edit_btn", "title_desc", "auto_triggered_actions", "on_load_actions")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
                SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
                EDIT_BTN_FIELD_NUMBER: _ClassVar[int]
                TITLE_DESC_FIELD_NUMBER: _ClassVar[int]
                AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
                ON_LOAD_ACTIONS_FIELD_NUMBER: _ClassVar[int]
                title: str
                primary_cta: PaymentMethodWalletsWidget.Cta
                secondary_cta: PaymentMethodWalletsWidget.Cta
                edit_btn: PaymentMethodWalletsWidget.Cta
                title_desc: PaymentMethodWalletsWidget.Titles
                auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
                on_load_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
                def __init__(self, title: _Optional[str] = ..., primary_cta: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., secondary_cta: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., edit_btn: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., title_desc: _Optional[_Union[PaymentMethodWalletsWidget.Titles, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., on_load_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
            class PaytmSuccess(_message.Message):
                __slots__ = ("title", "edit_btn", "primary_cta", "title_desc", "auto_triggered_actions")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                EDIT_BTN_FIELD_NUMBER: _ClassVar[int]
                PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
                TITLE_DESC_FIELD_NUMBER: _ClassVar[int]
                AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
                title: str
                edit_btn: PaymentMethodWalletsWidget.Cta
                primary_cta: PaymentMethodWalletsWidget.Cta
                title_desc: PaymentMethodWalletsWidget.Titles
                auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
                def __init__(self, title: _Optional[str] = ..., edit_btn: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., primary_cta: _Optional[_Union[PaymentMethodWalletsWidget.Cta, _Mapping]] = ..., title_desc: _Optional[_Union[PaymentMethodWalletsWidget.Titles, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
            VERIFY_PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
            VERIFY_OTP_FIELD_NUMBER: _ClassVar[int]
            PAYMENT_FAILED_FIELD_NUMBER: _ClassVar[int]
            PAYMENT_METHOD_META_FIELD_NUMBER: _ClassVar[int]
            SUFFICIENT_BALANCE_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            PREFIXNODE_FIELD_NUMBER: _ClassVar[int]
            verify_phone_number: PaymentMethodWalletsWidget.Wallet.Paytm.VerifyPhoneNumer
            verify_otp: PaymentMethodWalletsWidget.Wallet.Paytm.VerifyOtp
            payment_failed: PaymentMethodWalletsWidget.Wallet.Paytm.PaytmError
            payment_method_meta: _payment_method_commons_pb2.PaymentMethodCommonsWidget
            sufficient_balance: PaymentMethodWalletsWidget.Wallet.Paytm.PaytmSuccess
            actions: _actions_pb2.Actions
            prefixNode: str
            def __init__(self, verify_phone_number: _Optional[_Union[PaymentMethodWalletsWidget.Wallet.Paytm.VerifyPhoneNumer, _Mapping]] = ..., verify_otp: _Optional[_Union[PaymentMethodWalletsWidget.Wallet.Paytm.VerifyOtp, _Mapping]] = ..., payment_failed: _Optional[_Union[PaymentMethodWalletsWidget.Wallet.Paytm.PaytmError, _Mapping]] = ..., payment_method_meta: _Optional[_Union[_payment_method_commons_pb2.PaymentMethodCommonsWidget, _Mapping]] = ..., sufficient_balance: _Optional[_Union[PaymentMethodWalletsWidget.Wallet.Paytm.PaytmSuccess, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., prefixNode: _Optional[str] = ...) -> None: ...
        class OtherWallet(_message.Message):
            __slots__ = ("name", "img", "actions")
            NAME_FIELD_NUMBER: _ClassVar[int]
            IMG_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            name: str
            img: _image_pb2.Image
            actions: _actions_pb2.Actions
            def __init__(self, name: _Optional[str] = ..., img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        PAYTM_FIELD_NUMBER: _ClassVar[int]
        OTHER_WALLET_FIELD_NUMBER: _ClassVar[int]
        paytm: PaymentMethodWalletsWidget.Wallet.Paytm
        other_wallet: PaymentMethodWalletsWidget.Wallet.OtherWallet
        def __init__(self, paytm: _Optional[_Union[PaymentMethodWalletsWidget.Wallet.Paytm, _Mapping]] = ..., other_wallet: _Optional[_Union[PaymentMethodWalletsWidget.Wallet.OtherWallet, _Mapping]] = ...) -> None: ...
    class Titles(_message.Message):
        __slots__ = ("title", "sub_title")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "icon_name", "action", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        action: _actions_pb2.Actions
        actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class Timer(_message.Message):
        __slots__ = ("text", "sub_text", "timeoutInMS", "icon")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        TIMEOUTINMS_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        text: str
        sub_text: str
        timeoutInMS: int
        icon: str
        def __init__(self, text: _Optional[str] = ..., sub_text: _Optional[str] = ..., timeoutInMS: _Optional[int] = ..., icon: _Optional[str] = ...) -> None: ...
    class Input(_message.Message):
        __slots__ = ("title", "placeholder", "validations", "restrictions", "image", "default_value")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
        RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
        title: str
        placeholder: str
        validations: _containers.RepeatedCompositeFieldContainer[_validations_pb2.Validation]
        restrictions: _containers.RepeatedCompositeFieldContainer[_restrictions_pb2.Restriction]
        image: _image_pb2.Image
        default_value: str
        def __init__(self, title: _Optional[str] = ..., placeholder: _Optional[str] = ..., validations: _Optional[_Iterable[_Union[_validations_pb2.Validation, _Mapping]]] = ..., restrictions: _Optional[_Iterable[_Union[_restrictions_pb2.Restriction, _Mapping]]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., default_value: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    WALLET_ARR_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_META_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    wallet_arr: _containers.RepeatedCompositeFieldContainer[PaymentMethodWalletsWidget.Wallet]
    payment_method_meta: _payment_method_commons_pb2.PaymentMethodCommonsWidget
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., wallet_arr: _Optional[_Iterable[_Union[PaymentMethodWalletsWidget.Wallet, _Mapping]]] = ..., payment_method_meta: _Optional[_Union[_payment_method_commons_pb2.PaymentMethodCommonsWidget, _Mapping]] = ...) -> None: ...
