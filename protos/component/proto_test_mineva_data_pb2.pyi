from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestEnum(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TEST_ENUM_UNSPECIFIED: _ClassVar[TestEnum]
    TEST_ENUM_OK1: _ClassVar[TestEnum]
    TEST_ENUM_OK2: _ClassVar[TestEnum]
TEST_ENUM_UNSPECIFIED: TestEnum
TEST_ENUM_OK1: TestEnum
TEST_ENUM_OK2: TestEnum

class ProtoTestMinervaData(_message.Message):
    __slots__ = ("message_id", "ts_received_ms", "test_str", "test_uint64", "test_fixed32", "test_sfixed64", "test_float", "test_double", "test_bool", "test_oneof_str", "test_oneof_int32")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TS_RECEIVED_MS_FIELD_NUMBER: _ClassVar[int]
    TEST_STR_FIELD_NUMBER: _ClassVar[int]
    TEST_UINT64_FIELD_NUMBER: _ClassVar[int]
    TEST_FIXED32_FIELD_NUMBER: _ClassVar[int]
    TEST_SFIXED64_FIELD_NUMBER: _ClassVar[int]
    TEST_FLOAT_FIELD_NUMBER: _ClassVar[int]
    TEST_DOUBLE_FIELD_NUMBER: _ClassVar[int]
    TEST_BOOL_FIELD_NUMBER: _ClassVar[int]
    TEST_ONEOF_STR_FIELD_NUMBER: _ClassVar[int]
    TEST_ONEOF_INT32_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    ts_received_ms: int
    test_str: str
    test_uint64: int
    test_fixed32: int
    test_sfixed64: int
    test_float: float
    test_double: float
    test_bool: bool
    test_oneof_str: str
    test_oneof_int32: int
    def __init__(self, message_id: _Optional[str] = ..., ts_received_ms: _Optional[int] = ..., test_str: _Optional[str] = ..., test_uint64: _Optional[int] = ..., test_fixed32: _Optional[int] = ..., test_sfixed64: _Optional[int] = ..., test_float: _Optional[float] = ..., test_double: _Optional[float] = ..., test_bool: bool = ..., test_oneof_str: _Optional[str] = ..., test_oneof_int32: _Optional[int] = ...) -> None: ...

class TestMessage(_message.Message):
    __slots__ = ("msg_str",)
    MSG_STR_FIELD_NUMBER: _ClassVar[int]
    msg_str: str
    def __init__(self, msg_str: _Optional[str] = ...) -> None: ...

class ProtoTestMinervaData2(_message.Message):
    __slots__ = ("message_id", "ts_received_ms", "test2_int32", "test2_enum", "rep_test2_enums", "rep_test2_strs", "test2_msg", "rep_test2_msgs", "test2_map", "test2_oneof_str", "test2_oneof_int32")
    class Test2MapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TS_RECEIVED_MS_FIELD_NUMBER: _ClassVar[int]
    TEST2_INT32_FIELD_NUMBER: _ClassVar[int]
    TEST2_ENUM_FIELD_NUMBER: _ClassVar[int]
    REP_TEST2_ENUMS_FIELD_NUMBER: _ClassVar[int]
    REP_TEST2_STRS_FIELD_NUMBER: _ClassVar[int]
    TEST2_MSG_FIELD_NUMBER: _ClassVar[int]
    REP_TEST2_MSGS_FIELD_NUMBER: _ClassVar[int]
    TEST2_MAP_FIELD_NUMBER: _ClassVar[int]
    TEST2_ONEOF_STR_FIELD_NUMBER: _ClassVar[int]
    TEST2_ONEOF_INT32_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    ts_received_ms: int
    test2_int32: int
    test2_enum: TestEnum
    rep_test2_enums: _containers.RepeatedScalarFieldContainer[TestEnum]
    rep_test2_strs: _containers.RepeatedScalarFieldContainer[str]
    test2_msg: TestMessage
    rep_test2_msgs: _containers.RepeatedCompositeFieldContainer[TestMessage]
    test2_map: _containers.ScalarMap[str, int]
    test2_oneof_str: str
    test2_oneof_int32: int
    def __init__(self, message_id: _Optional[str] = ..., ts_received_ms: _Optional[int] = ..., test2_int32: _Optional[int] = ..., test2_enum: _Optional[_Union[TestEnum, str]] = ..., rep_test2_enums: _Optional[_Iterable[_Union[TestEnum, str]]] = ..., rep_test2_strs: _Optional[_Iterable[str]] = ..., test2_msg: _Optional[_Union[TestMessage, _Mapping]] = ..., rep_test2_msgs: _Optional[_Iterable[_Union[TestMessage, _Mapping]]] = ..., test2_map: _Optional[_Mapping[str, int]] = ..., test2_oneof_str: _Optional[str] = ..., test2_oneof_int32: _Optional[int] = ...) -> None: ...
