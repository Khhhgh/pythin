import requests

# URL الخاص بـ API
url = (
    'https://api22-normal-c-alisg.tiktokv.com/aweme/v1/user/following/list/'
    '?user_id=6766540108016485382'
    '&sec_user_id=MS4wLjABAAAAc6iBs3MABOnzNWCmq0dsf2PLc_WkzVry9RasyoxqIP8PuazRB5rueM4A8r3eJBvq'
    '&max_time=0&count=40&offset=0&source_type=4&address_book_access=1&live_sort_by=0'
    '&os=android&_rticket=1732136745775&is_pad=0&last_install_time=1732135704&host_abi=arm64-v8a'
    '&ts=1732136746&'
)

# Headers مرتبة
headers = {
    "Host": "api22-normal-c-alisg.tiktokv.com",
    "cookie": "store-idc=alisg; install_id=7439466035134269240; "
              "ttreq=1$ca53de79ab1b9915311337093ffd439ee236f1da; "
              "passport_csrf_token=8203e6746ae331b50a40f78af0479453; "
              "passport_csrf_token_default=8203e6746ae331b50a40f78af0479453; "
              "d_ticket=710d6bd0acae24bb97db754e065581b23a5e9; "
              "multi_sids=7400423753840526342%3A9403995098d4f857af62a84ef4a61030; "
              "odin_tt=837bfe819c1e56addaabcc8eaef2ce17569a2477f80bf25b61c7f895ef81af115bbf9b26ff5c7fa815f3ce485d92d91869e1a4d107c3945b9696c6a5eb5f175e150f89c6e253815d952e3fa4c8ada4af; "
              "cmpl_token=AgQQAPOnF-RPsLaNeJZjNd0_-LNepgiQ_4QsYNsZtA; "
              "sid_guard=9403995098d4f857af62a84ef4a61030%7C1732135722%7C15552000%7CMon%2C+19-May-2025+20%3A48%3A42+GMT; "
              "uid_tt=c6ec874bebb119bd27886bdfa46951472c9bef02ffb31a988a617e556cc45457; "
              "uid_tt_ss=c6ec874bebb119bd27886bdfa46951472c9bef02ffb31a988a617e556cc45457; "
              "sid_tt=9403995098d4f857af62a84ef4a61030; "
              "sessionid=9403995098d4f857af62a84ef4a61030; "
              "sessionid_ss=9403995098d4f857af62a84ef4a61030; "
              "store-country-code=iq; store-country-code-src=uid; "
              "tt-target-idc=useast1a; msToken=vWdloF3Gz2-jDr1lUX7Eb_xNDtRiTE5skfahwoc7tQcV8nuiatVlrks7JwSVKnD0x0ZT3jnMXk8k4G1n0tomVucoJRXit2w_vXgVdfyX5IrXCWnV5lWznSDZTw==",
    "x-tt-pba-enable": "1",
    "sdk-version": "2",
    "x-bd-kmsv": "0",
    "x-tt-dm-status": "login=1;ct=1;rt=1",
    "x-tt-token": "039403995098d4f857af62a84ef4a6103002b2af495646244fc84d62ebb624a4d2516060c59d23b9c59656dae42beffe3d901b35a9dce13ec030490510e8c649df0d58147b96fd43450f700af68463b2e2b15da3e8320c6de6e54c6f68eac5d4dcd6b-CkA3ZjE0YWE2M2U1NWIyMDhmM2Y0MjkwYzJlNGE4MmVlZGQwMGUyNWQ4ZTBlMGJlNWU5M2EzNjY1NWRlNDYzOTAx-2.0.0",
    "x-ss-req-ticket": "1732136745780",
    "passport-sdk-version": "6031490",
    "x-vc-bdturing-sdk-version": "2.3.8.i18n",
    "x-tt-store-region": "iq",
    "x-tt-store-region-src": "uid",
    "rpc-persist-pyxis-policy-v-tnc": "1",
    "x-ss-dp": "1233",
    "x-tt-trace-id": "00-4b653cd31062d2c795a70fc6066604d1-4b653cd31062d2c7-01",
    "user-agent": "com.zhiliaoapp.musically/2023701040 (Linux; U; Android 11; ar_IQ; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:f6248591 2024-09-11 QuicVersion:182d68c8 2024-05-28)",
    "accept-encoding": "gzip, deflate, br",
    "x-argus": "V9XZaDqplqmifAi6Lh0hMpT2Hzl5eN8x58mLKk9X8I+/v+bqPxb8VesjloVYw4WTqiMeJpKDOnO+WBcAnEJ3q4jP82fR89VEH+bRtB7V+wddpR/mfPswj14wWSE2DVtHCyrutwjzrBgTNbAxlD1YCTE/fer3H85jGPF4Bwh0BoRRDDOPK/+F9+3y1sIw0uG78IEGqoKCRzC62D7Kq6gW0CnaI69wBZaVoQNaVwfAI0jmpQqg64bao0lPZTG3aZdZYFmgYOMhsPBG2cEVDNbmR2Fz848cPp8BRQBpuX0mPvU8ddpZqxdVBXmYSV5CmMCX7/y2vQbLmMuUKqKKxPMTO2ExQfPVR0yIfxaj6x2G1ZQTjdCEZbUUck/A2phJBMeT0B98eQHF//L+4gC/uHDq9COCMVIZO02uNaGBg8it2i/oOftzdl3z7QcMPo8+lNd1Z2PJMNSOKlI2w11507mg+vSugZrU50VilQDelJo/kcFqudjNoOg6jU3yCkCgeyWrqyPhCSSz/gUAW0afq459IWbEtuoXlx5gq6VW9Wmy4ixwXS8I/Rz2VICReBwg5d83T3o/qqfOuL2oCCw/Vb3deog5rRwqfje8YJ4H8ZixJMVRyLuDBPDc9U4kkdI0DmcfTMw=",
    "x-gorgon": "8404105b1400ba5ddc0af896727247fc07519c184c1a2aabd14c",
    "x-khronos": "1732136744",
    "x-ladon": "A7ZOYOsd88YEajsqNxWYXt4a6EpItaQRbMfxS7BDA1R91+jj",
    "x-common-params-v2": "ab_version=37.1.4&ac=WIFI&ac2=wifi&aid=1233&app_language=ar&app_name=musical_ly&app_type=normal&build_number=37.1.4&carrier_region=IQ&carrier_region_v2=418&cdid=ce880740-5b25-411d-8b71-ecc64cbd4b74&channel=googleplay&device_brand=realme&device_id=7439466035134269240&device_platform=android&device_type=RMX3269&dpi=270&imsi=418203500000000&is_my_cn=0&locale=ar-IQ&mcc_mnc=41820&manifest_version_code=2023701040&oaid=f911e828-2bd3-f077-fde3-c88ce6db05ec&openudid=23419d9ea97a7779&os=android&os_api=30&os_version=11&package=com.zhiliaoapp.musically&region=IQ&resolution=720*1440&sdk_version=2&sim_region=IQ&storage_region=iq&timezone_offset=10800&ttnet_version=f6248591&update_version_code=2023701040&version_code=370104&version_name=37.1.4"
}

# إرسال الطلب
response = requests.get(url, headers=headers)

# عرض النتيجة
if response.status_code == 200:
    print("البيانات المستلمة:", response.text)
else:
    print("خطأ في الطلب:", response.status_code)