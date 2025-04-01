# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/sports_cricket_summary_card.proto
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
    'widget/sports_cricket_summary_card.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from widget import polling_pb2 as widget_dot_polling__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from widget import sports_cricket_team_pb2 as widget_dot_sports__cricket__team__pb2
from feature.sports import game_pb2 as feature_dot_sports_dot_game__pb2
from feature.sports import cricket_team_pb2 as feature_dot_sports_dot_cricket__team__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(widget/sports_cricket_summary_card.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x14widget/polling.proto\x1a\x19\x66\x65\x61ture/image/image.proto\x1a widget/sports_cricket_team.proto\x1a\x19\x66\x65\x61ture/sports/game.proto\x1a!feature/sports/cricket_team.proto\"\xee\x01\n\x1f\x43ricketPollingSummaryCardWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12:\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32,.widget.CricketPollingSummaryCardWidget.Data\x1a\\\n\x04\x44\x61ta\x12.\n\x04\x63\x61rd\x18\x01 \x01(\x0b\x32 .widget.CricketSummaryCardWidget\x12$\n\x07polling\x18\x02 \x01(\x0b\x32\x13.widget.PollingDataJ\x04\x08\x02\x10\x0b\"\xb6\x08\n\x18\x43ricketSummaryCardWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x33\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32%.widget.CricketSummaryCardWidget.Data\x1a\x94\x05\n\x04\x44\x61ta\x12\'\n\tgame_info\x18\x0b \x01(\x0b\x32\x14.feature.sports.Game\x12\x32\n\rfirst_team_v2\x18\x0c \x01(\x0b\x32\x1b.feature.sports.CricketTeam\x12\x33\n\x0esecond_team_v2\x18\r \x01(\x0b\x32\x1b.feature.sports.CricketTeam\x12\x16\n\x0elatest_summary\x18\x07 \x01(\t\x12\x17\n\x0fis_test_cricket\x18\x08 \x01(\x08\x12H\n\x0elast_few_balls\x18\t \x03(\x0b\x32\x30.widget.CricketSummaryCardWidget.LastFewBallItem\x12\x0f\n\x07innings\x18\n \x03(\t\x12!\n\x19\x63urrent_batting_team_name\x18\x0e \x01(\t\x12\x10\n\x04name\x18\x01 \x01(\tB\x02\x18\x01\x12\x42\n\x05state\x18\x02 \x01(\x0e\x32/.widget.CricketSummaryCardWidget.Data.GameStateB\x02\x18\x01\x12\x15\n\tmeta_desc\x18\x03 \x01(\tB\x02\x18\x01\x12\x42\n\nmedia_info\x18\x04 \x01(\x0b\x32*.widget.CricketSummaryCardWidget.MediaInfoB\x02\x18\x01\x12+\n\nfirst_team\x18\x05 \x01(\x0b\x32\x13.widget.CricketTeamB\x02\x18\x01\x12,\n\x0bsecond_team\x18\x06 \x01(\x0b\x32\x13.widget.CricketTeamB\x02\x18\x01\"?\n\tGameState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tNOT_START\x10\x01\x12\x08\n\x04LIVE\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\x1aM\n\tMediaInfo\x12)\n\x0bthumb_image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x15\n\rclip_duration\x18\x02 \x01(\t\x1a\xcb\x01\n\x0fLastFewBallItem\x12L\n\tball_type\x18\x01 \x01(\x0e\x32\x39.widget.CricketSummaryCardWidget.LastFewBallItem.BallType\x12\x12\n\nball_score\x18\x02 \x01(\t\"V\n\x08\x42\x61llType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x08OVER_NUM\x10\x01\x12\x10\n\x0cNORMAL_SCORE\x10\x02\x12\x08\n\x04\x46OUR\x10\x03\x12\x07\n\x03SIX\x10\x04\x12\n\n\x06WICKET\x10\x05J\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.sports_cricket_summary_card_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['name']._loaded_options = None
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['name']._serialized_options = b'\030\001'
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['state']._loaded_options = None
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['state']._serialized_options = b'\030\001'
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['meta_desc']._loaded_options = None
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['meta_desc']._serialized_options = b'\030\001'
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['media_info']._loaded_options = None
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['media_info']._serialized_options = b'\030\001'
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['first_team']._loaded_options = None
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['first_team']._serialized_options = b'\030\001'
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['second_team']._loaded_options = None
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA'].fields_by_name['second_team']._serialized_options = b'\030\001'
  _globals['_CRICKETPOLLINGSUMMARYCARDWIDGET']._serialized_start=225
  _globals['_CRICKETPOLLINGSUMMARYCARDWIDGET']._serialized_end=463
  _globals['_CRICKETPOLLINGSUMMARYCARDWIDGET_DATA']._serialized_start=365
  _globals['_CRICKETPOLLINGSUMMARYCARDWIDGET_DATA']._serialized_end=457
  _globals['_CRICKETSUMMARYCARDWIDGET']._serialized_start=466
  _globals['_CRICKETSUMMARYCARDWIDGET']._serialized_end=1544
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA']._serialized_start=593
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA']._serialized_end=1253
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA_GAMESTATE']._serialized_start=1190
  _globals['_CRICKETSUMMARYCARDWIDGET_DATA_GAMESTATE']._serialized_end=1253
  _globals['_CRICKETSUMMARYCARDWIDGET_MEDIAINFO']._serialized_start=1255
  _globals['_CRICKETSUMMARYCARDWIDGET_MEDIAINFO']._serialized_end=1332
  _globals['_CRICKETSUMMARYCARDWIDGET_LASTFEWBALLITEM']._serialized_start=1335
  _globals['_CRICKETSUMMARYCARDWIDGET_LASTFEWBALLITEM']._serialized_end=1538
  _globals['_CRICKETSUMMARYCARDWIDGET_LASTFEWBALLITEM_BALLTYPE']._serialized_start=1452
  _globals['_CRICKETSUMMARYCARDWIDGET_LASTFEWBALLITEM_BALLTYPE']._serialized_end=1538
# @@protoc_insertion_point(module_scope)
