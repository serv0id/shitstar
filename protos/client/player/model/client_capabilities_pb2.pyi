from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientCapabilities(_message.Message):
    __slots__ = ("packages", "containers", "ads", "audio_channels", "encryptions", "video_codecs", "ladders", "resolutions", "dynamic_ranges", "true_resolutions", "audio_codecs", "video_codecs_non_secure", "orientations")
    class Package(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PACKAGE_UNSPECIFIED: _ClassVar[ClientCapabilities.Package]
        PACKAGE_DASH: _ClassVar[ClientCapabilities.Package]
        PACKAGE_HLS: _ClassVar[ClientCapabilities.Package]
    PACKAGE_UNSPECIFIED: ClientCapabilities.Package
    PACKAGE_DASH: ClientCapabilities.Package
    PACKAGE_HLS: ClientCapabilities.Package
    class Container(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTAINER_UNSPECIFIED: _ClassVar[ClientCapabilities.Container]
        CONTAINER_FMP4: _ClassVar[ClientCapabilities.Container]
        CONTAINER_FMP4_BR: _ClassVar[ClientCapabilities.Container]
        CONTAINER_TS: _ClassVar[ClientCapabilities.Container]
        CONTAINER_WEBM: _ClassVar[ClientCapabilities.Container]
    CONTAINER_UNSPECIFIED: ClientCapabilities.Container
    CONTAINER_FMP4: ClientCapabilities.Container
    CONTAINER_FMP4_BR: ClientCapabilities.Container
    CONTAINER_TS: ClientCapabilities.Container
    CONTAINER_WEBM: ClientCapabilities.Container
    class Ads(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADS_UNSPECIFIED: _ClassVar[ClientCapabilities.Ads]
        ADS_SSAI: _ClassVar[ClientCapabilities.Ads]
        ADS_NON_SSAI: _ClassVar[ClientCapabilities.Ads]
        ADS_SGAI: _ClassVar[ClientCapabilities.Ads]
    ADS_UNSPECIFIED: ClientCapabilities.Ads
    ADS_SSAI: ClientCapabilities.Ads
    ADS_NON_SSAI: ClientCapabilities.Ads
    ADS_SGAI: ClientCapabilities.Ads
    class AudioChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_CHANNEL_UNSPECIFIED: _ClassVar[ClientCapabilities.AudioChannel]
        AUDIO_CHANNEL_STEREO: _ClassVar[ClientCapabilities.AudioChannel]
        AUDIO_CHANNEL_ATMOS: _ClassVar[ClientCapabilities.AudioChannel]
        AUDIO_CHANNEL_DOLBY_51: _ClassVar[ClientCapabilities.AudioChannel]
    AUDIO_CHANNEL_UNSPECIFIED: ClientCapabilities.AudioChannel
    AUDIO_CHANNEL_STEREO: ClientCapabilities.AudioChannel
    AUDIO_CHANNEL_ATMOS: ClientCapabilities.AudioChannel
    AUDIO_CHANNEL_DOLBY_51: ClientCapabilities.AudioChannel
    class Encryption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCRYPTION_UNSPECIFIED: _ClassVar[ClientCapabilities.Encryption]
        ENCRYPTION_PLAIN: _ClassVar[ClientCapabilities.Encryption]
        ENCRYPTION_WIDEVINE: _ClassVar[ClientCapabilities.Encryption]
        ENCRYPTION_FAIRPLAY: _ClassVar[ClientCapabilities.Encryption]
        ENCRYPTION_PLAYREADY: _ClassVar[ClientCapabilities.Encryption]
    ENCRYPTION_UNSPECIFIED: ClientCapabilities.Encryption
    ENCRYPTION_PLAIN: ClientCapabilities.Encryption
    ENCRYPTION_WIDEVINE: ClientCapabilities.Encryption
    ENCRYPTION_FAIRPLAY: ClientCapabilities.Encryption
    ENCRYPTION_PLAYREADY: ClientCapabilities.Encryption
    class VideoCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VIDEO_CODEC_UNSPECIFIED: _ClassVar[ClientCapabilities.VideoCodec]
        VIDEO_CODEC_H264: _ClassVar[ClientCapabilities.VideoCodec]
        VIDEO_CODEC_H265: _ClassVar[ClientCapabilities.VideoCodec]
        VIDEO_CODEC_DV_H265: _ClassVar[ClientCapabilities.VideoCodec]
        VIDEO_CODEC_AV1: _ClassVar[ClientCapabilities.VideoCodec]
    VIDEO_CODEC_UNSPECIFIED: ClientCapabilities.VideoCodec
    VIDEO_CODEC_H264: ClientCapabilities.VideoCodec
    VIDEO_CODEC_H265: ClientCapabilities.VideoCodec
    VIDEO_CODEC_DV_H265: ClientCapabilities.VideoCodec
    VIDEO_CODEC_AV1: ClientCapabilities.VideoCodec
    class Ladder(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LADDER_UNSPECIFIED: _ClassVar[ClientCapabilities.Ladder]
        LADDER_PHONE: _ClassVar[ClientCapabilities.Ladder]
        LADDER_TV: _ClassVar[ClientCapabilities.Ladder]
        LADDER_LOWRES: _ClassVar[ClientCapabilities.Ladder]
    LADDER_UNSPECIFIED: ClientCapabilities.Ladder
    LADDER_PHONE: ClientCapabilities.Ladder
    LADDER_TV: ClientCapabilities.Ladder
    LADDER_LOWRES: ClientCapabilities.Ladder
    class Resolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESOLUTION_UNSPECIFIED: _ClassVar[ClientCapabilities.Resolution]
        RESOLUTION_SD: _ClassVar[ClientCapabilities.Resolution]
        RESOLUTION_HD: _ClassVar[ClientCapabilities.Resolution]
        RESOLUTION_FHD: _ClassVar[ClientCapabilities.Resolution]
        RESOLUTION_4K: _ClassVar[ClientCapabilities.Resolution]
    RESOLUTION_UNSPECIFIED: ClientCapabilities.Resolution
    RESOLUTION_SD: ClientCapabilities.Resolution
    RESOLUTION_HD: ClientCapabilities.Resolution
    RESOLUTION_FHD: ClientCapabilities.Resolution
    RESOLUTION_4K: ClientCapabilities.Resolution
    class DynamicRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DYNAMIC_RANGE_UNSPECIFIED: _ClassVar[ClientCapabilities.DynamicRange]
        DYNAMIC_RANGE_SDR: _ClassVar[ClientCapabilities.DynamicRange]
        DYNAMIC_RANGE_HDR10: _ClassVar[ClientCapabilities.DynamicRange]
        DYNAMIC_RANGE_DV: _ClassVar[ClientCapabilities.DynamicRange]
    DYNAMIC_RANGE_UNSPECIFIED: ClientCapabilities.DynamicRange
    DYNAMIC_RANGE_SDR: ClientCapabilities.DynamicRange
    DYNAMIC_RANGE_HDR10: ClientCapabilities.DynamicRange
    DYNAMIC_RANGE_DV: ClientCapabilities.DynamicRange
    class AudioCodec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_CODEC_UNSPECIFIED: _ClassVar[ClientCapabilities.AudioCodec]
        AUDIO_CODEC_AAC: _ClassVar[ClientCapabilities.AudioCodec]
        AUDIO_CODEC_EC3: _ClassVar[ClientCapabilities.AudioCodec]
        AUDIO_CODEC_OPUS: _ClassVar[ClientCapabilities.AudioCodec]
        AUDIO_CODEC_AC4: _ClassVar[ClientCapabilities.AudioCodec]
    AUDIO_CODEC_UNSPECIFIED: ClientCapabilities.AudioCodec
    AUDIO_CODEC_AAC: ClientCapabilities.AudioCodec
    AUDIO_CODEC_EC3: ClientCapabilities.AudioCodec
    AUDIO_CODEC_OPUS: ClientCapabilities.AudioCodec
    AUDIO_CODEC_AC4: ClientCapabilities.AudioCodec
    class Orientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORIENTATION_UNSPECIFIED: _ClassVar[ClientCapabilities.Orientation]
        ORIENTATION_VR: _ClassVar[ClientCapabilities.Orientation]
    ORIENTATION_UNSPECIFIED: ClientCapabilities.Orientation
    ORIENTATION_VR: ClientCapabilities.Orientation
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    ADS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTIONS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODECS_FIELD_NUMBER: _ClassVar[int]
    LADDERS_FIELD_NUMBER: _ClassVar[int]
    RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_RANGES_FIELD_NUMBER: _ClassVar[int]
    TRUE_RESOLUTIONS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CODECS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODECS_NON_SECURE_FIELD_NUMBER: _ClassVar[int]
    ORIENTATIONS_FIELD_NUMBER: _ClassVar[int]
    packages: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Package]
    containers: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Container]
    ads: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Ads]
    audio_channels: _containers.RepeatedScalarFieldContainer[ClientCapabilities.AudioChannel]
    encryptions: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Encryption]
    video_codecs: _containers.RepeatedScalarFieldContainer[ClientCapabilities.VideoCodec]
    ladders: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Ladder]
    resolutions: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Resolution]
    dynamic_ranges: _containers.RepeatedScalarFieldContainer[ClientCapabilities.DynamicRange]
    true_resolutions: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Resolution]
    audio_codecs: _containers.RepeatedScalarFieldContainer[ClientCapabilities.AudioCodec]
    video_codecs_non_secure: _containers.RepeatedScalarFieldContainer[ClientCapabilities.VideoCodec]
    orientations: _containers.RepeatedScalarFieldContainer[ClientCapabilities.Orientation]
    def __init__(self, packages: _Optional[_Iterable[_Union[ClientCapabilities.Package, str]]] = ..., containers: _Optional[_Iterable[_Union[ClientCapabilities.Container, str]]] = ..., ads: _Optional[_Iterable[_Union[ClientCapabilities.Ads, str]]] = ..., audio_channels: _Optional[_Iterable[_Union[ClientCapabilities.AudioChannel, str]]] = ..., encryptions: _Optional[_Iterable[_Union[ClientCapabilities.Encryption, str]]] = ..., video_codecs: _Optional[_Iterable[_Union[ClientCapabilities.VideoCodec, str]]] = ..., ladders: _Optional[_Iterable[_Union[ClientCapabilities.Ladder, str]]] = ..., resolutions: _Optional[_Iterable[_Union[ClientCapabilities.Resolution, str]]] = ..., dynamic_ranges: _Optional[_Iterable[_Union[ClientCapabilities.DynamicRange, str]]] = ..., true_resolutions: _Optional[_Iterable[_Union[ClientCapabilities.Resolution, str]]] = ..., audio_codecs: _Optional[_Iterable[_Union[ClientCapabilities.AudioCodec, str]]] = ..., video_codecs_non_secure: _Optional[_Iterable[_Union[ClientCapabilities.VideoCodec, str]]] = ..., orientations: _Optional[_Iterable[_Union[ClientCapabilities.Orientation, str]]] = ...) -> None: ...
