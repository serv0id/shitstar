# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/watch/change_brightness.proto
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
    'client/watch/change_brightness.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$client/watch/change_brightness.proto\x12\x0c\x63lient.watch\"\xeb\x02\n\x1a\x43hangeBrightnessProperties\x12\x1f\n\x17previous_brightness_pct\x18\x01 \x01(\x05\x12\x1a\n\x12new_brightness_pct\x18\x02 \x01(\x05\x12P\n\rchange_source\x18\x03 \x01(\x0e\x32\x39.client.watch.ChangeBrightnessProperties.BrightnessSource\"\xbd\x01\n\x10\x42rightnessSource\x12!\n\x1d\x42RIGHTNESS_SOURCE_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x42RIGHTNESS_SOURCE_GESTURE\x10\x01\x12$\n\x1c\x42RIGHTNESS_SOURCE_VOLUME_BAR\x10\x02\x1a\x02\x08\x01\x12\x1b\n\x17\x42RIGHTNESS_SOURCE_PHONE\x10\x03\x12$\n BRIGHTNESS_SOURCE_BRIGHTNESS_BAR\x10\x04\x42k\n$com.hotstar.event.model.client.watchP\x01ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watchb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.watch.change_brightness_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.hotstar.event.model.client.watchP\001ZAgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/watch'
  _globals['_CHANGEBRIGHTNESSPROPERTIES_BRIGHTNESSSOURCE'].values_by_name["BRIGHTNESS_SOURCE_VOLUME_BAR"]._loaded_options = None
  _globals['_CHANGEBRIGHTNESSPROPERTIES_BRIGHTNESSSOURCE'].values_by_name["BRIGHTNESS_SOURCE_VOLUME_BAR"]._serialized_options = b'\010\001'
  _globals['_CHANGEBRIGHTNESSPROPERTIES']._serialized_start=55
  _globals['_CHANGEBRIGHTNESSPROPERTIES']._serialized_end=418
  _globals['_CHANGEBRIGHTNESSPROPERTIES_BRIGHTNESSSOURCE']._serialized_start=229
  _globals['_CHANGEBRIGHTNESSPROPERTIES_BRIGHTNESSSOURCE']._serialized_end=418
# @@protoc_insertion_point(module_scope)
