from selenium import webdriver
import pandas as pd
import time
from selenium import common
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# qs_url = "https://www.topuniversities.com/university-rankings/world-university-rankings/2023"
# browser.get(qs_url)
# browser.maximize_window()

time.sleep(3)

name_lst = []
rank_lst = []
country_lst = []
source_lst = []
student_lst = []

# def get_country(country):
#     if ',' in country.text:
#         return country.text.split(',')[1]
#     else:
#         return country.text
#
# for i in range(1):
#     names = browser.find_elements("xpath", '//*[@id="ranking-data-load"]/div/div/div/div/div[3]/div/div/div[1]/a')
#     names = list(map(lambda x: x.text, names))
#     name_lst += names
#
#     ranks = browser.find_elements("xpath", '//*[@id="ranking-data-load"]/div/div/div/div/div[1]')
#     ranks = list(map(lambda x: x.text, ranks))
#     rank_lst += ranks
#
#     countries = browser.find_elements("xpath", '//*[@id="ranking-data-load"]/div/div/div/div/div[3]/div/div/div[2]')
#     countries = list(map(get_country, countries))
#     country_lst += countries
#
#     page_tmp = browser.find_element("xpath", '//*[@id="alt-style-pagination"]')
#     page_num = page_tmp.text.split('\n')
#     next_path = r'//*[@id="alt-style-pagination"]/li/a[@class="page-link next"]'
#     loc_path = r'//*[@id="ranking-data-load"]/div[12]'
#     next_button = browser.find_element("xpath",loc_path)
#     # scroll to specific position.
#     browser.execute_script("arguments[0].scrollIntoView();", next_button)
#     # click the next button
#     browser.find_element("xpath",next_path).click()
#     time.sleep(2)
#
# print(name_lst)
# print(rank_lst)
# print(country_lst)

#      US news rank has bugs #########################################################################################
# us_url = "https://www.usnews.com/education/best-global-universities/rankings"
# browser.get(us_url)
# browser.maximize_window()
# time.sleep(5)

# local_path = r'//*[@id="johns-hopkins-university-162928"]/div/div[1]/p'
# next_path = r'//*[@id="rankings"]/div[3]/button[@class="button__ButtonStyled-sc-1vhaw8r-1 kDQStt pager__ButtonStyled-sc-1i8e93j-1 dypUdv type-secondary size-large"]'
# next_button = browser.find_element("xpath",local_path)
# browser.execute_script("arguments[0].scrollIntoView()",next_button)
# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, next_path))).click()
# time.sleep(3)
# names = browser.find_elements("xpath", '/html/body/main/div[3]/article/div/div[5]/div[1]/div/div/div[2]/ol/li/section/div/div[1]/div[1]/h2/a')
# print(list(map(lambda x: x.text, names)))
############################################################################################################################















# dataframe = pd.DataFrame({'Name':name_lst, 'Rank':rank_lst, 'Country':country_lst,
#                           'Source': [qs_url for i in range(len(country_lst))]})
# dataframe.to_csv('Myoutput.csv',encoding = 'utf_8_sig',index=False)