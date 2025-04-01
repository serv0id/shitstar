from client.crm.model import crm_page_info_pb2 as _crm_page_info_pb2
from client.crm.properties import help_page_properties_pb2 as _help_page_properties_pb2
from client.crm.properties import help_user_properties_pb2 as _help_user_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelpSearchProperties(_message.Message):
    __slots__ = ("help_user_properties", "help_page_properties", "help_search_query", "help_search_no_of_results", "help_search_article_id_clicked")
    HELP_USER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    HELP_PAGE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    HELP_SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
    HELP_SEARCH_NO_OF_RESULTS_FIELD_NUMBER: _ClassVar[int]
    HELP_SEARCH_ARTICLE_ID_CLICKED_FIELD_NUMBER: _ClassVar[int]
    help_user_properties: _help_user_properties_pb2.HelpUserProperties
    help_page_properties: _help_page_properties_pb2.HelpPageProperties
    help_search_query: str
    help_search_no_of_results: int
    help_search_article_id_clicked: str
    def __init__(self, help_user_properties: _Optional[_Union[_help_user_properties_pb2.HelpUserProperties, _Mapping]] = ..., help_page_properties: _Optional[_Union[_help_page_properties_pb2.HelpPageProperties, _Mapping]] = ..., help_search_query: _Optional[str] = ..., help_search_no_of_results: _Optional[int] = ..., help_search_article_id_clicked: _Optional[str] = ...) -> None: ...
