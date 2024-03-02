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

class fresh_start(_message.Message):
    __slots__ = ["idk", "version", "_"]
    class inner_body(_message.Message):
        __slots__ = []
        class device_id(_message.Message):
            __slots__ = ["_"]
            class inner_device_id(_message.Message):
                __slots__ = ["dev_id"]
                DEV_ID_FIELD_NUMBER: _ClassVar[int]
                dev_id: str
                def __init__(self, dev_id: _Optional[str] = ...) -> None: ...
            __FIELD_NUMBER: _ClassVar[int]
            _: fresh_start.inner_body.device_id.inner_device_id
            def __init__(self, _: _Optional[_Union[fresh_start.inner_body.device_id.inner_device_id, _Mapping]] = ...) -> None: ...
        class device_id_other(_message.Message):
            __slots__ = ["_"]
            class inner_device_id_other(_message.Message):
                __slots__ = ["dev_id_other", "idk"]
                DEV_ID_OTHER_FIELD_NUMBER: _ClassVar[int]
                IDK_FIELD_NUMBER: _ClassVar[int]
                dev_id_other: str
                idk: int
                def __init__(self, dev_id_other: _Optional[str] = ..., idk: _Optional[int] = ...) -> None: ...
            __FIELD_NUMBER: _ClassVar[int]
            _: fresh_start.inner_body.device_id_other.inner_device_id_other
            def __init__(self, _: _Optional[_Union[fresh_start.inner_body.device_id_other.inner_device_id_other, _Mapping]] = ...) -> None: ...
        class sim_details(_message.Message):
            __slots__ = ["_"]
            class inner_sim_details(_message.Message):
                __slots__ = ["isp", "os", "os_version"]
                ISP_FIELD_NUMBER: _ClassVar[int]
                OS_FIELD_NUMBER: _ClassVar[int]
                OS_VERSION_FIELD_NUMBER: _ClassVar[int]
                isp: str
                os: str
                os_version: str
                def __init__(self, isp: _Optional[str] = ..., os: _Optional[str] = ..., os_version: _Optional[str] = ...) -> None: ...
            __FIELD_NUMBER: _ClassVar[int]
            _: fresh_start.inner_body.sim_details.inner_sim_details
            def __init__(self, _: _Optional[_Union[fresh_start.inner_body.sim_details.inner_sim_details, _Mapping]] = ...) -> None: ...
        def __init__(self) -> None: ...
    IDK_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    __FIELD_NUMBER: _ClassVar[int]
    idk: str
    version: int
    _: fresh_start.inner_body
    def __init__(self, idk: _Optional[str] = ..., version: _Optional[int] = ..., _: _Optional[_Union[fresh_start.inner_body, _Mapping]] = ...) -> None: ...
