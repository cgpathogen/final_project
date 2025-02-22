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

    added_cart_item_name = ("xpath","(//a[@class='intec-cl-text-hover'])[1]")
    added_cart_item_2_name = ("xpath", "(//a[@class='intec-cl-text-hover'])[2]")

    added_cart_item_price = ("xpath", "(//div[@class='basket-item-total-value'])[1]")
    added_cart_item_price_2 = ("xpath", "(//div[@class='basket-item-total-value'])[2]")

    added_item_count = ("xpath","(//input[@class='intec-ui-part-input'])[1]")
    added_item_2_count = ("xpath", "(//input[@class='intec-ui-part-input'])[2]")

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
        return self.wait.until(EC.visibility_of_element_located(self.added_item_count))


    def get_added_item_2_count(self):
        return self.wait.until(EC.element_to_be_clickable(self.added_item_2_count))


    def get_place_order_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.place_order_btn))


    # actions


    def compare(self):
        float_price_1 = float(self.get_added_cart_item_price().text.split(" ")[0])
        float_price_3 = float(self.get_added_cart_item_price_2().text.split(" ")[0])
        # assert names
        assert self.read_name(1) == self.get_added_cart_item_name().text
        assert self.read_name(2) == self.get_added_cart_item_2_name().text
        # assert prices
        assert self.read_price(1) * 2 == float_price_1 # 1st item price
        assert self.read_price(3) == float_price_3 # 3rd item price
        assert self.read_price(5) == float_price_1 + float_price_3 # total price


    # methods


    def place_order(self):
        self.get_current_url()
        self.compare()
        self.scroll_page_with_500px()
        self.get_place_order_btn().click()
        print("start placing the order")