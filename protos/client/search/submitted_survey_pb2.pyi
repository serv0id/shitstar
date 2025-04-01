from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmittedSurveyProperties(_message.Message):
    __slots__ = ("survey_question", "response_list", "selected_response_count", "user_written_review", "query_text", "page_type")
    SURVEY_QUESTION_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_LIST_FIELD_NUMBER: _ClassVar[int]
    SELECTED_RESPONSE_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_WRITTEN_REVIEW_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    survey_question: str
    response_list: ResponseList
    selected_response_count: int
    user_written_review: str
    query_text: str
    page_type: str
    def __init__(self, survey_question: _Optional[str] = ..., response_list: _Optional[_Union[ResponseList, _Mapping]] = ..., selected_response_count: _Optional[int] = ..., user_written_review: _Optional[str] = ..., query_text: _Optional[str] = ..., page_type: _Optional[str] = ...) -> None: ...

class ResponseList(_message.Message):
    __slots__ = ("responses",)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, responses: _Optional[_Iterable[str]] = ...) -> None: ...
