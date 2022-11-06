from selenium import webdriver
import time
from selenium import common
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
qs_url = "https://www.topuniversities.com/university-rankings/world-university-rankings/2023"
browser.get(qs_url)
browser.maximize_window()
# browser.find_element("xpath", '//*[@id="popup-buttons"]/button')
#
# browser.find_element("xpath", '/html/body/div[1]/div/div/header/div[1]/div/div[2]/ul/li[3]/a').click()
# browser.find_element("xpath", '//*[@id="edit-name"]').send_keys('zhc1226995003@gmail.com')
# browser.find_element("xpath", '//*[@id="edit-pass"]').send_keys('a1923371964')
# browser.find_element("xpath", '//*[@id="edit-actions-submit"]').click()
# time.sleep(1)
#
time.sleep(8)

name_lst = []
rank_lst = []
country_lst = []
source_lst = []



for i in range(20):
    ranks = browser.find_elements("xpath", '//*[@id="ranking-data-load"]/div/div/div/div/div[1]')
    ranks = list(map(lambda x: x.text, ranks))
    rank_lst = rank_lst + ranks

    page_tmp = browser.find_element("xpath", '//*[@id="alt-style-pagination"]')
    page_num = page_tmp.text.split('\n')
    print(page_num)
    next_path = r'//*[@id="alt-style-pagination"]/li/a[@class="page-link next"]'


    loc_path = r'//*[@id="ranking-data-load"]/div[12]'
    next_button = browser.find_element("xpath",loc_path)
    # scroll to specific position.
    browser.execute_script("arguments[0].scrollIntoView();", next_button)
    # click the next button
    browser.find_element("xpath",next_path).click()
    time.sleep(2)

print(rank_lst)

