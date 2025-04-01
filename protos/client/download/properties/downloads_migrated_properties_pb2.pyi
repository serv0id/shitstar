from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadsMigratedProperties(_message.Message):
    __slots__ = ("from_downloads_db_version", "to_downloads_db_version", "number_of_total_contents", "number_of_successful_contents", "number_of_failed_contents", "number_of_skipped_contents")
    FROM_DOWNLOADS_DB_VERSION_FIELD_NUMBER: _ClassVar[int]
    TO_DOWNLOADS_DB_VERSION_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_TOTAL_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_SUCCESSFUL_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_FAILED_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    NUMBER_OF_SKIPPED_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    from_downloads_db_version: int
    to_downloads_db_version: int
    number_of_total_contents: int
    number_of_successful_contents: int
    number_of_failed_contents: int
    number_of_skipped_contents: int
    def __init__(self, from_downloads_db_version: _Optional[int] = ..., to_downloads_db_version: _Optional[int] = ..., number_of_total_contents: _Optional[int] = ..., number_of_successful_contents: _Optional[int] = ..., number_of_failed_contents: _Optional[int] = ..., number_of_skipped_contents: _Optional[int] = ...) -> None: ...
