# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/prelaunch_footer.proto
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
    'widget/prelaunch_footer.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.branding import brand_pb2 as feature_dot_branding_dot_brand__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwidget/prelaunch_footer.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x1c\x66\x65\x61ture/branding/brand.proto\x1a\x12\x62\x61se/actions.proto\"\xb1\x02\n\x15PrelaunchFooterWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x30\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\".widget.PrelaunchFooterWidget.Data\x1aw\n\x04\x44\x61ta\x12)\n\x04logo\x18\x01 \x01(\x0e\x32\x17.feature.branding.BrandB\x02\x18\x01\x12\x31\n\x05links\x18\x02 \x03(\x0b\x32\".widget.PrelaunchFooterWidget.Link\x12\x11\n\tinfo_msgs\x18\x03 \x03(\t\x1a\x34\n\x04Link\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.ActionsJ\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.prelaunch_footer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PRELAUNCHFOOTERWIDGET_DATA'].fields_by_name['logo']._loaded_options = None
  _globals['_PRELAUNCHFOOTERWIDGET_DATA'].fields_by_name['logo']._serialized_options = b'\030\001'
  _globals['_PRELAUNCHFOOTERWIDGET']._serialized_start=119
  _globals['_PRELAUNCHFOOTERWIDGET']._serialized_end=424
  _globals['_PRELAUNCHFOOTERWIDGET_DATA']._serialized_start=239
  _globals['_PRELAUNCHFOOTERWIDGET_DATA']._serialized_end=358
  _globals['_PRELAUNCHFOOTERWIDGET_LINK']._serialized_start=360
  _globals['_PRELAUNCHFOOTERWIDGET_LINK']._serialized_end=412
# @@protoc_insertion_point(module_scope)
