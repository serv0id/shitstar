# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/previous_logins.proto
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
    'widget/previous_logins.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import template_pb2 as base_dot_template__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.branding import brand_pb2 as feature_dot_branding_dot_brand__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cwidget/previous_logins.proto\x12\x06widget\x1a\x13\x62\x61se/template.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x1c\x66\x65\x61ture/branding/brand.proto\x1a\x12\x62\x61se/actions.proto\"\x81\x07\n\x14PreviousLoginsWidget\x12$\n\x08template\x18\x01 \x01(\x0b\x32\x0e.base.TemplateB\x02\x18\x01\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12/\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32!.widget.PreviousLoginsWidget.Data\x1a\x96\x02\n\x04\x44\x61ta\x12)\n\x04logo\x18\x01 \x01(\x0e\x32\x17.feature.branding.BrandB\x02\x18\x01\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0bmanage_text\x18\x03 \x01(\t\x12X\n\x1alogin_with_another_account\x18\x04 \x01(\x0b\x32\x34.widget.PreviousLoginsWidget.LoginWithAnotherAccount\x12M\n\x14previous_login_items\x18\x05 \x03(\x0b\x32/.widget.PreviousLoginsWidget.PreviousLoginItems\x12\x16\n\x0ehelp_rich_text\x18\x06 \x01(\t\x1aG\n\x17LoginWithAnotherAccount\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a\xcd\x02\n\x12PreviousLoginItems\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1c\n\x14\x65ncrypted_identifier\x18\x03 \x01(\t\x12J\n\x12subscription_badge\x18\x04 \x01(\x0e\x32..widget.PreviousLoginsWidget.SubscriptionBadge\x12Q\n\x0c\x66orget_login\x18\x05 \x01(\x0b\x32;.widget.PreviousLoginsWidget.PreviousLoginItems.ForgetLogin\x12\x1e\n\x07\x61\x63tions\x18\x06 \x01(\x0b\x32\r.base.Actions\x1a\x36\n\x0b\x46orgetLogin\x12\r\n\x05title\x18\x01 \x01(\t\x12\x18\n\x10\x66orget_login_url\x18\x02 \x01(\t\"-\n\x11SubscriptionBadge\x12\x08\n\x04NONE\x10\x00\x12\x0e\n\nSUBSCRIBER\x10\x01J\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.previous_logins_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PREVIOUSLOGINSWIDGET_DATA'].fields_by_name['logo']._loaded_options = None
  _globals['_PREVIOUSLOGINSWIDGET_DATA'].fields_by_name['logo']._serialized_options = b'\030\001'
  _globals['_PREVIOUSLOGINSWIDGET'].fields_by_name['template']._loaded_options = None
  _globals['_PREVIOUSLOGINSWIDGET'].fields_by_name['template']._serialized_options = b'\030\001'
  _globals['_PREVIOUSLOGINSWIDGET']._serialized_start=139
  _globals['_PREVIOUSLOGINSWIDGET']._serialized_end=1036
  _globals['_PREVIOUSLOGINSWIDGET_DATA']._serialized_start=296
  _globals['_PREVIOUSLOGINSWIDGET_DATA']._serialized_end=574
  _globals['_PREVIOUSLOGINSWIDGET_LOGINWITHANOTHERACCOUNT']._serialized_start=576
  _globals['_PREVIOUSLOGINSWIDGET_LOGINWITHANOTHERACCOUNT']._serialized_end=647
  _globals['_PREVIOUSLOGINSWIDGET_PREVIOUSLOGINITEMS']._serialized_start=650
  _globals['_PREVIOUSLOGINSWIDGET_PREVIOUSLOGINITEMS']._serialized_end=983
  _globals['_PREVIOUSLOGINSWIDGET_PREVIOUSLOGINITEMS_FORGETLOGIN']._serialized_start=929
  _globals['_PREVIOUSLOGINSWIDGET_PREVIOUSLOGINITEMS_FORGETLOGIN']._serialized_end=983
  _globals['_PREVIOUSLOGINSWIDGET_SUBSCRIPTIONBADGE']._serialized_start=985
  _globals['_PREVIOUSLOGINSWIDGET_SUBSCRIPTIONBADGE']._serialized_end=1030
# @@protoc_insertion_point(module_scope)
