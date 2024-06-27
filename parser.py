import requests
from bs4 import BeautifulSoup

import time
from datetime import datetime
from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import *
# from twocaptcha import TwoCaptcha

URL = "https://clck.ru/3BXDhp"

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection': 'keep-alive',
    'Host': 'r.onliner.by',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0'
}


def get_html(url):
    html = requests.get(url, headers=HEADERS)
    if html.status_code == 200:
        return html
    else:
        print("Error with getting html!")
        exit()


def get_info(html):
    soup = BeautifulSoup(html, "html.parser")

    slots = soup.find('div', class_="classifieds-bar__item")

    try:
        count = int(slots.get_text().split()[0])
    except:
        print("count is null")
        count = 0
    return count


def selenium_parser():
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    # service = Service(ChromeDriverManager().install())

    driver = None
    page_opened = False
    while not page_opened:
        try:
            driver = webdriver.Chrome(
                # service=service,
                options=options
            )

            driver.get("https://clck.ru/3BXDhp")
            # driver.get("https://r.onliner.by/ak/") # все аренды
            page_opened = True

        except:
            print("\nScrapper stopped, launching again in 30 seconds...")
            time.sleep(30)

    while True:
        driver.refresh()
        time.sleep(20)
        yield get_info(driver.page_source)


# def captcha_solving():
#     driver.get("https://clck.ru/showcaptcha?cc=1&mt=956B0F15598E74B83A80633C91479D0A157AB3815DD35E317FD315D32BA561D682B5F535B7A13C85E0A7508C786E1EA41062AB1F7FD080BD32AF03C167F85231BE00509BE6EADF8BFB4D79CE4B98E613BA4E851E41B7D4E9330960475891344518B6237D5ABC959F26340C91104ECE0C78040C84AB8B17A9B33D75A85E6142B92A9159E9EB2BA838B46B2BCA49395531501229858B659B00A746E05F74BD1AA862CC968148D1EB13362B8A61DA3FC2DF493CFD2B086C15D7E55B1C0374403B4BCE6C47D8AD7BF91C50305D98CEDC9D0E0C645361DD767AC4477F3338ED12&retpath=aHR0cHM6Ly9jbGNrLnJ1LzNCWERocD8%2C_7d2c9cf257e8da43a40651158a5cc1bc&t=2/1719510658/5a688469c07bbcfee7c6950852e9a417&u=43e5ac92-27da5fe0-f45866bb-b6220169&s=08229fad4f2edcc3639dd156dcda06c2")
#     print("solving captcha")
#     solver = TwoCaptcha("2CAPTCHA_API_KEY")
#     response = solver.recaptcha(sitekey='SITE_KEY', url=captcha_page_url)
#     code = response['code']
#     print(f"Successfully solved the Captcha. The solve code is {code}")


