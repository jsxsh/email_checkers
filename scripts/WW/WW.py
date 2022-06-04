import requests
import logging

from shared.proxy import Proxy
from scripts.WW.WWConfig import *


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
            s.headers.update(headers_main)
            r = s.post(url_main, json ={'value':self.email},timeout=10,proxies=Proxy)
            response = r.json()
            if "200" in str(r):
                answer = str(response["data"]["loginView"])
                if (answer == "2") or (answer == "4"):
                    self.result = ((self.email,"Registered")) 
            else:
                raise Exception("Response isn't 200")


#best max_workers - 120
