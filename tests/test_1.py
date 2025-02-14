import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pages.main_page import Main_page

def test_launch_browser():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--useragent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.3")
    options.add_argument("--disable-blink-features=AutomationControlled")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options,service=service)

    mp = Main_page(driver)
    mp.authorization()

    time.sleep(3)