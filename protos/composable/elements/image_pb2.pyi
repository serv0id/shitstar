from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from composable.base import commons_pb2 as _commons_pb2
from composable.elements import composable_pb2 as _composable_pb2
from base import actions_pb2 as _actions_pb2
from composable.base import layout_traits_pb2 as _layout_traits_pb2
from composable.base import corner_radius_pb2 as _corner_radius_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AspectRatio(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ASPECT_RATIO_UNSPECIFIED: _ClassVar[AspectRatio]
    ASPECT_RATIO_3_4: _ClassVar[AspectRatio]
    ASPECT_RATIO_16_9: _ClassVar[AspectRatio]
    ASPECT_RATIO_4_3: _ClassVar[AspectRatio]
    ASPECT_RATIO_1_1: _ClassVar[AspectRatio]
ASPECT_RATIO_UNSPECIFIED: AspectRatio
ASPECT_RATIO_3_4: AspectRatio
ASPECT_RATIO_16_9: AspectRatio
ASPECT_RATIO_4_3: AspectRatio
ASPECT_RATIO_1_1: AspectRatio

class Width(_message.Message):
    __slots__ = ("fixed", "trait")
    class Trait(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FILL: _ClassVar[Width.Trait]
    FILL: Width.Trait
    FIXED_FIELD_NUMBER: _ClassVar[int]
    TRAIT_FIELD_NUMBER: _ClassVar[int]
    fixed: int
    trait: Width.Trait
    def __init__(self, fixed: _Optional[int] = ..., trait: _Optional[_Union[Width.Trait, str]] = ...) -> None: ...

class Height(_message.Message):
    __slots__ = ("fixed", "trait")
    class Trait(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HUG: _ClassVar[Height.Trait]
    HUG: Height.Trait
    FIXED_FIELD_NUMBER: _ClassVar[int]
    TRAIT_FIELD_NUMBER: _ClassVar[int]
    fixed: int
    trait: Height.Trait
    def __init__(self, fixed: _Optional[int] = ..., trait: _Optional[_Union[Height.Trait, str]] = ...) -> None: ...

class Image(_message.Message):
    __slots__ = ("source", "accessibility", "composable_commons", "image_height", "image_width", "height", "width", "placeholder", "corner_radius", "actions")
    class Source(_message.Message):
        __slots__ = ("src", "aspect_ratio", "src_prefix")
        SRC_FIELD_NUMBER: _ClassVar[int]
        ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
        SRC_PREFIX_FIELD_NUMBER: _ClassVar[int]
        src: str
        aspect_ratio: AspectRatio
        src_prefix: str
        def __init__(self, src: _Optional[str] = ..., aspect_ratio: _Optional[_Union[AspectRatio, str]] = ..., src_prefix: _Optional[str] = ...) -> None: ...
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    IMAGE_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    CORNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    source: Image.Source
    accessibility: _accessibility_pb2.Accessibility
    composable_commons: _commons_pb2.ComposableCommons
    image_height: _layout_traits_pb2.Layout
    image_width: _layout_traits_pb2.LayoutFillFixed
    height: Height
    width: Width
    placeholder: _composable_pb2.Composable
    corner_radius: _corner_radius_pb2.CornerRadius
    actions: _actions_pb2.Actions
    def __init__(self, source: _Optional[_Union[Image.Source, _Mapping]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., image_height: _Optional[_Union[_layout_traits_pb2.Layout, _Mapping]] = ..., image_width: _Optional[_Union[_layout_traits_pb2.LayoutFillFixed, _Mapping]] = ..., height: _Optional[_Union[Height, _Mapping]] = ..., width: _Optional[_Union[Width, _Mapping]] = ..., placeholder: _Optional[_Union[_composable_pb2.Composable, _Mapping]] = ..., corner_radius: _Optional[_Union[_corner_radius_pb2.CornerRadius, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
