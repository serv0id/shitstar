from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AppUpgradeWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "title", "description", "upgrade_cta", "skip_cta")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_CTA_FIELD_NUMBER: _ClassVar[int]
        SKIP_CTA_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        title: str
        description: str
        upgrade_cta: AppUpgradeWidget.UpgradeCTA
        skip_cta: AppUpgradeWidget.SkipCTA
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., upgrade_cta: _Optional[_Union[AppUpgradeWidget.UpgradeCTA, _Mapping]] = ..., skip_cta: _Optional[_Union[AppUpgradeWidget.SkipCTA, _Mapping]] = ...) -> None: ...
    class UpgradeCTA(_message.Message):
        __slots__ = ("text", "upgrade_action")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_ACTION_FIELD_NUMBER: _ClassVar[int]
        text: str
        upgrade_action: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, text: _Optional[str] = ..., upgrade_action: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class SkipCTA(_message.Message):
        __slots__ = ("text", "icon_name", "skip_action")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        SKIP_ACTION_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        skip_action: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., skip_action: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AppUpgradeWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AppUpgradeWidget.Data, _Mapping]] = ...) -> None: ...
