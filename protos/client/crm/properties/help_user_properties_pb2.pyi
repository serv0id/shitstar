from client.crm.model import crm_user_info_pb2 as _crm_user_info_pb2
from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HelpUserProperties(_message.Message):
    __slots__ = ("ab_experiment_flags", "subscription_type", "app_version")
    AB_EXPERIMENT_FLAGS_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    ab_experiment_flags: _containers.RepeatedCompositeFieldContainer[_crm_user_info_pb2.AbExperimentFlag]
    subscription_type: str
    app_version: str
    def __init__(self, ab_experiment_flags: _Optional[_Iterable[_Union[_crm_user_info_pb2.AbExperimentFlag, _Mapping]]] = ..., subscription_type: _Optional[str] = ..., app_version: _Optional[str] = ...) -> None: ...
