# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/download/model/download_request_info.proto
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
    'client/download/model/download_request_info.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from client.download.model import available_quality_pb2 as client_dot_download_dot_model_dot_available__quality__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1client/download/model/download_request_info.proto\x12\x15\x63lient.download.model\x1a-client/download/model/available_quality.proto\"\xb2\x04\n\x13\x44ownloadRequestInfo\x12\x17\n\x0f\x61vailable_sizes\x18\x01 \x01(\r\x12J\n\x19highest_available_quality\x18\x02 \x01(\x0e\x32\'.client.download.model.AvailableQuality\x12]\n\x15\x64ownload_manager_name\x18\x03 \x01(\x0e\x32>.client.download.model.DownloadRequestInfo.DownloadManagerName\x12$\n\x18\x64ownload_manager_version\x18\x04 \x01(\tB\x02\x18\x01\x12\x42\n\x11requested_quality\x18\x05 \x01(\x0e\x32\'.client.download.model.AvailableQuality\x12 \n\x18is_bilingual_ui_opted_in\x18\x06 \x01(\x08\x12\x44\n\x13\x61vailable_qualities\x18\x07 \x03(\x0e\x32\'.client.download.model.AvailableQuality\"\x84\x01\n\x13\x44ownloadManagerName\x12%\n!DOWNLOAD_MANAGER_NAME_UNSPECIFIED\x10\x00\x12$\n DOWNLOAD_MANAGER_NAME_HS_ANDROID\x10\x01\x12 \n\x1c\x44OWNLOAD_MANAGER_NAME_HS_IOS\x10\x02\x42}\n-com.hotstar.event.model.client.download.modelP\x01ZJgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/download/modelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.download.model.download_request_info_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n-com.hotstar.event.model.client.download.modelP\001ZJgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/download/model'
  _globals['_DOWNLOADREQUESTINFO'].fields_by_name['download_manager_version']._loaded_options = None
  _globals['_DOWNLOADREQUESTINFO'].fields_by_name['download_manager_version']._serialized_options = b'\030\001'
  _globals['_DOWNLOADREQUESTINFO']._serialized_start=124
  _globals['_DOWNLOADREQUESTINFO']._serialized_end=686
  _globals['_DOWNLOADREQUESTINFO_DOWNLOADMANAGERNAME']._serialized_start=554
  _globals['_DOWNLOADREQUESTINFO_DOWNLOADMANAGERNAME']._serialized_end=686
# @@protoc_insertion_point(module_scope)
