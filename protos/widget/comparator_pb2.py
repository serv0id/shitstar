# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/comparator.proto
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
    'widget/comparator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17widget/comparator.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\"\xa2\x06\n\x14PlanComparatorWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.PlanComparatorWidget.Data\x1a\x80\x01\n\x04\x44\x61ta\x12\x39\n\x07heading\x18\x01 \x03(\x0b\x32(.widget.PlanComparatorWidget.PlanHeading\x12=\n\titem_list\x18\x02 \x03(\x0b\x32*.widget.PlanComparatorWidget.ComparatorRow\x1a\\\n\x0bPlanHeading\x12\x0f\n\x07heading\x18\x01 \x01(\t\x12\x13\n\x0bsub_heading\x18\x02 \x01(\t\x12\x13\n\x0bis_selected\x18\x03 \x01(\x08\x12\x12\n\nidentifier\x18\x04 \x03(\t\x1a\x83\x01\n\rComparatorRow\x12\x32\n\x03usp\x18\x01 \x01(\x0b\x32%.widget.PlanComparatorWidget.TextItem\x12>\n\nitem_value\x18\x02 \x03(\x0b\x32*.widget.PlanComparatorWidget.ComparatorCol\x1a\x91\x01\n\rComparatorCol\x12\x13\n\x0bis_selected\x18\x03 \x01(\x08\x12\x12\n\nidentifier\x18\x04 \x03(\t\x12\x13\n\ticon_name\x18\x01 \x01(\tH\x00\x12\x35\n\x04text\x18\x02 \x01(\x0b\x32%.widget.PlanComparatorWidget.TextItemH\x00\x42\x0b\n\titem_type\x1aS\n\x08TextItem\x12\r\n\x05title\x18\x01 \x01(\t\x12\x38\n\tsub_title\x18\x02 \x01(\x0b\x32%.widget.PlanComparatorWidget.Subtitle\x1a\x30\n\x08Subtitle\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x16\n\x0eis_highlighted\x18\x02 \x01(\x08J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.comparator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PLANCOMPARATORWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_PLANCOMPARATORWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_PLANCOMPARATORWIDGET']._serialized_start=84
  _globals['_PLANCOMPARATORWIDGET']._serialized_end=886
  _globals['_PLANCOMPARATORWIDGET_DATA']._serialized_start=241
  _globals['_PLANCOMPARATORWIDGET_DATA']._serialized_end=369
  _globals['_PLANCOMPARATORWIDGET_PLANHEADING']._serialized_start=371
  _globals['_PLANCOMPARATORWIDGET_PLANHEADING']._serialized_end=463
  _globals['_PLANCOMPARATORWIDGET_COMPARATORROW']._serialized_start=466
  _globals['_PLANCOMPARATORWIDGET_COMPARATORROW']._serialized_end=597
  _globals['_PLANCOMPARATORWIDGET_COMPARATORCOL']._serialized_start=600
  _globals['_PLANCOMPARATORWIDGET_COMPARATORCOL']._serialized_end=745
  _globals['_PLANCOMPARATORWIDGET_TEXTITEM']._serialized_start=747
  _globals['_PLANCOMPARATORWIDGET_TEXTITEM']._serialized_end=830
  _globals['_PLANCOMPARATORWIDGET_SUBTITLE']._serialized_start=832
  _globals['_PLANCOMPARATORWIDGET_SUBTITLE']._serialized_end=880
# @@protoc_insertion_point(module_scope)
