from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ("major", "minor", "patch", "suffix")
    MAJOR_FIELD_NUMBER: _ClassVar[int]
    MINOR_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    major: int
    minor: int
    patch: int
    suffix: str
    def __init__(self, major: _Optional[int] = ..., minor: _Optional[int] = ..., patch: _Optional[int] = ..., suffix: _Optional[str] = ...) -> None: ...

class CodeGeneratorRequest(_message.Message):
    __slots__ = ("file_to_generate", "parameter", "proto_file", "compiler_version")
    FILE_TO_GENERATE_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    PROTO_FILE_FIELD_NUMBER: _ClassVar[int]
    COMPILER_VERSION_FIELD_NUMBER: _ClassVar[int]
    file_to_generate: _containers.RepeatedScalarFieldContainer[str]
    parameter: str
    proto_file: _containers.RepeatedCompositeFieldContainer[_descriptor_pb2.FileDescriptorProto]
    compiler_version: Version
    def __init__(self, file_to_generate: _Optional[_Iterable[str]] = ..., parameter: _Optional[str] = ..., proto_file: _Optional[_Iterable[_Union[_descriptor_pb2.FileDescriptorProto, _Mapping]]] = ..., compiler_version: _Optional[_Union[Version, _Mapping]] = ...) -> None: ...

class CodeGeneratorResponse(_message.Message):
    __slots__ = ("error", "supported_features", "file")
    class Feature(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FEATURE_NONE: _ClassVar[CodeGeneratorResponse.Feature]
        FEATURE_PROTO3_OPTIONAL: _ClassVar[CodeGeneratorResponse.Feature]
    FEATURE_NONE: CodeGeneratorResponse.Feature
    FEATURE_PROTO3_OPTIONAL: CodeGeneratorResponse.Feature
    class File(_message.Message):
        __slots__ = ("name", "insertion_point", "content", "generated_code_info")
        NAME_FIELD_NUMBER: _ClassVar[int]
        INSERTION_POINT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        GENERATED_CODE_INFO_FIELD_NUMBER: _ClassVar[int]
        name: str
        insertion_point: str
        content: str
        generated_code_info: _descriptor_pb2.GeneratedCodeInfo
        def __init__(self, name: _Optional[str] = ..., insertion_point: _Optional[str] = ..., content: _Optional[str] = ..., generated_code_info: _Optional[_Union[_descriptor_pb2.GeneratedCodeInfo, _Mapping]] = ...) -> None: ...
    ERROR_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_FEATURES_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    error: str
    supported_features: int
    file: _containers.RepeatedCompositeFieldContainer[CodeGeneratorResponse.File]
    def __init__(self, error: _Optional[str] = ..., supported_features: _Optional[int] = ..., file: _Optional[_Iterable[_Union[CodeGeneratorResponse.File, _Mapping]]] = ...) -> None: ...
