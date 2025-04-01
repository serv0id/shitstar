from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PartnerFamily(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARTNER_FAMILY_UNSPECIFIED: _ClassVar[PartnerFamily]
    PARTNER_FAMILY_MCA: _ClassVar[PartnerFamily]
    PARTNER_FAMILY_VIDAA: _ClassVar[PartnerFamily]
    PARTNER_FAMILY_ASTRO: _ClassVar[PartnerFamily]
    PARTNER_FAMILY_COOLITA: _ClassVar[PartnerFamily]
PARTNER_FAMILY_UNSPECIFIED: PartnerFamily
PARTNER_FAMILY_MCA: PartnerFamily
PARTNER_FAMILY_VIDAA: PartnerFamily
PARTNER_FAMILY_ASTRO: PartnerFamily
PARTNER_FAMILY_COOLITA: PartnerFamily
