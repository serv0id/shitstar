from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditProfileWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "name_edit_label", "delete_label", "maturity_text", "save_action", "delete_option", "name_input_regex", "delete_btn", "invalid_name_user_message", "name_max_length")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        NAME_EDIT_LABEL_FIELD_NUMBER: _ClassVar[int]
        DELETE_LABEL_FIELD_NUMBER: _ClassVar[int]
        MATURITY_TEXT_FIELD_NUMBER: _ClassVar[int]
        SAVE_ACTION_FIELD_NUMBER: _ClassVar[int]
        DELETE_OPTION_FIELD_NUMBER: _ClassVar[int]
        NAME_INPUT_REGEX_FIELD_NUMBER: _ClassVar[int]
        DELETE_BTN_FIELD_NUMBER: _ClassVar[int]
        INVALID_NAME_USER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        NAME_MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
        title: str
        name_edit_label: str
        delete_label: str
        maturity_text: str
        save_action: EditProfileWidget.CTA
        delete_option: EditProfileWidget.DeleteOption
        name_input_regex: str
        delete_btn: EditProfileWidget.CTA
        invalid_name_user_message: str
        name_max_length: str
        def __init__(self, title: _Optional[str] = ..., name_edit_label: _Optional[str] = ..., delete_label: _Optional[str] = ..., maturity_text: _Optional[str] = ..., save_action: _Optional[_Union[EditProfileWidget.CTA, _Mapping]] = ..., delete_option: _Optional[_Union[EditProfileWidget.DeleteOption, _Mapping]] = ..., name_input_regex: _Optional[str] = ..., delete_btn: _Optional[_Union[EditProfileWidget.CTA, _Mapping]] = ..., invalid_name_user_message: _Optional[str] = ..., name_max_length: _Optional[str] = ...) -> None: ...
    class DeleteOption(_message.Message):
        __slots__ = ("title", "desc", "cancel", "delete")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        CANCEL_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_NUMBER: _ClassVar[int]
        title: str
        desc: str
        cancel: EditProfileWidget.CTA
        delete: EditProfileWidget.CTA
        def __init__(self, title: _Optional[str] = ..., desc: _Optional[str] = ..., cancel: _Optional[_Union[EditProfileWidget.CTA, _Mapping]] = ..., delete: _Optional[_Union[EditProfileWidget.CTA, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("label", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: EditProfileWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[EditProfileWidget.Data, _Mapping]] = ...) -> None: ...
