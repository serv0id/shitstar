from protos.base import template_pb2 as _template_pb2
from protos.base import widget_commons_pb2 as _widget_commons_pb2
from protos.base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginSuccessWidget(_message.Message):
    __slots__ = ["template", "widget_commons", "data"]
    class Data(_message.Message):
        __slots__ = ["text", "user_identity", "on_complete_actions", "mobile_number", "email_address"]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        USER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
        ON_COMPLETE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        text: str
        user_identity: str
        on_complete_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        mobile_number: str
        email_address: str
        def __init__(self, text: _Optional[str] = ..., user_identity: _Optional[str] = ..., on_complete_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., mobile_number: _Optional[str] = ..., email_address: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LoginSuccessWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LoginSuccessWidget.Data, _Mapping]] = ...) -> None: ...
