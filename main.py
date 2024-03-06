import sys
import uuid

import requests
from loguru import logger
import click
from typing import Any

import config
import creds
from helpers import utils
from helpers.protohelper import ProtoHelper

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
            "X-Hs-UserToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcHBJZCI6Ijc5ZTQxNTU2LTk3MWYtNDM5ZC1hYmVlLWM3NGZhYmFiM2YwMiIsImF1ZCI6InVtX2FjY2VzcyIsImV4cCI6MTcwOTkzODc2OCwiaWF0IjoxNzA5MzMzOTY4LCJpc3MiOiJUUyIsImp0aSI6IjAzNjlmMjgzZDM2YjQxNTU5MjA0ZGM2YjNlNDY2Y2ZlIiwic3ViIjoie1wiaElkXCI6XCI4N2Q5ZDZlOWJiYjk0NTFiYTcyNDA3Mzk5YTVjNmMxMlwiLFwicElkXCI6XCJmZDdkMWUzNjM3MTA0YjU1OTUyOWFmNTdjNGIyNTFhN1wiLFwibmFtZVwiOlwiWW91XCIsXCJpcFwiOlwiMjQwMTo0OTAwOjFjMmE6OGZmZjo6MTc0OjljYmFcIixcImNvdW50cnlDb2RlXCI6XCJpblwiLFwiY3VzdG9tZXJUeXBlXCI6XCJudVwiLFwidHlwZVwiOlwiZ3Vlc3RcIixcImlzRW1haWxWZXJpZmllZFwiOmZhbHNlLFwiaXNQaG9uZVZlcmlmaWVkXCI6ZmFsc2UsXCJkZXZpY2VJZFwiOlwiZDViMmNlOGMtNzU1Mi00MzNlLTlhYWMtYWQ5NTAzYTFjNDk2XCIsXCJwcm9maWxlXCI6XCJBRFVMVFwiLFwidmVyc2lvblwiOlwidjJcIixcInN1YnNjcmlwdGlvbnNcIjp7XCJpblwiOnt9fSxcImlzc3VlZEF0XCI6MTcwOTMzMzk2ODA1NCxcImRwaWRcIjpcImZkN2QxZTM2MzcxMDRiNTU5NTI5YWY1N2M0YjI1MWE3XCIsXCJzdFwiOjEsXCJkYXRhXCI6XCJDZ1FJQUJJQUNnUUlBQ29BQ2d3SUFDSUlrQUg5Nk1EUHJ6RUtCQWdBT2dBS0JBZ0FNZ0FLTGdnQVFpb0tLRUV6WWpFMFpEUTJPRFJqTURrME1UaGlPV0kxWlRBME9EVmxObVZoTURkaFprRjNXV1pLT1dNPVwifSIsInZlcnNpb24iOiIxXzAifQ.7dMpLk4cg1zTbCKrpmDqMvbZn585xeeS7k3w9iVULEc",
            # utils.get_guest_token(self.session, self.device_id)
        }, data=ProtoHelper.get_otp(self.mobile_number))

        print(s.content)

        if "Enter OTP sent to" not in s.text:  # figure out a way to do proper validation
            logger.error("Some error occurred! Please debug.")
            sys.exit(0)

        s = self.session.post(url=config.OTP_VERIFY_ENDPOINT, params={
            "action": "verifyOtp"
        }, headers={
            "X-HS-Request-Id": str(uuid.uuid4()),
            "hotstarauth": utils.get_hs_auth(),
            "X-Hs-UserToken": ""
        }, data=ProtoHelper.verify_otp(input("Enter OTP: ")))

        login_response = ProtoHelper.parse_success_widget(s.content)
        #
        # else:
        #     logger.error("Invalid OTP! Try again..")
        #     sys.exit(0)


@click.command()
@click.option('--refresh', is_flag=True, help='Refresh access token')
@click.argument("title_id")
@logger.catch
def main(title_id: str, refresh: bool) -> None:
    logger.info("Welcome to 💩⭐")
    shitstar = ShitStar(title_id, refresh)


if __name__ == "__main__":
    main()
