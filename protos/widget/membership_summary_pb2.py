# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/membership_summary.proto
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
    'widget/membership_summary.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwidget/membership_summary.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\"\xba\x07\n\x17MembershipSummaryWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x32\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32$.widget.MembershipSummaryWidget.Data\x1a\xa9\x02\n\x04\x44\x61ta\x12\x34\n\x05title\x18\x01 \x01(\x0b\x32%.widget.MembershipSummaryWidget.Title\x12\x19\n\x11primary_sub_title\x18\x02 \x01(\t\x12\x1b\n\x13secondary_sub_title\x18\x03 \x01(\t\x12\x30\n\x03\x63ta\x18\x04 \x01(\x0b\x32#.widget.MembershipSummaryWidget.Cta\x12\x38\n\x07subtext\x18\x05 \x01(\x0b\x32\'.widget.MembershipSummaryWidget.Subtext\x12G\n\x11help_settings_cta\x18\x06 \x01(\x0b\x32,.widget.MembershipSummaryWidget.HelpSettings\x1an\n\x05Title\x12\r\n\x05value\x18\x01 \x01(\t\x12\x37\n\x04type\x18\x02 \x01(\x0e\x32).widget.MembershipSummaryWidget.TitleType\x12\x1d\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32\r.base.Actions\x1aO\n\x03\x43ta\x12\r\n\x05value\x18\x01 \x01(\t\x12\x1d\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\r.base.Actions\x12\x1a\n\x12strikethrough_text\x18\x03 \x01(\t\x1aS\n\x07Subtext\x12\r\n\x05value\x18\x01 \x01(\t\x12\x39\n\x04type\x18\x02 \x01(\x0e\x32+.widget.MembershipSummaryWidget.SubtextType\x1aO\n\x0cHelpSettings\x12\x11\n\ticon_name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x1d\n\x06\x61\x63tion\x18\x03 \x01(\x0b\x32\r.base.Actions\"?\n\x0bSubtextType\x12\x08\n\x04\x42\x41SE\x10\x00\x12\x13\n\x0bHIGHLIGHTED\x10\x01\x1a\x02\x08\x01\x12\x11\n\rERROR_SUBTEXT\x10\x02\">\n\tTitleType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\r\n\x05\x45RROR\x10\x01\x1a\x02\x08\x01\x12\x15\n\x11HIGHLIGHTED_TITLE\x10\x02J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.membership_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_MEMBERSHIPSUMMARYWIDGET_SUBTEXTTYPE'].values_by_name["HIGHLIGHTED"]._loaded_options = None
  _globals['_MEMBERSHIPSUMMARYWIDGET_SUBTEXTTYPE'].values_by_name["HIGHLIGHTED"]._serialized_options = b'\010\001'
  _globals['_MEMBERSHIPSUMMARYWIDGET_TITLETYPE'].values_by_name["ERROR"]._loaded_options = None
  _globals['_MEMBERSHIPSUMMARYWIDGET_TITLETYPE'].values_by_name["ERROR"]._serialized_options = b'\010\001'
  _globals['_MEMBERSHIPSUMMARYWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_MEMBERSHIPSUMMARYWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_MEMBERSHIPSUMMARYWIDGET']._serialized_start=112
  _globals['_MEMBERSHIPSUMMARYWIDGET']._serialized_end=1066
  _globals['_MEMBERSHIPSUMMARYWIDGET_DATA']._serialized_start=275
  _globals['_MEMBERSHIPSUMMARYWIDGET_DATA']._serialized_end=572
  _globals['_MEMBERSHIPSUMMARYWIDGET_TITLE']._serialized_start=574
  _globals['_MEMBERSHIPSUMMARYWIDGET_TITLE']._serialized_end=684
  _globals['_MEMBERSHIPSUMMARYWIDGET_CTA']._serialized_start=686
  _globals['_MEMBERSHIPSUMMARYWIDGET_CTA']._serialized_end=765
  _globals['_MEMBERSHIPSUMMARYWIDGET_SUBTEXT']._serialized_start=767
  _globals['_MEMBERSHIPSUMMARYWIDGET_SUBTEXT']._serialized_end=850
  _globals['_MEMBERSHIPSUMMARYWIDGET_HELPSETTINGS']._serialized_start=852
  _globals['_MEMBERSHIPSUMMARYWIDGET_HELPSETTINGS']._serialized_end=931
  _globals['_MEMBERSHIPSUMMARYWIDGET_SUBTEXTTYPE']._serialized_start=933
  _globals['_MEMBERSHIPSUMMARYWIDGET_SUBTEXTTYPE']._serialized_end=996
  _globals['_MEMBERSHIPSUMMARYWIDGET_TITLETYPE']._serialized_start=998
  _globals['_MEMBERSHIPSUMMARYWIDGET_TITLETYPE']._serialized_end=1060
# @@protoc_insertion_point(module_scope)
