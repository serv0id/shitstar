# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/notification_settings.proto
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
    'widget/notification_settings.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.consent import consent_type_pb2 as feature_dot_consent_dot_consent__type__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"widget/notification_settings.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\"feature/consent/consent_type.proto\"\x81\x06\n\x1aNotificationSettingsWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x35\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\'.widget.NotificationSettingsWidget.Data\x1a\x90\x03\n\x04\x44\x61ta\x12J\n\x10\x61pp_notification\x18\x01 \x01(\x0b\x32\x30.widget.NotificationSettingsWidget.ToggleSetting\x12J\n\x10sms_notification\x18\x02 \x01(\x0b\x32\x30.widget.NotificationSettingsWidget.ToggleSetting\x12O\n\x15whatsapp_notification\x18\x03 \x01(\x0b\x32\x30.widget.NotificationSettingsWidget.ToggleSetting\x12L\n\x12\x65mail_notification\x18\x04 \x01(\x0b\x32\x30.widget.NotificationSettingsWidget.ToggleSetting\x12Q\n\x17\x63ommercial_notification\x18\x05 \x01(\x0b\x32\x30.widget.NotificationSettingsWidget.ToggleSetting\x1a\xe5\x01\n\rToggleSetting\x12\x11\n\ticon_name\x18\x02 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bis_selected\x18\x05 \x01(\x08\x12\x1e\n\x07\x61\x63tions\x18\x06 \x01(\x0b\x32\r.base.Actions\x12\x35\n\x0fpreference_type\x18\x07 \x01(\x0e\x32\x1c.feature.consent.ConsentType\x12\x1a\n\x12preference_version\x18\x08 \x01(\x03\x12\x15\n\rpreference_id\x18\t \x01(\tJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.notification_settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_NOTIFICATIONSETTINGSWIDGET']._serialized_start=130
  _globals['_NOTIFICATIONSETTINGSWIDGET']._serialized_end=899
  _globals['_NOTIFICATIONSETTINGSWIDGET_DATA']._serialized_start=261
  _globals['_NOTIFICATIONSETTINGSWIDGET_DATA']._serialized_end=661
  _globals['_NOTIFICATIONSETTINGSWIDGET_TOGGLESETTING']._serialized_start=664
  _globals['_NOTIFICATIONSETTINGSWIDGET_TOGGLESETTING']._serialized_end=893
# @@protoc_insertion_point(module_scope)
