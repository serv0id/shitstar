from component.content import artwork_tag_pb2 as _artwork_tag_pb2
from component.content import content_callout_tag_pb2 as _content_callout_tag_pb2
from component.content import episode_additional_attributes_pb2 as _episode_additional_attributes_pb2
from component.content import image_attributes_pb2 as _image_attributes_pb2
from component.content import show_additional_attributes_pb2 as _show_additional_attributes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentCardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_CARD_TYPE_UNSPECIFIED: _ClassVar[ContentCardType]
    CONTENT_CARD_TYPE_HOVER_CARD: _ClassVar[ContentCardType]
    CONTENT_CARD_TYPE_LR_UAT: _ClassVar[ContentCardType]
    CONTENT_CARD_TYPE_HERO_GEC_CARD: _ClassVar[ContentCardType]
CONTENT_CARD_TYPE_UNSPECIFIED: ContentCardType
CONTENT_CARD_TYPE_HOVER_CARD: ContentCardType
CONTENT_CARD_TYPE_LR_UAT: ContentCardType
CONTENT_CARD_TYPE_HERO_GEC_CARD: ContentCardType

class Content(_message.Message):
    __slots__ = ("id", "title", "sub_title", "type", "genre", "sub_title_id", "content_provider", "channel_name", "is_paid", "sub_genre", "available_languages", "original_language", "match_id", "clip_type", "studio_id", "tv_show_id", "tv_season_id", "tv_episode_id", "sports_game_id", "sports_match_id", "sports_season_id", "sports_tournament_id", "is_monetizable", "is_coming_soon", "trailer_id", "callout_tags", "content_callout_tags", "promotion_time_left_mins", "is_promotion_timer_visible", "artwork_tag", "image_attributes", "artwork_attributes", "is_free_preview", "watch_progress", "footer_tag_in_tray", "is_autoplay_available", "meta_impression_list", "content_card_type", "initiation_src", "footer_details_in_tray", "is_hp_free_preview", "episode_attributes", "show_attributes")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PAID_FIELD_NUMBER: _ClassVar[int]
    SUB_GENRE_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    CLIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    STUDIO_ID_FIELD_NUMBER: _ClassVar[int]
    TV_SHOW_ID_FIELD_NUMBER: _ClassVar[int]
    TV_SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    TV_EPISODE_ID_FIELD_NUMBER: _ClassVar[int]
    SPORTS_GAME_ID_FIELD_NUMBER: _ClassVar[int]
    SPORTS_MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    SPORTS_SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    SPORTS_TOURNAMENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_MONETIZABLE_FIELD_NUMBER: _ClassVar[int]
    IS_COMING_SOON_FIELD_NUMBER: _ClassVar[int]
    TRAILER_ID_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_TAGS_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CALLOUT_TAGS_FIELD_NUMBER: _ClassVar[int]
    PROMOTION_TIME_LEFT_MINS_FIELD_NUMBER: _ClassVar[int]
    IS_PROMOTION_TIMER_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    ARTWORK_TAG_FIELD_NUMBER: _ClassVar[int]
    IMAGE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ARTWORK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    WATCH_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    FOOTER_TAG_IN_TRAY_FIELD_NUMBER: _ClassVar[int]
    IS_AUTOPLAY_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    META_IMPRESSION_LIST_FIELD_NUMBER: _ClassVar[int]
    CONTENT_CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATION_SRC_FIELD_NUMBER: _ClassVar[int]
    FOOTER_DETAILS_IN_TRAY_FIELD_NUMBER: _ClassVar[int]
    IS_HP_FREE_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    EPISODE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SHOW_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    sub_title: str
    type: str
    genre: str
    sub_title_id: int
    content_provider: str
    channel_name: str
    is_paid: bool
    sub_genre: str
    available_languages: _containers.RepeatedScalarFieldContainer[str]
    original_language: str
    match_id: str
    clip_type: str
    studio_id: str
    tv_show_id: str
    tv_season_id: str
    tv_episode_id: str
    sports_game_id: str
    sports_match_id: str
    sports_season_id: str
    sports_tournament_id: str
    is_monetizable: bool
    is_coming_soon: bool
    trailer_id: str
    callout_tags: _containers.RepeatedCompositeFieldContainer[_content_callout_tag_pb2.ContentCalloutTag]
    content_callout_tags: _containers.RepeatedCompositeFieldContainer[_content_callout_tag_pb2.ContentCalloutTag]
    promotion_time_left_mins: int
    is_promotion_timer_visible: bool
    artwork_tag: _artwork_tag_pb2.ArtworkTag
    image_attributes: _image_attributes_pb2.ImageAttributes
    artwork_attributes: str
    is_free_preview: bool
    watch_progress: float
    footer_tag_in_tray: str
    is_autoplay_available: bool
    meta_impression_list: str
    content_card_type: ContentCardType
    initiation_src: str
    footer_details_in_tray: str
    is_hp_free_preview: bool
    episode_attributes: _episode_additional_attributes_pb2.EpisodeAdditionalAttributes
    show_attributes: _show_additional_attributes_pb2.ShowAdditionalAttributes
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., type: _Optional[str] = ..., genre: _Optional[str] = ..., sub_title_id: _Optional[int] = ..., content_provider: _Optional[str] = ..., channel_name: _Optional[str] = ..., is_paid: bool = ..., sub_genre: _Optional[str] = ..., available_languages: _Optional[_Iterable[str]] = ..., original_language: _Optional[str] = ..., match_id: _Optional[str] = ..., clip_type: _Optional[str] = ..., studio_id: _Optional[str] = ..., tv_show_id: _Optional[str] = ..., tv_season_id: _Optional[str] = ..., tv_episode_id: _Optional[str] = ..., sports_game_id: _Optional[str] = ..., sports_match_id: _Optional[str] = ..., sports_season_id: _Optional[str] = ..., sports_tournament_id: _Optional[str] = ..., is_monetizable: bool = ..., is_coming_soon: bool = ..., trailer_id: _Optional[str] = ..., callout_tags: _Optional[_Iterable[_Union[_content_callout_tag_pb2.ContentCalloutTag, _Mapping]]] = ..., content_callout_tags: _Optional[_Iterable[_Union[_content_callout_tag_pb2.ContentCalloutTag, _Mapping]]] = ..., promotion_time_left_mins: _Optional[int] = ..., is_promotion_timer_visible: bool = ..., artwork_tag: _Optional[_Union[_artwork_tag_pb2.ArtworkTag, _Mapping]] = ..., image_attributes: _Optional[_Union[_image_attributes_pb2.ImageAttributes, _Mapping]] = ..., artwork_attributes: _Optional[str] = ..., is_free_preview: bool = ..., watch_progress: _Optional[float] = ..., footer_tag_in_tray: _Optional[str] = ..., is_autoplay_available: bool = ..., meta_impression_list: _Optional[str] = ..., content_card_type: _Optional[_Union[ContentCardType, str]] = ..., initiation_src: _Optional[str] = ..., footer_details_in_tray: _Optional[str] = ..., is_hp_free_preview: bool = ..., episode_attributes: _Optional[_Union[_episode_additional_attributes_pb2.EpisodeAdditionalAttributes, _Mapping]] = ..., show_attributes: _Optional[_Union[_show_additional_attributes_pb2.ShowAdditionalAttributes, _Mapping]] = ...) -> None: ...
