from base import page_data_commons_pb2 as _page_data_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuizPageData(_message.Message):
    __slots__ = ("page_data_commons", "meta_data")
    class PageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        QUIZ: _ClassVar[QuizPageData.PageType]
        POLL: _ClassVar[QuizPageData.PageType]
    QUIZ: QuizPageData.PageType
    POLL: QuizPageData.PageType
    class QuizMetaData(_message.Message):
        __slots__ = ("title", "season_id", "round_id", "backdrop_img", "page_type")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SEASON_ID_FIELD_NUMBER: _ClassVar[int]
        ROUND_ID_FIELD_NUMBER: _ClassVar[int]
        BACKDROP_IMG_FIELD_NUMBER: _ClassVar[int]
        PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        title: str
        season_id: str
        round_id: str
        backdrop_img: _image_pb2.Image
        page_type: QuizPageData.PageType
        def __init__(self, title: _Optional[str] = ..., season_id: _Optional[str] = ..., round_id: _Optional[str] = ..., backdrop_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., page_type: _Optional[_Union[QuizPageData.PageType, str]] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    meta_data: QuizPageData.QuizMetaData
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., meta_data: _Optional[_Union[QuizPageData.QuizMetaData, _Mapping]] = ...) -> None: ...
