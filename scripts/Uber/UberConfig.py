
url_first = "https://auth.uber.com/login/session"
url_last = "https://auth.uber.com/login/handleanswer"

headers_first = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"auth.uber.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
}


headers_last = {
    "Accept":"application/json",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Alt-Used":"auth.uber.com",
    "Content-Type":"application/json",
    "Host":"auth.uber.com",
    "Origin":"https://auth.uber.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0",
    "x-csrf-token":""
}

payload = {
    "answer":{"type":"VERIFY_INPUT_EMAIL",
        "userIdentifier":{"email":""}},
    "init":"true"}

