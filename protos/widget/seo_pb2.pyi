from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SEOWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class HeaderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        h1: _ClassVar[SEOWidget.HeaderType]
        h2: _ClassVar[SEOWidget.HeaderType]
        h3: _ClassVar[SEOWidget.HeaderType]
        h4: _ClassVar[SEOWidget.HeaderType]
        h5: _ClassVar[SEOWidget.HeaderType]
        h6: _ClassVar[SEOWidget.HeaderType]
    h1: SEOWidget.HeaderType
    h2: SEOWidget.HeaderType
    h3: SEOWidget.HeaderType
    h4: SEOWidget.HeaderType
    h5: SEOWidget.HeaderType
    h6: SEOWidget.HeaderType
    class HeaderTagType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[SEOWidget.HeaderTagType]
        H1: _ClassVar[SEOWidget.HeaderTagType]
        H2: _ClassVar[SEOWidget.HeaderTagType]
        H3: _ClassVar[SEOWidget.HeaderTagType]
        H4: _ClassVar[SEOWidget.HeaderTagType]
        H5: _ClassVar[SEOWidget.HeaderTagType]
        H6: _ClassVar[SEOWidget.HeaderTagType]
    DEFAULT: SEOWidget.HeaderTagType
    H1: SEOWidget.HeaderTagType
    H2: SEOWidget.HeaderTagType
    H3: SEOWidget.HeaderTagType
    H4: SEOWidget.HeaderTagType
    H5: SEOWidget.HeaderTagType
    H6: SEOWidget.HeaderTagType
    class Data(_message.Message):
        __slots__ = ("meta_tags", "url_tags", "json_ld_data", "header_tags", "facebook_tags", "twitter_tags", "faq", "social_tags")
        META_TAGS_FIELD_NUMBER: _ClassVar[int]
        URL_TAGS_FIELD_NUMBER: _ClassVar[int]
        JSON_LD_DATA_FIELD_NUMBER: _ClassVar[int]
        HEADER_TAGS_FIELD_NUMBER: _ClassVar[int]
        FACEBOOK_TAGS_FIELD_NUMBER: _ClassVar[int]
        TWITTER_TAGS_FIELD_NUMBER: _ClassVar[int]
        FAQ_FIELD_NUMBER: _ClassVar[int]
        SOCIAL_TAGS_FIELD_NUMBER: _ClassVar[int]
        meta_tags: SEOWidget.MetaTags
        url_tags: SEOWidget.UrlTags
        json_ld_data: SEOWidget.JsonLdData
        header_tags: _containers.RepeatedCompositeFieldContainer[SEOWidget.HeaderTag]
        facebook_tags: SEOWidget.FacebookTags
        twitter_tags: SEOWidget.TwitterTags
        faq: SEOWidget.FAQ
        social_tags: _containers.RepeatedCompositeFieldContainer[SEOWidget.SocialTag]
        def __init__(self, meta_tags: _Optional[_Union[SEOWidget.MetaTags, _Mapping]] = ..., url_tags: _Optional[_Union[SEOWidget.UrlTags, _Mapping]] = ..., json_ld_data: _Optional[_Union[SEOWidget.JsonLdData, _Mapping]] = ..., header_tags: _Optional[_Iterable[_Union[SEOWidget.HeaderTag, _Mapping]]] = ..., facebook_tags: _Optional[_Union[SEOWidget.FacebookTags, _Mapping]] = ..., twitter_tags: _Optional[_Union[SEOWidget.TwitterTags, _Mapping]] = ..., faq: _Optional[_Union[SEOWidget.FAQ, _Mapping]] = ..., social_tags: _Optional[_Iterable[_Union[SEOWidget.SocialTag, _Mapping]]] = ...) -> None: ...
    class MetaTags(_message.Message):
        __slots__ = ("title", "description", "keywords", "contact", "area_served", "website_url", "brand")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        KEYWORDS_FIELD_NUMBER: _ClassVar[int]
        CONTACT_FIELD_NUMBER: _ClassVar[int]
        AREA_SERVED_FIELD_NUMBER: _ClassVar[int]
        WEBSITE_URL_FIELD_NUMBER: _ClassVar[int]
        BRAND_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        keywords: str
        contact: str
        area_served: str
        website_url: str
        brand: str
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., keywords: _Optional[str] = ..., contact: _Optional[str] = ..., area_served: _Optional[str] = ..., website_url: _Optional[str] = ..., brand: _Optional[str] = ...) -> None: ...
    class UrlTags(_message.Message):
        __slots__ = ("canonical_url", "alternate_urls")
        CANONICAL_URL_FIELD_NUMBER: _ClassVar[int]
        ALTERNATE_URLS_FIELD_NUMBER: _ClassVar[int]
        canonical_url: str
        alternate_urls: _containers.RepeatedCompositeFieldContainer[SEOWidget.AlternateUrl]
        def __init__(self, canonical_url: _Optional[str] = ..., alternate_urls: _Optional[_Iterable[_Union[SEOWidget.AlternateUrl, _Mapping]]] = ...) -> None: ...
    class AlternateUrl(_message.Message):
        __slots__ = ("url", "lang_code")
        URL_FIELD_NUMBER: _ClassVar[int]
        LANG_CODE_FIELD_NUMBER: _ClassVar[int]
        url: str
        lang_code: str
        def __init__(self, url: _Optional[str] = ..., lang_code: _Optional[str] = ...) -> None: ...
    class JsonLdData(_message.Message):
        __slots__ = ("schemas",)
        SCHEMAS_FIELD_NUMBER: _ClassVar[int]
        schemas: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, schemas: _Optional[_Iterable[str]] = ...) -> None: ...
    class HeaderTag(_message.Message):
        __slots__ = ("type", "content", "header_type", "header_tag_type")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        HEADER_TYPE_FIELD_NUMBER: _ClassVar[int]
        HEADER_TAG_TYPE_FIELD_NUMBER: _ClassVar[int]
        type: str
        content: str
        header_type: SEOWidget.HeaderType
        header_tag_type: SEOWidget.HeaderTagType
        def __init__(self, type: _Optional[str] = ..., content: _Optional[str] = ..., header_type: _Optional[_Union[SEOWidget.HeaderType, str]] = ..., header_tag_type: _Optional[_Union[SEOWidget.HeaderTagType, str]] = ...) -> None: ...
    class FacebookTags(_message.Message):
        __slots__ = ("ogLocale", "ogType", "ogTitle", "ogDescription", "ogUrl", "ogSiteName", "ogImage", "ogImageWidth", "ogImageHeight", "ogImageAlt", "ogImageType", "ogVideoWidth", "ogVideoHeight", "ogContentType")
        OGLOCALE_FIELD_NUMBER: _ClassVar[int]
        OGTYPE_FIELD_NUMBER: _ClassVar[int]
        OGTITLE_FIELD_NUMBER: _ClassVar[int]
        OGDESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        OGURL_FIELD_NUMBER: _ClassVar[int]
        OGSITENAME_FIELD_NUMBER: _ClassVar[int]
        OGIMAGE_FIELD_NUMBER: _ClassVar[int]
        OGIMAGEWIDTH_FIELD_NUMBER: _ClassVar[int]
        OGIMAGEHEIGHT_FIELD_NUMBER: _ClassVar[int]
        OGIMAGEALT_FIELD_NUMBER: _ClassVar[int]
        OGIMAGETYPE_FIELD_NUMBER: _ClassVar[int]
        OGVIDEOWIDTH_FIELD_NUMBER: _ClassVar[int]
        OGVIDEOHEIGHT_FIELD_NUMBER: _ClassVar[int]
        OGCONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
        ogLocale: str
        ogType: str
        ogTitle: str
        ogDescription: str
        ogUrl: str
        ogSiteName: str
        ogImage: str
        ogImageWidth: str
        ogImageHeight: str
        ogImageAlt: str
        ogImageType: str
        ogVideoWidth: str
        ogVideoHeight: str
        ogContentType: str
        def __init__(self, ogLocale: _Optional[str] = ..., ogType: _Optional[str] = ..., ogTitle: _Optional[str] = ..., ogDescription: _Optional[str] = ..., ogUrl: _Optional[str] = ..., ogSiteName: _Optional[str] = ..., ogImage: _Optional[str] = ..., ogImageWidth: _Optional[str] = ..., ogImageHeight: _Optional[str] = ..., ogImageAlt: _Optional[str] = ..., ogImageType: _Optional[str] = ..., ogVideoWidth: _Optional[str] = ..., ogVideoHeight: _Optional[str] = ..., ogContentType: _Optional[str] = ...) -> None: ...
    class TwitterTags(_message.Message):
        __slots__ = ("card", "title", "description", "site", "image")
        CARD_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SITE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        card: str
        title: str
        description: str
        site: str
        image: str
        def __init__(self, card: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., site: _Optional[str] = ..., image: _Optional[str] = ...) -> None: ...
    class FAQ(_message.Message):
        __slots__ = ("title", "question_answer_pairs")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        QUESTION_ANSWER_PAIRS_FIELD_NUMBER: _ClassVar[int]
        title: str
        question_answer_pairs: _containers.RepeatedCompositeFieldContainer[SEOWidget.QuestionAnswerPair]
        def __init__(self, title: _Optional[str] = ..., question_answer_pairs: _Optional[_Iterable[_Union[SEOWidget.QuestionAnswerPair, _Mapping]]] = ...) -> None: ...
    class QuestionAnswerPair(_message.Message):
        __slots__ = ("question", "answer")
        QUESTION_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        question: str
        answer: str
        def __init__(self, question: _Optional[str] = ..., answer: _Optional[str] = ...) -> None: ...
    class SocialTag(_message.Message):
        __slots__ = ("property", "content")
        PROPERTY_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        property: str
        content: str
        def __init__(self, property: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SEOWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SEOWidget.Data, _Mapping]] = ...) -> None: ...
