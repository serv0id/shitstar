# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/options.proto
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
    'widget/options.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14widget/options.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\"\x99\x03\n\rOptionsWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12(\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\x1a.widget.OptionsWidget.Data\x1a\x80\x02\n\x04\x44\x61ta\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x04type\x18\x02 \x01(\x0e\x32(.widget.OptionsWidget.Data.SelectionType\x12-\n\x04size\x18\x03 \x01(\x0e\x32\x1f.widget.OptionsWidget.Data.Size\x12\x38\n\rinput_options\x18\x04 \x03(\x0b\x32!.widget.OptionsWidget.InputOption\")\n\rSelectionType\x12\n\n\x06SINGLE\x10\x00\x12\x0c\n\x08MULTIPLE\x10\x01\" \n\x04Size\x12\t\n\x05\x46LUID\x10\x00\x12\r\n\tFULLWIDTH\x10\x01\x1a(\n\x0bInputOption\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\tJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.options_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_OPTIONSWIDGET']._serialized_start=60
  _globals['_OPTIONSWIDGET']._serialized_end=469
  _globals['_OPTIONSWIDGET_DATA']._serialized_start=165
  _globals['_OPTIONSWIDGET_DATA']._serialized_end=421
  _globals['_OPTIONSWIDGET_DATA_SELECTIONTYPE']._serialized_start=346
  _globals['_OPTIONSWIDGET_DATA_SELECTIONTYPE']._serialized_end=387
  _globals['_OPTIONSWIDGET_DATA_SIZE']._serialized_start=389
  _globals['_OPTIONSWIDGET_DATA_SIZE']._serialized_end=421
  _globals['_OPTIONSWIDGET_INPUTOPTION']._serialized_start=423
  _globals['_OPTIONSWIDGET_INPUTOPTION']._serialized_end=463
# @@protoc_insertion_point(module_scope)
