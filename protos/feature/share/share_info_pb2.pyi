from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShareInfo(_message.Message):
    __slots__ = ("image_type", "text_type", "share_params")
    class ImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ShareInfo.ImageType]
        SCREENCAP: _ClassVar[ShareInfo.ImageType]
        IMAGE_URL: _ClassVar[ShareInfo.ImageType]
    UNSPECIFIED: ShareInfo.ImageType
    SCREENCAP: ShareInfo.ImageType
    IMAGE_URL: ShareInfo.ImageType
    class ShareUsingAppPackage(_message.Message):
        __slots__ = ("data", "title", "package_name")
        DATA_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        data: str
        title: str
        package_name: str
        def __init__(self, data: _Optional[str] = ..., title: _Optional[str] = ..., package_name: _Optional[str] = ...) -> None: ...
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARE_PARAMS_FIELD_NUMBER: _ClassVar[int]
    image_type: ShareInfo.ImageType
    text_type: str
    share_params: ShareInfo.ShareUsingAppPackage
    def __init__(self, image_type: _Optional[_Union[ShareInfo.ImageType, str]] = ..., text_type: _Optional[str] = ..., share_params: _Optional[_Union[ShareInfo.ShareUsingAppPackage, _Mapping]] = ...) -> None: ...
