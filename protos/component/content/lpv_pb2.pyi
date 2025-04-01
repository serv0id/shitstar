from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LanguagePreference(_message.Message):
    __slots__ = ("lpv", "odp")
    class Lpv(_message.Message):
        __slots__ = ("weights", "is_cold_start")
        WEIGHTS_FIELD_NUMBER: _ClassVar[int]
        IS_COLD_START_FIELD_NUMBER: _ClassVar[int]
        weights: _containers.RepeatedCompositeFieldContainer[LanguagePreference.LanguageWeight]
        is_cold_start: bool
        def __init__(self, weights: _Optional[_Iterable[_Union[LanguagePreference.LanguageWeight, _Mapping]]] = ..., is_cold_start: bool = ...) -> None: ...
    class Odp(_message.Message):
        __slots__ = ("odp_preferences", "is_cold_start_odp")
        ODP_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
        IS_COLD_START_ODP_FIELD_NUMBER: _ClassVar[int]
        odp_preferences: _containers.RepeatedCompositeFieldContainer[LanguagePreference.OdpPreference]
        is_cold_start_odp: bool
        def __init__(self, odp_preferences: _Optional[_Iterable[_Union[LanguagePreference.OdpPreference, _Mapping]]] = ..., is_cold_start_odp: bool = ...) -> None: ...
    class LanguageWeight(_message.Message):
        __slots__ = ("lang_code", "weight")
        LANG_CODE_FIELD_NUMBER: _ClassVar[int]
        WEIGHT_FIELD_NUMBER: _ClassVar[int]
        lang_code: str
        weight: float
        def __init__(self, lang_code: _Optional[str] = ..., weight: _Optional[float] = ...) -> None: ...
    class OdpPreference(_message.Message):
        __slots__ = ("original_lang_code", "dubbed_preferences")
        ORIGINAL_LANG_CODE_FIELD_NUMBER: _ClassVar[int]
        DUBBED_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
        original_lang_code: str
        dubbed_preferences: _containers.RepeatedCompositeFieldContainer[LanguagePreference.LanguageWeight]
        def __init__(self, original_lang_code: _Optional[str] = ..., dubbed_preferences: _Optional[_Iterable[_Union[LanguagePreference.LanguageWeight, _Mapping]]] = ...) -> None: ...
    LPV_FIELD_NUMBER: _ClassVar[int]
    ODP_FIELD_NUMBER: _ClassVar[int]
    lpv: LanguagePreference.Lpv
    odp: LanguagePreference.Odp
    def __init__(self, lpv: _Optional[_Union[LanguagePreference.Lpv, _Mapping]] = ..., odp: _Optional[_Union[LanguagePreference.Odp, _Mapping]] = ...) -> None: ...
