from email.mime import base
import requests
from bs4 import BeautifulSoup
import json

from amazoncaptcha import AmazonCaptcha


def solve_captcha():
    HEADERS = ({'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36",
                'Accept-Language': 'fr-CH, fr;q=0.9, en;q=0.8, de;q=0.7, *;q=0.5'})
    
    base_url = 'https://www.amazon.com/errors/validateCaptcha'

    source_code = requests.get(base_url, headers=HEADERS)
    source_content = source_code.content

    soup = BeautifulSoup(source_content, features="lxml")

    captcha_tag = soup.find('img')
    captcha_img = captcha_tag['src']
    print(captcha_img)
    captcha = AmazonCaptcha.fromlink(captcha_img)
    solution = captcha.solve()

    print(solution)
    params = {
        'field-keyword': solution
    }
    r = requests.get(base_url, params=params, headers=HEADERS)
    print(r.status_code)

    
if __name__ == "__main__":
    solve_captcha()