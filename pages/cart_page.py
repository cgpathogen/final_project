import time

from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Cart_page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.action = ActionChains(self.driver)


    # xpath locators


    place_order_btn = ("xpath","//button[@class='basket-order-button intec-ui intec-ui-control-button intec-ui-mod-round-2 intec-ui-scheme-current intec-ui-mod-block intec-ui-size-2']")


    # getters


    def get_place_order_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.place_order_btn))


    # actions


    def place_order(self):
        self.get_current_url()
        self.scroll_page_with_500px()
        self.get_place_order_btn().click()
        print("start placing the order")