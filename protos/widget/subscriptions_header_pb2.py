# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/subscriptions_header.proto
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
    'widget/subscriptions_header.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from widget import logo_pb2 as widget_dot_logo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!widget/subscriptions_header.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x11widget/logo.proto\"\xcd\x05\n\x19SubscriptionsHeaderWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x34\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32&.widget.SubscriptionsHeaderWidget.Data\x1a\xc7\x01\n\x04\x44\x61ta\x12P\n\x13help_setting_button\x18\x01 \x01(\x0b\x32\x33.widget.SubscriptionsHeaderWidget.HelpSettingButton\x12K\n\rsubscriptions\x18\x02 \x03(\x0b\x32\x34.widget.SubscriptionsHeaderWidget.SubscriptionDetail\x12 \n\x04logo\x18\x03 \x01(\x0b\x32\x12.widget.LogoWidget\x1a\x41\n\x11HelpSettingButton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1a\xd5\x01\n\x12SubscriptionDetail\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tplan_name\x18\x02 \x01(\t\x12\x15\n\rmobile_number\x18\x03 \x01(\t\x12#\n\x1bnumber_of_logged_in_devices\x18\x04 \x01(\r\x12\x1d\n\x15\x64\x65vice_logged_in_text\x18\x05 \x01(\t\x12\x45\n\rmanage_button\x18\x06 \x01(\x0b\x32..widget.SubscriptionsHeaderWidget.ManageButton\x1a<\n\x0cManageButton\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.ActionsJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.subscriptions_header_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_SUBSCRIPTIONSHEADERWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_SUBSCRIPTIONSHEADERWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_SUBSCRIPTIONSHEADERWIDGET']._serialized_start=133
  _globals['_SUBSCRIPTIONSHEADERWIDGET']._serialized_end=850
  _globals['_SUBSCRIPTIONSHEADERWIDGET_DATA']._serialized_start=300
  _globals['_SUBSCRIPTIONSHEADERWIDGET_DATA']._serialized_end=499
  _globals['_SUBSCRIPTIONSHEADERWIDGET_HELPSETTINGBUTTON']._serialized_start=501
  _globals['_SUBSCRIPTIONSHEADERWIDGET_HELPSETTINGBUTTON']._serialized_end=566
  _globals['_SUBSCRIPTIONSHEADERWIDGET_SUBSCRIPTIONDETAIL']._serialized_start=569
  _globals['_SUBSCRIPTIONSHEADERWIDGET_SUBSCRIPTIONDETAIL']._serialized_end=782
  _globals['_SUBSCRIPTIONSHEADERWIDGET_MANAGEBUTTON']._serialized_start=784
  _globals['_SUBSCRIPTIONSHEADERWIDGET_MANAGEBUTTON']._serialized_end=844
# @@protoc_insertion_point(module_scope)
