from selenium import webdriver
import time
from bs4 import BeautifulSoup

def login_website(account, password):
    s = requests.Session()
    payload = {
        'login': str(account),
        'password': str(password),
    }
    header = {
        "x-october-request-handler": "onSignin",
        "x-requested-with": "XMLHttpRequest"
    }
    try:
        s.post("http://applecity.ge/login", data=payload, headers=header, allow_redirects=False)
        info = s.get("http://applecity.ge/profile")
        soup = BeautifulSoup(info.content, "html.parser")
        div = soup.find_all("input", {"id": "accountName"})
        information = div[0].get("value")
        return information
    except:
        return False

def login_website_selenium(email, password, show_browser=False):
    if not show_browser:  
        from selenium.webdriver.chrome.options import Options
        options_ = Options()
        options_.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=options_)
    else:
        browser = webdriver.Chrome()

    browser.get(r"http://applecity.ge/login")
    username_field = browser.find_element_by_xpath(r'//*[@id="userSigninLogin"]')
    password_field = browser.find_element_by_xpath(r'//*[@id="userSigninPassword"]')
    username_field.send_keys(email)
    password_field.send_keys(password)
    try:
        browser.find_element_by_xpath('//button[text()="ავტორიზაცია"]').click()
        time.sleep(1)
        browser.get(r"http://applecity.ge/profile")
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        div = soup.find_all("input", {"id": "accountName"})
        information = div[0].get("value")
        return information
    except:
        return False
