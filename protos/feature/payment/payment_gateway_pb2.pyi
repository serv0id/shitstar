from feature.payment import init_payment_payload_pb2 as _init_payment_payload_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentGateway(_message.Message):
    __slots__ = ["processors"]
    class PaymentProcessor(_message.Message):
        __slots__ = ["meta", "init_payload", "update_instrument_payload"]
        META_FIELD_NUMBER: _ClassVar[int]
        INIT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        UPDATE_INSTRUMENT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
        meta: PaymentGateway.PaymentProcessorMeta
        init_payload: _init_payment_payload_pb2.InitPaymentPayload
        update_instrument_payload: _init_payment_payload_pb2.InitPaymentPayload
        def __init__(self, meta: _Optional[_Union[PaymentGateway.PaymentProcessorMeta, _Mapping]] = ..., init_payload: _Optional[_Union[_init_payment_payload_pb2.InitPaymentPayload, _Mapping]] = ..., update_instrument_payload: _Optional[_Union[_init_payment_payload_pb2.InitPaymentPayload, _Mapping]] = ...) -> None: ...
    class PaymentProcessorMeta(_message.Message):
        __slots__ = ["flow", "imageUrl", "applicationPackageName", "number", "balance", "image", "label", "stringified_app_click_action", "stringified_app_on_load_action", "use_async_init"]
        FLOW_FIELD_NUMBER: _ClassVar[int]
        IMAGEURL_FIELD_NUMBER: _ClassVar[int]
        APPLICATIONPACKAGENAME_FIELD_NUMBER: _ClassVar[int]
        NUMBER_FIELD_NUMBER: _ClassVar[int]
        BALANCE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        STRINGIFIED_APP_CLICK_ACTION_FIELD_NUMBER: _ClassVar[int]
        STRINGIFIED_APP_ON_LOAD_ACTION_FIELD_NUMBER: _ClassVar[int]
        USE_ASYNC_INIT_FIELD_NUMBER: _ClassVar[int]
        flow: str
        imageUrl: str
        applicationPackageName: str
        number: str
        balance: str
        image: _image_pb2.Image
        label: str
        stringified_app_click_action: str
        stringified_app_on_load_action: str
        use_async_init: bool
        def __init__(self, flow: _Optional[str] = ..., imageUrl: _Optional[str] = ..., applicationPackageName: _Optional[str] = ..., number: _Optional[str] = ..., balance: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., label: _Optional[str] = ..., stringified_app_click_action: _Optional[str] = ..., stringified_app_on_load_action: _Optional[str] = ..., use_async_init: bool = ...) -> None: ...
    PROCESSORS_FIELD_NUMBER: _ClassVar[int]
    processors: _containers.RepeatedCompositeFieldContainer[PaymentGateway.PaymentProcessor]
    def __init__(self, processors: _Optional[_Iterable[_Union[PaymentGateway.PaymentProcessor, _Mapping]]] = ...) -> None: ...
