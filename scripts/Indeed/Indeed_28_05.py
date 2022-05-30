import requests
import logging

from shared.proxy import Proxy
from scripts.Indeed.IndeedConfig import *


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
                    page_html = r.text

                    id_payload = page_html.split("var tk = encodeURIComponent('")[1].split("'")[0]
                    payload["__email"] = self.email
                    payload["form_tk"] = id_payload

                    s.cookies.clear()

                    r = s.post(PostUrl,data=payload, headers=headers_post,timeout=5)
                    response = r.json()

                    if response["isEmailInvalid"] == True:
                        raise Exception("EmailInvalid")

                    if (response["isEmailTaken"]==True):
                        self.result = ((self.email,"Registered"))                  
                break
            except Exception as exc:
                self.error_count+=1
                if self.error_count>5:
                    logging.error((self.email,exc))
                    self.skipped = ((self.email,exc))
                    break
        self.response = (self.result,self.skipped)

#best max_workers - 100
