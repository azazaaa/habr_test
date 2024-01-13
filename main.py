import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep
import re
import sys
import os
value = os.environ.get("MAIL")
test = os.environ.get("TEST")
print(value,test)


# LOGIN = sys.argv[1]
# PASSWORD = sys.argv[2]
TOKEN = sys.argv[1]
# TOKEN = sys.argv[3]

CHAT_ID = 836801516
# name_file = "img.png"
#
options = Options()
options.add_argument("-headless")
driver = webdriver.Firefox(options=options)
#driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://account.mail.ru/login")
sleep(5)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys(value)

driver.save_screenshot("name_file")
files = {'photo': open("name_file", 'rb')}
print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())

#
# driver.get("https://account.mail.ru/login")
# sleep(5)
# driver.find_element(By.XPATH, "//input[@name='username']").send_keys(MAIL)
# driver.find_element(By.XPATH, "//button/span").click()
# sleep(1)
# driver.find_element(By.XPATH, "//input[@name='password']").send_keys(PASSWORD_MAIL)
# driver.find_element(By.XPATH, "//span").click()
# sleep(5)
# driver.get("https://e.mail.ru/search/?q_query=GitHub")
# driver.find_element(By.XPATH, "//span[2]/div/span/span/span[3]").click()
# sleep(1)
# data = driver.page_source
#
# # with open("text.txt") as f:
# #     data = f.read()
#
# code = re.findall(r'Verification code: [\d]+<br>', data)
# code = code[0].split()[-1].replace("<br>", "")
# driver.get("https://github.com/sessions/verified-device")
# print(code)

# with open("text.txt", "w") as f:
#     f.writelines(html)

# driver.get("https://github.com/login")
# sleep(3)
# driver.find_element(By.ID, "login_field").send_keys(LOGIN)
# driver.find_element(By.ID, "password").send_keys(PASSWORD)
# driver.find_element(By.NAME, "commit").click()
# sleep(5)
# if "verified-device" in driver.current_url:
#     driver.get("https://mail.ru/")
#     driver.find_element(By.CSS_SELECTOR, ".resplash-btn_primary").click()
#     driver.find_element(By.NAME, "username").send_keys(MAIL)
#     driver.find_element(By.XPATH, "//button/span").click()
#     driver.find_element(By.NAME, "password").send_keys(PASSWORD_MAIL)
#     driver.find_element(By.XPATH, "//span").click()
#     sleep(5)
#     driver.get("https://e.mail.ru/search/?q_query=GitHub")
#     driver.find_element(By.XPATH, "//span[2]/div/span/span/span[3]").click()
#     sleep(1)
#     html = driver.page_source
#     with open("text.html", "w") as f:
#         f.writelines(html)
# driver.get("https://account.habr.com/login/?consumer=career&state=bslogin")
# sleep(3)
# driver.find_element(By.CSS_SELECTOR, ".socials-buttons__button_github > svg").click()
# sleep(5)
# driver.save_screenshot(name_file)
# files = {'photo': open(name_file, 'rb')}
# print(requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id={CHAT_ID}', files=files).json())
#
# driver.close()
