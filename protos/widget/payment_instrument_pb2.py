# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/payment_instrument.proto
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
    'widget/payment_instrument.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from base import widget_commons_pb2 as base_dot_widget__commons__pb2
from base import actions_pb2 as base_dot_actions__pb2
from feature.image import image_pb2 as feature_dot_image_dot_image__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwidget/payment_instrument.proto\x12\x06widget\x1a\x19\x62\x61se/widget_commons.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x66\x65\x61ture/image/image.proto\"\xcd\x03\n\x17PaymentInstrumentWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x32\n\x04\x64\x61ta\x18\x0b \x01(\x0b\x32$.widget.PaymentInstrumentWidget.Data\x1a\x8d\x01\n\x04\x44\x61ta\x12\r\n\x05title\x18\x01 \x01(\t\x12>\n\ninstrument\x18\x02 \x01(\x0b\x32*.widget.PaymentInstrumentWidget.Instrument\x12\x36\n\x06\x62utton\x18\x03 \x01(\x0b\x32&.widget.PaymentInstrumentWidget.Button\x1ap\n\nInstrument\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\ticon_name\x18\x02 \x01(\tB\x02\x18\x01\x12\x0e\n\x04icon\x18\x03 \x01(\tH\x00\x12%\n\x05image\x18\x04 \x01(\x0b\x32\x14.feature.image.ImageH\x00\x42\x06\n\x04\x64\x61ta\x1aI\n\x06\x42utton\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\ticon_name\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.ActionsJ\x04\x08\x03\x10\x0b\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.payment_instrument_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_PAYMENTINSTRUMENTWIDGET_INSTRUMENT'].fields_by_name['icon_name']._loaded_options = None
  _globals['_PAYMENTINSTRUMENTWIDGET_INSTRUMENT'].fields_by_name['icon_name']._serialized_options = b'\030\001'
  _globals['_PAYMENTINSTRUMENTWIDGET']._serialized_start=118
  _globals['_PAYMENTINSTRUMENTWIDGET']._serialized_end=579
  _globals['_PAYMENTINSTRUMENTWIDGET_DATA']._serialized_start=243
  _globals['_PAYMENTINSTRUMENTWIDGET_DATA']._serialized_end=384
  _globals['_PAYMENTINSTRUMENTWIDGET_INSTRUMENT']._serialized_start=386
  _globals['_PAYMENTINSTRUMENTWIDGET_INSTRUMENT']._serialized_end=498
  _globals['_PAYMENTINSTRUMENTWIDGET_BUTTON']._serialized_start=500
  _globals['_PAYMENTINSTRUMENTWIDGET_BUTTON']._serialized_end=573
# @@protoc_insertion_point(module_scope)
