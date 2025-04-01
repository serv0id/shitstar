import sys
import time
import uuid
import re
import json

import requests
from loguru import logger
import click
from typing import Any
from tabulate import tabulate

import config
import creds
from helpers import utils
from helpers.protohelper import ProtoHelper

NoneType = type(None)


class ShitStar(object):
    def __init__(self, title_id, refresh, search, manifest):
        """
        Initialise the ShitStar class
        :param title_id:
        :param refresh:
        :param search:
        :param manifest:
        """
        self.session = requests.Session()

        self.title_id = title_id
        self.refresh = refresh
        self.search = search
        self.manifest_type = manifest

        if not ((self.title_id is not None) ^ (self.search is not None)):
            logger.error("Please specify only either a Title ID or a search parameter!")
            exit(0)

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
        self.user_token = utils.get_creds().get('user_token')

        self.session.headers.update({
            "X-HS-Usertoken": self.user_token
        })

        if self.title_id is not None:
            self.get_manifest()
        else:
            self.search_title()

    def set_auth(self) -> None:
        """
        Sets authentication credentials. If not cached,
        logs in to the service.
        :return: None
        """
        if self.refresh:
            logger.debug("Refreshing token")
            utils.dump_creds(self.login())

        logger.info("Attempting to load credentials")

        credict = utils.get_creds()

        if not credict.get("user_token"):
            logger.error("Invalid credentials! Attempting to log in")
            utils.dump_creds(self.login())
            logger.info(f"Saved token to {config.CREDFILE}")

    def login(self) -> dict:
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
            "X-Hs-UserToken": utils.get_guest_token(self.session, self.device_id)
        }, data=ProtoHelper.get_otp(self.mobile_number))

        if "Enter OTP sent to" not in s.text:  # TODO: figure out a way to do proper validation
            logger.error("Some error occurred! Please debug.")
            sys.exit(0)

        s = self.session.post(url=config.OTP_VERIFY_ENDPOINT, params={
            "action": "verifyOtp"
        }, headers={
            "X-HS-Request-Id": str(uuid.uuid4()),
            "hotstarauth": utils.get_hs_auth(),
            "X-Hs-UserToken": utils.get_guest_token(self.session, self.device_id)
        }, data=ProtoHelper.verify_otp(self.mobile_number, input("Enter OTP: ")))

        login_response = ProtoHelper.parse_success_widget(s.content)

        cred_dict = {
            "user_token": login_response,
            "mobile_number": self.mobile_number,
            "time": int(time.time())
        }

        return cred_dict

    def search_title(self) -> None:
        logger.info(f"Searching for the keyword {self.search}!")

        s = self.session.get(url=config.SEARCH_URL, params={
            "search_query": self.search,
        })

        search_res = json.loads(ProtoHelper.parse_search_page(s.content))

        results: list = []

        for item in search_res["data"]["items"]:
            results.append({
                "title": item["searchHorizontalContentCard"]["data"]["title"],
                "duration": item["searchHorizontalContentCard"]["data"].get("duration"),
                "title_id": item["searchHorizontalContentCard"]["data"]["actions"]["onClick"][1]["pageNavigation"]["pageSlug"]
            })

        print(tabulate(results))

    def get_manifest(self) -> None:
        logger.info(f"Retrieving manifest for title {self.title_id}!")
        
        s = self.session.get(url=config.WATCH_URL, params={
            "content_id": self.title_id,
            "filters": "content_type=movie",
            "client_capabilities": config.CLIENT_CAPABILITIES,
            "drm_parameters": config.DRM_CAPABILITIES_PR
         }, headers={
            "app_name": "android",
            "hotstarauth": utils.get_hs_auth()
        })

        manifest_res = json.loads(ProtoHelper.parse_manifest(s.content))

        print(manifest_res)

@click.command()
@click.option('-r', '--refresh', is_flag=True, help='Refresh access token')
@click.option('-s', '--search', help='Search for a title')
@click.option('-m', '--manifest', type=click.Choice(['DASH', 'MSS', 'HLS']), required=True, help='Retrieve manifest type')
@click.option('-t', '--title-id', help="ID for the title")
@logger.catch
def main(title_id: str, manifest: str, refresh: bool = False, search: bool = False) -> None:
    logger.info("Welcome to 💩⭐")
    shitstar = ShitStar(title_id, refresh, search, manifest)


if __name__ == "__main__":
    main()
