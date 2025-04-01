from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TabInvokeProperties(_message.Message):
    __slots__ = ("tab_invoke_source",)
    class TabInvokeSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TAB_INVOKE_SOURCE_UNSPECIFIED: _ClassVar[TabInvokeProperties.TabInvokeSource]
        TAB_INVOKE_SOURCE_BUTTON: _ClassVar[TabInvokeProperties.TabInvokeSource]
        TAB_INVOKE_SOURCE_PEEK_TRAY: _ClassVar[TabInvokeProperties.TabInvokeSource]
        TAB_INVOKE_SOURCE_SWIPE_UP: _ClassVar[TabInvokeProperties.TabInvokeSource]
        TAB_INVOKE_SOURCE_SWITCH_TABS: _ClassVar[TabInvokeProperties.TabInvokeSource]
    TAB_INVOKE_SOURCE_UNSPECIFIED: TabInvokeProperties.TabInvokeSource
    TAB_INVOKE_SOURCE_BUTTON: TabInvokeProperties.TabInvokeSource
    TAB_INVOKE_SOURCE_PEEK_TRAY: TabInvokeProperties.TabInvokeSource
    TAB_INVOKE_SOURCE_SWIPE_UP: TabInvokeProperties.TabInvokeSource
    TAB_INVOKE_SOURCE_SWITCH_TABS: TabInvokeProperties.TabInvokeSource
    TAB_INVOKE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    tab_invoke_source: TabInvokeProperties.TabInvokeSource
    def __init__(self, tab_invoke_source: _Optional[_Union[TabInvokeProperties.TabInvokeSource, str]] = ...) -> None: ...
