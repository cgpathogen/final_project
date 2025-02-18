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

    added_cart_item_name = ("xpath","//a[@class='intec-cl-text-hover']")
    added_cart_item_2_name = ("xpath", "(//a[@class='intec-cl-text-hover'])[2]")

    added_cart_item_price = ("xpath", "//div[@class='basket-item-total-value']")
    added_cart_item_price_2 = ("xpath", "(//div[@class='basket-item-total-value'])[2]")

    added_item_count = ("xpath","//input[@class='intec-ui-part-input']")
    added_item_2_count = ("xpath", "//input[@class='intec-ui-part-input']")

    place_order_btn = ("xpath","//button[@class='basket-order-button intec-ui intec-ui-control-button intec-ui-mod-round-2 intec-ui-scheme-current intec-ui-mod-block intec-ui-size-2']")


    # getters

    def get_added_cart_item_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.added_cart_item_name))


    def get_added_cart_item_2_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.added_cart_item_2_name))


    def get_added_cart_item_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.added_cart_item_price))


    def get_added_cart_item_price_2(self):
        return self.wait.until(EC.visibility_of_element_located(self.added_cart_item_price_2))


    def get_added_item_count(self):
        return self.wait.until(EC.element_to_be_clickable(self.added_item_count))


    def get_added_item_2_count(self):
        return self.wait.until(EC.element_to_be_clickable(self.added_item_2_count))


    def get_place_order_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.place_order_btn))

