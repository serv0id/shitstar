import hashlib
import hmac
import json
import secrets
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
        "client_capabilities": '{"package":["dash","hls"],"container":["fmp4","fmp4br","ts"],"ads":["non_ssai","ssai","sgai"],"audio_channel":["stereo"],"encryption":["plain","widevine"],"video_codec":["h264","h265","vp9"],"video_codec_non_secure":["h264","h265","vp9"],"ladder":["phone","tv"],"resolution":["sd","hd","fhd"],"true_resolution":["sd","hd","fhd"],"dynamic_range":["sdr"]}',
        "drm_parameters": '{"widevine_security_level":["HW_SECURE_DECODE","HW_SECURE_ALL"],"hdcp_version":["HDCP_V2_3"]}',
        "subs": "null",
        "login": "UNKNOWN"
    }, headers={
        "X-HS-FP-Info": "MDA3MGYyZTAtZGYxMS00ODhjLThlNmItYjczYmEwNjNhYjIz.BPicufgJ44ZZHXqTv8pNoJXgX2WYShUBEW8vws__IjBu1VBsW5t32-Q0A8EFjVP0Wl7fvAEIDtfDMTqUQHJ5bNIRd9uO6-6mviC7-Axb9ZSwD3VCAclSrxGotyIgcaxpXZSC9w6rijZGqbp8Hr3FkiHZTG6fqCdlVifI0ONKxowYqWKwfL9PqzngxBW4IGLm6k__sMgoPTDTEdUJDM3AgsFd2RIdw4WpU8ydA1OnXiyjlrqIJvNQ0riuqrLILC4UQ4j3oU_-yNwQPO1NRChLMCiQzLsG8Gr35oMPhcxoKur0Rv3M7oJR-PaFVrtwZhnreWtZ3Yyj5ySkkhFFh7qHENQRRj-paiWnaNny4BLhlcWPji1Lb6sZLTdjQAEvXTL38KMiFBcgxkaVgRAFhCiuTVqx4LPQ3oicviTI5LdocPAfGHunCSPwi-nnML_hEAXRlw3GXGZcsmujLeMgrJVwyn05yNJC6RXPWRuYpv4Z00XI7Arm9Ze3mczscGj6EEapvocDMaJ22lHs-_YXBDEFVYti-wxbi6Pm94xksOc5lK7M2ak3tjtYMS1bGr1u94sw8eo4iw260Nd7pffC9-g2S2V_otN6Ep1lDudRkFciZf5V6h3GVsyOpY78QYcNRhSfUUxVN1WIKwzuV_xjKKc2P8H_LRUle51dcxQ0J0cDY1J56vu7xgIkRQOBTDJs7mGP4WpVZh3A7xftZADA2nGIW9kFWiMDruCw7lUVv-5DPV62fOvvdvNA7ovAxhr-ulhcR3T-BdPp3aLsuG2w23ZeL1S2va6pX_XYnViTiqRQzkXlCTQf4EhW7EFxKJBAOQs0V9Rv6Ffp-mdsxvb1U1YvBFaMmHwp-XMBWilf2v6DD63RsmFWeIjGg0EqG8vwlIeMYXqs2b4jFDy-6LMWH1YTsqrBRWVb-Uw7dQtU57lDhu4xeOAUyb78h_T8C4g4m6SNv0LnT4zAvoN1OqH_my7pmD6PQzWy8lNGBAz3MdvcZGHj5JUemyngYSPWF33lyGrRfpC_WFSeqMYbLZ8-46gjjQQPKHS0igkbLs-O8oknkROq_rsQwgas75kXKAEydl0xSdOw3fcPuT7hPIk0N1OwyFSqkQbrqrwYFZHANLp6tebU6vOqgPmc265o-X1NOfxeiQidmS27pr4DIFiANhn1zPmx3JF4YgIHWeSOFYdlw05ashCCDtDO-vqsUiU-4cNnyVgex9lL6ed8JucOjLlycQW6TOftwElBbNdZ_sT6ydcs50L2sr5FkOoLA1Gnj4hitW5LZQUJpY7YqzYllFi5z99711aAfHcLH3M7EdCo0GaM",
        "X-HS-Request-Id": "288fb503-18aa-43ab-9fd8-a2ab69e98cb3",
        'hotstarauth': get_hs_auth()
    }, data=ProtoHelper.get_freshstart(device_id))

    return resp.headers["x-hs-updatedusertoken"]


if __name__ == "__main__":
    logger.error("Please import the module rather than running it!")
