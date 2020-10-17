# coding:utf-8
import time
import json

# selenium模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 读取信息
import account

driver = webdriver.Chrome()

# 登录
driver.get('http://www.fenqubiao.com/')
driver.find_element_by_xpath("//input[@id='Username']").send_keys(account.username)
driver.find_element_by_xpath("//input[@id='Password']").send_keys(account.password)
time.sleep(2)
driver.find_element_by_xpath("//input[@id='login_button']").click()
time.sleep(5)

# 储存cookies
try:
  cookies = driver.get_cookies()
  jsoncookies = json.dumps(cookies)
  with open('cookies.txt', 'w') as f:
      f.write(jsoncookies)
except:
  print('Store Cookies error!Please try again')
else:
  print('Store Cookies successfully')
driver.quit()