from feature.image import image_pb2 as _image_pb2
from feature.text import text_pb2 as _text_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CalloutTag(_message.Message):
    __slots__ = ("tag_template_name", "img", "txt", "img_txt_vertical", "txt_img_vertical", "img_txt_horizontal", "txt_img_horizontal")
    class ImageTag(_message.Message):
        __slots__ = ("image", "actions")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class TextTag(_message.Message):
        __slots__ = ("text", "actions", "text_v2", "text_tag_type")
        class TextTagType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEFAULT: _ClassVar[CalloutTag.TextTag.TextTagType]
            BADGE: _ClassVar[CalloutTag.TextTag.TextTagType]
        DEFAULT: CalloutTag.TextTag.TextTagType
        BADGE: CalloutTag.TextTag.TextTagType
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_V2_FIELD_NUMBER: _ClassVar[int]
        TEXT_TAG_TYPE_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        text_v2: _text_pb2.Text
        text_tag_type: CalloutTag.TextTag.TextTagType
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text_v2: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., text_tag_type: _Optional[_Union[CalloutTag.TextTag.TextTagType, str]] = ...) -> None: ...
    class ImageTextVerticalTag(_message.Message):
        __slots__ = ("image", "text", "actions", "text_v2")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_V2_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        text: str
        actions: _actions_pb2.Actions
        text_v2: _text_pb2.Text
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text_v2: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    class TextImageVerticalTag(_message.Message):
        __slots__ = ("image", "text", "actions", "text_v2")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_V2_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        text: str
        actions: _actions_pb2.Actions
        text_v2: _text_pb2.Text
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text_v2: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    class ImageTextHorizontalTag(_message.Message):
        __slots__ = ("image", "text", "actions", "text_v2")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_V2_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        text: str
        actions: _actions_pb2.Actions
        text_v2: _text_pb2.Text
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text_v2: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    class TextImageHorizontalTag(_message.Message):
        __slots__ = ("image", "text", "actions", "text_v2")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_V2_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        text: str
        actions: _actions_pb2.Actions
        text_v2: _text_pb2.Text
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text_v2: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    TAG_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    IMG_FIELD_NUMBER: _ClassVar[int]
    TXT_FIELD_NUMBER: _ClassVar[int]
    IMG_TXT_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    TXT_IMG_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    IMG_TXT_HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
    TXT_IMG_HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
    tag_template_name: str
    img: CalloutTag.ImageTag
    txt: CalloutTag.TextTag
    img_txt_vertical: CalloutTag.ImageTextVerticalTag
    txt_img_vertical: CalloutTag.TextImageVerticalTag
    img_txt_horizontal: CalloutTag.ImageTextHorizontalTag
    txt_img_horizontal: CalloutTag.TextImageHorizontalTag
    def __init__(self, tag_template_name: _Optional[str] = ..., img: _Optional[_Union[CalloutTag.ImageTag, _Mapping]] = ..., txt: _Optional[_Union[CalloutTag.TextTag, _Mapping]] = ..., img_txt_vertical: _Optional[_Union[CalloutTag.ImageTextVerticalTag, _Mapping]] = ..., txt_img_vertical: _Optional[_Union[CalloutTag.TextImageVerticalTag, _Mapping]] = ..., img_txt_horizontal: _Optional[_Union[CalloutTag.ImageTextHorizontalTag, _Mapping]] = ..., txt_img_horizontal: _Optional[_Union[CalloutTag.TextImageHorizontalTag, _Mapping]] = ...) -> None: ...
