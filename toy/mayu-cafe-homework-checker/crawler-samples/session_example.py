import requests
from bs4 import BeautifulSoup

naver_login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'

with requests.Session() as session:
    req = session.get(naver_login_url)
    html = req.html
    headers = req.headers
    status_code = req.status_code
    is_ok = req.ok
