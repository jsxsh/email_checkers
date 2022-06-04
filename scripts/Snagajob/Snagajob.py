import requests
import logging

from shared.proxy import Proxy
from scripts.Snagajob.SnagajobConfig import *


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
            url_last_full = url_last+self.email
            r = s.get(url_last_full,headers=headers_last,timeout=5)
            if r.json() == False: #Site returns "True" if email is available
                self.result = ((self.email,"Registered"))   

#best max_workers - 30
