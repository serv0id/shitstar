# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: v2/langcommons/language_codes.proto
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
    'v2/langcommons/language_codes.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#v2/langcommons/language_codes.proto\x12\x0clang_commons*\x91\x0f\n\rLanguageCodes\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x16\n\tUNDEFINED\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x07\n\x03\x62\x65n\x10\x02\x12\x0b\n\x07\x42\x45NGALI\x10\x02\x12\x07\n\x03\x65ng\x10\x03\x12\x0b\n\x07\x45NGLISH\x10\x03\x12\x07\n\x03mar\x10\x04\x12\x0b\n\x07MARATHI\x10\x04\x12\x07\n\x03tam\x10\x05\x12\t\n\x05TAMIL\x10\x05\x12\x07\n\x03guj\x10\x06\x12\x0c\n\x08GUJARATI\x10\x06\x12\x07\n\x03kan\x10\x07\x12\x0b\n\x07KANNADA\x10\x07\x12\x07\n\x03mal\x10\x08\x12\r\n\tMALAYALAM\x10\x08\x12\x07\n\x03hin\x10\t\x12\t\n\x05HINDI\x10\t\x12\x07\n\x03tel\x10\n\x12\n\n\x06TELUGU\x10\n\x12\x07\n\x03spa\x10w\x12\x0b\n\x07SPANISH\x10w\x12\x08\n\x03\x66ra\x10\x84\x02\x12\x0b\n\x06\x46RENCH\x10\x84\x02\x12\x08\n\x03\x66\x61s\x10\xb3\x02\x12\x0c\n\x07PERSIAN\x10\xb3\x02\x12\x08\n\x03ori\x10\xb6\x02\x12\n\n\x05ORIYA\x10\xb6\x02\x12\x08\n\x03pan\x10\xb7\x02\x12\x0c\n\x07PUNJABI\x10\xb7\x02\x12\x08\n\x03\x62ho\x10\xb8\x02\x12\r\n\x08\x42HOJPURI\x10\xb8\x02\x12\x08\n\x03san\x10\xb9\x02\x12\r\n\x08SANSKRIT\x10\xb9\x02\x12\x08\n\x03tur\x10\xba\x02\x12\x0c\n\x07TURKISH\x10\xba\x02\x12\x08\n\x03mni\x10\xbb\x02\x12\r\n\x08MANIPURI\x10\xbb\x02\x12\x08\n\x03kok\x10\xbc\x02\x12\x0c\n\x07KONKANI\x10\xbc\x02\x12\x08\n\x03raj\x10\xbd\x02\x12\x0f\n\nRAJASTHANI\x10\xbd\x02\x12\x08\n\x03kat\x10\xb8\x07\x12\r\n\x08GEORGIAN\x10\xb8\x07\x12\x08\n\x03\x64ug\x10\xb9\x07\x12\x0b\n\x06\x44UGOUT\x10\xb9\x07\x12\x08\n\x03\x61ra\x10\xbb\x07\x12\x0b\n\x06\x41RABIC\x10\xbb\x07\x12\x08\n\x03\x63mn\x10\xbc\x07\x12\r\n\x08MANDARIN\x10\xbc\x07\x12\x08\n\x03tha\x10\xbd\x07\x12\t\n\x04THAI\x10\xbd\x07\x12\x08\n\x03zho\x10\xbe\x07\x12\x0c\n\x07\x43HINESE\x10\xbe\x07\x12\x08\n\x03ind\x10\xc0\x07\x12\x0f\n\nINDONESIAN\x10\xc0\x07\x12\x08\n\x03msa\x10\xc2\x07\x12\n\n\x05MALAY\x10\xc2\x07\x12\x08\n\x03kor\x10\xc3\x07\x12\x0b\n\x06KOREAN\x10\xc3\x07\x12\x08\n\x03vie\x10\xc4\x07\x12\x0f\n\nVIETNAMESE\x10\xc4\x07\x12\x08\n\x03yue\x10\xc5\x07\x12\x0e\n\tCANTONESE\x10\xc5\x07\x12\x08\n\x03jpn\x10\xc6\x07\x12\r\n\x08JAPANESE\x10\xc6\x07\x12\x08\n\x03nld\x10\xc7\x07\x12\n\n\x05\x44UTCH\x10\xc7\x07\x12\x0b\n\x06\x65ng_GB\x10\xd0\x07\x12\x0f\n\nENGLISH_UK\x10\xd0\x07\x12\x0b\n\x06\x65ng_AU\x10\xd1\x07\x12\x16\n\x11\x45NGLISH_AUSTRALIA\x10\xd1\x07\x12\x08\n\x03heb\x10\xc8\x07\x12\x0b\n\x06HEBREW\x10\xc8\x07\x12\x08\n\x03\x61rb\x10\xc9\x07\x12\x1b\n\x16\x41RABIC_MODERN_STANDARD\x10\xc9\x07\x12\x08\n\x03\x61rz\x10\xca\x07\x12\x1c\n\x17\x41RABIC_CLASSIC_EGYPTIAN\x10\xca\x07\x12\x0b\n\x06\x61rb_EG\x10\xd8\x07\x12\x14\n\x0f\x45GYPTIAN_ARABIC\x10\xd8\x07\x12\x0b\n\x06\x66ra_FR\x10\xcb\x07\x12\x14\n\x0f\x46RENCH_PARISIAN\x10\xcb\x07\x12\x0b\n\x06\x66ra_CA\x10\xd2\x07\x12\x14\n\x0f\x46RENCH_CANADIAN\x10\xd2\x07\x12\x0c\n\x07spa_419\x10\xd5\x07\x12\x1a\n\x15SPANISH_LATIN_AMERICA\x10\xd5\x07\x12\x0b\n\x06spa_ES\x10\xd6\x07\x12\x1f\n\x1aSPANISH_CASTILIAN_EUROPEAN\x10\xd6\x07\x12\x08\n\x03\x64\x65u\x10\xcd\x07\x12\x0b\n\x06GERMAN\x10\xcd\x07\x12\x0b\n\x06\x64\x65u_AT\x10\xd3\x07\x12\x14\n\x0fGERMAN_AUSTRIAN\x10\xd3\x07\x12\x08\n\x03ita\x10\xce\x07\x12\x0c\n\x07ITALIAN\x10\xce\x07\x12\x08\n\x03por\x10\xcf\x07\x12\x0f\n\nPORTUGUESE\x10\xcf\x07\x12\x0b\n\x06por_BR\x10\xd4\x07\x12\x16\n\x11PORTUGUESE_BRAZIL\x10\xd4\x07\x12\x0b\n\x06por_PT\x10\xd7\x07\x12\x18\n\x13PORTUGUESE_EUROPEAN\x10\xd7\x07\x12\x08\n\x03rus\x10\xdb\x07\x12\x0c\n\x07RUSSIAN\x10\xdb\x07\x12\x0b\n\x06\x63mn_TW\x10\xdc\x07\x12\x14\n\x0fMANDARIN_TAIWAN\x10\xdc\x07\x12\x08\n\x03\x65ll\x10\xdd\x07\x12\n\n\x05GREEK\x10\xdd\x07\x12\x08\n\x03nor\x10\xde\x07\x12\x0e\n\tNORWEGIAN\x10\xde\x07\x12\x08\n\x03\x64\x61n\x10\xdf\x07\x12\x0b\n\x06\x44\x41NISH\x10\xdf\x07\x12\x08\n\x03\x66in\x10\xe0\x07\x12\x0c\n\x07\x46INNISH\x10\xe0\x07\x12\x08\n\x03swe\x10\xe1\x07\x12\x0c\n\x07SWEDISH\x10\xe1\x07\x12\x08\n\x03pol\x10\xe2\x07\x12\x0b\n\x06POLISH\x10\xe2\x07\x12\x08\n\x03ron\x10\xe3\x07\x12\r\n\x08ROMANIAN\x10\xe3\x07\x12\x08\n\x03\x63\x65s\x10\xe4\x07\x12\n\n\x05\x43ZECH\x10\xe4\x07\x12\x08\n\x03slk\x10\xe5\x07\x12\x0b\n\x06SLOVAK\x10\xe5\x07\x12\x08\n\x03hun\x10\xe6\x07\x12\x0e\n\tHUNGARIAN\x10\xe6\x07\x12\x0b\n\x06nld_BE\x10\xe7\x07\x12\x0c\n\x07\x46LEMISH\x10\xe7\x07\x12\r\n\x08zho_Hans\x10\xe8\x07\x12\x17\n\x12\x43HINESE_SIMPLIFIED\x10\xe8\x07\x12\r\n\x08zho_Hant\x10\xe9\x07\x12\x18\n\x13\x43HINESE_TRADITIONAL\x10\xe9\x07\x12\x08\n\x03tts\x10\xea\x07\x12\x0f\n\nTHAI_ISARN\x10\xea\x07\x12\x08\n\x03\x63\x61t\x10\xeb\x07\x12\x0c\n\x07\x43\x41TALAN\x10\xeb\x07\x12\x08\n\x03isl\x10\xec\x07\x12\x0e\n\tICELANDIC\x10\xec\x07\x12\x08\n\x03mri\x10\xed\x07\x12\n\n\x05MAORI\x10\xed\x07\x12\x08\n\x03tgl\x10\xee\x07\x12\x0c\n\x07TAGALOG\x10\xee\x07\x12\n\n\x05\x61r_SY\x10\xef\x07\x12\x12\n\rARABIC_SYRIAN\x10\xef\x07\x1a\x02\x10\x01\x42X\n\"com.hotstar.bff.api.v2.langcommonsP\x01Z0github.com/hotstar/hs-core-api-go/v2/langcommonsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v2.langcommons.language_codes_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\"com.hotstar.bff.api.v2.langcommonsP\001Z0github.com/hotstar/hs-core-api-go/v2/langcommons'
  _globals['_LANGUAGECODES']._loaded_options = None
  _globals['_LANGUAGECODES']._serialized_options = b'\020\001'
  _globals['_LANGUAGECODES']._serialized_start=54
  _globals['_LANGUAGECODES']._serialized_end=1991
# @@protoc_insertion_point(module_scope)
