from v2.langcommons import language_codes_pb2 as _language_codes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserLanguagePreferencesV2(_message.Message):
    __slots__ = ("status", "data")
    class DataStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DATA_STATUS: _ClassVar[UserLanguagePreferencesV2.DataStatus]
        UPDATED: _ClassVar[UserLanguagePreferencesV2.DataStatus]
        STALE: _ClassVar[UserLanguagePreferencesV2.DataStatus]
        FAILED: _ClassVar[UserLanguagePreferencesV2.DataStatus]
        OVERSIZE: _ClassVar[UserLanguagePreferencesV2.DataStatus]
    UNKNOWN_DATA_STATUS: UserLanguagePreferencesV2.DataStatus
    UPDATED: UserLanguagePreferencesV2.DataStatus
    STALE: UserLanguagePreferencesV2.DataStatus
    FAILED: UserLanguagePreferencesV2.DataStatus
    OVERSIZE: UserLanguagePreferencesV2.DataStatus
    class UserLanguagePreferences(_message.Message):
        __slots__ = ("userLangPreferences",)
        USERLANGPREFERENCES_FIELD_NUMBER: _ClassVar[int]
        userLangPreferences: _containers.RepeatedCompositeFieldContainer[UserLanguagePreferencesV2.UserLanguagePreference]
        def __init__(self, userLangPreferences: _Optional[_Iterable[_Union[UserLanguagePreferencesV2.UserLanguagePreference, _Mapping]]] = ...) -> None: ...
    class UserLanguagePreference(_message.Message):
        __slots__ = ("prefType", "prefDataList", "updatedAt")
        class PreferenceType(_message.Message):
            __slots__ = ("value", "version")
            class PreferenceTypeValue(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                USR_SEL_AUDIO_LANG: _ClassVar[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue]
                LPV: _ClassVar[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue]
                ONBOARDED_LANG: _ClassVar[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue]
                PRIMARY_LANG: _ClassVar[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue]
                SPORTS_LANG: _ClassVar[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue]
                ODP: _ClassVar[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue]
            USR_SEL_AUDIO_LANG: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue
            LPV: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue
            ONBOARDED_LANG: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue
            PRIMARY_LANG: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue
            SPORTS_LANG: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue
            ODP: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue
            VALUE_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            value: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue
            version: float
            def __init__(self, value: _Optional[_Union[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType.PreferenceTypeValue, str]] = ..., version: _Optional[float] = ...) -> None: ...
        PREFTYPE_FIELD_NUMBER: _ClassVar[int]
        PREFDATALIST_FIELD_NUMBER: _ClassVar[int]
        UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
        prefType: UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType
        prefDataList: _containers.RepeatedCompositeFieldContainer[UserLanguagePreferencesV2.PreferenceData]
        updatedAt: int
        def __init__(self, prefType: _Optional[_Union[UserLanguagePreferencesV2.UserLanguagePreference.PreferenceType, _Mapping]] = ..., prefDataList: _Optional[_Iterable[_Union[UserLanguagePreferencesV2.PreferenceData, _Mapping]]] = ..., updatedAt: _Optional[int] = ...) -> None: ...
    class PreferenceData(_message.Message):
        __slots__ = ("audio_lang", "subtitle_lang", "prefCtxt", "weight", "dubbedPrefList", "audio_lang_v2")
        class PreferenceContext(_message.Message):
            __slots__ = ("key", "value", "updatedAt")
            class ContextKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SHOW_ID: _ClassVar[UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey]
                SPORTS: _ClassVar[UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey]
                STUDIO: _ClassVar[UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey]
                CONTENT_ID: _ClassVar[UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey]
                PRIMARY_LANG: _ClassVar[UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey]
                CONTENT_TYPE: _ClassVar[UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey]
            SHOW_ID: UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey
            SPORTS: UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey
            STUDIO: UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey
            CONTENT_ID: UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey
            PRIMARY_LANG: UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey
            CONTENT_TYPE: UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            UPDATEDAT_FIELD_NUMBER: _ClassVar[int]
            key: UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey
            value: str
            updatedAt: int
            def __init__(self, key: _Optional[_Union[UserLanguagePreferencesV2.PreferenceData.PreferenceContext.ContextKey, str]] = ..., value: _Optional[str] = ..., updatedAt: _Optional[int] = ...) -> None: ...
        class DubbedPreference(_message.Message):
            __slots__ = ("audio_lang", "weight")
            AUDIO_LANG_FIELD_NUMBER: _ClassVar[int]
            WEIGHT_FIELD_NUMBER: _ClassVar[int]
            audio_lang: _language_codes_pb2.LanguageCodes
            weight: int
            def __init__(self, audio_lang: _Optional[_Union[_language_codes_pb2.LanguageCodes, str]] = ..., weight: _Optional[int] = ...) -> None: ...
        AUDIO_LANG_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_LANG_FIELD_NUMBER: _ClassVar[int]
        PREFCTXT_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        DUBBEDPREFLIST_FIELD_NUMBER: _ClassVar[int]
        AUDIO_LANG_V2_FIELD_NUMBER: _ClassVar[int]
        audio_lang: str
        subtitle_lang: str
        prefCtxt: _containers.RepeatedCompositeFieldContainer[UserLanguagePreferencesV2.PreferenceData.PreferenceContext]
        weight: float
        dubbedPrefList: _containers.RepeatedCompositeFieldContainer[UserLanguagePreferencesV2.PreferenceData.DubbedPreference]
        audio_lang_v2: _language_codes_pb2.LanguageCodes
        def __init__(self, audio_lang: _Optional[str] = ..., subtitle_lang: _Optional[str] = ..., prefCtxt: _Optional[_Iterable[_Union[UserLanguagePreferencesV2.PreferenceData.PreferenceContext, _Mapping]]] = ..., weight: _Optional[float] = ..., dubbedPrefList: _Optional[_Iterable[_Union[UserLanguagePreferencesV2.PreferenceData.DubbedPreference, _Mapping]]] = ..., audio_lang_v2: _Optional[_Union[_language_codes_pb2.LanguageCodes, str]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: UserLanguagePreferencesV2.DataStatus
    data: UserLanguagePreferencesV2.UserLanguagePreferences
    def __init__(self, status: _Optional[_Union[UserLanguagePreferencesV2.DataStatus, str]] = ..., data: _Optional[_Union[UserLanguagePreferencesV2.UserLanguagePreferences, _Mapping]] = ...) -> None: ...
