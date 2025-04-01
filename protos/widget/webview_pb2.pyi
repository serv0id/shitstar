from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.trackers import url_trackers_pb2 as _url_trackers_pb2
from feature.request import http_token_request_pb2 as _http_token_request_pb2
from widget import header_pb2 as _header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebviewWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("content", "tracker", "allowed_fields", "enable_javascript", "widget_additional_properties", "jit", "disable_zoom")
        class JsBridgeFields(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            PINCODE: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            NAME: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            LOGIN_STATUS: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            FORM_SUBMIT: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            EXTERNAL_NAV: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            AD_ERROR: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            CITY: _ClassVar[WebviewWidget.Data.JsBridgeFields]
            STATE: _ClassVar[WebviewWidget.Data.JsBridgeFields]
        UNKNOWN: WebviewWidget.Data.JsBridgeFields
        PINCODE: WebviewWidget.Data.JsBridgeFields
        NAME: WebviewWidget.Data.JsBridgeFields
        LOGIN_STATUS: WebviewWidget.Data.JsBridgeFields
        FORM_SUBMIT: WebviewWidget.Data.JsBridgeFields
        EXTERNAL_NAV: WebviewWidget.Data.JsBridgeFields
        AD_ERROR: WebviewWidget.Data.JsBridgeFields
        CITY: WebviewWidget.Data.JsBridgeFields
        STATE: WebviewWidget.Data.JsBridgeFields
        class Content(_message.Message):
            __slots__ = ("meta", "header", "webview_url")
            class Meta(_message.Message):
                __slots__ = ("webpage_logo", "webpage_title")
                WEBPAGE_LOGO_FIELD_NUMBER: _ClassVar[int]
                WEBPAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
                webpage_logo: _image_pb2.Image
                webpage_title: str
                def __init__(self, webpage_logo: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., webpage_title: _Optional[str] = ...) -> None: ...
            META_FIELD_NUMBER: _ClassVar[int]
            HEADER_FIELD_NUMBER: _ClassVar[int]
            WEBVIEW_URL_FIELD_NUMBER: _ClassVar[int]
            meta: WebviewWidget.Data.Content.Meta
            header: _header_pb2.HeaderWidget
            webview_url: str
            def __init__(self, meta: _Optional[_Union[WebviewWidget.Data.Content.Meta, _Mapping]] = ..., header: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ..., webview_url: _Optional[str] = ...) -> None: ...
        class WidgetAdditionalPropertiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        TRACKER_FIELD_NUMBER: _ClassVar[int]
        ALLOWED_FIELDS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_JAVASCRIPT_FIELD_NUMBER: _ClassVar[int]
        WIDGET_ADDITIONAL_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        JIT_FIELD_NUMBER: _ClassVar[int]
        DISABLE_ZOOM_FIELD_NUMBER: _ClassVar[int]
        content: WebviewWidget.Data.Content
        tracker: _url_trackers_pb2.UrlTrackers
        allowed_fields: _containers.RepeatedScalarFieldContainer[WebviewWidget.Data.JsBridgeFields]
        enable_javascript: bool
        widget_additional_properties: _containers.ScalarMap[str, str]
        jit: _http_token_request_pb2.HttpTokenRequest
        disable_zoom: bool
        def __init__(self, content: _Optional[_Union[WebviewWidget.Data.Content, _Mapping]] = ..., tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ..., allowed_fields: _Optional[_Iterable[_Union[WebviewWidget.Data.JsBridgeFields, str]]] = ..., enable_javascript: bool = ..., widget_additional_properties: _Optional[_Mapping[str, str]] = ..., jit: _Optional[_Union[_http_token_request_pb2.HttpTokenRequest, _Mapping]] = ..., disable_zoom: bool = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: WebviewWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[WebviewWidget.Data, _Mapping]] = ...) -> None: ...
