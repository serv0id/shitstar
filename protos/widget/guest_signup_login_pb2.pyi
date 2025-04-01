from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GuestSignupLoginWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "sub_title", "login_btn_text", "actions", "image", "primary_button", "help_rich_text", "help_support_cta")
        class Button(_message.Message):
            __slots__ = ("label", "actions", "icon_name")
            LABEL_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            ICON_NAME_FIELD_NUMBER: _ClassVar[int]
            label: str
            actions: _actions_pb2.Actions
            icon_name: str
            def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon_name: _Optional[str] = ...) -> None: ...
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        LOGIN_BTN_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        HELP_SUPPORT_CTA_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        login_btn_text: str
        actions: _actions_pb2.Actions
        image: _image_pb2.Image
        primary_button: GuestSignupLoginWidget.Data.Button
        help_rich_text: str
        help_support_cta: GuestSignupLoginWidget.Data.Button
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., login_btn_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., primary_button: _Optional[_Union[GuestSignupLoginWidget.Data.Button, _Mapping]] = ..., help_rich_text: _Optional[str] = ..., help_support_cta: _Optional[_Union[GuestSignupLoginWidget.Data.Button, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: GuestSignupLoginWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[GuestSignupLoginWidget.Data, _Mapping]] = ...) -> None: ...
