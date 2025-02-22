# Endpoints
OTP_ENDPOINT = "https://apix.hotstar.com/v2/pages/1/spaces/1/widgets/8"
OTP_VERIFY_ENDPOINT = "https://apix.hotstar.com/v2/pages/1/spaces/1/widgets/9"
GUEST_URL = "https://apix.hotstar.com/v2/freshstart"
SEARCH_URL = "https://apix.hotstar.com/v2/pages/search"
WATCH_URL = "https://apix.hotstar.com/v2/pages/watch"

# Misc
USER_AGENT = "Hotstar;in.startv.hotstar/25.01.27.1.11013 (Android/13)"
PROTOBUF_CONTENT_TYPE = "application/x-protobuf"

APP_VALUE = "11013"
APP_VALUE_ID = "c86aad81-d602-46e5-b6a0-6d3891199063"

# edit these values to match your own if needed
HS_CLIENT = ("platform:android;app_id:in.startv.hotstar;app_version:25.01.27.1;os:Android;os_version:13;"
             "schema_version:0.0.1421;brand:Xiaomi;model:Redmi Note 12 4G;carrier:airtel;network_data:NETWORK_TYPE_WIFI")

HS_CLIENT_TARGETING = "ad_id:d5b2ce8c-7552-433e-9aac-ad9503a1c496;user_lat:false;hw_id:43fdd27a0f0eb904"

HS_PLATFORM = "android"

HS_SCHEMA_VERSION = "0.0.1421"

FP_SAMPLE_VALUE = ('MDA3MGYyZTAtZGYxMS00ODhjLThlNmItYjczYmEwNjNhYjIz.BPicufgJ44ZZHXqTv8pNoJXgX2WYShUBEW8vws'
                   '__IjBu1VBsW5t32-Q0A8EFjVP0Wl7fvAEIDtfDMTqUQHJ5bNIRd9uO6-6mviC7-Axb9ZSwD3VCAclSrxGotyIgc'
                   'axpXZSC9w6rijZGqbp8Hr3FkiHZTG6fqCdlVifI0ONKxowYqWKwfL9PqzngxBW4IGLm6k__sMgoPTDTEdUJDM3A'
                   'gsFd2RIdw4WpU8ydA1OnXiyjlrqIJvNQ0riuqrLILC4UQ4j3oU_-yNwQPO1NRChLMCiQzLsG8Gr35oMPhcxoKur'
                   '0Rv3M7oJR-PaFVrtwZhnreWtZ3Yyj5ySkkhFFh7qHENQRRj-paiWnaNny4BLhlcWPji1Lb6sZLTdjQAEvXTL38K'
                   'MiFBcgxkaVgRAFhCiuTVqx4LPQ3oicviTI5LdocPAfGHunCSPwi-nnML_hEAXRlw3GXGZcsmujLeMgrJVwyn05y'
                   'NJC6RXPWRuYpv4Z00XI7Arm9Ze3mczscGj6EEapvocDMaJ22lHs-_YXBDEFVYti-wxbi6Pm94xksOc5lK7M2ak3'
                   'tjtYMS1bGr1u94sw8eo4iw260Nd7pffC9-g2S2V_otN6Ep1lDudRkFciZf5V6h3GVsyOpY78QYcNRhSfUUxVN1W'
                   'IKwzuV_xjKKc2P8H_LRUle51dcxQ0J0cDY1J56vu7xgIkRQOBTDJs7mGP4WpVZh3A7xftZADA2nGIW9kFWiMDru'
                   'Cw7lUVv-5DPV62fOvvdvNA7ovAxhr-ulhcR3T-BdPp3aLsuG2w23ZeL1S2va6pX_XYnViTiqRQzkXlCTQf4EhW7'
                   'EFxKJBAOQs0V9Rv6Ffp-mdsxvb1U1YvBFaMmHwp-XMBWilf2v6DD63RsmFWeIjGg0EqG8vwlIeMYXqs2b4jFDy-'
                   '6LMWH1YTsqrBRWVb-Uw7dQtU57lDhu4xeOAUyb78h_T8C4g4m6SNv0LnT4zAvoN1OqH_my7pmD6PQzWy8lNGBAz'
                   '3MdvcZGHj5JUemyngYSPWF33lyGrRfpC_WFSeqMYbLZ8-46gjjQQPKHS0igkbLs-O8oknkROq_rsQwgas75kXKA'
                   'Eydl0xSdOw3fcPuT7hPIk0N1OwyFSqkQbrqrwYFZHANLp6tebU6vOqgPmc265o-X1NOfxeiQidmS27pr4DIFiAN'
                   'hn1zPmx3JF4YgIHWeSOFYdlw05ashCCDtDO-vqsUiU-4cNnyVgex9lL6ed8JucOjLlycQW6TOftwElBbNdZ_sT6'
                   'ydcs50L2sr5FkOoLA1Gnj4hitW5LZQUJpY7YqzYllFi5z99711aAfHcLH3M7EdCo0GaM')


CLIENT_CAPABILITIES = ('{"package": ["dash", "hls"], "container": ["fmp4", "fmp4br", "ts"],'
                       '"ads": ["non_ssai", "ssai"], "audio_channel": ["stereo","dolby51","atmos"],'
                       '"encryption": ["plain", "widevine"], "video_codec": ["h265"],'
                       '"ladder": ["tv"],'
                       '"resolution": ["sd", "hd", "fhd", "4k"], "true_resolution": ["sd", "hd", "fhd", "4k"],'
                       '"dynamic_range": ["hdr10"]}')

DRM_CAPABILITIES_WV = ('{"widevine_security_level": ["HW_SECURE_DECODE", "HW_SECURE_ALL"],'
                       '"hdcp_version": ["HDCP_V2_3"]}')  # Google Widevine

DRM_CAPABILITIES_PR = ('{"playready_security_level": ["HW_SECURE_DECODE", "HW_SECURE_ALL"],'
                       '"hdcp_version": ["HDCP_V2_3"]}')  # Microsoft PlayReady

DRM_CAPABILITIES_FP = {}  # Apple Fairplay

# Secrets
HSAUTH_ENCRYPTION_KEY = b"\x05\xfc\x1a\x01\xca\xc9\x4b\xc4\x12\xfc\x53\x12\x07\x75\xf9\xee"

# Paths
CREDFILE = "token.json"
