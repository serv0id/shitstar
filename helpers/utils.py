import hashlib
import hmac
import json
import time
import uuid

import requests
from loguru import logger

import config
from helpers.protohelper import ProtoHelper


def get_hs_auth() -> str:
    """
    Generate the 'hotstarauth' header sent in
    every request.
    :return: string
    """
    start_time = int(time.time())
    expiry_time = start_time + 6000
    auth = f"st={start_time}~exp={expiry_time}~acl=/*"

    auth += "~hmac=" + hmac.new(
        config.HSAUTH_ENCRYPTION_KEY,
        auth.encode(),
        hashlib.sha256
    ).hexdigest()

    return auth


def get_device_id() -> str:
    """
    Generate a random 16-byte device identification
    value. Does not seem to be linked to session.
    :return:
    """
    return str(uuid.uuid4())


def get_creds() -> dict:
    """
    Retrieves credentials from the credfile.
    :return: creds
    """
    with open(config.CREDFILE, 'r') as f:
        return json.load(f)


def dump_creds(creds: dict) -> None:
    """
    Saves credentials to the credfile.
    :param creds:
    :return:
    """
    with open(config.CREDFILE, 'w') as f:
        json.dump(creds, f)


def get_guest_token(session: requests.Session, device_id: str) -> str:
    resp = session.post(url=config.GUEST_URL, params={
        "client_capabilities": config.CLIENT_CAPABILITIES,
        "drm_parameters": config.DRM_CAPABILITIES_WV,
        "subs": "null",
        "login": "UNKNOWN"
    }, headers={
        "X-HS-FP-Info": config.FP_SAMPLE_VALUE,
        'hotstarauth': get_hs_auth()
    }, data=ProtoHelper.get_freshstart(device_id))

    return resp.headers["x-hs-updatedusertoken"]


if __name__ == "__main__":
    logger.error("Please import the module rather than running it!")
