# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: widget/refreshable_status.proto
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
    'widget/refreshable_status.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.refresh import refresh_info_pb2 as feature_dot_refresh_dot_refresh__info__pb2
from base import actions_pb2 as base_dot_actions__pb2
from base import widget_commons_pb2 as base_dot_widget__commons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fwidget/refreshable_status.proto\x12\x06widget\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\"feature/refresh/refresh_info.proto\x1a\x12\x62\x61se/actions.proto\x1a\x19\x62\x61se/widget_commons.proto\"\x93\x0b\n\x17RefreshableStatusWidget\x12+\n\x0ewidget_commons\x18\x01 \x01(\x0b\x32\x13.base.WidgetCommons\x12\x32\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32$.widget.RefreshableStatusWidget.Data\x1a\xa8\x04\n\x04\x44\x61ta\x12\x32\n\x0crefresh_info\x18\x01 \x01(\x0b\x32\x1c.feature.refresh.RefreshInfo\x12\x34\n\x05title\x18\x04 \x01(\x0b\x32%.widget.RefreshableStatusWidget.Title\x12\x37\n\x07\x64\x65tails\x18\x05 \x03(\x0b\x32&.widget.RefreshableStatusWidget.Detail\x12\x38\n\x0bprimary_cta\x18\x06 \x01(\x0b\x32#.widget.RefreshableStatusWidget.Cta\x12:\n\rsecondary_cta\x18\x07 \x01(\x0b\x32#.widget.RefreshableStatusWidget.Cta\x12\x13\n\x0bis_closable\x18\x08 \x01(\x08\x12-\n\x0fon_load_actions\x18\t \x03(\x0b\x32\x14.base.Actions.Action\x12\x19\n\x11use_force_refresh\x18\n \x01(\x08\x12\x16\n\x0eis_plan_active\x18\x0b \x01(\x08\x12\x1d\n\x15polling_timeout_in_ms\x18\x0c \x01(\x03\x12#\n\x03img\x18\x02 \x01(\x0b\x32\x14.feature.image.ImageH\x00\x12>\n\tanimation\x18\x03 \x01(\x0b\x32).widget.RefreshableStatusWidget.AnimationH\x00\x42\x0c\n\nmedia_item\x1a\x91\x02\n\tAnimation\x12\x10\n\x04type\x18\x01 \x01(\tB\x02\x18\x01\x12O\n\x0e\x61nimation_type\x18\x03 \x01(\x0e\x32\x37.widget.RefreshableStatusWidget.Animation.AnimationType\x12\x0b\n\x03url\x18\x02 \x01(\t\x12I\n\x10\x61nimatation_meta\x18\x04 \x01(\x0b\x32/.widget.RefreshableStatusWidget.AnimatationMeta\"I\n\rAnimationType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07LOADING\x10\x01\x12\x0b\n\x07SUCCESS\x10\x02\x12\r\n\tTRANSFORM\x10\x03\x1a~\n\x0f\x41nimatationMeta\x12&\n\x08\x66rom_img\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12$\n\x06to_img\x18\x02 \x01(\x0b\x32\x14.feature.image.Image\x12\x1d\n\x15\x61nimation_duration_ms\x18\x03 \x01(\x03\x1aR\n\x06\x44\x65tail\x12\x13\n\x0b\x64\x65scription\x18\x01 \x01(\t\x12\x33\n\x05links\x18\x02 \x03(\x0b\x32$.widget.RefreshableStatusWidget.Link\x1a/\n\x04Link\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x1a\x46\n\x03\x43ta\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x11\n\ticon_name\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x1a\x8a\x01\n\x05Title\x12\x0c\n\x04text\x18\x01 \x01(\t\x12=\n\x04type\x18\x02 \x01(\x0e\x32/.widget.RefreshableStatusWidget.Title.TitleType\"4\n\tTitleType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x42O\n\x1b\x63om.hotstar.ui.model.widgetP\x01Z.github.com/hotstar/hs-core-ui-models-go/widgetb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'widget.refreshable_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.hotstar.ui.model.widgetP\001Z.github.com/hotstar/hs-core-ui-models-go/widget'
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATION'].fields_by_name['type']._loaded_options = None
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATION'].fields_by_name['type']._serialized_options = b'\030\001'
  _globals['_REFRESHABLESTATUSWIDGET']._serialized_start=154
  _globals['_REFRESHABLESTATUSWIDGET']._serialized_end=1581
  _globals['_REFRESHABLESTATUSWIDGET_DATA']._serialized_start=279
  _globals['_REFRESHABLESTATUSWIDGET_DATA']._serialized_end=831
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATION']._serialized_start=834
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATION']._serialized_end=1107
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATION_ANIMATIONTYPE']._serialized_start=1034
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATION_ANIMATIONTYPE']._serialized_end=1107
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATATIONMETA']._serialized_start=1109
  _globals['_REFRESHABLESTATUSWIDGET_ANIMATATIONMETA']._serialized_end=1235
  _globals['_REFRESHABLESTATUSWIDGET_DETAIL']._serialized_start=1237
  _globals['_REFRESHABLESTATUSWIDGET_DETAIL']._serialized_end=1319
  _globals['_REFRESHABLESTATUSWIDGET_LINK']._serialized_start=1321
  _globals['_REFRESHABLESTATUSWIDGET_LINK']._serialized_end=1368
  _globals['_REFRESHABLESTATUSWIDGET_CTA']._serialized_start=1370
  _globals['_REFRESHABLESTATUSWIDGET_CTA']._serialized_end=1440
  _globals['_REFRESHABLESTATUSWIDGET_TITLE']._serialized_start=1443
  _globals['_REFRESHABLESTATUSWIDGET_TITLE']._serialized_end=1581
  _globals['_REFRESHABLESTATUSWIDGET_TITLE_TITLETYPE']._serialized_start=1529
  _globals['_REFRESHABLESTATUSWIDGET_TITLE_TITLETYPE']._serialized_end=1581
# @@protoc_insertion_point(module_scope)
