from base import page_data_commons_pb2 as _page_data_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SurveyPageData(_message.Message):
    __slots__ = ("page_data_commons", "meta_data")
    class SurveyMetaData(_message.Message):
        __slots__ = ("title", "survey_id")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SURVEY_ID_FIELD_NUMBER: _ClassVar[int]
        title: str
        survey_id: str
        def __init__(self, title: _Optional[str] = ..., survey_id: _Optional[str] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    META_DATA_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    meta_data: SurveyPageData.SurveyMetaData
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., meta_data: _Optional[_Union[SurveyPageData.SurveyMetaData, _Mapping]] = ...) -> None: ...
