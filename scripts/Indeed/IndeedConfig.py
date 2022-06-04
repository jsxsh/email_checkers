
headers_main = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    #"Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"secure.indeed.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}

headers_post = {
    "Accept":"*/*",
    #"Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "content-type":"application/x-www-form-urlencoded",
    "Host":"secure.indeed.com",
    "Origin":"https://secure.indeed.com",
    "Referer":"https://secure.indeed.com/auth",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
}

payload = {
    "__email":"",
    "form_tk":"",
    "h-captcha-response":"",
}


url_main = "https://secure.indeed.com/auth"
PostUrl = "https://secure.indeed.com/account/emailvalidation"

