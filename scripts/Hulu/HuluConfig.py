headers_main = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Host':'www.hulu.com',
    #'Sec-Fetch-Dest':'document',
    #'Sec-Fetch-Mode':'navigate',
    #'Sec-Fetch-Site':'none',
    #'Sec-Fetch-User':'?1',
    #'Sec-GPC':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}

headers_post = {
    'Accept':'application/json',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
    'Host':'auth.hulu.com',
    'Origin':'https://www.hulu.com',
    'Referer':'https://www.hulu.com/welcome',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'Sec-GPC':'1',
    'TE':'trailers',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}

headers_get_csrf = {
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
    'Host':'secure.hulu.com',
    'Origin':'https://www.hulu.com',
    'Referer':'https://www.hulu.com/welcome',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-site',
    'Sec-GPC':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0'
}

url_get_csrf = 'https://secure.hulu.com/api/4.0/generate_csrf_value?for_hoth=true&path=/v3/web/password/authenticate'

url_main = "https://www.hulu.com/welcome"

url_post = "https://auth.hulu.com/v3/web/password/authenticate"

payload = {
    'csrf':'',
    'user_email':'',
    'password':'',
    'use_enterprise_version':'true',
    'recaptcha_type':'web_invisible',
    'rrventerprise':''
}