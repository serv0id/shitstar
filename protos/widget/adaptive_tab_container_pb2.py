# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/adaptive_tab_container.proto
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
    'widget/adaptive_tab_container.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from widget import tab_pb2 as widget_dot_tab__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#widget/adaptive_tab_container.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x10widget/tab.proto\x1a\x12\x62\x61se/actions.proto\"\xba\x02\n\x1a\x41\x64\x61ptiveTabContainerWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x35\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32\'.widget.AdaptiveTabContainerWidget.Data\x1a\xb1\x01\n\x04\x44\x61ta\x12\x36\n\rportrait_tabs\x18\x01 \x03(\x0b\x32\x1f.widget.category_tray.TabWidget\x12\x37\n\x0elandscape_tabs\x18\x02 \x03(\x0b\x32\x1f.widget.category_tray.TabWidget\x12\x38\n\x0fside_sheet_tabs\x18\x03 \x03(\x0b\x32\x1f.widget.category_tray.TabWidgetJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.adaptive_tab_container_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_ADAPTIVETABCONTAINERWIDGET']._serialized_start=113
  _globals['_ADAPTIVETABCONTAINERWIDGET']._serialized_end=427
  _globals['_ADAPTIVETABCONTAINERWIDGET_DATA']._serialized_start=244
  _globals['_ADAPTIVETABCONTAINERWIDGET_DATA']._serialized_end=421
# @@protoc_insertion_point(module_scope)
