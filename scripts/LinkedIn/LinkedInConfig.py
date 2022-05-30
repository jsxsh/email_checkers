
def generate_pass():
    import string
    import random
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all = lower + upper + num
    passw = ""
    for x in range(0,20):
        passw += random.choice(all)
    return passw

headers_main = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Host":"www.linkedin.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

headers_post = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.5",
    "Content-Type":"application/x-www-form-urlencoded",
    "Host":"www.linkedin.com",
    "Origin":"https://www.linkedin.com",
    "Referer":"https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"
}

payload = {
    "csrfToken":"", #cookie, first request
    "session_key":"", #email
    "ac":"0",
    "sIdString":"", #html, first request
    "parentPageKey":"d_checkpoint_lg_consumerLogin",
    "pageInstance":"", #html, first request, other is static
    "trk":"guest_homepage-basic_nav-header-signin",
    "authUUID":"",
    "session_redirect":"",
    "loginCsrfParam":"", #cookie
    "fp_data":"default",
    "apfc":"", #try empty and not inluce, seems like fingerprints
    "_d":"d",
    "showGoogleOneTapLogin":"true",
    "controlId":"d_checkpoint_lg_consumerLogin-login_submit_button",
    "session_password":generate_pass()
}

url_main = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
PostUrl = "https://www.linkedin.com/checkpoint/lg/login-submit"
