from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AD_TYPE_UNSPECIFIED: _ClassVar[AdType]
    AD_TYPE_SKINNY: _ClassVar[AdType]
    AD_TYPE_DISPLAY_IMAGE: _ClassVar[AdType]
    AD_TYPE_DISPLAY_VIDEO: _ClassVar[AdType]
    AD_TYPE_DISPLAY_CAROUSEL: _ClassVar[AdType]
    AD_TYPE_PREROLL: _ClassVar[AdType]
    AD_TYPE_MIDROLL: _ClassVar[AdType]
AD_TYPE_UNSPECIFIED: AdType
AD_TYPE_SKINNY: AdType
AD_TYPE_DISPLAY_IMAGE: AdType
AD_TYPE_DISPLAY_VIDEO: AdType
AD_TYPE_DISPLAY_CAROUSEL: AdType
AD_TYPE_PREROLL: AdType
AD_TYPE_MIDROLL: AdType
