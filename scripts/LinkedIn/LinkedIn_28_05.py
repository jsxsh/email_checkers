import requests
from bs4 import BeautifulSoup
import logging

from shared.proxy import Proxy
from scripts.LinkedIn.LinkedInConfig import *


class checker:
    def __init__(self,email):
        self.email = email
        self.error_count = 0
        self.check()

    def check(self):
        self.result = ()
        self.skipped = () 
        while True:
            try:
                with requests.Session() as s:
                    s.proxies.update(Proxy)
                    r = s.get(url_main,headers=headers_main,timeout=5)
                    sIdString = r.text.split('type="hidden" name="sIdString" value="')[1].split('"')[0]
                    pageinstance = r.text.split('<input type="hidden" name="pageInstance" value="')[1].split('"')[0] #check if something
                    csrfToken = s.cookies["JSESSIONID"].replace('"','')
                    loginCsrfParam = s.cookies['bcookie'].replace('"v=2&','').replace('"','')
                    payload["csrfToken"] = csrfToken
                    payload["session_key"] = self.email
                    payload["sIdString"] = sIdString
                    payload["pageInstance"] = pageinstance
                    payload["loginCsrfParam"] = loginCsrfParam
                    r = s.post(PostUrl,headers=headers_post,timeout=5,data=payload)

                    soup = BeautifulSoup(r.text,'html.parser')
                    resp = (soup.select_one('form.login__form').text.replace("\n\n",""))
                    if "s not the right password." in resp:
                        self.result = ((self.email,"Registered"))
                    elif ("Couldn’t find a LinkedIn account associated with this email." in resp) or ("We don't recognize that email." in resp):
                        pass
                    else:
                        raise Exception("Retrying")
                                       
                break
            except Exception as exc:
                self.error_count+=1
                if self.error_count>5:
                    logging.error((self.email,exc))
                    self.skipped = ((self.email,exc))
                    break
        self.response = (self.result,self.skipped)

#best max_workers - 50
