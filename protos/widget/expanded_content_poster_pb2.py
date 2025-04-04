# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/expanded_content_poster.proto
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
    'widget/expanded_content_poster.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.autoplay import autoplay_info_pb2 as feature_dot_autoplay_dot_autoplay__info__pb2
from feature.content_language_preference import content_language_preference_pb2 as feature_dot_content__language__preference_dot_content__language__preference__pb2
from feature.language import language_pb2 as feature_dot_language_dot_language__pb2
from feature.remind_me import remind_me_info_pb2 as feature_dot_remind__me_dot_remind__me__info__pb2
from feature.watchlist import watchlist_info_pb2 as feature_dot_watchlist_dot_watchlist__info__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$widget/expanded_content_poster.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a$feature/autoplay/autoplay_info.proto\x1a\x45\x66\x65\x61ture/content_language_preference/content_language_preference.proto\x1a\x1f\x66\x65\x61ture/language/language.proto\x1a&feature/remind_me/remind_me_info.proto\x1a&feature/watchlist/watchlist_info.proto\"\x9b\r\n\x1b\x45xpandedContentPosterWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x36\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32(.widget.ExpandedContentPosterWidget.Data\x1a\xa4\x01\n\x04\x44\x61ta\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x45\n\x0c\x63ontent_info\x18\x02 \x01(\x0b\x32/.widget.ExpandedContentPosterWidget.ContentInfo\x12\x30\n\x12on_visible_actions\x18\x03 \x03(\x0b\x32\x14.base.Actions.Action\x1a\x84\x05\n\x0b\x43ontentInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12*\n\x0ctitle_cutout\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x35\n\x04tags\x18\x04 \x03(\x0b\x32\'.widget.ExpandedContentPosterWidget.Tag\x12\x10\n\x08progress\x18\x05 \x01(\x05\x12J\n\rwatchlist_cta\x18\x06 \x01(\x0b\x32\x33.widget.ExpandedContentPosterWidget.WatchlistButton\x12I\n\x0csee_more_cta\x18\x07 \x01(\x0b\x32\x33.widget.ExpandedContentPosterWidget.IconLabelButton\x12\x35\n\rautoplay_info\x18\x08 \x01(\x0b\x32\x1e.feature.autoplay.AutoplayInfo\x12`\n\x18language_preference_info\x18\t \x01(\x0b\x32>.feature.content_language_preference.ContentLanguagePreference\x12^\n\x19\x63ontent_language_selector\x18\n \x01(\x0b\x32;.widget.ExpandedContentPosterWidget.ContentLanguageSelector\x12L\n\x0eprimary_button\x18\x0b \x01(\x0b\x32\x34.widget.ExpandedContentPosterWidget.ContentCTAButton\x1aS\n\x0fIconLabelButton\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1a\x41\n\x0fWatchlistButton\x12.\n\x04info\x18\x01 \x01(\x0b\x32 .feature.watchlist.WatchlistInfo\x1a\x34\n\x03Tag\x12\r\n\x05value\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a\x65\n\x17\x43ontentLanguageSelector\x12J\n\tlanguages\x18\x01 \x03(\x0b\x32\x37.widget.ExpandedContentPosterWidget.ContentLanguageItem\x1a\xa1\x01\n\x13\x43ontentLanguageItem\x12,\n\x08language\x18\x01 \x01(\x0b\x32\x1a.feature.language.Language\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nis_default\x18\x03 \x01(\x08\x12\x13\n\x0bis_selected\x18\x04 \x01(\x08\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x1a\xbb\x01\n\x10\x43ontentCTAButton\x12I\n\ncta_button\x18\x01 \x01(\x0b\x32\x33.widget.ExpandedContentPosterWidget.IconLabelButtonH\x00\x12U\n\x14remind_me_cta_button\x18\x02 \x01(\x0b\x32\x35.widget.ExpandedContentPosterWidget.RemindMeCTAButtonH\x00\x42\x05\n\x03\x63ta\x1aL\n\x11RemindMeCTAButton\x12\x37\n\x0eremind_me_info\x18\x01 \x01(\x0b\x32\x1f.feature.remind_me.ReminderInfoJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.expanded_content_poster_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_EXPANDEDCONTENTPOSTERWIDGET']._serialized_start=366
  _globals['_EXPANDEDCONTENTPOSTERWIDGET']._serialized_end=2057
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_DATA']._serialized_start=499
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_DATA']._serialized_end=663
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTINFO']._serialized_start=666
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTINFO']._serialized_end=1310
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_ICONLABELBUTTON']._serialized_start=1312
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_ICONLABELBUTTON']._serialized_end=1395
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_WATCHLISTBUTTON']._serialized_start=1397
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_WATCHLISTBUTTON']._serialized_end=1462
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_TAG']._serialized_start=1464
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_TAG']._serialized_end=1516
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTLANGUAGESELECTOR']._serialized_start=1518
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTLANGUAGESELECTOR']._serialized_end=1619
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTLANGUAGEITEM']._serialized_start=1622
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTLANGUAGEITEM']._serialized_end=1783
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTCTABUTTON']._serialized_start=1786
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_CONTENTCTABUTTON']._serialized_end=1973
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_REMINDMECTABUTTON']._serialized_start=1975
  _globals['_EXPANDEDCONTENTPOSTERWIDGET_REMINDMECTABUTTON']._serialized_end=2051
# @@protoc_insertion_point(module_scope)
