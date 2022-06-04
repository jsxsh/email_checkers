import requests 
import logging
import datetime

from shared.proxy import Proxy
from scripts.BK.BKConfig import *


class Checker:
    def __init__(self,email):
        self.email = email
        self.error_count = 0
        self.check()

    def check(self):
        self.result = ()
        self.skipped = () 
        while True:
            try:
                self.send_requests()                
                break
            except Exception as exc:
                self.error_count+=1
                if self.error_count>5:
                    logging.error((self.email,exc))
                    self.skipped = ((self.email,exc))
                    break
        self.response = (self.result,self.skipped)

    def send_requests(self):
        with requests.Session() as s:
            s.proxies.update(Proxy)
            headers_post["x-user-datetime"] = str(datetime.datetime.now().astimezone().replace(microsecond=0).isoformat())
            token = generate_payload_token()
            payload["variables"]["input"]["email"] = self.email
            payload['variables']['input']['sessionId'] = token
            headers_post['X-Session-Id'] = generate_token()
            headers_post['x-forter-token'] = f'{generate_forter_token()}_{get_time_stamp()}_dUAL43_13ck_tt'
            r = s.post(url_main,headers=headers_post,json=payload,timeout=5)
            if "maxValidateAttempts" in str(r.json()):
                self.result = ((self.email,"Registered"))  


#best max_workers - 50

