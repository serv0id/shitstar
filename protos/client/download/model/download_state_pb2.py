# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: client/download/model/download_state.proto
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
    'client/download/model/download_state.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*client/download/model/download_state.proto\x12\x15\x63lient.download.model*\xdd\x07\n\rDownloadState\x12\x1e\n\x1a\x44OWNLOAD_STATE_UNSPECIFIED\x10\x00\x12\x17\n\x13\x44OWNLOAD_STATE_NONE\x10\x01\x12\x1c\n\x18\x44OWNLOAD_STATE_INITIATED\x10\x02\x12\x1a\n\x16\x44OWNLOAD_STATE_STARTED\x10\x03\x12\x19\n\x15\x44OWNLOAD_STATE_PAUSED\x10\x04\x12\x1c\n\x18\x44OWNLOAD_STATE_COMPLETED\x10\x05\x12\x19\n\x15\x44OWNLOAD_STATE_FAILED\x10\x06\x12\x1c\n\x18\x44OWNLOAD_STATE_CANCELLED\x10\x07\x12\x1d\n\x19\x44OWNLOAD_STATE_TERMINATED\x10\x08\x12\x1e\n\x1a\x44OWNLOAD_STATE_IN_PROGRESS\x10\t\x12\x1a\n\x16\x44OWNLOAD_STATE_RESUMED\x10\n\x12\x1a\n\x16\x44OWNLOAD_STATE_DELETED\x10\x0b\x12$\n DOWNLOAD_STATE_MARKED_AS_DELETED\x10\x0c\x12\x19\n\x15\x44OWNLOAD_STATE_QUEUED\x10\r\x12\x1a\n\x16\x44OWNLOAD_STATE_EXPIRED\x10\x0e\x12\x30\n,DOWNLOAD_STATE_FAILED_DUE_TO_APP_TERMINATION\x10\x0f\x12/\n+DOWNLOAD_STATE_LICENSE_FETCHING_IN_PROGRESS\x10\x10\x12*\n&DOWNLOAD_STATE_LICENSE_FETCHING_FAILED\x10\x11\x12\x30\n,DOWNLOAD_STATE_DOWNLOAD_PAUSED_OVER_CELLULAR\x10\x12\x12 \n\x1c\x44OWNLOAD_STATE_PREPROCESSING\x10\x13\x12!\n\x1d\x44OWNLOAD_STATE_CHECK_DOWNLOAD\x10\x14\x12!\n\x1d\x44OWNLOAD_STATE_START_DOWNLOAD\x10\x15\x12\x1e\n\x1a\x44OWNLOAD_STATE_SIZE_MODULE\x10\x16\x12\x1d\n\x19\x44OWNLOAD_STATE_DRM_MODULE\x10\x17\x12+\n\'DOWNLOAD_STATE_FAILED_AT_CHECK_DOWNLOAD\x10\x18\x12+\n\'DOWNLOAD_STATE_FAILED_AT_START_DOWNLOAD\x10\x19\x12(\n$DOWNLOAD_STATE_FAILED_AT_SIZE_MODULE\x10\x1a\x12\'\n#DOWNLOAD_STATE_FAILED_AT_DRM_MODULE\x10\x1b\x42}\n-com.hotstar.event.model.client.download.modelP\x01ZJgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/download/modelb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'client.download.model.download_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n-com.hotstar.event.model.client.download.modelP\001ZJgithub.com/hotstar/data-event-schemas-go/hsanalytics/client/download/model'
  _globals['_DOWNLOADSTATE']._serialized_start=70
  _globals['_DOWNLOADSTATE']._serialized_end=1059
# @@protoc_insertion_point(module_scope)
