from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OnboardingPurpose(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[OnboardingPurpose]
    LOGIN: _ClassVar[OnboardingPurpose]
    ONBOARDING_LITE: _ClassVar[OnboardingPurpose]

class InteractiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_TYPE: _ClassVar[InteractiveType]
    QUIZ: _ClassVar[InteractiveType]
    POLLING: _ClassVar[InteractiveType]
    CHAT: _ClassVar[InteractiveType]
UNKNOWN: OnboardingPurpose
LOGIN: OnboardingPurpose
ONBOARDING_LITE: OnboardingPurpose
UNKNOWN_TYPE: InteractiveType
QUIZ: InteractiveType
POLLING: InteractiveType
CHAT: InteractiveType

class StateContext(_message.Message):
    __slots__ = ["action_context"]
    ACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    action_context: ActionContext
    def __init__(self, action_context: _Optional[_Union[ActionContext, _Mapping]] = ...) -> None: ...

class ActionContext(_message.Message):
    __slots__ = ["subscribe_action_context", "watch_action_context", "onboarding_action_context"]
    SUBSCRIBE_ACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WATCH_ACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ONBOARDING_ACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    subscribe_action_context: SubscribeActionContext
    watch_action_context: WatchActionContext
    onboarding_action_context: OnboardingActionContext
    def __init__(self, subscribe_action_context: _Optional[_Union[SubscribeActionContext, _Mapping]] = ..., watch_action_context: _Optional[_Union[WatchActionContext, _Mapping]] = ..., onboarding_action_context: _Optional[_Union[OnboardingActionContext, _Mapping]] = ...) -> None: ...

class SubscribeActionContext(_message.Message):
    __slots__ = ["purpose", "content_id", "plan_family", "content_type", "failed_pc_entitlement_required", "failed_pc_entitlement_context", "is_content_paid", "paywall_ts", "content_title", "pack_id", "plan_duration", "plan_frequency", "partner_name", "promo_code", "plan_title", "parent_content_id", "parent_content_title", "sport_type", "source"]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FAMILY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    FAILED_PC_ENTITLEMENT_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    FAILED_PC_ENTITLEMENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IS_CONTENT_PAID_FIELD_NUMBER: _ClassVar[int]
    PAYWALL_TS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    PACK_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_DURATION_FIELD_NUMBER: _ClassVar[int]
    PLAN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    PARTNER_NAME_FIELD_NUMBER: _ClassVar[int]
    PROMO_CODE_FIELD_NUMBER: _ClassVar[int]
    PLAN_TITLE_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    SPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    purpose: OnboardingPurpose
    content_id: str
    plan_family: str
    content_type: str
    failed_pc_entitlement_required: str
    failed_pc_entitlement_context: str
    is_content_paid: bool
    paywall_ts: str
    content_title: str
    pack_id: str
    plan_duration: str
    plan_frequency: str
    partner_name: str
    promo_code: str
    plan_title: str
    parent_content_id: str
    parent_content_title: str
    sport_type: str
    source: str
    def __init__(self, purpose: _Optional[_Union[OnboardingPurpose, str]] = ..., content_id: _Optional[str] = ..., plan_family: _Optional[str] = ..., content_type: _Optional[str] = ..., failed_pc_entitlement_required: _Optional[str] = ..., failed_pc_entitlement_context: _Optional[str] = ..., is_content_paid: bool = ..., paywall_ts: _Optional[str] = ..., content_title: _Optional[str] = ..., pack_id: _Optional[str] = ..., plan_duration: _Optional[str] = ..., plan_frequency: _Optional[str] = ..., partner_name: _Optional[str] = ..., promo_code: _Optional[str] = ..., plan_title: _Optional[str] = ..., parent_content_id: _Optional[str] = ..., parent_content_title: _Optional[str] = ..., sport_type: _Optional[str] = ..., source: _Optional[str] = ...) -> None: ...

class WatchActionContext(_message.Message):
    __slots__ = ["purpose", "content_id", "content_title", "content_image_url", "content_type", "source", "parent_content_id", "parent_content_title", "sport_type", "skip_login", "interactive_type"]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    SPORT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKIP_LOGIN_FIELD_NUMBER: _ClassVar[int]
    INTERACTIVE_TYPE_FIELD_NUMBER: _ClassVar[int]
    purpose: OnboardingPurpose
    content_id: str
    content_title: str
    content_image_url: str
    content_type: str
    source: str
    parent_content_id: str
    parent_content_title: str
    sport_type: str
    skip_login: bool
    interactive_type: InteractiveType
    def __init__(self, purpose: _Optional[_Union[OnboardingPurpose, str]] = ..., content_id: _Optional[str] = ..., content_title: _Optional[str] = ..., content_image_url: _Optional[str] = ..., content_type: _Optional[str] = ..., source: _Optional[str] = ..., parent_content_id: _Optional[str] = ..., parent_content_title: _Optional[str] = ..., sport_type: _Optional[str] = ..., skip_login: bool = ..., interactive_type: _Optional[_Union[InteractiveType, str]] = ...) -> None: ...

class OnboardingActionContext(_message.Message):
    __slots__ = ["purpose"]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    purpose: OnboardingPurpose
    def __init__(self, purpose: _Optional[_Union[OnboardingPurpose, str]] = ...) -> None: ...
