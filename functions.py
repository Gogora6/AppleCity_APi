from selenium import webdriver
import time, requests
from bs4 import BeautifulSoup


class AppleCity:
    def __init__(self):
        self.login_url = r"http://applecity.ge/login"
        self.profile_url = r"http://applecity.ge/profile"

    def login_website(self, account, password):
        s = requests.Session()
        payload = {
            'login': account,
            'password': password,
        }
        header = {
            "x-october-request-handler": "onSignin",
            "x-requested-with": "XMLHttpRequest"
        }
        try:
            s.post(self.login_url, data=payload, headers=header, allow_redirects=False)
            info = s.get(self.profile_url)
            soup = BeautifulSoup(info.content, "html.parser")
            div = soup.find_all("input", {"id": "accountName"})
            information = div[0].get("value")
            return information
        except:
            return False

    def login_website_selenium(self, email, password, show_browser=False):
        if not show_browser:
            from selenium.webdriver.chrome.options import Options
            options_ = Options()
            options_.add_argument("--headless")
            browser = webdriver.Chrome(chrome_options=options_)
        else:
            browser = webdriver.Chrome()

        browser.get(self.login_url)
        username_field = browser.find_element_by_xpath(r'//*[@id="userSigninLogin"]')
        password_field = browser.find_element_by_xpath(r'//*[@id="userSigninPassword"]')
        username_field.send_keys(email)
        password_field.send_keys(password)
        try:
            browser.find_element_by_xpath('//button[text()="ავტორიზაცია"]').click()
            time.sleep(1)
            browser.get(self.profile_url)
            html = browser.page_source
            soup = BeautifulSoup(html, "html.parser")
            div = soup.find_all("input", {"id": "accountName"})
            information = div[0].get("value")
            return information
        except:
            return False
