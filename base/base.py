import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10,poll_frequency=1)
        self.action = ActionChains(self.driver)


    main_url = "https://legendbaikal.ru/"
    cookie_accept_alert = ("xpath", "//*[@id='nca-cookiesaccept-line-accept-btn']")


    def accept_ccokies(self):
        self.wait.until(EC.visibility_of_element_located(self.cookie_accept_alert)).click()

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
            return float(f.split(" ")[0])


    def create_txt_name(self, name, index):
        with open(f"names/name_{index}.txt", "w") as file:
            file.write(name)


    def read_name(self,index):
        with open(f"names/name_{index}.txt", "r") as file:
            f = file.read()
            return f
