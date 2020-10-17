import requests
from requests.cookies import RequestsCookieJar
s = requests.session()
import json
import xlrd
import xlwt
from xlutils.copy import copy
import math

# selenium模块
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

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

# 尝试读取爬取历史
global index
try:
    with open('./history.txt', 'r') as f:
        index = int(f.readline())
        print(index)
        f.close()
    writebook = copy(xlrd.open_workbook('./Result.xls'))
    writesheet = writebook.get_sheet(-1)  # 获取工作簿中所有表格中的的第一个表格
    print('成功读取历史记录')
    has_his = 1

except:
    print('读取历史记录失败，初始化中')
    index = 0
    # Create a new Excel
    writebook = xlwt.Workbook(encoding='utf-8')
    writesheet = writebook.add_sheet('res')
    has_his = 0


# 登录
driver.get('http://www.fenqubiao.com/')
driver.find_element_by_xpath("//input[@id='Username']").send_keys(account.username)
driver.find_element_by_xpath("//input[@id='Password']").send_keys(account.password)
time.sleep(2)
driver.find_element_by_xpath("//input[@id='login_button']").click()
# time.sleep(10)

url = 'http://www.fenqubiao.com/Core/BatchSearch.aspx'

# 读取表格
workbook = xlrd.open_workbook('./list.xlsx')
sheet = workbook.sheet_by_index(0)

# 写入表格
if not has_his:
  writesheet.write(0,0, label = '序号')
  writesheet.write(0,1, label = '刊名全称')
  writesheet.write(0,2, label = 'ISSN')
  writesheet.write(0,3, label = '所属小类')
  writesheet.write(0,4, label = '2016影响因子')
  writesheet.write(0,5, label = '2017影响因子')
  writesheet.write(0,6, label = '2018影响因子')
  writesheet.write(0,7, label = '平均影响因子')
  writesheet.write(0,8, label = '2017被引次数')
  writesheet.write(0,9, label = '2018被引次数')
  writesheet.write(0,10, label = '两年被引次数')

def getData(_str):
  global index
  driver.get(url)
  driver.find_element_by_xpath("//textarea[@id='ContentPlaceHolder1_tbxSearch']").send_keys(_str)
  time.sleep(0.5)
  driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_btnSearch']").click()
  time.sleep(0.5)
  driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_btnSearch']").click()
  time.sleep(0.5)
  driver.find_element_by_xpath("//input[@id='ContentPlaceHolder1_btnSearch']").click()
  eles = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, "//tbody/tr")))
  for i in range(0, len(eles)):
    index += 1
    paper = driver.find_elements_by_xpath('//tbody/tr')[i].find_elements_by_xpath('./td')
    writesheet.write(index,0, label = index)
    writesheet.write(index,1, label = paper[3].get_attribute("textContent"))
    writesheet.write(index,2, label = paper[4].get_attribute("textContent"))
    writesheet.write(index,3, label = paper[5].get_attribute("textContent"))
    writesheet.write(index,4, label = paper[7].get_attribute("textContent"))
    writesheet.write(index,5, label = paper[8].get_attribute("textContent"))
    writesheet.write(index,6, label = paper[9].get_attribute("textContent"))
    writesheet.write(index,7, label = paper[10].get_attribute("textContent"))
    writesheet.write(index,8, label = paper[11].get_attribute("textContent"))
    writesheet.write(index,9, label = paper[12].get_attribute("textContent"))
    writesheet.write(index,10, label = paper[13].get_attribute("textContent"))
  writebook.save('./Result.xls')
  # 记录爬取历史以便断电继续工作
  fo = open("./history.txt", "w")
  fo.writelines(str(index))
  fo.close()



for i in range(14, math.ceil(len(sheet.col(0))/50)):
  _str = ''
  for j in range(i*50+2, (i+1)*50+2):
    _str += str(sheet.cell_value(j, 0))
    _str += '\n'
  print(i)
  getData(_str)

driver.quit()
