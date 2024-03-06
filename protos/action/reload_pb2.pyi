from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReloadAction(_message.Message):
    __slots__ = ["context"]
    class Context(_message.Message):
        __slots__ = ["page_context", "space_context", "widget_context"]
        PAGE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        SPACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        WIDGET_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        page_context: ReloadAction.PageContext
        space_context: ReloadAction.SpaceContext
        widget_context: ReloadAction.WidgetContext
        def __init__(self, page_context: _Optional[_Union[ReloadAction.PageContext, _Mapping]] = ..., space_context: _Optional[_Union[ReloadAction.SpaceContext, _Mapping]] = ..., widget_context: _Optional[_Union[ReloadAction.WidgetContext, _Mapping]] = ...) -> None: ...
    class PageContext(_message.Message):
        __slots__ = ["reload_with_url"]
        RELOAD_WITH_URL_FIELD_NUMBER: _ClassVar[int]
        reload_with_url: str
        def __init__(self, reload_with_url: _Optional[str] = ...) -> None: ...
    class SpaceContext(_message.Message):
        __slots__ = ["reload_with_url"]
        RELOAD_WITH_URL_FIELD_NUMBER: _ClassVar[int]
        reload_with_url: str
        def __init__(self, reload_with_url: _Optional[str] = ...) -> None: ...
    class WidgetContext(_message.Message):
        __slots__ = ["reload_with_url"]
        RELOAD_WITH_URL_FIELD_NUMBER: _ClassVar[int]
        reload_with_url: str
        def __init__(self, reload_with_url: _Optional[str] = ...) -> None: ...
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    context: ReloadAction.Context
    def __init__(self, context: _Optional[_Union[ReloadAction.Context, _Mapping]] = ...) -> None: ...
