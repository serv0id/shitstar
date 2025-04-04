# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/player_control_menu.proto
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
    'widget/player_control_menu.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.accessibility import accessibility_pb2 as feature_dot_accessibility_dot_accessibility__pb2
from feature.player import player_settings_type_pb2 as feature_dot_player_dot_player__settings__type__pb2
from widget import playable_content_pb2 as widget_dot_playable__content__pb2
from widget import content_rating_cta_pb2 as widget_dot_content__rating__cta__pb2
from feature.branding import brand_pb2 as feature_dot_branding_dot_brand__pb2
from feature.image import illustration_pb2 as feature_dot_image_dot_illustration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n widget/player_control_menu.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a)feature/accessibility/accessibility.proto\x1a)feature/player/player_settings_type.proto\x1a\x1dwidget/playable_content.proto\x1a\x1fwidget/content_rating_cta.proto\x1a\x1c\x66\x65\x61ture/branding/brand.proto\x1a feature/image/illustration.proto\"\xa3\x10\n\x17PlayerControlMenuWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x32\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32$.widget.PlayerControlMenuWidget.Data\x1a\xef\x01\n\x04\x44\x61ta\x12H\n\x05items\x18\x01 \x03(\x0b\x32\x35.widget.PlayerControlMenuWidget.PlayerControlMenuItemB\x02\x18\x01\x12N\n\x0flandscape_items\x18\x02 \x03(\x0b\x32\x35.widget.PlayerControlMenuWidget.PlayerControlMenuItem\x12M\n\x0eportrait_items\x18\x03 \x03(\x0b\x32\x35.widget.PlayerControlMenuWidget.PlayerControlMenuItem\x1a\xcc\x01\n\x1cOpenPlayerSettingsActionItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12*\n\x05types\x18\x04 \x03(\x0e\x32\x1b.feature.PlayerSettingsType\x12\x1e\n\x07\x61\x63tions\x18\x05 \x01(\x0b\x32\r.base.Actions\x12\x31\n\x03\x61lt\x18\x06 \x01(\x0b\x32$.feature.accessibility.Accessibility\x1a\xa9\x01\n\x11GeneralActionItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\n \x01(\x0b\x32\r.base.Actions\x12\x37\n\x10playable_content\x18\x0b \x01(\x0b\x32\x1d.widget.PlayableContentWidget\x1aP\n\x11\x46\x61nModeActionItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x0b \x01(\x0b\x32\r.base.Actions\x1aq\n\x1bOpenPlaybackSpeedActionItem\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12#\n\x1boverlay_duration_in_seconds\x18\x04 \x01(\x05\x1a\x97\x04\n\x1ePlayInThreeSixtyModeActionItem\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x03 \x01(\t\x12\x12\n\npage_title\x18\x04 \x01(\t\x12\x15\n\rpage_subtitle\x18\x05 \x01(\t\x12\x12\n\ncontent_id\x18\x06 \x01(\t\x12#\n\x1bwatch_in_vr_headset_enabled\x18\x07 \x01(\x08\x12\x1f\n\x17motion_tracking_enabled\x18\x08 \x01(\x08\x12\x1e\n\x07\x61\x63tions\x18\t \x01(\x0b\x32\r.base.Actions\x12$\n\x1cmotion_tracking_toggle_label\x18\n \x01(\t\x12\x1d\n\x15watch_in_vr_cta_label\x18\x0b \x01(\t\x12\x1e\n\x16vr_swipe_gesture_label\x18\r \x01(\t\x12\x13\n\x0b\x65rror_title\x18\x0e \x01(\t\x12\x16\n\x0e\x65rror_subtitle\x18\x0f \x01(\t\x12\x1d\n\x15\x65rror_retry_cta_label\x18\x10 \x01(\t\x12+\n\nbrand_icon\x18\x11 \x01(\x0e\x32\x17.feature.branding.Brand\x12\x12\n\nlive_label\x18\x12 \x01(\t\x12/\n\nlive_badge\x18\x13 \x01(\x0b\x32\x1b.feature.image.Illustration\x1a\xae\x04\n\x15PlayerControlMenuItem\x12Z\n\x12open_settings_item\x18\x01 \x01(\x0b\x32<.widget.PlayerControlMenuWidget.OpenPlayerSettingsActionItemH\x00\x12P\n\x13general_action_item\x18\x02 \x01(\x0b\x32\x31.widget.PlayerControlMenuWidget.GeneralActionItemH\x00\x12Q\n\x14\x66\x61n_mode_action_item\x18\x03 \x01(\x0b\x32\x31.widget.PlayerControlMenuWidget.FanModeActionItemH\x00\x12Z\n\x13playback_speed_item\x18\x04 \x01(\x0b\x32;.widget.PlayerControlMenuWidget.OpenPlaybackSpeedActionItemH\x00\x12\x43\n\x19\x63ontent_rating_cta_widget\x18\x05 \x01(\x0b\x32\x1e.widget.ContentRatingCtaWidgetH\x00\x12k\n!play_three_sixty_mode_action_item\x18\x06 \x01(\x0b\x32>.widget.PlayerControlMenuWidget.PlayInThreeSixtyModeActionItemH\x00\x42\x06\n\x04itemJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.player_control_menu_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PLAYERCONTROLMENUWIDGET_DATA'].fields_by_name['items']._loaded_options = None
  _globals['_PLAYERCONTROLMENUWIDGET_DATA'].fields_by_name['items']._serialized_options = b'\030\001'
  _globals['_PLAYERCONTROLMENUWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_PLAYERCONTROLMENUWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_PLAYERCONTROLMENUWIDGET']._serialized_start=327
  _globals['_PLAYERCONTROLMENUWIDGET']._serialized_end=2410
  _globals['_PLAYERCONTROLMENUWIDGET_DATA']._serialized_start=490
  _globals['_PLAYERCONTROLMENUWIDGET_DATA']._serialized_end=729
  _globals['_PLAYERCONTROLMENUWIDGET_OPENPLAYERSETTINGSACTIONITEM']._serialized_start=732
  _globals['_PLAYERCONTROLMENUWIDGET_OPENPLAYERSETTINGSACTIONITEM']._serialized_end=936
  _globals['_PLAYERCONTROLMENUWIDGET_GENERALACTIONITEM']._serialized_start=939
  _globals['_PLAYERCONTROLMENUWIDGET_GENERALACTIONITEM']._serialized_end=1108
  _globals['_PLAYERCONTROLMENUWIDGET_FANMODEACTIONITEM']._serialized_start=1110
  _globals['_PLAYERCONTROLMENUWIDGET_FANMODEACTIONITEM']._serialized_end=1190
  _globals['_PLAYERCONTROLMENUWIDGET_OPENPLAYBACKSPEEDACTIONITEM']._serialized_start=1192
  _globals['_PLAYERCONTROLMENUWIDGET_OPENPLAYBACKSPEEDACTIONITEM']._serialized_end=1305
  _globals['_PLAYERCONTROLMENUWIDGET_PLAYINTHREESIXTYMODEACTIONITEM']._serialized_start=1308
  _globals['_PLAYERCONTROLMENUWIDGET_PLAYINTHREESIXTYMODEACTIONITEM']._serialized_end=1843
  _globals['_PLAYERCONTROLMENUWIDGET_PLAYERCONTROLMENUITEM']._serialized_start=1846
  _globals['_PLAYERCONTROLMENUWIDGET_PLAYERCONTROLMENUITEM']._serialized_end=2404
# @@protoc_insertion_point(module_scope)
