# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: component/content/content.proto
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
    'component/content/content.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from component.content import artwork_tag_pb2 as component_dot_content_dot_artwork__tag__pb2
from component.content import content_callout_tag_pb2 as component_dot_content_dot_content__callout__tag__pb2
from component.content import episode_additional_attributes_pb2 as component_dot_content_dot_episode__additional__attributes__pb2
from component.content import image_attributes_pb2 as component_dot_content_dot_image__attributes__pb2
from component.content import show_additional_attributes_pb2 as component_dot_content_dot_show__additional__attributes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1f\x63omponent/content/content.proto\x12\x11\x63omponent.content\x1a#component/content/artwork_tag.proto\x1a+component/content/content_callout_tag.proto\x1a\x35\x63omponent/content/episode_additional_attributes.proto\x1a(component/content/image_attributes.proto\x1a\x32\x63omponent/content/show_additional_attributes.proto\"\xc8\n\n\x07\x43ontent\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x11\n\tsub_title\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\r\n\x05genre\x18\x05 \x01(\t\x12\x14\n\x0csub_title_id\x18\x06 \x01(\x03\x12\x18\n\x10\x63ontent_provider\x18\x07 \x01(\t\x12\x14\n\x0c\x63hannel_name\x18\x08 \x01(\t\x12\x0f\n\x07is_paid\x18\t \x01(\x08\x12\x11\n\tsub_genre\x18\x0c \x01(\t\x12\x1b\n\x13\x61vailable_languages\x18\r \x03(\t\x12\x19\n\x11original_language\x18\x0e \x01(\t\x12\x10\n\x08match_id\x18\x0f \x01(\t\x12\x11\n\tclip_type\x18\x10 \x01(\t\x12\x11\n\tstudio_id\x18\x11 \x01(\t\x12\x12\n\ntv_show_id\x18\x12 \x01(\t\x12\x14\n\x0ctv_season_id\x18\x13 \x01(\t\x12\x15\n\rtv_episode_id\x18\x14 \x01(\t\x12\x16\n\x0esports_game_id\x18\x15 \x01(\t\x12\x17\n\x0fsports_match_id\x18\x16 \x01(\t\x12\x18\n\x10sports_season_id\x18\x17 \x01(\t\x12\x1c\n\x14sports_tournament_id\x18\x18 \x01(\t\x12\x16\n\x0eis_monetizable\x18\x19 \x01(\x08\x12\x16\n\x0eis_coming_soon\x18\x1a \x01(\x08\x12\x12\n\ntrailer_id\x18\x1b \x01(\t\x12>\n\x0c\x63\x61llout_tags\x18\x1c \x03(\x0b\x32$.component.content.ContentCalloutTagB\x02\x18\x01\x12\x42\n\x14\x63ontent_callout_tags\x18\x1d \x03(\x0b\x32$.component.content.ContentCalloutTag\x12 \n\x18promotion_time_left_mins\x18\x1e \x01(\x03\x12\"\n\x1ais_promotion_timer_visible\x18\x1f \x01(\x08\x12\x36\n\x0b\x61rtwork_tag\x18  \x01(\x0b\x32\x1d.component.content.ArtworkTagB\x02\x18\x01\x12@\n\x10image_attributes\x18! \x01(\x0b\x32\".component.content.ImageAttributesB\x02\x18\x01\x12\x1a\n\x12\x61rtwork_attributes\x18\" \x01(\t\x12\x17\n\x0fis_free_preview\x18# \x01(\x08\x12\x16\n\x0ewatch_progress\x18$ \x01(\x02\x12\x1a\n\x12\x66ooter_tag_in_tray\x18% \x01(\t\x12\x1d\n\x15is_autoplay_available\x18& \x01(\x08\x12\x1c\n\x14meta_impression_list\x18\' \x01(\t\x12=\n\x11\x63ontent_card_type\x18( \x01(\x0e\x32\".component.content.ContentCardType\x12\x16\n\x0einitiation_src\x18) \x01(\t\x12\x1e\n\x16\x66ooter_details_in_tray\x18* \x01(\t\x12\x1a\n\x12is_hp_free_preview\x18+ \x01(\x08\x12L\n\x12\x65pisode_attributes\x18\n \x01(\x0b\x32..component.content.EpisodeAdditionalAttributesH\x00\x12\x46\n\x0fshow_attributes\x18\x0b \x01(\x0b\x32+.component.content.ShowAdditionalAttributesH\x00\x42\x17\n\x15\x61\x64\x64itional_attributes*\x99\x01\n\x0f\x43ontentCardType\x12!\n\x1d\x43ONTENT_CARD_TYPE_UNSPECIFIED\x10\x00\x12 \n\x1c\x43ONTENT_CARD_TYPE_HOVER_CARD\x10\x01\x12\x1c\n\x18\x43ONTENT_CARD_TYPE_LR_UAT\x10\x02\x12#\n\x1f\x43ONTENT_CARD_TYPE_HERO_GEC_CARD\x10\x03\x42m\n!com.hotstar.event.model.componentP\x01ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/contentb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'component.content.content_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!com.hotstar.event.model.componentP\001ZFgithub.com/hotstar/data-event-schemas-go/hsanalytics/component/content'
  _globals['_CONTENT'].fields_by_name['callout_tags']._loaded_options = None
  _globals['_CONTENT'].fields_by_name['callout_tags']._serialized_options = b'\030\001'
  _globals['_CONTENT'].fields_by_name['artwork_tag']._loaded_options = None
  _globals['_CONTENT'].fields_by_name['artwork_tag']._serialized_options = b'\030\001'
  _globals['_CONTENT'].fields_by_name['image_attributes']._loaded_options = None
  _globals['_CONTENT'].fields_by_name['image_attributes']._serialized_options = b'\030\001'
  _globals['_CONTENTCARDTYPE']._serialized_start=1641
  _globals['_CONTENTCARDTYPE']._serialized_end=1794
  _globals['_CONTENT']._serialized_start=286
  _globals['_CONTENT']._serialized_end=1638
# @@protoc_insertion_point(module_scope)
