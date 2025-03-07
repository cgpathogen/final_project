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
    main_logo = ("xpath", "//a[@class='widget-container-item widget-container-logotype intec-ui-picture']")
    cookie_accept_alert = ("xpath", "//*[@id='nca-cookiesaccept-line-accept-btn']")


    def click_logo(self):
        self.wait.until(EC.visibility_of_element_located(self.main_logo)).click()
        print("cliked on main logo")


    def accept_cookies(self):
        self.wait.until(EC.visibility_of_element_located(self.cookie_accept_alert)).click()
        print("cookies accepted")

    def go_to_main_url(self):
        self.driver.get(url=self.main_url)


    def get_current_url(self):
        print(f"\nCurrent URL: {self.driver.current_url}")


    def scroll_page(self, amount):
        self.driver.execute_script(f"window.scrollTo(0, {amount})")


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
