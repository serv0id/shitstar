from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TooltipActionMenuWidget(_message.Message):
    __slots__ = ("widget_commons", "actionable_options")
    class ActionableOption(_message.Message):
        __slots__ = ("reaction_item",)
        REACTION_ITEM_FIELD_NUMBER: _ClassVar[int]
        reaction_item: TooltipActionMenuWidget.ReactionItem
        def __init__(self, reaction_item: _Optional[_Union[TooltipActionMenuWidget.ReactionItem, _Mapping]] = ...) -> None: ...
    class ReactionItem(_message.Message):
        __slots__ = ("reaction_id", "label", "is_selected", "subtle_lottie", "subtle_image", "on_select_lottie", "on_select_image", "on_select_actions", "on_deselect_actions")
        class ReactionId(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEFAULT: _ClassVar[TooltipActionMenuWidget.ReactionItem.ReactionId]
            LOVE: _ClassVar[TooltipActionMenuWidget.ReactionItem.ReactionId]
            LIKE: _ClassVar[TooltipActionMenuWidget.ReactionItem.ReactionId]
            NOT_FOR_ME: _ClassVar[TooltipActionMenuWidget.ReactionItem.ReactionId]
            DISLIKE: _ClassVar[TooltipActionMenuWidget.ReactionItem.ReactionId]
        DEFAULT: TooltipActionMenuWidget.ReactionItem.ReactionId
        LOVE: TooltipActionMenuWidget.ReactionItem.ReactionId
        LIKE: TooltipActionMenuWidget.ReactionItem.ReactionId
        NOT_FOR_ME: TooltipActionMenuWidget.ReactionItem.ReactionId
        DISLIKE: TooltipActionMenuWidget.ReactionItem.ReactionId
        REACTION_ID_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        SUBTLE_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        SUBTLE_IMAGE_FIELD_NUMBER: _ClassVar[int]
        ON_SELECT_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        ON_SELECT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        ON_SELECT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ON_DESELECT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        reaction_id: TooltipActionMenuWidget.ReactionItem.ReactionId
        label: str
        is_selected: bool
        subtle_lottie: _lottie_pb2.Lottie
        subtle_image: _image_pb2.Image
        on_select_lottie: _lottie_pb2.Lottie
        on_select_image: _image_pb2.Image
        on_select_actions: _actions_pb2.Actions
        on_deselect_actions: _actions_pb2.Actions
        def __init__(self, reaction_id: _Optional[_Union[TooltipActionMenuWidget.ReactionItem.ReactionId, str]] = ..., label: _Optional[str] = ..., is_selected: bool = ..., subtle_lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., subtle_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., on_select_lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., on_select_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., on_select_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., on_deselect_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    ACTIONABLE_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    actionable_options: _containers.RepeatedCompositeFieldContainer[TooltipActionMenuWidget.ActionableOption]
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., actionable_options: _Optional[_Iterable[_Union[TooltipActionMenuWidget.ActionableOption, _Mapping]]] = ...) -> None: ...
