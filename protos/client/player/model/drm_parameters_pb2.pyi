from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DrmParameters(_message.Message):
    __slots__ = ("widevine_security_levels", "hdcp_versions", "playready_security_levels")
    class WidevineSecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WIDEVINE_SECURITY_LEVEL_UNSPECIFIED: _ClassVar[DrmParameters.WidevineSecurityLevel]
        WIDEVINE_SECURITY_LEVEL_SW_SECURE_CRYPTO: _ClassVar[DrmParameters.WidevineSecurityLevel]
        WIDEVINE_SECURITY_LEVEL_SW_SECURE_DECODE: _ClassVar[DrmParameters.WidevineSecurityLevel]
        WIDEVINE_SECURITY_LEVEL_HW_SECURE_CRYPTO: _ClassVar[DrmParameters.WidevineSecurityLevel]
        WIDEVINE_SECURITY_LEVEL_HW_SECURE_DECODE: _ClassVar[DrmParameters.WidevineSecurityLevel]
        WIDEVINE_SECURITY_LEVEL_HW_SECURE_ALL: _ClassVar[DrmParameters.WidevineSecurityLevel]
    WIDEVINE_SECURITY_LEVEL_UNSPECIFIED: DrmParameters.WidevineSecurityLevel
    WIDEVINE_SECURITY_LEVEL_SW_SECURE_CRYPTO: DrmParameters.WidevineSecurityLevel
    WIDEVINE_SECURITY_LEVEL_SW_SECURE_DECODE: DrmParameters.WidevineSecurityLevel
    WIDEVINE_SECURITY_LEVEL_HW_SECURE_CRYPTO: DrmParameters.WidevineSecurityLevel
    WIDEVINE_SECURITY_LEVEL_HW_SECURE_DECODE: DrmParameters.WidevineSecurityLevel
    WIDEVINE_SECURITY_LEVEL_HW_SECURE_ALL: DrmParameters.WidevineSecurityLevel
    class HdcpVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HDCP_VERSION_UNSPECIFIED: _ClassVar[DrmParameters.HdcpVersion]
        HDCP_VERSION_HDCP_NONE: _ClassVar[DrmParameters.HdcpVersion]
        HDCP_VERSION_HDCP_V1: _ClassVar[DrmParameters.HdcpVersion]
        HDCP_VERSION_HDCP_V2: _ClassVar[DrmParameters.HdcpVersion]
        HDCP_VERSION_HDCP_V2_1: _ClassVar[DrmParameters.HdcpVersion]
        HDCP_VERSION_HDCP_V2_2: _ClassVar[DrmParameters.HdcpVersion]
        HDCP_VERSION_HDCP_NO_DIGITAL_OUTPUT: _ClassVar[DrmParameters.HdcpVersion]
        HDCP_VERSION_HDCP_V2_3: _ClassVar[DrmParameters.HdcpVersion]
    HDCP_VERSION_UNSPECIFIED: DrmParameters.HdcpVersion
    HDCP_VERSION_HDCP_NONE: DrmParameters.HdcpVersion
    HDCP_VERSION_HDCP_V1: DrmParameters.HdcpVersion
    HDCP_VERSION_HDCP_V2: DrmParameters.HdcpVersion
    HDCP_VERSION_HDCP_V2_1: DrmParameters.HdcpVersion
    HDCP_VERSION_HDCP_V2_2: DrmParameters.HdcpVersion
    HDCP_VERSION_HDCP_NO_DIGITAL_OUTPUT: DrmParameters.HdcpVersion
    HDCP_VERSION_HDCP_V2_3: DrmParameters.HdcpVersion
    class PlayreadySecurityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAYREADY_SECURITY_LEVEL_UNSPECIFIED: _ClassVar[DrmParameters.PlayreadySecurityLevel]
        PLAYREADY_SECURITY_LEVEL_SL3000: _ClassVar[DrmParameters.PlayreadySecurityLevel]
        PLAYREADY_SECURITY_LEVEL_SL2000: _ClassVar[DrmParameters.PlayreadySecurityLevel]
        PLAYREADY_SECURITY_LEVEL_SL150: _ClassVar[DrmParameters.PlayreadySecurityLevel]
    PLAYREADY_SECURITY_LEVEL_UNSPECIFIED: DrmParameters.PlayreadySecurityLevel
    PLAYREADY_SECURITY_LEVEL_SL3000: DrmParameters.PlayreadySecurityLevel
    PLAYREADY_SECURITY_LEVEL_SL2000: DrmParameters.PlayreadySecurityLevel
    PLAYREADY_SECURITY_LEVEL_SL150: DrmParameters.PlayreadySecurityLevel
    WIDEVINE_SECURITY_LEVELS_FIELD_NUMBER: _ClassVar[int]
    HDCP_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    PLAYREADY_SECURITY_LEVELS_FIELD_NUMBER: _ClassVar[int]
    widevine_security_levels: _containers.RepeatedScalarFieldContainer[DrmParameters.WidevineSecurityLevel]
    hdcp_versions: _containers.RepeatedScalarFieldContainer[DrmParameters.HdcpVersion]
    playready_security_levels: _containers.RepeatedScalarFieldContainer[DrmParameters.PlayreadySecurityLevel]
    def __init__(self, widevine_security_levels: _Optional[_Iterable[_Union[DrmParameters.WidevineSecurityLevel, str]]] = ..., hdcp_versions: _Optional[_Iterable[_Union[DrmParameters.HdcpVersion, str]]] = ..., playready_security_levels: _Optional[_Iterable[_Union[DrmParameters.PlayreadySecurityLevel, str]]] = ...) -> None: ...
