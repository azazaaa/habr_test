import re
import os
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAIL = os.environ.get("MAIL")
PASSWORD_GIT = os.environ.get("PASSWORD_GIT")
PASSWORD_MAIL = os.environ.get("PASSWORD_MAIL")
TOKEN = os.environ.get("TOKEN")
CHAT_ID = 836801516

name_file = "img.png"
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"

options = Options()
options.add_argument("-headless")
profile = FirefoxProfile()
profile.set_preference("general.useragent.override", my_user_agent)
options.profile = profile
driver = webdriver.Firefox(options=options)

driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://github.com/login")
sleep(3)
driver.find_element(By.ID, "login_field").send_keys(MAIL)
driver.find_element(By.ID, "password").send_keys(PASSWORD_GIT)
driver.find_element(By.NAME, "commit").click()
sleep(5)

if "verified-device" in driver.current_url:

    driver.get("https://account.mail.ru/login")
    sleep(5)
    driver.find_element(By.NAME, "username").send_keys(MAIL)
    sleep(1)
    driver.find_element(By.XPATH, "//button/span").click()
    sleep(5)
    driver.save_screenshot(name_file)
    files = {'photo': open(name_file, 'rb')}
    print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())
    driver.find_element(By.NAME, "password").send_keys(PASSWORD_MAIL)
    sleep(1)
    driver.find_element(By.XPATH, "//span").click()
    sleep(5)
    driver.save_screenshot(name_file)
    files = {'photo': open(name_file, 'rb')}
    print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())
    html = driver.page_source

    with open("text.html", "w") as f:
        f.writelines(html)

    files = {'document': open("text.html", 'rb')}

    print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={CHAT_ID}', files=files).json())
    driver.get("https://e.mail.ru/search/?q_query=GitHub")
    sleep(5)
    driver.find_element(By.XPATH, "//span[2]/div/span/span/span[3]").click()
    sleep(1)
    data = driver.page_source
    code = re.findall(r'Verification code: [\d]+<br>', data)
    code = code[0].split()[-1].replace("<br>", "")
    driver.get("https://github.com/sessions/verified-device")
    sleep(3)
    driver.find_element(By.NAME, "otp").send_keys(code)
    print(code)

driver.get("https://account.habr.com/login/?consumer=career&state=bslogin")
sleep(3)
driver.find_element(By.CSS_SELECTOR, ".socials-buttons__button_github > svg").click()
sleep(5)
driver.save_screenshot(name_file)
files = {'photo': open(name_file, 'rb')}
print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())

driver.close()
