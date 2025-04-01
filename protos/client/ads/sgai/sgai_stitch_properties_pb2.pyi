from client.ads.sgai import ad_break_pb2 as _ad_break_pb2
from client.ads.sgai import content_meta_pb2 as _content_meta_pb2
from client.ads.sgai import stitch_attributes_pb2 as _stitch_attributes_pb2
from client.ads.sgai import user_properties_pb2 as _user_properties_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SgaiStitchProperties(_message.Message):
    __slots__ = ("content_meta", "stitch_attributes", "ad_breaks", "user_properties")
    CONTENT_META_FIELD_NUMBER: _ClassVar[int]
    STITCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    AD_BREAKS_FIELD_NUMBER: _ClassVar[int]
    USER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    content_meta: _content_meta_pb2.ContentMeta
    stitch_attributes: _stitch_attributes_pb2.StitchAttributes
    ad_breaks: _containers.RepeatedCompositeFieldContainer[_ad_break_pb2.AdBreak]
    user_properties: _user_properties_pb2.UserProperties
    def __init__(self, content_meta: _Optional[_Union[_content_meta_pb2.ContentMeta, _Mapping]] = ..., stitch_attributes: _Optional[_Union[_stitch_attributes_pb2.StitchAttributes, _Mapping]] = ..., ad_breaks: _Optional[_Iterable[_Union[_ad_break_pb2.AdBreak, _Mapping]]] = ..., user_properties: _Optional[_Union[_user_properties_pb2.UserProperties, _Mapping]] = ...) -> None: ...
