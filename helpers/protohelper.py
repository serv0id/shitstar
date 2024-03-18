from loguru import logger
import protos.login_pb2 as login_proto
import protos.v2.request.start_request_pb2 as start_proto
import protos.widget.login_success_pb2 as success_proto
import protos.v2.response.widget_response_pb2 as widget_response_proto
import protos.v2.widget_pb2 as widget_proto
import protos.pagedata.search_pb2 as search_proto


class ProtoHelper(object):

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
        verify_phone_body.unknown = 1
        verify_phone_body.device.CopyFrom(device_body)

        verify_body.identifier = "type.googleapis.com/feature.login.VerifyPhoneLoginRequest"
        verify_body.phone_details.CopyFrom(verify_phone_body)

        verify.body.CopyFrom(verify_body)

        return verify.SerializeToString()

    @staticmethod
    def get_freshstart(device_id: str) -> bytes:
        freshstart = start_proto.StartRequest()
        freshstart.app_launch_count = 1

        devid = start_proto.StartRequest.DeviceInfo.DeviceId()
        devid.id = device_id
        devid.type = start_proto.StartRequest.DeviceInfo.DeviceIdType.DEVICE_ID

        freshstart.device_info.device_ids.add().CopyFrom(devid)

        freshstart.device_info.device_meta.network_operator = "airtel"  # Sample
        freshstart.device_info.device_meta.os_name = "Android"
        freshstart.device_info.device_meta.os_version = "13"

        return freshstart.SerializeToString()

    @staticmethod
    def parse_success_widget(content: bytes) -> str:
        widget_response = widget_response_proto.WidgetResponse()
        widget_response.ParseFromString(content)

        widget_wrapper = widget_proto.WidgetWrapper()
        widget_wrapper.CopyFrom(widget_response.success.widget_wrapper)

        if widget_wrapper.template == "VerifyOtpWidget":
            logger.error("Wrong OTP Entered!")
            exit()

        login_success = success_proto.LoginSuccessWidget()

        widget_wrapper.widget.Unpack(login_success)

        logger.debug("Successfully logged in!")
        return login_success.data.user_identity

    @staticmethod
    def parse_search_page(content: bytes) -> dict:
        pass



if __name__ == "__main__":
    logger.error("Please import the module rather than running it!")
