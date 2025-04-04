# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feature/callout_tag/callout_tag.proto
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
    'feature/callout_tag/callout_tag.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from feature.image import image_pb2 as feature_dot_image_dot_image__pb2
from feature.text import text_pb2 as feature_dot_text_dot_text__pb2
from base import actions_pb2 as base_dot_actions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%feature/callout_tag/callout_tag.proto\x12\x13\x66\x65\x61ture.callout_tag\x1a\x19\x66\x65\x61ture/image/image.proto\x1a\x17\x66\x65\x61ture/text/text.proto\x1a\x12\x62\x61se/actions.proto\"\xda\n\n\nCalloutTag\x12\x19\n\x11tag_template_name\x18\x07 \x01(\t\x12\x37\n\x03img\x18\x01 \x01(\x0b\x32(.feature.callout_tag.CalloutTag.ImageTagH\x00\x12\x36\n\x03txt\x18\x02 \x01(\x0b\x32\'.feature.callout_tag.CalloutTag.TextTagH\x00\x12P\n\x10img_txt_vertical\x18\x03 \x01(\x0b\x32\x34.feature.callout_tag.CalloutTag.ImageTextVerticalTagH\x00\x12P\n\x10txt_img_vertical\x18\x04 \x01(\x0b\x32\x34.feature.callout_tag.CalloutTag.TextImageVerticalTagH\x00\x12T\n\x12img_txt_horizontal\x18\x05 \x01(\x0b\x32\x36.feature.callout_tag.CalloutTag.ImageTextHorizontalTagH\x00\x12T\n\x12txt_img_horizontal\x18\x06 \x01(\x0b\x32\x36.feature.callout_tag.CalloutTag.TextImageHorizontalTagH\x00\x1aO\n\x08ImageTag\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x1a\xcf\x01\n\x07TextTag\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x02 \x01(\x0b\x32\r.base.Actions\x12#\n\x07text_v2\x18\x03 \x01(\x0b\x32\x12.feature.text.Text\x12J\n\rtext_tag_type\x18\x04 \x01(\x0e\x32\x33.feature.callout_tag.CalloutTag.TextTag.TextTagType\"%\n\x0bTextTagType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\t\n\x05\x42\x41\x44GE\x10\x01\x1a\x8e\x01\n\x14ImageTextVerticalTag\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x12#\n\x07text_v2\x18\x04 \x01(\x0b\x32\x12.feature.text.Text\x1a\x8e\x01\n\x14TextImageVerticalTag\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x12#\n\x07text_v2\x18\x04 \x01(\x0b\x32\x12.feature.text.Text\x1a\x90\x01\n\x16ImageTextHorizontalTag\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x12#\n\x07text_v2\x18\x04 \x01(\x0b\x32\x12.feature.text.Text\x1a\x90\x01\n\x16TextImageHorizontalTag\x12#\n\x05image\x18\x01 \x01(\x0b\x32\x14.feature.image.Image\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x1e\n\x07\x61\x63tions\x18\x03 \x01(\x0b\x32\r.base.Actions\x12#\n\x07text_v2\x18\x04 \x01(\x0b\x32\x12.feature.text.TextB\x05\n\x03tagB=Z;github.com/hotstar/hs-core-ui-models-go/feature/callout_tagb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feature.callout_tag.callout_tag_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z;github.com/hotstar/hs-core-ui-models-go/feature/callout_tag'
  _globals['_CALLOUTTAG']._serialized_start=135
  _globals['_CALLOUTTAG']._serialized_end=1505
  _globals['_CALLOUTTAG_IMAGETAG']._serialized_start=625
  _globals['_CALLOUTTAG_IMAGETAG']._serialized_end=704
  _globals['_CALLOUTTAG_TEXTTAG']._serialized_start=707
  _globals['_CALLOUTTAG_TEXTTAG']._serialized_end=914
  _globals['_CALLOUTTAG_TEXTTAG_TEXTTAGTYPE']._serialized_start=877
  _globals['_CALLOUTTAG_TEXTTAG_TEXTTAGTYPE']._serialized_end=914
  _globals['_CALLOUTTAG_IMAGETEXTVERTICALTAG']._serialized_start=917
  _globals['_CALLOUTTAG_IMAGETEXTVERTICALTAG']._serialized_end=1059
  _globals['_CALLOUTTAG_TEXTIMAGEVERTICALTAG']._serialized_start=1062
  _globals['_CALLOUTTAG_TEXTIMAGEVERTICALTAG']._serialized_end=1204
  _globals['_CALLOUTTAG_IMAGETEXTHORIZONTALTAG']._serialized_start=1207
  _globals['_CALLOUTTAG_IMAGETEXTHORIZONTALTAG']._serialized_end=1351
  _globals['_CALLOUTTAG_TEXTIMAGEHORIZONTALTAG']._serialized_start=1354
  _globals['_CALLOUTTAG_TEXTIMAGEHORIZONTALTAG']._serialized_end=1498
# @@protoc_insertion_point(module_scope)
