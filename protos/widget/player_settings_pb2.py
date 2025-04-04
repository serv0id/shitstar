# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/player_settings.proto
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
    'widget/player_settings.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.player import player_settings_type_pb2 as feature_dot_player_dot_player__settings__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cwidget/player_settings.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a)feature/player/player_settings_type.proto\"\x85\x0e\n\x14PlayerSettingsWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.PlayerSettingsWidget.Data\x1a\x85\x03\n\x04\x44\x61ta\x12M\n\x0foption_list_map\x18\x01 \x03(\x0b\x32\x34.widget.PlayerSettingsWidget.Data.OptionListMapEntry\x12`\n\x1clandscape_option_list_groups\x18\x0b \x03(\x0b\x32:.widget.PlayerSettingsWidget.PlayerSettingsOptionListGroup\x12_\n\x1bportrait_option_list_groups\x18\x0c \x03(\x0b\x32:.widget.PlayerSettingsWidget.PlayerSettingsOptionListGroup\x1ak\n\x12OptionListMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x44\n\x05value\x18\x02 \x01(\x0b\x32\x35.widget.PlayerSettingsWidget.PlayerSettingsOptionList:\x02\x38\x01\x1aH\n\x1dPlayerSettingsOptionListGroup\x12\r\n\x05title\x18\x01 \x01(\t\x12\x18\n\x10option_list_keys\x18\x02 \x03(\t\x1a\x92\x01\n\x18PlayerSettingsOptionList\x12\r\n\x05title\x18\x01 \x01(\t\x12)\n\x04type\x18\x02 \x01(\x0e\x32\x1b.feature.PlayerSettingsType\x12<\n\x07options\x18\x03 \x03(\x0b\x32+.widget.PlayerSettingsWidget.SettingsOption\x1a\xa0\x02\n\x0eSettingsOption\x12]\n\x14video_quality_option\x18\x01 \x01(\x0b\x32=.widget.PlayerSettingsWidget.PlayerSettingsVideoQualityOptionH\x00\x12N\n\x0c\x61udio_option\x18\x02 \x01(\x0b\x32\x36.widget.PlayerSettingsWidget.PlayerSettingsAudioOptionH\x00\x12T\n\x0fsubtitle_option\x18\x03 \x01(\x0b\x32\x39.widget.PlayerSettingsWidget.PlayerSettingsSubtitleOptionH\x00\x42\t\n\x07options\x1a\xfc\x02\n PlayerSettingsVideoQualityOption\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12[\n\nbadge_type\x18\x04 \x01(\x0e\x32G.widget.PlayerSettingsWidget.PlayerSettingsVideoQualityOption.BadgeType\x12\x13\n\x0bis_selected\x18\x05 \x01(\x08\x12\x0f\n\x07\x62itrate\x18\x06 \x01(\x05\x12\r\n\x05width\x18\x07 \x01(\x05\x12\x0e\n\x06height\x18\x08 \x01(\x05\x12\x12\n\nmin_height\x18\t \x01(\x05\x12\x12\n\nmax_height\x18\n \x01(\x05\x12\x15\n\rmin_bandwidth\x18\x0b \x01(\x05\x12\x15\n\rmax_bandwidth\x18\x0c \x01(\x05\"*\n\tBadgeType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x10\n\x0cNEED_UPGRADE\x10\x01\x1a\xb5\x01\n\x19PlayerSettingsAudioOption\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bis_selected\x18\x03 \x01(\x08\x12\x10\n\x08iso2code\x18\x04 \x01(\t\x12\x10\n\x08iso3code\x18\x05 \x01(\t\x12\x17\n\x0fname_in_english\x18\x06 \x01(\t\x12\x14\n\x0clanguage_tag\x18\x07 \x01(\t\x12\x15\n\rchannel_count\x18\x08 \x01(\x05J\x04\x08\x02\x10\x03R\x04\x63ode\x1a\xa1\x01\n\x1cPlayerSettingsSubtitleOption\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bis_selected\x18\x03 \x01(\x08\x12\x10\n\x08iso2code\x18\x04 \x01(\t\x12\x10\n\x08iso3code\x18\x05 \x01(\t\x12\x17\n\x0fname_in_english\x18\x06 \x01(\t\x12\x14\n\x0clanguage_tag\x18\x07 \x01(\tJ\x04\x08\x02\x10\x03R\x04\x63odeJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.player_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PLAYERSETTINGSWIDGET_DATA_OPTIONLISTMAPENTRY']._loaded_options = None
  _globals['_PLAYERSETTINGSWIDGET_DATA_OPTIONLISTMAPENTRY']._serialized_options = b'8\001'
  _globals['_PLAYERSETTINGSWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_PLAYERSETTINGSWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_PLAYERSETTINGSWIDGET']._serialized_start=132
  _globals['_PLAYERSETTINGSWIDGET']._serialized_end=1929
  _globals['_PLAYERSETTINGSWIDGET_DATA']._serialized_start=289
  _globals['_PLAYERSETTINGSWIDGET_DATA']._serialized_end=678
  _globals['_PLAYERSETTINGSWIDGET_DATA_OPTIONLISTMAPENTRY']._serialized_start=571
  _globals['_PLAYERSETTINGSWIDGET_DATA_OPTIONLISTMAPENTRY']._serialized_end=678
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSOPTIONLISTGROUP']._serialized_start=680
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSOPTIONLISTGROUP']._serialized_end=752
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSOPTIONLIST']._serialized_start=755
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSOPTIONLIST']._serialized_end=901
  _globals['_PLAYERSETTINGSWIDGET_SETTINGSOPTION']._serialized_start=904
  _globals['_PLAYERSETTINGSWIDGET_SETTINGSOPTION']._serialized_end=1192
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSVIDEOQUALITYOPTION']._serialized_start=1195
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSVIDEOQUALITYOPTION']._serialized_end=1575
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSVIDEOQUALITYOPTION_BADGETYPE']._serialized_start=1533
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSVIDEOQUALITYOPTION_BADGETYPE']._serialized_end=1575
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSAUDIOOPTION']._serialized_start=1578
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSAUDIOOPTION']._serialized_end=1759
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSSUBTITLEOPTION']._serialized_start=1762
  _globals['_PLAYERSETTINGSWIDGET_PLAYERSETTINGSSUBTITLEOPTION']._serialized_end=1923
# @@protoc_insertion_point(module_scope)
