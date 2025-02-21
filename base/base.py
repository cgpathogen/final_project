import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10,poll_frequency=1)
        self.action = ActionChains(self.driver)

    main_url = "https://legendbaikal.ru/"

    def go_to_main_url(self):
        self.driver.get(url=self.main_url)


    def get_current_url(self):
        print(f"\nCurrent URL: {self.driver.current_url}")


    def scroll_page_with_500px(self):
        self.driver.execute_script("window.scrollTo(0, 500)")


    def create_txt_price_1(self, price_1):
        with open(f"prices/price_1.txt", "w") as file:
            file.write(price_1)


    def read_price_1(self):
        with open(f"prices/price_1.txt", "r") as file:
            f = file.read()
            print(float(f.split(" ")[0]))