import hashlib
import hmac
import json
import secrets
import time

from loguru import logger

import config


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
    return secrets.token_bytes(8).hex()


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


if __name__ == "__main__":
    logger.error("Please import the module rather than running it!")
