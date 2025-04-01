from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import dialog_pb2 as _dialog_pb2
from feature.image import image_pb2 as _image_pb2
from feature.atom import button_pb2 as _button_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppLanguageSwitchWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "language_list", "dialog", "change_language", "close")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        DIALOG_FIELD_NUMBER: _ClassVar[int]
        CHANGE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        CLOSE_FIELD_NUMBER: _ClassVar[int]
        title: str
        language_list: AppLanguageSwitchWidget.LanguageList
        dialog: _dialog_pb2.DialogWidget
        change_language: _button_pb2.Button
        close: _button_pb2.Button
        def __init__(self, title: _Optional[str] = ..., language_list: _Optional[_Union[AppLanguageSwitchWidget.LanguageList, _Mapping]] = ..., dialog: _Optional[_Union[_dialog_pb2.DialogWidget, _Mapping]] = ..., change_language: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., close: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    class LanguageList(_message.Message):
        __slots__ = ("options",)
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        options: _containers.RepeatedCompositeFieldContainer[AppLanguageSwitchWidget.ListOption]
        def __init__(self, options: _Optional[_Iterable[_Union[AppLanguageSwitchWidget.ListOption, _Mapping]]] = ...) -> None: ...
    class ListOption(_message.Message):
        __slots__ = ("label", "lang_code", "is_selected")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LANG_CODE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        label: str
        lang_code: str
        is_selected: bool
        def __init__(self, label: _Optional[str] = ..., lang_code: _Optional[str] = ..., is_selected: bool = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AppLanguageSwitchWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AppLanguageSwitchWidget.Data, _Mapping]] = ...) -> None: ...
