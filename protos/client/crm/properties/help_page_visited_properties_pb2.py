# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/crm/properties/help_page_visited_properties.proto
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
    'client/crm/properties/help_page_visited_properties.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.crm.model import crm_page_info_pb2 as client_dot_crm_dot_model_dot_crm__page__info__pb2
from client.crm.properties import help_page_properties_pb2 as client_dot_crm_dot_properties_dot_help__page__properties__pb2
from client.crm.properties import help_user_properties_pb2 as client_dot_crm_dot_properties_dot_help__user__properties__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8client/crm/properties/help_page_visited_properties.proto\x12\x15\x63lient.crm.properties\x1a$client/crm/model/crm_page_info.proto\x1a\x30\x63lient/crm/properties/help_page_properties.proto\x1a\x30\x63lient/crm/properties/help_user_properties.proto\"\xad\x01\n\x19HelpPageVisitedProperties\x12G\n\x14help_user_properties\x18\x01 \x01(\x0b\x32).client.crm.properties.HelpUserProperties\x12G\n\x14help_page_properties\x18\x02 \x01(\x0b\x32).client.crm.properties.HelpPagePropertiesB}\n-com.hotstar.event.model.client.crm.propertiesP\x01ZJgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/crm/propertiesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.crm.properties.help_page_visited_properties_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n-com.hotstar.event.model.client.crm.propertiesP\001ZJgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/crm/properties'
  _globals['_HELPPAGEVISITEDPROPERTIES']._serialized_start=222
  _globals['_HELPPAGEVISITEDPROPERTIES']._serialized_end=395
# @@protoc_insertion_point(module_scope)
