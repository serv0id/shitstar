# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/vertical_content_poster.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'widget/vertical_content_poster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import actions_pb2 as base_dot_actions__pb2
from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.accessibility import accessibility_pb2 as feature_dot_accessibility_dot_accessibility__pb2
from feature.autoplay import autoplay_info_pb2 as feature_dot_autoplay_dot_autoplay__info__pb2
from feature.content_language_preference import content_language_preference_pb2 as feature_dot_content__language__preference_dot_content__language__preference__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.language import language_pb2 as feature_dot_language_dot_language__pb2
from feature.language_selector import language_selector_pb2 as feature_dot_language__selector_dot_language__selector__pb2
from feature.remind_me import remind_me_info_pb2 as feature_dot_remind__me_dot_remind__me__info__pb2
from feature.watchlist import watchlist_info_pb2 as feature_dot_watchlist_dot_watchlist__info__pb2
from widget import spotlight_info_pb2 as widget_dot_spotlight__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$widget/vertical_content_poster.proto\x12\x06widget\x1a\x12\x62\x61se/actions.proto\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a)feature/accessibility/accessibility.proto\x1a$feature/autoplay/autoplay_info.proto\x1a\x45\x66\x65\x61ture/content_language_preference/content_language_preference.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x1f\x66\x65\x61ture/language/language.proto\x1a\x31\x66\x65\x61ture/language_selector/language_selector.proto\x1a&feature/remind_me/remind_me_info.proto\x1a&feature/watchlist/watchlist_info.proto\x1a\x1bwidget/spotlight_info.proto\"\xe7\x14\n\x1bVerticalContentPosterWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x36\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32(.widget.VerticalContentPosterWidget.Data\x1a\xb2\x03\n\x04\x44\x61ta\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x12Z\n\x17\x65xpanded_content_poster\x18\x03 \x01(\x0b\x32\x39.widget.VerticalContentPosterWidget.ExpandedContentPoster\x12\x33\n\x0espotlight_info\x18\x04 \x01(\x0b\x32\x1b.widget.SpotlightInfoWidget\x12\x41\n\nlive_badge\x18\x05 \x01(\x0b\x32-.widget.VerticalContentPosterWidget.LiveBadge\x12\x31\n\x03\x61lt\x18\x06 \x01(\x0b\x32$.feature.accessibility.Accessibility\x12J\n\rwatchlist_cta\x18\x07 \x01(\x0b\x32\x33.widget.VerticalContentPosterWidget.WatchlistButton\x12\x12\n\ncontent_id\x18\x08 \x01(\t\x1a\xb5\x01\n\x15\x45xpandedContentPoster\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x45\n\x0c\x63ontent_info\x18\x02 \x01(\x0b\x32/.widget.VerticalContentPosterWidget.ContentInfo\x12\x30\n\x12on_visible_actions\x18\x03 \x03(\x0b\x32\x14.base.Actions.Action\x1a\xf1\x07\n\x0b\x43ontentInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12*\n\x0ctitle_cutout\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x35\n\x04tags\x18\x04 \x03(\x0b\x32\'.widget.VerticalContentPosterWidget.Tag\x12\x43\n\tlanguages\x18\x05 \x03(\x0b\x32,.widget.VerticalContentPosterWidget.LanguageB\x02\x18\x01\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12L\n\x0bprimary_cta\x18\x07 \x01(\x0b\x32\x33.widget.VerticalContentPosterWidget.IconLabelButtonB\x02\x18\x01\x12J\n\rwatchlist_cta\x18\x08 \x01(\x0b\x32\x33.widget.VerticalContentPosterWidget.WatchlistButton\x12I\n\x0csee_more_cta\x18\t \x01(\x0b\x32\x33.widget.VerticalContentPosterWidget.IconLabelButton\x12\x35\n\rautoplay_info\x18\n \x01(\x0b\x32\x1e.feature.autoplay.AutoplayInfo\x12J\n\x11language_selector\x18\x0b \x01(\x0b\x32+.feature.language_selector.LanguageSelectorB\x02\x18\x01\x12`\n\x18language_preference_info\x18\x0c \x01(\x0b\x32>.feature.content_language_preference.ContentLanguagePreference\x12^\n\x19\x63ontent_language_selector\x18\r \x01(\x0b\x32;.widget.VerticalContentPosterWidget.ContentLanguageSelector\x12L\n\x0eprimary_button\x18\x0e \x01(\x0b\x32\x34.widget.VerticalContentPosterWidget.ContentCTAButton\x12H\n\x13secondary_meta_tags\x18\x0f \x03(\x0b\x32\'.widget.VerticalContentPosterWidget.TagB\x02\x18\x01\x12\x42\n\x11\x63\x61llout_meta_tags\x18\x10 \x03(\x0b\x32\'.widget.VerticalContentPosterWidget.Tag\x1aS\n\x0fIconLabelButton\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1a\x41\n\x0fWatchlistButton\x12.\n\x04info\x18\x01 \x01(\x0b\x32 .feature.watchlist.WatchlistInfo\x1a\x34\n\x03Tag\x12\r\n\x05value\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a:\n\x08Language\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x12\n\nis_default\x18\x03 \x01(\x08\x1a\x65\n\x17\x43ontentLanguageSelector\x12J\n\tlanguages\x18\x01 \x03(\x0b\x32\x37.widget.VerticalContentPosterWidget.ContentLanguageItem\x1a\xa1\x01\n\x13\x43ontentLanguageItem\x12,\n\x08language\x18\x01 \x01(\x0b\x32\x1a.feature.language.Language\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nis_default\x18\x03 \x01(\x08\x12\x13\n\x0bis_selected\x18\x04 \x01(\x08\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x1a\x35\n\tLiveBadge\x12(\n\ntext_image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x1a\xbb\x01\n\x10\x43ontentCTAButton\x12I\n\ncta_button\x18\x01 \x01(\x0b\x32\x33.widget.VerticalContentPosterWidget.IconLabelButtonH\x00\x12U\n\x14remind_me_cta_button\x18\x02 \x01(\x0b\x32\x35.widget.VerticalContentPosterWidget.RemindMeCTAButtonH\x00\x42\x05\n\x03\x63ta\x1aL\n\x11RemindMeCTAButton\x12\x37\n\x0eremind_me_info\x18\x01 \x01(\x0b\x32\x1f.feature.remind_me.ReminderInfoJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.vertical_content_poster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['languages']._loaded_options = None
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['languages']._serialized_options = b'\030\001'
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['primary_cta']._loaded_options = None
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['primary_cta']._serialized_options = b'\030\001'
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['language_selector']._loaded_options = None
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['language_selector']._serialized_options = b'\030\001'
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['secondary_meta_tags']._loaded_options = None
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO'].fields_by_name['secondary_meta_tags']._serialized_options = b'\030\001'
  _globals['_VERTICALCONTENTPOSTERWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_VERTICALCONTENTPOSTERWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_VERTICALCONTENTPOSTERWIDGET']._serialized_start=489
  _globals['_VERTICALCONTENTPOSTERWIDGET']._serialized_end=3152
  _globals['_VERTICALCONTENTPOSTERWIDGET_DATA']._serialized_start=660
  _globals['_VERTICALCONTENTPOSTERWIDGET_DATA']._serialized_end=1094
  _globals['_VERTICALCONTENTPOSTERWIDGET_EXPANDEDCONTENTPOSTER']._serialized_start=1097
  _globals['_VERTICALCONTENTPOSTERWIDGET_EXPANDEDCONTENTPOSTER']._serialized_end=1278
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO']._serialized_start=1281
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTINFO']._serialized_end=2290
  _globals['_VERTICALCONTENTPOSTERWIDGET_ICONLABELBUTTON']._serialized_start=2292
  _globals['_VERTICALCONTENTPOSTERWIDGET_ICONLABELBUTTON']._serialized_end=2375
  _globals['_VERTICALCONTENTPOSTERWIDGET_WATCHLISTBUTTON']._serialized_start=2377
  _globals['_VERTICALCONTENTPOSTERWIDGET_WATCHLISTBUTTON']._serialized_end=2442
  _globals['_VERTICALCONTENTPOSTERWIDGET_TAG']._serialized_start=2444
  _globals['_VERTICALCONTENTPOSTERWIDGET_TAG']._serialized_end=2496
  _globals['_VERTICALCONTENTPOSTERWIDGET_LANGUAGE']._serialized_start=2498
  _globals['_VERTICALCONTENTPOSTERWIDGET_LANGUAGE']._serialized_end=2556
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTLANGUAGESELECTOR']._serialized_start=2558
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTLANGUAGESELECTOR']._serialized_end=2659
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTLANGUAGEITEM']._serialized_start=2662
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTLANGUAGEITEM']._serialized_end=2823
  _globals['_VERTICALCONTENTPOSTERWIDGET_LIVEBADGE']._serialized_start=2825
  _globals['_VERTICALCONTENTPOSTERWIDGET_LIVEBADGE']._serialized_end=2878
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTCTABUTTON']._serialized_start=2881
  _globals['_VERTICALCONTENTPOSTERWIDGET_CONTENTCTABUTTON']._serialized_end=3068
  _globals['_VERTICALCONTENTPOSTERWIDGET_REMINDMECTABUTTON']._serialized_start=3070
  _globals['_VERTICALCONTENTPOSTERWIDGET_REMINDMECTABUTTON']._serialized_end=3146
# @@protoc_insertion_point(module_scope)
