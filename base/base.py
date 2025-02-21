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


    def create_txt_price(self, price, index):
        with open(f"prices/price_{index}.txt", "w") as file:
            file.write(price)


    def read_price(self, index):
        with open(f"prices/price_{index}.txt", "r") as file:
            f = file.read()
            print(float(f.split(" ")[0]))
