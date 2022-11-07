from selenium import webdriver
from selenium.webdriver.chrome.service import Service

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
driver.get('http://www.baidu.com')

# 关闭
driver.quit()
driver_service.stop()
