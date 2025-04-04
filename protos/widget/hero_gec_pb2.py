# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/hero_gec.proto
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
    'widget/hero_gec.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.download import download_info_pb2 as feature_dot_download_dot_download__info__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.cw import cw_info_pb2 as feature_dot_cw_dot_cw__info__pb2
from feature.watchlist import watchlist_info_pb2 as feature_dot_watchlist_dot_watchlist__info__pb2
from feature.remind_me import remind_me_info_pb2 as feature_dot_remind__me_dot_remind__me__info__pb2
from feature.community import community_info_pb2 as feature_dot_community_dot_community__info__pb2
from feature.language_selector import language_selector_pb2 as feature_dot_language__selector_dot_language__selector__pb2
from widget import spotlight_info_pb2 as widget_dot_spotlight__info__pb2
from feature.autoplay import autoplay_info_pb2 as feature_dot_autoplay_dot_autoplay__info__pb2
from feature.content_language_preference import content_language_preference_pb2 as feature_dot_content__language__preference_dot_content__language__preference__pb2
from feature.language import language_pb2 as feature_dot_language_dot_language__pb2
from feature.callout_tag import callout_tag_pb2 as feature_dot_callout__tag_dot_callout__tag__pb2
from widget import lottie_banner_pb2 as widget_dot_lottie__banner__pb2
from widget import content_rating_cta_pb2 as widget_dot_content__rating__cta__pb2
from feature.accessibility import accessibility_pb2 as feature_dot_accessibility_dot_accessibility__pb2
from widget import timer_pb2 as widget_dot_timer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15widget/hero_gec.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a$feature/download/download_info.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x18\x66\x65\x61ture/cw/cw_info.proto\x1a&feature/watchlist/watchlist_info.proto\x1a&feature/remind_me/remind_me_info.proto\x1a&feature/community/community_info.proto\x1a\x31\x66\x65\x61ture/language_selector/language_selector.proto\x1a\x1bwidget/spotlight_info.proto\x1a$feature/autoplay/autoplay_info.proto\x1a\x45\x66\x65\x61ture/content_language_preference/content_language_preference.proto\x1a\x1f\x66\x65\x61ture/language/language.proto\x1a%feature/callout_tag/callout_tag.proto\x1a\x1awidget/lottie_banner.proto\x1a\x1fwidget/content_rating_cta.proto\x1a)feature/accessibility/accessibility.proto\x1a\x12widget/timer.proto\"\xdc%\n\rHeroGECWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12(\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1a.widget.HeroGECWidget.Data\x1a\x95\x06\n\x04\x44\x61ta\x12&\n\x08hero_img\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12>\n\x0c\x63ontent_info\x18\x02 \x01(\x0b\x32(.widget.HeroGECWidget.HeroGECContentInfo\x12#\n\x07\x63w_info\x18\x03 \x01(\x0b\x32\x12.feature.cw.CwInfo\x12.\n\x07trailer\x18\x04 \x01(\x0b\x32\x1d.widget.HeroGECWidget.Trailer\x12\x38\n\x0bprimary_cta\x18\x05 \x01(\x0b\x32\x1f.widget.HeroGECWidget.CTAButtonB\x02\x18\x01\x12:\n\rsecondary_cta\x18\x06 \x01(\x0b\x32\x1f.widget.HeroGECWidget.CTAButtonB\x02\x18\x01\x12\x44\n\x13\x63ontent_actions_row\x18\x07 \x01(\x0b\x32\'.widget.HeroGECWidget.ContentActionsRow\x12\x33\n\x0espotlight_info\x18\x08 \x01(\x0b\x32\x1b.widget.SpotlightInfoWidget\x12\x35\n\rautoplay_info\x18\t \x01(\x0b\x32\x1e.feature.autoplay.AutoplayInfo\x12>\n\x0eprimary_button\x18\n \x01(\x0b\x32&.widget.HeroGECWidget.ContentCTAButton\x12@\n\x10secondary_button\x18\x0b \x01(\x0b\x32&.widget.HeroGECWidget.ContentCTAButton\x12\x34\n\x16\x61nimating_vertical_img\x18\x0c \x01(\x0b\x32\x14.feature.image.Image\x12\x31\n\rlottie_banner\x18\r \x01(\x0b\x32\x1a.widget.LottieBannerWidget\x12=\n\x10hero_gec_ui_type\x18\x0e \x01(\x0e\x32#.widget.HeroGECWidget.HeroGECUiType\x1a\xcd\r\n\x12HeroGECContentInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12*\n\x0ctitle_cutout\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x14\n\x0c\x63\x61llout_text\x18\x04 \x01(\t\x12H\n\x0esubscript_tags\x18\x05 \x03(\x0b\x32,.widget.HeroGECWidget.HeroGECContentInfo.TagB\x02\x18\x01\x12J\n\x10superscript_tags\x18\x06 \x03(\x0b\x32,.widget.HeroGECWidget.HeroGECContentInfo.TagB\x02\x18\x01\x12J\n\x11language_selector\x18\x07 \x01(\x0b\x32+.feature.language_selector.LanguageSelectorB\x02\x18\x01\x12\x44\n\x0e\x63ore_meta_tags\x18\x08 \x03(\x0b\x32,.widget.HeroGECWidget.HeroGECContentInfo.Tag\x12H\n\x12\x65nriched_meta_tags\x18\t \x03(\x0b\x32,.widget.HeroGECWidget.HeroGECContentInfo.Tag\x12`\n\x18language_preference_info\x18\n \x01(\x0b\x32>.feature.content_language_preference.ContentLanguagePreference\x12\x10\n\x08starcast\x18\x0b \x01(\t\x12P\n\x19\x63ontent_language_selector\x18\x0c \x01(\x0b\x32-.widget.HeroGECWidget.ContentLanguageSelector\x12G\n\x11\x63\x61llout_meta_tags\x18\r \x03(\x0b\x32,.widget.HeroGECWidget.HeroGECContentInfo.Tag\x12I\n\x13secondary_meta_tags\x18\x0e \x03(\x0b\x32,.widget.HeroGECWidget.HeroGECContentInfo.Tag\x12\x31\n\x03\x61lt\x18\x0f \x01(\x0b\x32$.feature.accessibility.Accessibility\x12@\n\x12\x63ore_meta_tags_alt\x18\x10 \x01(\x0b\x32$.feature.accessibility.Accessibility\x12\x44\n\x16\x65nriched_meta_tags_alt\x18\x11 \x01(\x0b\x32$.feature.accessibility.Accessibility\x12\x43\n\x15\x63\x61llout_meta_tags_alt\x18\x12 \x01(\x0b\x32$.feature.accessibility.Accessibility\x12\"\n\x05timer\x18\x13 \x01(\x0b\x32\x13.widget.TimerWidget\x1a\x9a\x03\n\x03Tag\x12\x10\n\x04type\x18\x01 \x01(\tB\x02\x18\x01\x12\x11\n\x05value\x18\x02 \x01(\tB\x02\x18\x01\x12\"\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.ActionsB\x02\x18\x01\x12\x35\n\x03\x61lt\x18\x08 \x01(\x0b\x32$.feature.accessibility.AccessibilityB\x02\x18\x01\x12\x44\n\x08text_tag\x18\x04 \x01(\x0b\x32\x30.widget.HeroGECWidget.HeroGECContentInfo.TextTagH\x00\x12\x46\n\tbadge_tag\x18\x05 \x01(\x0b\x32\x31.widget.HeroGECWidget.HeroGECContentInfo.BadgeTagH\x00\x12\x46\n\timage_tag\x18\x06 \x01(\x0b\x32\x31.widget.HeroGECWidget.HeroGECContentInfo.ImageTagH\x00\x12\x36\n\x0b\x63\x61llout_tag\x18\x07 \x01(\x0b\x32\x1f.feature.callout_tag.CalloutTagH\x00\x42\x05\n\x03tag\x1a\x38\n\x07TextTag\x12\r\n\x05value\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a\x39\n\x08\x42\x61\x64geTag\x12\r\n\x05value\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1aO\n\x08ImageTag\x12#\n\x05value\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a\t\n\x07Trailer\x1a\xcf\x04\n\x11\x43ontentActionsRow\x12[\n\x16\x63ontent_action_buttons\x18\x01 \x03(\x0b\x32;.widget.HeroGECWidget.ContentActionsRow.ContentActionButton\x1a\xdc\x03\n\x13\x43ontentActionButton\x12^\n icon_label_content_action_button\x18\x01 \x01(\x0b\x32\x32.widget.HeroGECWidget.IconLabelContentActionButtonH\x00\x12]\n\x1fwatchlist_content_action_button\x18\x02 \x01(\x0b\x32\x32.widget.HeroGECWidget.WatchlistContentActionButtonH\x00\x12[\n\x1e\x64ownload_content_action_button\x18\x03 \x01(\x0b\x32\x31.widget.HeroGECWidget.DownloadContentActionButtonH\x00\x12Z\n\x1f\x63ommunity_content_action_button\x18\x04 \x01(\x0b\x32/.widget.HeroGECWidget.CommunityJoinActionButtonH\x00\x12\x43\n\x19\x63ontent_rating_cta_widget\x18\x05 \x01(\x0b\x32\x1e.widget.ContentRatingCtaWidgetH\x00\x42\x08\n\x06\x62utton\x1a\x92\x01\n\tCTAButton\x12\r\n\x05label\x18\x01 \x01(\t\x12\x10\n\x08sublabel\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x12\x11\n\ticon_name\x18\x04 \x01(\t\x12\x31\n\x03\x61lt\x18\x05 \x01(\x0b\x32$.feature.accessibility.Accessibility\x1a\x93\x01\n\x1cIconLabelContentActionButton\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x12\x31\n\x03\x61lt\x18\x04 \x01(\x0b\x32$.feature.accessibility.Accessibility\x1a\xa5\x01\n\x1cWatchlistContentActionButton\x12.\n\x04info\x18\x01 \x01(\x0b\x32 .feature.watchlist.WatchlistInfo\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x12\x35\n\x03\x61lt\x18\x03 \x01(\x0b\x32$.feature.accessibility.AccessibilityB\x02\x18\x01\x1a\xd2\x01\n\x19\x43ommunityJoinActionButton\x12\x38\n\x0e\x63ommunity_info\x18\x01 \x01(\x0b\x32 .feature.community.CommunityInfo\x12\x12\n\nis_enabled\x18\x02 \x01(\x08\x12\x14\n\x0c\x63\x61llback_url\x18\x03 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x04 \x01(\x0b\x32\r.base.Actions\x12\x31\n\x03\x61lt\x18\x05 \x01(\x0b\x32$.feature.accessibility.Accessibility\x1a\xb6\x01\n\x1b\x44ownloadContentActionButton\x12\r\n\x05label\x18\x01 \x01(\t\x12\x35\n\rdownload_info\x18\x02 \x01(\x0b\x32\x1e.feature.download.DownloadInfo\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x12\x31\n\x03\x61lt\x18\x04 \x01(\x0b\x32$.feature.accessibility.Accessibility\x1a\x8a\x01\n\x17\x43ontentLanguageSelector\x12<\n\tlanguages\x18\x01 \x03(\x0b\x32).widget.HeroGECWidget.ContentLanguageItem\x12\x31\n\x03\x61lt\x18\x02 \x01(\x0b\x32$.feature.accessibility.Accessibility\x1a\xa1\x01\n\x13\x43ontentLanguageItem\x12,\n\x08language\x18\x01 \x01(\x0b\x32\x1a.feature.language.Language\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\nis_default\x18\x03 \x01(\x08\x12\x13\n\x0bis_selected\x18\x04 \x01(\x08\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x1a\x99\x01\n\x10\x43ontentCTAButton\x12\x35\n\ncta_button\x18\x01 \x01(\x0b\x32\x1f.widget.HeroGECWidget.CTAButtonH\x00\x12G\n\x14remind_me_cta_button\x18\x02 \x01(\x0b\x32\'.widget.HeroGECWidget.RemindMeCTAButtonH\x00\x42\x05\n\x03\x63ta\x1a\x83\x01\n\x11RemindMeCTAButton\x12\x37\n\x0eremind_me_info\x18\x01 \x01(\x0b\x32\x1f.feature.remind_me.ReminderInfo\x12\x35\n\x03\x61lt\x18\x02 \x01(\x0b\x32$.feature.accessibility.AccessibilityB\x02\x18\x01\"O\n\rHeroGECUiType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x10\n\x0c\x42ROWSE_SHEET\x10\x01\x12\r\n\tFEED_CARD\x10\x02\x12\x10\n\x0c\x41\x43TION_SHEET\x10\x03J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.hero_gec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_HEROGECWIDGET_DATA'].fields_by_name['primary_cta']._loaded_options = None
  _globals['_HEROGECWIDGET_DATA'].fields_by_name['primary_cta']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_DATA'].fields_by_name['secondary_cta']._loaded_options = None
  _globals['_HEROGECWIDGET_DATA'].fields_by_name['secondary_cta']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['type']._loaded_options = None
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['type']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['value']._loaded_options = None
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['value']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['actions']._loaded_options = None
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['actions']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['alt']._loaded_options = None
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG'].fields_by_name['alt']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO'].fields_by_name['subscript_tags']._loaded_options = None
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO'].fields_by_name['subscript_tags']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO'].fields_by_name['superscript_tags']._loaded_options = None
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO'].fields_by_name['superscript_tags']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO'].fields_by_name['language_selector']._loaded_options = None
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO'].fields_by_name['language_selector']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_WATCHLISTCONTENTACTIONBUTTON'].fields_by_name['alt']._loaded_options = None
  _globals['_HEROGECWIDGET_WATCHLISTCONTENTACTIONBUTTON'].fields_by_name['alt']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET_REMINDMECTABUTTON'].fields_by_name['alt']._loaded_options = None
  _globals['_HEROGECWIDGET_REMINDMECTABUTTON'].fields_by_name['alt']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_HEROGECWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_HEROGECWIDGET']._serialized_start=698
  _globals['_HEROGECWIDGET']._serialized_end=5526
  _globals['_HEROGECWIDGET_DATA']._serialized_start=841
  _globals['_HEROGECWIDGET_DATA']._serialized_end=1630
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO']._serialized_start=1633
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO']._serialized_end=3374
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG']._serialized_start=2766
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TAG']._serialized_end=3176
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TEXTTAG']._serialized_start=3178
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_TEXTTAG']._serialized_end=3234
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_BADGETAG']._serialized_start=3236
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_BADGETAG']._serialized_end=3293
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_IMAGETAG']._serialized_start=3295
  _globals['_HEROGECWIDGET_HEROGECCONTENTINFO_IMAGETAG']._serialized_end=3374
  _globals['_HEROGECWIDGET_TRAILER']._serialized_start=3376
  _globals['_HEROGECWIDGET_TRAILER']._serialized_end=3385
  _globals['_HEROGECWIDGET_CONTENTACTIONSROW']._serialized_start=3388
  _globals['_HEROGECWIDGET_CONTENTACTIONSROW']._serialized_end=3979
  _globals['_HEROGECWIDGET_CONTENTACTIONSROW_CONTENTACTIONBUTTON']._serialized_start=3503
  _globals['_HEROGECWIDGET_CONTENTACTIONSROW_CONTENTACTIONBUTTON']._serialized_end=3979
  _globals['_HEROGECWIDGET_CTABUTTON']._serialized_start=3982
  _globals['_HEROGECWIDGET_CTABUTTON']._serialized_end=4128
  _globals['_HEROGECWIDGET_ICONLABELCONTENTACTIONBUTTON']._serialized_start=4131
  _globals['_HEROGECWIDGET_ICONLABELCONTENTACTIONBUTTON']._serialized_end=4278
  _globals['_HEROGECWIDGET_WATCHLISTCONTENTACTIONBUTTON']._serialized_start=4281
  _globals['_HEROGECWIDGET_WATCHLISTCONTENTACTIONBUTTON']._serialized_end=4446
  _globals['_HEROGECWIDGET_COMMUNITYJOINACTIONBUTTON']._serialized_start=4449
  _globals['_HEROGECWIDGET_COMMUNITYJOINACTIONBUTTON']._serialized_end=4659
  _globals['_HEROGECWIDGET_DOWNLOADCONTENTACTIONBUTTON']._serialized_start=4662
  _globals['_HEROGECWIDGET_DOWNLOADCONTENTACTIONBUTTON']._serialized_end=4844
  _globals['_HEROGECWIDGET_CONTENTLANGUAGESELECTOR']._serialized_start=4847
  _globals['_HEROGECWIDGET_CONTENTLANGUAGESELECTOR']._serialized_end=4985
  _globals['_HEROGECWIDGET_CONTENTLANGUAGEITEM']._serialized_start=4988
  _globals['_HEROGECWIDGET_CONTENTLANGUAGEITEM']._serialized_end=5149
  _globals['_HEROGECWIDGET_CONTENTCTABUTTON']._serialized_start=5152
  _globals['_HEROGECWIDGET_CONTENTCTABUTTON']._serialized_end=5305
  _globals['_HEROGECWIDGET_REMINDMECTABUTTON']._serialized_start=5308
  _globals['_HEROGECWIDGET_REMINDMECTABUTTON']._serialized_end=5439
  _globals['_HEROGECWIDGET_HEROGECUITYPE']._serialized_start=5441
  _globals['_HEROGECWIDGET_HEROGECUITYPE']._serialized_end=5520
# @@protoc_insertion_point(module_scope)
