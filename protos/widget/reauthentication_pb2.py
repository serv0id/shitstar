# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/reauthentication.proto
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
    'widget/reauthentication.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import actions_pb2 as base_dot_actions__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dwidget/reauthentication.proto\x12\x06widget\x1a\x12\x62\x61se/actions.proto\x1a\x19\x62\x61se/widget_commons.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\xc2\x04\n\x16ReAuthenticationWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x31\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32#.widget.ReAuthenticationWidget.Data\x1a\xf9\x02\n\x04\x44\x61ta\x12*\n\x0cillustration\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x10\n\x08pin_size\x18\x04 \x01(\x05\x12\x36\n\nresend_otp\x18\x05 \x01(\x0b\x32\".widget.ReAuthenticationWidget.CTA\x12;\n\x0fverify_via_call\x18\x06 \x01(\x0b\x32\".widget.ReAuthenticationWidget.CTA\x12\x11\n\ttime_text\x18\x07 \x01(\t\x12\x1d\n\x06submit\x18\x08 \x01(\x0b\x32\r.base.Actions\x12\x15\n\rerror_message\x18\t \x01(\t\x12#\n\x1bresend_disable_duration_sec\x18\n \x01(\x05\x12\x18\n\x10submit_btn_label\x18\x0b \x01(\t\x12\x19\n\x11recaptcha_enabled\x18\x0c \x01(\x08\x1a\x46\n\x03\x43TA\x12\r\n\x05label\x18\x01 \x01(\t\x12\x1d\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\r.base.Actions\x12\x11\n\ticon_name\x18\x03 \x01(\tJ\x04\x08\x02\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.reauthentication_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_REAUTHENTICATIONWIDGET']._serialized_start=116
  _globals['_REAUTHENTICATIONWIDGET']._serialized_end=694
  _globals['_REAUTHENTICATIONWIDGET_DATA']._serialized_start=239
  _globals['_REAUTHENTICATIONWIDGET_DATA']._serialized_end=616
  _globals['_REAUTHENTICATIONWIDGET_CTA']._serialized_start=618
  _globals['_REAUTHENTICATIONWIDGET_CTA']._serialized_end=688
# @@protoc_insertion_point(module_scope)
