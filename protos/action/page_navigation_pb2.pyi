from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageNavigationAction(_message.Message):
    __slots__ = ["page_type", "page_url", "page_slug", "params", "replace"]
    class Params(_message.Message):
        __slots__ = ["watch_params"]
        WATCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
        watch_params: PageNavigationAction.WatchParams
        def __init__(self, watch_params: _Optional[_Union[PageNavigationAction.WatchParams, _Mapping]] = ...) -> None: ...
    class WatchParams(_message.Message):
        __slots__ = ["loading_image", "is_fullscreen_by_default", "refresh_spaces"]
        class SpaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            UNKNOWN: _ClassVar[PageNavigationAction.WatchParams.SpaceType]
            PLAYER: _ClassVar[PageNavigationAction.WatchParams.SpaceType]
            WATCH_OVERLAY: _ClassVar[PageNavigationAction.WatchParams.SpaceType]
            ADAPTIVE_TRAY: _ClassVar[PageNavigationAction.WatchParams.SpaceType]
            ADAPTIVE_TAB_CONTAINER: _ClassVar[PageNavigationAction.WatchParams.SpaceType]
        UNKNOWN: PageNavigationAction.WatchParams.SpaceType
        PLAYER: PageNavigationAction.WatchParams.SpaceType
        WATCH_OVERLAY: PageNavigationAction.WatchParams.SpaceType
        ADAPTIVE_TRAY: PageNavigationAction.WatchParams.SpaceType
        ADAPTIVE_TAB_CONTAINER: PageNavigationAction.WatchParams.SpaceType
        LOADING_IMAGE_FIELD_NUMBER: _ClassVar[int]
        IS_FULLSCREEN_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        REFRESH_SPACES_FIELD_NUMBER: _ClassVar[int]
        loading_image: _image_pb2.Image
        is_fullscreen_by_default: bool
        refresh_spaces: _containers.RepeatedScalarFieldContainer[PageNavigationAction.WatchParams.SpaceType]
        def __init__(self, loading_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., is_fullscreen_by_default: bool = ..., refresh_spaces: _Optional[_Iterable[_Union[PageNavigationAction.WatchParams.SpaceType, str]]] = ...) -> None: ...
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SLUG_FIELD_NUMBER: _ClassVar[int]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    page_type: str
    page_url: str
    page_slug: str
    params: PageNavigationAction.Params
    replace: bool
    def __init__(self, page_type: _Optional[str] = ..., page_url: _Optional[str] = ..., page_slug: _Optional[str] = ..., params: _Optional[_Union[PageNavigationAction.Params, _Mapping]] = ..., replace: bool = ...) -> None: ...
