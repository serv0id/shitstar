from client.crm.model import crm_page_info_pb2 as _crm_page_info_pb2
from options import opts_pb2 as _opts_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelpPageProperties(_message.Message):
    __slots__ = ("type", "language", "title", "referrer")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    type: _crm_page_info_pb2.PageType
    language: str
    title: str
    referrer: str
    def __init__(self, type: _Optional[_Union[_crm_page_info_pb2.PageType, str]] = ..., language: _Optional[str] = ..., title: _Optional[str] = ..., referrer: _Optional[str] = ...) -> None: ...
