import requests
import logging

from shared.proxy import Proxy
from scripts.Uber.UberConfig import *


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
                self.send_reuqests()
                break
            except Exception as exc:
                self.error_count+=1
                if self.error_count>5:
                    logging.error((self.email,exc))
                    self.skipped = ((self.email,exc))
                    break
        self.response = (self.result,self.skipped)

    def send_reuqests(self):
        with requests.Session() as s:
            s.proxies.update(Proxy)
            r = s.get(url_first,headers=headers_first,timeout=5)
            token_one = r.headers['x-csrf-token']

            headers_last['x-csrf-token'] = token_one
            payload['answer']['userIdentifier']['email'] = self.email

            r = s.post(url_last,headers=headers_last,json=payload,timeout=5)
            response = str(r.content)

            if "RECAPTCHA" in response:
                self.result = ((self.email,"Registered"))  

#best max_workers - 100(last save was 50)
