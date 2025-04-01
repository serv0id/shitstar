# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/player_control_v2.proto
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
    'widget/player_control_v2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import orientation_pb2 as base_dot_orientation__pb2
from feature.commons import alignment_pb2 as feature_dot_commons_dot_alignment__pb2
from feature.atom import button_pb2 as feature_dot_atom_dot_button__pb2
from feature.atom import toggle_button_pb2 as feature_dot_atom_dot_toggle__button__pb2
from feature.atom import toggle_lottie_button_pb2 as feature_dot_atom_dot_toggle__lottie__button__pb2
from feature.atom import event_observer_button_pb2 as feature_dot_atom_dot_event__observer__button__pb2
from feature.text import text_pb2 as feature_dot_text_dot_text__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ewidget/player_control_v2.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x16\x62\x61se/orientation.proto\x1a\x1f\x66\x65\x61ture/commons/alignment.proto\x1a\x19\x66\x65\x61ture/atom/button.proto\x1a feature/atom/toggle_button.proto\x1a\'feature/atom/toggle_lottie_button.proto\x1a(feature/atom/event_observer_button.proto\x1a\x17\x66\x65\x61ture/text/text.proto\"\xf1\t\n\x15PlayerControlV2Widget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x30\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\".widget.PlayerControlV2Widget.Data\x1a\xc9\x01\n\x04\x44\x61ta\x12\x43\n\x0e\x63ontent_header\x18\x01 \x01(\x0b\x32+.widget.PlayerControlV2Widget.ContentHeader\x12\x38\n\x08settings\x18\x02 \x01(\x0b\x32&.widget.PlayerControlV2Widget.Settings\x12\x42\n\rsticky_header\x18\x03 \x01(\x0b\x32+.widget.PlayerControlV2Widget.ContentHeader\x1aH\n\rContentHeader\x12\x37\n\x05items\x18\x01 \x03(\x0b\x32(.widget.PlayerControlV2Widget.HeaderItem\x1a\x44\n\x08Settings\x12\x38\n\x05items\x18\x01 \x03(\x0b\x32).widget.PlayerControlV2Widget.SettingItem\x1aY\n\x0eTextHeaderItem\x12!\n\x05title\x18\x01 \x01(\x0b\x32\x12.feature.text.Text\x12$\n\x08subtitle\x18\x02 \x01(\x0b\x32\x12.feature.text.Text\x1a\x98\x03\n\nHeaderItem\x12&\n\x0borientation\x18\n \x01(\x0e\x32\x11.base.Orientation\x12-\n\talignment\x18\x0b \x01(\x0e\x32\x1a.feature.commons.Alignment\x12&\n\x06\x62utton\x18\x01 \x01(\x0b\x32\x14.feature.atom.ButtonH\x00\x12\x33\n\rtoggle_button\x18\x02 \x01(\x0b\x32\x1a.feature.atom.ToggleButtonH\x00\x12@\n\x14toggle_lottie_button\x18\x03 \x01(\x0b\x32 .feature.atom.ToggleLottieButtonH\x00\x12\x42\n\x15\x65vent_observer_button\x18\x04 \x01(\x0b\x32!.feature.atom.EventObserverButtonH\x00\x12H\n\x10text_header_item\x18\x05 \x01(\x0b\x32,.widget.PlayerControlV2Widget.TextHeaderItemH\x00\x42\x06\n\x04item\x1a\xa0\x02\n\x0bSettingItem\x12&\n\x0borientation\x18\n \x01(\x0e\x32\x11.base.Orientation\x12&\n\x06\x62utton\x18\x01 \x01(\x0b\x32\x14.feature.atom.ButtonH\x00\x12\x33\n\rtoggle_button\x18\x02 \x01(\x0b\x32\x1a.feature.atom.ToggleButtonH\x00\x12@\n\x14toggle_lottie_button\x18\x03 \x01(\x0b\x32 .feature.atom.ToggleLottieButtonH\x00\x12\x42\n\x15\x65vent_observer_button\x18\x04 \x01(\x0b\x32!.feature.atom.EventObserverButtonH\x00\x42\x06\n\x04itemJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.player_control_v2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PLAYERCONTROLV2WIDGET']._serialized_start=296
  _globals['_PLAYERCONTROLV2WIDGET']._serialized_end=1561
  _globals['_PLAYERCONTROLV2WIDGET_DATA']._serialized_start=417
  _globals['_PLAYERCONTROLV2WIDGET_DATA']._serialized_end=618
  _globals['_PLAYERCONTROLV2WIDGET_CONTENTHEADER']._serialized_start=620
  _globals['_PLAYERCONTROLV2WIDGET_CONTENTHEADER']._serialized_end=692
  _globals['_PLAYERCONTROLV2WIDGET_SETTINGS']._serialized_start=694
  _globals['_PLAYERCONTROLV2WIDGET_SETTINGS']._serialized_end=762
  _globals['_PLAYERCONTROLV2WIDGET_TEXTHEADERITEM']._serialized_start=764
  _globals['_PLAYERCONTROLV2WIDGET_TEXTHEADERITEM']._serialized_end=853
  _globals['_PLAYERCONTROLV2WIDGET_HEADERITEM']._serialized_start=856
  _globals['_PLAYERCONTROLV2WIDGET_HEADERITEM']._serialized_end=1264
  _globals['_PLAYERCONTROLV2WIDGET_SETTINGITEM']._serialized_start=1267
  _globals['_PLAYERCONTROLV2WIDGET_SETTINGITEM']._serialized_end=1555
# @@protoc_insertion_point(module_scope)
