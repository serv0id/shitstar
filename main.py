import sys
import uuid

import requests
from loguru import logger
import click
from typing import Union, Any

import config
import creds
import utils
from protohelper import ProtoHelper

NoneType = type(None)


class ShitStar(object):
    def __init__(self, title_id, refresh):
        self.session = requests.Session()
        self.title_id = title_id
        self.refresh = refresh

        self.device_id = utils.get_device_id()
        self.mobile_number = creds.PHONE_NUMBER
        self.user_token = None

        self.session.headers.update({
            "User-Agent": config.USER_AGENT,
            "Content-Type": config.PROTOBUF_CONTENT_TYPE,
            "app_name": "android",
            "X-Country-Code": "in",
            "X-HS-App": config.APP_VALUE,
            "X-HS-APP-ID": config.APP_VALUE_ID,
            "X-HS-Client": config.HS_CLIENT,
            "X-HS-Client-Targeting": config.HS_CLIENT_TARGETING.format(self.device_id),
            "X-HS-Device-Id": self.device_id,
            "X-HS-Platform": "android",
            "X-HS-Schema-Version": config.HS_SCHEMA_VERSION
        })

        self.set_auth()

    def set_auth(self) -> None:
        """
        Sets authentication credentials. If not cached,
        logs in to the service.
        :return:
        """
        if self.refresh:
            logger.debug("Refreshing token..")
            utils.dump_creds(self.login())

        logger.info("Attempting to load credentials..")
        credict = utils.get_creds()
        if not credict.get("user_token"):
            logger.error("Invalid credentials! Attempting to log in..")
            self.login()

    def login(self) -> Any:
        """
        Logs into Hotstar with phone number
        and OTP.
        :return: credentials
        """
        s = self.session.post(url=config.OTP_ENDPOINT, params={
            "action": "sendOtp"
        }, headers={
            "X-HS-Request-Id": str(uuid.uuid4()),
            "hotstarauth": utils.get_hs_auth(),
            "X-Hs-UserToken": ""
        }, data=ProtoHelper.get_otp(self.mobile_number))

        if "Enter OTP sent to" not in s.text:  # figure out a way to do proper validation
            logger.error("Some error occurred! Please debug.")
            sys.exit(0)

        s = self.session.post(url=config.OTP_VERIFY_ENDPOINT, params={
            "action": "verifyOtp"
        }, headers={
            "X-HS-Request-Id": str(uuid.uuid4()),
            "hotstarauth": utils.get_hs_auth(),
            "X-Hs-UserToken": ""
        }, data=ProtoHelper.verify_otp(self.mobile_number, input("Enter OTP: ")))

        if "LoginSuccessWidget" in s.text:
            logger.info("Logged in successfully! Saving token..")
            # save token
        else:
            logger.error("Invalid OTP! Try again..")
            sys.exit(0)


@click.command()
@click.option('--refresh', is_flag=True, help='Refresh access token')
@click.argument("title_id")
@logger.catch
def main(title_id: str, refresh: bool) -> None:
    logger.info("Welcome to 💩⭐")
    shitstar = ShitStar(title_id, refresh)


if __name__ == "__main__":
    main()
