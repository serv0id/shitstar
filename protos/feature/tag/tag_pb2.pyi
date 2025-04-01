from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tag(_message.Message):
    __slots__ = ("text_tag", "badge_tag", "image_tag", "callout_tag")
    class TextTag(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class BadgeTag(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class ImageTag(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: _image_pb2.Image
        def __init__(self, value: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    TEXT_TAG_FIELD_NUMBER: _ClassVar[int]
    BADGE_TAG_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_TAG_FIELD_NUMBER: _ClassVar[int]
    text_tag: Tag.TextTag
    badge_tag: Tag.BadgeTag
    image_tag: Tag.ImageTag
    callout_tag: _callout_tag_pb2.CalloutTag
    def __init__(self, text_tag: _Optional[_Union[Tag.TextTag, _Mapping]] = ..., badge_tag: _Optional[_Union[Tag.BadgeTag, _Mapping]] = ..., image_tag: _Optional[_Union[Tag.ImageTag, _Mapping]] = ..., callout_tag: _Optional[_Union[_callout_tag_pb2.CalloutTag, _Mapping]] = ...) -> None: ...
