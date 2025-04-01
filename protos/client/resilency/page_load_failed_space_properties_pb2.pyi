from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PageLoadFailedSpaceProperties(_message.Message):
    __slots__ = ("failed_space_template", "failed_widgets_templates")
    FAILED_SPACE_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    FAILED_WIDGETS_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    failed_space_template: str
    failed_widgets_templates: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, failed_space_template: _Optional[str] = ..., failed_widgets_templates: _Optional[_Iterable[str]] = ...) -> None: ...
