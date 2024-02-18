# import proto
from loguru import logger
import protos.login_pb2 as login_proto
import blackboxprotobuf


class ProtoHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def get_otp(phone: str) -> bytes:
        otp_body = login_proto.send_otp()
        outer_body = login_proto.send_otp.outer_send_otp()
        phone_body = login_proto.send_otp.phone()

        phone_body.number = phone
        outer_body.identifier = "type.googleapis.com/feature.login.InitiatePhoneLoginRequest"
        outer_body.phone_num.CopyFrom(phone_body)

        otp_body.body.CopyFrom(outer_body)
        return otp_body.SerializeToString()

    @staticmethod
    def verify_otp(phone: str, otp: str) -> bytes:
        verify = login_proto.verify_otp()
        verify_body = login_proto.verify_otp.outer_body()

        verify_phone_body = login_proto.verify_otp.outer_body.verify_phone()
        device_body = login_proto.verify_otp.outer_body.verify_phone.device_details()

        device_body.device_type = "Xiaomi Phone"
        verify_phone_body.number = phone
        verify_phone_body.otp = otp
        verify_phone_body.device.CopyFrom(device_body)

        verify_body.identifier = "type.googleapis.com/feature.login.VerifyPhoneLoginRequest"
        verify_body.phone_details.CopyFrom(verify_phone_body)

        verify.body.CopyFrom(verify_body)

        return verify.SerializeToString()


if __name__ == "__main__":
    logger.error("Please import the module rather than running it!")
