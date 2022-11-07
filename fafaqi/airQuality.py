from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from selenium import common
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# 启动ChromeDriver服务
driver_service = Service('D:\HKU fintech课程\7033coding\2022 Fall MFIN7033\2022 Fall MFIN7033\chromedriver.exe')  # 括号内填写 驱动路径
driver_service.command_line_args()
driver_service.start()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("enable-automation")
# chrome_options.add_argument("--headless")  # 无头模式
# 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-browser-side-navigation")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)
browser = driver


url = "https://www.aqistudy.cn/historydata/"
browser.get(url)
browser.maximize_window()

time.sleep(3)



all_sections = browser.find_elements("xpath", '/html/body/div[3]/div/div[1]/div[2]/div[2]/ul/div[2]/li/a')
print(all_sections)
for i in all_sections:
    print(i.text)

path = '/html/body/div[3]/div/div[1]/div[2]/div[2]/ul[1]/div[2]/li[2]/a'
browser.find_element("xpath", path).click()
time.sleep(60)
year_lst = []
month_lst = []
aqi_lst = []
range_lst = []
air_quality_level_lst = []
pm2_5_lst = []
pm10_lst = []
so2_lst = []
co_lst = []
np2_lst = []
o3_lst = []

year_month = browser.find_elements("xpath", '//*[@id="body"]/div[3]/div[1]/div[1]/table/tbody/tr/td[5]/a')
print(year_month)
for i in year_month:
    print(year_month.text)


browser.quit()
driver_service.stop()