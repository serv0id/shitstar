# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/download/properties/download_attempt_properties.proto
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
    'client/download/properties/download_attempt_properties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.download.model import journey_type_pb2 as client_dot_download_dot_model_dot_journey__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<client/download/properties/download_attempt_properties.proto\x12\x1a\x63lient.download.properties\x1a(client/download/model/journey_type.proto\"v\n\x19\x44ownloadAttemptProperties\x12\x42\n\x16requested_journey_type\x18\x01 \x01(\x0e\x32\".client.download.model.JourneyType\x12\x15\n\rdownload_uuid\x18\x02 \x01(\tB\x87\x01\n2com.hotstar.event.model.client.download.propertiesP\x01ZOgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/download/propertiesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.download.properties.download_attempt_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n2com.hotstar.event.model.client.download.propertiesP\001ZOgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/download/properties'
  _globals['_DOWNLOADATTEMPTPROPERTIES']._serialized_start=134
  _globals['_DOWNLOADATTEMPTPROPERTIES']._serialized_end=252
# @@protoc_insertion_point(module_scope)
