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
