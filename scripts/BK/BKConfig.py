def generate_token():
    import string
    import random

    upper = string.ascii_uppercase
    num = string.digits
    all = upper + num
    token = ""
    for x in range(0,32):
        token += random.choice(all)
        if (len(token) == 8) or (len(token) == 13) or (len(token) == 18) or (len(token) == 23):
            token+= "-"
    return token

def get_time_stamp():
    import datetime
    d = datetime.datetime.now()
    unixtime = datetime.datetime.timestamp(d)*1000
    
    return str(unixtime).replace(".","_")

def generate_payload_token():
    import string
    import random

    lower = string.ascii_lowercase
    num = string.digits
    all = lower + num
    token = ""
    for x in range(0,32):
        token += random.choice(all)
        if (len(token) == 8) or (len(token) == 13) or (len(token) == 18) or (len(token) == 23):
            token+= "-"
    return token


def generate_forter_token():
    import string
    import random

    lower = string.ascii_lowercase
    num = string.digits
    all = lower + num
    token = ""
    for x in range(0,32):
        token += random.choice(all)
    return token


headers_post = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "content-type":"application/json",
    "Host":"use1-prod-bk.rbictg.com",
    "Origin":"https://www.bk.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    "X-Session-Id": "",
    "x-forter-token":"",
    "x-user-datetime": "2022-05-05T23:26:51+03:00",
    "x-lr-session-url": "undefined",
    "x-ui-language": "en",
    "x-ui-region": "US",
    "x-ui-platform": "web"
}

headers_options = {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Access-Control-Request-Headers":"content-type,x-forter-token,x-lr-session-url,x-session-id,x-ui-language,x-ui-platform,x-ui-region,x-user-datetime", #content-type,x-forter-token,x-lr-session-url,x-session-id,x-ui-language,x-ui-platform,x-ui-region,x-user-datetime
    "Access-Control-Request-Method":"POST",
    "Host":"use1-prod-bk.rbictg.com",
    "Origin":"https://www.bk.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
}

payload = {
    "operationName":"CreateOTP",
    "variables":{"input":{"email":"","platform":"web","sessionId":""}},
    "query":"mutation CreateOTP($input: CreateOTPInput!) {\n  createOTP(input: $input) {\n    maxValidateAttempts\n    ttl\n    __typename\n  }\n}\n"}
    
url_main = "https://use1-prod-bk.rbictg.com/graphql"




