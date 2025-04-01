# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/device_restriction_container.proto
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
    'widget/device_restriction_container.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from widget import hero_pb2 as widget_dot_hero__pb2
from widget import device_manager_pb2 as widget_dot_device__manager__pb2
from widget import mini_banner_pb2 as widget_dot_mini__banner__pb2
from widget import divider_pb2 as widget_dot_divider__pb2
from base import actions_pb2 as base_dot_actions__pb2
from widget import dialog_pb2 as widget_dot_dialog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)widget/device_restriction_container.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x11widget/hero.proto\x1a\x1bwidget/device_manager.proto\x1a\x18widget/mini_banner.proto\x1a\x14widget/divider.proto\x1a\x12\x62\x61se/actions.proto\x1a\x13widget/dialog.proto\"\xe7\x04\n DeviceRestrictionContainerWidget\x12+\n\x0ewidget_commons\x18\x02 \x01(\x0b\x32\x13.base.WidgetCommons\x12;\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32-.widget.DeviceRestrictionContainerWidget.Data\x1a\xbe\x01\n\x04\x44\x61ta\x12H\n\x0b\x62\x61\x63k_button\x18\x01 \x01(\x0b\x32\x33.widget.DeviceRestrictionContainerWidget.BackButton\x12 \n\x04hero\x18\x02 \x01(\x0b\x32\x12.widget.HeroWidget\x12J\n\x0c\x63hild_widget\x18\x03 \x03(\x0b\x32\x34.widget.DeviceRestrictionContainerWidget.ChildWidget\x1a\xaf\x01\n\x0b\x43hildWidget\x12\x35\n\x0e\x64\x65vice_manager\x18\x01 \x01(\x0b\x32\x1b.widget.DeviceManagerWidgetH\x00\x12(\n\x07\x64ivider\x18\x02 \x01(\x0b\x32\x15.widget.DividerWidgetH\x00\x12/\n\x0bmini_banner\x18\x03 \x01(\x0b\x32\x18.widget.MiniBannerWidgetH\x00\x42\x0e\n\x0c\x63hild_widget\x1a`\n\nBackButton\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x12$\n\x06\x64ialog\x18\x03 \x01(\x0b\x32\x14.widget.DialogWidgetJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.device_restriction_container_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET']._serialized_start=218
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET']._serialized_end=833
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET_DATA']._serialized_start=361
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET_DATA']._serialized_end=551
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET_CHILDWIDGET']._serialized_start=554
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET_CHILDWIDGET']._serialized_end=729
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET_BACKBUTTON']._serialized_start=731
  _globals['_DEVICERESTRICTIONCONTAINERWIDGET_BACKBUTTON']._serialized_end=827
# @@protoc_insertion_point(module_scope)
