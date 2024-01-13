import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
import re
import os

MAIL = os.environ.get("MAIL")
PASSWORD_GIT = os.environ.get("PASSWORD_GIT")
PASSWORD_MAIL = os.environ.get("PASSWORD_MAIL")
TOKEN = os.environ.get("TOKEN")
CHAT_ID = 836801516

name_file = "img.png"

options = Options()
options.add_argument("-headless")
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
    driver.save_screenshot(name_file)
    files = {'photo': open(name_file, 'rb')}

    print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())

    driver.get("https://account.mail.ru/login")
    sleep(5)
    driver.find_element(By.XPATH, "//input[@name='username']").send_keys(MAIL)
    driver.find_element(By.XPATH, "//button/span").click()
    sleep(1)
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys(PASSWORD_MAIL)
    driver.find_element(By.XPATH, "//span").click()
    sleep(5)
    driver.get("https://e.mail.ru/search/?q_query=GitHub")
    sleep(3)
    driver.find_element(By.XPATH, "//span[2]/div/span/span/span[3]").click()
    sleep(1)
    data = driver.page_source
    code = re.findall(r'Verification code: [\d]+<br>', data)
    code = code[0].split()[-1].replace("<br>", "")
    driver.get("https://github.com/sessions/verified-device")
    sleep(3)
    driver.find_element(By.NAME, "otp").send_keys(code)
    driver.save_screenshot(name_file)
    files = {'photo': open(name_file, 'rb')}

    print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())
    print(code)
driver.get("https://account.habr.com/login/?consumer=career&state=bslogin")
sleep(3)
driver.find_element(By.CSS_SELECTOR, ".socials-buttons__button_github > svg").click()
sleep(5)
driver.save_screenshot(name_file)
files = {'photo': open(name_file, 'rb')}
print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())

driver.close()
