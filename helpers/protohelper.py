from loguru import logger
import protos.login_pb2 as login_proto
import protos.v2.request.start_request_pb2 as start_proto
import protos.widget.login_success_pb2 as success_proto
import protos.v2.response.widget_response_pb2 as widget_response_proto
import protos.v2.response.page_response_pb2 as page_response_proto
import protos.v2.page_pb2 as page_proto
import protos.v2.space_pb2 as space_proto
import protos.v2.widget_pb2 as widget_proto
import protos.widget.grid_pb2 as grid_proto
import google.protobuf.json_format as json_format


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

        dev_id = start_proto.StartRequest.DeviceInfo.DeviceId()
        dev_id.id = device_id
        dev_id.type = start_proto.StartRequest.DeviceInfo.DeviceIdType.DEVICE_ID

        freshstart.device_info.device_ids.add().CopyFrom(dev_id)

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
        page_response = page_response_proto.PageResponse()
        page_response.ParseFromString(content)

        page_wrapper = page_proto.Page()
        page_wrapper.CopyFrom(page_response.success.page)

        space_wrapper = space_proto.Space()
        space_wrapper.CopyFrom(page_wrapper.spaces["results"])

        widget_wrapper = widget_proto.WidgetWrapper()
        widget_wrapper.CopyFrom(space_wrapper.widget_wrappers[0])

        grid_wrapper = grid_proto.GridWidget()
        grid_wrapper.ParseFromString(widget_wrapper.widget.value)

        return json_format.MessageToJson(grid_wrapper)


if __name__ == "__main__":
    logger.error("Please import the module rather than running it!")
