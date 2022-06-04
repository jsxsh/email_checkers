import requests
import logging

from shared.proxy import Proxy
from scripts.Loopnet.LoopnetConfig import *


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
            r = s.get(url_first,headers=headers_first,timeout=5)

            csrf = r.text.split("csrfTokenValue: '")[1].split("'")[0]
            headers_last['RequestVerificationToken'] = csrf
            r = s.get(url_last+self.email,headers=headers_last,timeout=5)
            
            logging.info((self.email,r,r.content))








