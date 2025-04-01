from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectionTransformer(_message.Message):
    __slots__ = ("configs",)
    class Service(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[CollectionTransformer.Service]
        WATCHLIST: _ClassVar[CollectionTransformer.Service]
        CW: _ClassVar[CollectionTransformer.Service]
    UNSPECIFIED: CollectionTransformer.Service
    WATCHLIST: CollectionTransformer.Service
    CW: CollectionTransformer.Service
    class Transformer(_message.Message):
        __slots__ = ("derank", "discount")
        DERANK_FIELD_NUMBER: _ClassVar[int]
        DISCOUNT_FIELD_NUMBER: _ClassVar[int]
        derank: CollectionTransformer.Deranking
        discount: CollectionTransformer.Discounting
        def __init__(self, derank: _Optional[_Union[CollectionTransformer.Deranking, _Mapping]] = ..., discount: _Optional[_Union[CollectionTransformer.Discounting, _Mapping]] = ...) -> None: ...
    class Deranking(_message.Message):
        __slots__ = ("services",)
        SERVICES_FIELD_NUMBER: _ClassVar[int]
        services: _containers.RepeatedScalarFieldContainer[CollectionTransformer.Service]
        def __init__(self, services: _Optional[_Iterable[_Union[CollectionTransformer.Service, str]]] = ...) -> None: ...
    class Discounting(_message.Message):
        __slots__ = ("services",)
        SERVICES_FIELD_NUMBER: _ClassVar[int]
        services: _containers.RepeatedScalarFieldContainer[CollectionTransformer.Service]
        def __init__(self, services: _Optional[_Iterable[_Union[CollectionTransformer.Service, str]]] = ...) -> None: ...
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    configs: _containers.RepeatedCompositeFieldContainer[CollectionTransformer.Transformer]
    def __init__(self, configs: _Optional[_Iterable[_Union[CollectionTransformer.Transformer, _Mapping]]] = ...) -> None: ...
