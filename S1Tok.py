import requests
import random
import concurrent.futures

url = "https://api22-normal-c-alisg.tiktokv.com/aweme/v1/unique/id/check/"

class S1:
    def __init__(self):
        self.user = "".join(random.choices('qwertyuiopasdfghjklzxcvbnm1234567890_.', k=4))
        self.rticket = "".join(random.choices('1234567890', k=13))
        self.idd = "".join(random.choices('1234567890', k=19))
        self.openudid = "".join(random.choices('poiuytrewqlkjhgfdsamnbvcxz1234567890', k=16))
        self.cdid = "".join(random.choices('poiuytrewqlkjhgfdsamnbvcxz1234567890', k=32))
        self.device_id = "".join(random.choices('1234567890', k=19))
        self.ts = "".join(random.choices('1234567890', k=10))

    def build_params(self):
        return {
            'unique_id': self.user,
            'device_platform': "android",
            'os': "android",
            'ssmix': "a",
            '_rticket': self.rticket,
            'cdid': "63887845-c476-4c98-add4-348103e43b0d",
            'channel': "googleplay",
            'aid': "1233",
            'app_name': "musical_ly",
            'version_code': "370104",
            'version_name': "37.1.4",
            'manifest_version_code': "2023701040",
            'update_version_code': "2023701040",
            'ab_version': "37.1.4",
            'resolution': "720*1448",
            'dpi': "320",
            'device_type': "RMX3269",
            'device_brand': "realme",
            'language': "ar",
            'os_api': "30",
            'os_version': "11",
            'ac': "wifi",
            'is_pad': "0",
            'current_region': "IQ",
            'app_type': "normal",
            'sys_region': "IQ",
            'last_install_time': "1731267102",
            'timezone_name': "Asia/Baghdad",
            'carrier_region_v2': "418",
            'residence': "IQ",
            'app_language': "ar",
            'carrier_region': "IQ",
            'timezone_offset': "10800",
            'host_abi': "arm64-v8a",
            'locale': "ar",
            'ac2': "wifi",
            'uoo': "0",
            'op_region': "IQ",
            'build_number': "37.1.4",
            'region': "IQ",
            'ts': self.ts,
            'iid': self.idd,
            'device_id': self.device_id,
            'openudid': self.openudid
        }

    def build_headers(self):
        return {
            'User-Agent': "com.zhiliaoapp.musically/2023701040 (Linux; U; Android 11; ar_IQ; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:f6248591 2024-09-11 QuicVersion:182d68c8 2024-05-28)",
            'x-tt-pba-enable': "1",
            'sdk-version': "2",
            'x-bd-kmsv': "0",
            'x-tt-dm-status': "login=1;ct=1;rt=1",
            'x-tt-token': 'hh',
            'x-ss-req-ticket': "1731673312933",
            'passport-sdk-version': "6031490",
            'oec-vc-sdk-version': "3.0.4.i18n",
            'x-vc-bdturing-sdk-version': "2.3.8.i18n",
            'x-tt-request-tag': "n=0;nr=011;bg=0",
            'x-tt-store-region': "sa",
            'x-tt-store-region-src': "uid",
            'rpc-persist-pyxis-policy-v-tnc': "1",
            'x-ss-dp': "1233",
            'x-tt-trace-id': "00-2fc5d0411062d2c795a70fc6068e04d1-2fc5d0411062d2c7-01",
            'x-tt-dataflow-id': "671088640",
            'x-argus': "8GG8cUiZhdJ3waaw1jcdi+OjgEAprNCVSYdFXwJWo+5f5zW1UlHVBAYnhIvKD4uonqcjR733Mva8WaTtnc7Uhq4XUrbD434U6eScwdfVlEz+Z0hOfdIXdKpB3BjCWDCLk6DwPOfwrNVtPHetgOV59tFhf2tQmjp5Ato+rPN/+wAyMuIf9LmEDWfNmt0MwbLUDKS6q7W60PhhXQ6OJv5VVmdMCqOVnq3YTAA7a967JU3OvAvDpn/vLL8uwQfTc1E2L3VRAbkHE7VBlnRIdsURCmQv1cxZ+A+b2xvtXCcuhGr2L1jNXs0+NPffUX57+yjAxucouUXVlF8EDzAy0PIY/20LeG9MT5iV6+JmjkXkNj0jls8vcujjKbMNmTbyalOilPASqbWimbSIaXCAjoeShTClt3+sjPlE21Nvm8GZOSXEVh+P/jTwiEK38R99H37MJVrkOmk4xMbagRJw2dbZ4VufDjnPQtPGAgmMl9RrK0knC5p13Rfi51xfC3xxIlUx41JcpPQy8o81KhUC27uEh9Xy390b+YTUJqIj1/UPi3HqDtan5SBCSlwTW0SO871p3tvsRW5uphMMsaVetJFAB1+2bCE0+5ouaP2QhkbRw9/eYfH0hf0Cx1qHPJ4xDa/GRkk=",
            'x-gorgon': "840430901400a6a59259d822df0e8105e63c61d88fcbab57f4c2",
            'x-khronos': "1731673312",
            'x-ladon': "b3BUGicTzZm+MwzG9/tKyp7m0/ucVERF1sty+2zE0LmWXcEl",
            'Cookie': "store-idc=alisg; passport_csrf_token=e69db1526ef16600ddf5f1f9c5521ed9; passport_csrf_token_default=e69db1526ef16600ddf5f1f9c5521ed9; d_ticket=dc685737227407b00177f13de0bc69e63a5e9; multi_sids=7339266198948037633%3A4c2ae6a79aedba615a6c80936e726217; odin_tt=0cb1bd523dc349f1c19b904961d0c5b1ad5598af62b2fffc4cd37f7389153de76363aebd4feeb5e306fa2f815d1bad4b72436d40b578d10bd53d1a2b450dfca995612036d2d788fc38c3c940c3f81806; cmpl_token=AgQQAPO_F-RPsLXkoR6EZp04-LNepgiQ_4QsYNv70A; sid_guard=4c2ae6a79aedba615a6c80936e726217%7C1731673225%7C15552000%7CWed%2C+14-May-2025+12%3A20%3A25+GMT; uid_tt=c6df487f5f296f1cecce5580b32568d6fbd9f415e21fd936b70925f39c588968; uid_tt_ss=c6df487f5f296f1cecce5580b32568d6fbd9f415e21fd936b70925f39c588968"
        }

    def request(self):
        try:
            response = requests.get(url, headers=self.build_headers(), params=self.build_params())
            return response
        except Exception as e:
            print(f"Error making request: {e}")
            return None

# Define a function to handle multiple requests
def send_requests():
    s1_instance = S1()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(s1_instance.request) for _ in range(5)]
        results = [future.result() for future in futures]
        for result in results:
            if result:
                print(result.json())

if __name__ == "__main__":
    send_requests()