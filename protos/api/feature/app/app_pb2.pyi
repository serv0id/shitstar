from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class App(_message.Message):
    __slots__ = ("name", "version", "build", "library", "app_id", "is_spoofing_enabled", "active_app_themes", "shell_app_version", "installing_package_name")
    class Library(_message.Message):
        __slots__ = ("name", "version")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        name: str
        version: str
        def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    IS_SPOOFING_ENABLED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_APP_THEMES_FIELD_NUMBER: _ClassVar[int]
    SHELL_APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTALLING_PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: str
    build: int
    library: App.Library
    app_id: str
    is_spoofing_enabled: bool
    active_app_themes: _containers.RepeatedScalarFieldContainer[str]
    shell_app_version: str
    installing_package_name: str
    def __init__(self, name: _Optional[str] = ..., version: _Optional[str] = ..., build: _Optional[int] = ..., library: _Optional[_Union[App.Library, _Mapping]] = ..., app_id: _Optional[str] = ..., is_spoofing_enabled: bool = ..., active_app_themes: _Optional[_Iterable[str]] = ..., shell_app_version: _Optional[str] = ..., installing_package_name: _Optional[str] = ...) -> None: ...
