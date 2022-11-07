from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# 启动ChromeDriver服务
driver_service = Service(
    'D:\HKU fintech课程\7033coding\2022 Fall MFIN7033\2022 Fall MFIN7033\chromedriver.exe')  # 括号内填写 驱动路径
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

farfetch_url = "https://www.farfetch.com/hk/shopping/women/clothing-1/items.aspx"
driver.get(farfetch_url)

product_name_lst = []
product_desc_lst = []
original_price_lst = []
discounted_price_lst = []
price_change_lst = []

for i in range(5):
    driver.execute_script("document.body.style.zoom='0.045'")
    time.sleep(3)

    product_names = driver.find_elements("xpath",
                                         '//*[@id="slice-container"]/div[3]/div[2]/div[2]/div/div[1]/ul/li/div/a/div[2]/div[1]/p[1]')
    product_names = list(map(lambda x: x.text, product_names))
    product_name_lst += product_names

    product_descs = driver.find_elements("xpath",
                                         '//*[@id="slice-container"]/div[3]/div[2]/div[2]/div/div[1]/ul/li/div/a/div[2]/div[1]/p[2]')
    product_descs = list(map(lambda x: x.text, product_descs))
    product_desc_lst += product_descs

    original_prices = driver.find_elements("xpath",
                                           '//*[@id="slice-container"]/div[3]/div[2]/div[2]/div/div[1]/ul/li/div/a/div[2]/div[2]/p')
    original_prices = list(map(lambda x: int(x.text[3:].replace(',', '')), original_prices))
    original_price_lst += original_prices

    dis_lst = []
    for i in range(1, len(product_names) + 1):
        try:
            discount = driver.find_element("xpath",
                                           '//*[@id="slice-container"]/div[3]/div[2]/div[2]/div/div[1]/ul/li[{}]/div/a/div[1]/p'.format(
                                               i))
            dis_lst.append((100 - int(discount.text.replace('% off', ''))) * 0.01)
        except:
            dis_lst.append(1)

    original_discount_zip = zip(original_prices, dis_lst)
    discounted_prices = [i * j for i, j in original_discount_zip]
    discounted_price_lst += discounted_prices

    original_discounted_zip = zip(original_prices, discounted_prices)
    price_changes = [i - j for i, j in original_discounted_zip]
    price_change_lst += price_changes

    driver.execute_script("document.body.style.zoom='1'")
    next_path = r'//*[@id="slice-container"]/div[3]/div[2]/div[2]/div/div[2]/div/div[3]/a[@class="ltr-ol0ad9 e9mjthj3"]'
    driver.find_element("xpath", next_path).click()
    time.sleep(3)

dataframe = pd.DataFrame(
    {'Product name': product_name_lst, 'Product Description': product_desc_lst, 'Original Price': original_price_lst,
     'Discounted Price': discounted_price_lst, 'Price Change': price_change_lst})

dataframe.to_csv('Myoutput.csv', encoding='utf_8_sig', index=False)

driver.quit()
driver_service.stop()
