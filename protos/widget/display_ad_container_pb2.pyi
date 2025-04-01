from base import widget_commons_pb2 as _widget_commons_pb2
from widget import image_display_ad_pb2 as _image_display_ad_pb2
from widget import video_display_ad_pb2 as _video_display_ad_pb2
from widget import no_fill_ad_pb2 as _no_fill_ad_pb2
from widget import carousel_display_ad_pb2 as _carousel_display_ad_pb2
from widget import lottie_banner_pb2 as _lottie_banner_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from feature.image import aspect_ratio_pb2 as _aspect_ratio_pb2
from widget import video_quality_comparator_pb2 as _video_quality_comparator_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayAdContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("refresh_info", "auto_invoke", "poll_limit_reached", "image_ad", "no_fill_ad", "skinny_ad", "carousel_ad", "display_ad_placeholder", "video_ad", "video_quality_comparator")
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        AUTO_INVOKE_FIELD_NUMBER: _ClassVar[int]
        POLL_LIMIT_REACHED_FIELD_NUMBER: _ClassVar[int]
        IMAGE_AD_FIELD_NUMBER: _ClassVar[int]
        NO_FILL_AD_FIELD_NUMBER: _ClassVar[int]
        SKINNY_AD_FIELD_NUMBER: _ClassVar[int]
        CAROUSEL_AD_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_AD_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        VIDEO_AD_FIELD_NUMBER: _ClassVar[int]
        VIDEO_QUALITY_COMPARATOR_FIELD_NUMBER: _ClassVar[int]
        refresh_info: _refresh_info_pb2.RefreshInfo
        auto_invoke: bool
        poll_limit_reached: bool
        image_ad: _image_display_ad_pb2.ImageDisplayAdWidget
        no_fill_ad: _no_fill_ad_pb2.NoFillAdWidget
        skinny_ad: _lottie_banner_pb2.LottieBannerWidget
        carousel_ad: _carousel_display_ad_pb2.CarouselDisplayAdWidget
        display_ad_placeholder: DisplayAdContainerWidget.DisplayAdPlaceholder
        video_ad: _video_display_ad_pb2.VideoDisplayAdWidget
        video_quality_comparator: _video_quality_comparator_pb2.VideoQualityComparatorWidget
        def __init__(self, refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ..., auto_invoke: bool = ..., poll_limit_reached: bool = ..., image_ad: _Optional[_Union[_image_display_ad_pb2.ImageDisplayAdWidget, _Mapping]] = ..., no_fill_ad: _Optional[_Union[_no_fill_ad_pb2.NoFillAdWidget, _Mapping]] = ..., skinny_ad: _Optional[_Union[_lottie_banner_pb2.LottieBannerWidget, _Mapping]] = ..., carousel_ad: _Optional[_Union[_carousel_display_ad_pb2.CarouselDisplayAdWidget, _Mapping]] = ..., display_ad_placeholder: _Optional[_Union[DisplayAdContainerWidget.DisplayAdPlaceholder, _Mapping]] = ..., video_ad: _Optional[_Union[_video_display_ad_pb2.VideoDisplayAdWidget, _Mapping]] = ..., video_quality_comparator: _Optional[_Union[_video_quality_comparator_pb2.VideoQualityComparatorWidget, _Mapping]] = ...) -> None: ...
    class DisplayAdPlaceholder(_message.Message):
        __slots__ = ("widget_url", "aspect_ratio")
        WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
        widget_url: str
        aspect_ratio: _aspect_ratio_pb2.AspectRatio
        def __init__(self, widget_url: _Optional[str] = ..., aspect_ratio: _Optional[_Union[_aspect_ratio_pb2.AspectRatio, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DisplayAdContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DisplayAdContainerWidget.Data, _Mapping]] = ...) -> None: ...
