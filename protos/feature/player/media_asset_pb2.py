# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/player/media_asset.proto
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
    'feature/player/media_asset.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.player import playback_params_pb2 as feature_dot_player_dot_playback__params__pb2
from feature.player import playback_stream_params_pb2 as feature_dot_player_dot_playback__stream__params__pb2
from feature.content_language_preference import content_language_preference_pb2 as feature_dot_content__language__preference_dot_content__language__preference__pb2
from feature.player import subtitle_asset_pb2 as feature_dot_player_dot_subtitle__asset__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n feature/player/media_asset.proto\x12\x0e\x66\x65\x61ture.player\x1a$feature/player/playback_params.proto\x1a+feature/player/playback_stream_params.proto\x1a\x45\x66\x65\x61ture/content_language_preference/content_language_preference.proto\x1a#feature/player/subtitle_asset.proto\"\xaf\x03\n\nMediaAsset\x12/\n\x07primary\x18\x01 \x01(\x0b\x32\x1e.feature.player.PlaybackParams\x12\x30\n\x08\x66\x61llback\x18\x02 \x01(\x0b\x32\x1e.feature.player.PlaybackParams\x12\x13\n\x0brepeat_mode\x18\x03 \x01(\x08\x12\x1e\n\x16\x64\x65\x66\x61ult_audio_language\x18\x04 \x01(\t\x12\x1d\n\x15\x64\x65\x66\x61ult_text_language\x18\x05 \x01(\t\x12\x12\n\nsession_id\x18\x06 \x01(\t\x12`\n\x18language_preference_info\x18\x07 \x01(\x0b\x32>.feature.content_language_preference.ContentLanguagePreference\x12\x36\n\x0fsubtitle_assets\x18\x08 \x03(\x0b\x32\x1d.feature.player.SubtitleAsset\x12<\n\x0eprimary_stream\x18\t \x01(\x0b\x32$.feature.player.PlaybackStreamParamsB_\n#com.hotstar.ui.model.feature.playerP\x01Z6github.com/hotstar/hs-core-ui-models-go/feature/playerb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.player.media_asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#com.hotstar.ui.model.feature.playerP\001Z6github.com/hotstar/hs-core-ui-models-go/feature/player'
  _globals['_MEDIAASSET']._serialized_start=244
  _globals['_MEDIAASSET']._serialized_end=675
# @@protoc_insertion_point(module_scope)
