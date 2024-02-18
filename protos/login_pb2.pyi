from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class send_otp(_message.Message):
    __slots__ = ["body"]
    class outer_send_otp(_message.Message):
        __slots__ = ["identifier", "phone_num"]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUM_FIELD_NUMBER: _ClassVar[int]
        identifier: str
        phone_num: send_otp.phone
        def __init__(self, identifier: _Optional[str] = ..., phone_num: _Optional[_Union[send_otp.phone, _Mapping]] = ...) -> None: ...
    class phone(_message.Message):
        __slots__ = ["number", "get_by_call"]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        GET_BY_CALL_FIELD_NUMBER: _ClassVar[int]
        number: str
        get_by_call: int
        def __init__(self, number: _Optional[str] = ..., get_by_call: _Optional[int] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    body: send_otp.outer_send_otp
    def __init__(self, body: _Optional[_Union[send_otp.outer_send_otp, _Mapping]] = ...) -> None: ...

class verify_otp(_message.Message):
    __slots__ = ["body"]
    class outer_body(_message.Message):
        __slots__ = ["identifier", "phone_details"]
        class verify_phone(_message.Message):
            __slots__ = ["number", "otp", "device"]
            class device_details(_message.Message):
                __slots__ = ["device_type"]
                DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
                device_type: str
                def __init__(self, device_type: _Optional[str] = ...) -> None: ...
            NUMBER_FIELD_NUMBER: _ClassVar[int]
            OTP_FIELD_NUMBER: _ClassVar[int]
            DEVICE_FIELD_NUMBER: _ClassVar[int]
            number: str
            otp: str
            device: verify_otp.outer_body.verify_phone.device_details
            def __init__(self, number: _Optional[str] = ..., otp: _Optional[str] = ..., device: _Optional[_Union[verify_otp.outer_body.verify_phone.device_details, _Mapping]] = ...) -> None: ...
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        PHONE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        identifier: str
        phone_details: verify_otp.outer_body.verify_phone
        def __init__(self, identifier: _Optional[str] = ..., phone_details: _Optional[_Union[verify_otp.outer_body.verify_phone, _Mapping]] = ...) -> None: ...
    BODY_FIELD_NUMBER: _ClassVar[int]
    body: verify_otp.outer_body
    def __init__(self, body: _Optional[_Union[verify_otp.outer_body, _Mapping]] = ...) -> None: ...
