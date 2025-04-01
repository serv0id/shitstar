from feature.image import image_pb2 as _image_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from feature.image import screen_size_image_pb2 as _screen_size_image_pb2
from feature.trackers import url_trackers_pb2 as _url_trackers_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayImage(_message.Message):
    __slots__ = ("title", "subTitle", "desc", "badge_label", "logo", "image", "cta", "tracker", "badge", "creative_image", "display_image_type", "lottie", "alt", "footer", "auto_expand_cta_collapse", "hide_cta_on_collapse")
    class DisplayImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[DisplayImage.DisplayImageType]
        NATIVE_FRAME: _ClassVar[DisplayImage.DisplayImageType]
        BILLBOARD: _ClassVar[DisplayImage.DisplayImageType]
        TALL_VERTICAL: _ClassVar[DisplayImage.DisplayImageType]
        SHORT_SQUARE: _ClassVar[DisplayImage.DisplayImageType]
        EXPANDED_CONTENT: _ClassVar[DisplayImage.DisplayImageType]
        EMPTY: _ClassVar[DisplayImage.DisplayImageType]
    UNKNOWN: DisplayImage.DisplayImageType
    NATIVE_FRAME: DisplayImage.DisplayImageType
    BILLBOARD: DisplayImage.DisplayImageType
    TALL_VERTICAL: DisplayImage.DisplayImageType
    SHORT_SQUARE: DisplayImage.DisplayImageType
    EXPANDED_CONTENT: DisplayImage.DisplayImageType
    EMPTY: DisplayImage.DisplayImageType
    class Cta(_message.Message):
        __slots__ = ("label", "bg_color", "desc")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        BG_COLOR_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        label: str
        bg_color: str
        desc: str
        def __init__(self, label: _Optional[str] = ..., bg_color: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...
    class Badge(_message.Message):
        __slots__ = ("label", "desc")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        label: str
        desc: str
        def __init__(self, label: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("text", "placeholder", "link")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        text: str
        placeholder: str
        link: str
        def __init__(self, text: _Optional[str] = ..., placeholder: _Optional[str] = ..., link: _Optional[str] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    BADGE_LABEL_FIELD_NUMBER: _ClassVar[int]
    LOGO_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    CTA_FIELD_NUMBER: _ClassVar[int]
    TRACKER_FIELD_NUMBER: _ClassVar[int]
    BADGE_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOTTIE_FIELD_NUMBER: _ClassVar[int]
    ALT_FIELD_NUMBER: _ClassVar[int]
    FOOTER_FIELD_NUMBER: _ClassVar[int]
    AUTO_EXPAND_CTA_COLLAPSE_FIELD_NUMBER: _ClassVar[int]
    HIDE_CTA_ON_COLLAPSE_FIELD_NUMBER: _ClassVar[int]
    title: str
    subTitle: str
    desc: str
    badge_label: str
    logo: _image_pb2.Image
    image: _image_pb2.Image
    cta: DisplayImage.Cta
    tracker: _url_trackers_pb2.UrlTrackers
    badge: DisplayImage.Badge
    creative_image: _screen_size_image_pb2.ScreenSizeImage
    display_image_type: DisplayImage.DisplayImageType
    lottie: _lottie_pb2.Lottie
    alt: _accessibility_pb2.Accessibility
    footer: DisplayImage.Footer
    auto_expand_cta_collapse: bool
    hide_cta_on_collapse: bool
    def __init__(self, title: _Optional[str] = ..., subTitle: _Optional[str] = ..., desc: _Optional[str] = ..., badge_label: _Optional[str] = ..., logo: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., cta: _Optional[_Union[DisplayImage.Cta, _Mapping]] = ..., tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ..., badge: _Optional[_Union[DisplayImage.Badge, _Mapping]] = ..., creative_image: _Optional[_Union[_screen_size_image_pb2.ScreenSizeImage, _Mapping]] = ..., display_image_type: _Optional[_Union[DisplayImage.DisplayImageType, str]] = ..., lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., footer: _Optional[_Union[DisplayImage.Footer, _Mapping]] = ..., auto_expand_cta_collapse: bool = ..., hide_cta_on_collapse: bool = ...) -> None: ...
