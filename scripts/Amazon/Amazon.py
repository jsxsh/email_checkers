import requests 
import logging

from shared.proxy import Proxy
from scripts.Amazon.AmazonConfig import *


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

            page_html = r.text
            action_token = page_html.split('<input type="hidden" name="appActionToken" value="')[1].split('"')[0]
            openid_return_to = page_html.split('<input type="hidden" name="openid.return_to" value="')[1].split('"')[0]
            prev_rid = page_html.split('<input type="hidden" name="prevRID" value="')[1].split('"')[0]
            workflow_state = page_html.split('<input type="hidden" name="workflowState" value="')[1].split('"')[0]

            payload['email'] = self.email
            payload['appActionToken'] = action_token
            payload['openid.return_to'] = openid_return_to
            payload['prevRID'] = prev_rid
            payload['workflowState'] = workflow_state

            session_id = s.cookies["session-id"]
            url_last_completed = url_last+session_id

            r = s.post(url_last_completed,headers=headers_last,data=payload,timeout=5)

            if "Please Enable Cookies to Continue" in r.text:
                self.result = ((self.email,"Registered"))


#Best max_workers - 40