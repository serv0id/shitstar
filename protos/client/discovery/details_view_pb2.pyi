from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetailsView(_message.Message):
    __slots__ = ("details_view_type",)
    class DetailsViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DETAILS_VIEW_TYPE_UNSPECIFIED: _ClassVar[DetailsView.DetailsViewType]
        DETAILS_VIEW_TYPE_VERTICAL_HOVER_CARD: _ClassVar[DetailsView.DetailsViewType]
        DETAILS_VIEW_TYPE_SPOTLIGHT: _ClassVar[DetailsView.DetailsViewType]
    DETAILS_VIEW_TYPE_UNSPECIFIED: DetailsView.DetailsViewType
    DETAILS_VIEW_TYPE_VERTICAL_HOVER_CARD: DetailsView.DetailsViewType
    DETAILS_VIEW_TYPE_SPOTLIGHT: DetailsView.DetailsViewType
    DETAILS_VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    details_view_type: DetailsView.DetailsViewType
    def __init__(self, details_view_type: _Optional[_Union[DetailsView.DetailsViewType, str]] = ...) -> None: ...
