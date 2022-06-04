import requests
import logging
from random import choice

from shared.proxy import Proxy
from scripts.Hulu.HuluConfig import *


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
            r = s.get(url_main,headers=headers_main,timeout=5)
            r = s.get(url_get_csrf,headers=headers_get_csrf,timeout=5)
            csrf = s.cookies['_tcv']
            payload['csrf'] = csrf
            payload['user_email'] = self.email
            payload['password'] = (''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)') for i in range(10)]))
            r = s.post(url_post,headers=headers_post,data=payload,timeout=5)
            if "Hulu is available in the U.S. only" in str(r.json()):
                    self.result = ((self.email,"Registered"))


#best max_workers - 10



