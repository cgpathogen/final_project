import time
from itertools import product

from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Product_Page(Base):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10,poll_frequency=1)
        self.action = ActionChains(self.driver)


    # xpaths:


    cart = ("xpath", "(//div[@class='ns-intec-universe c-sale-basket-small c-sale-basket-small-icons-1'])[1]")
    cart_hover_field = ("xpath", '(//div[@class="sale-basket-small-popup sale-basket-small-popup-basket"])[1]')
    cart_hover_item_text = ("xpath", "(//a[@class='sale-basket-small-product-name intec-cl-text-hover'])[1]")
    cart_hover_item_price = ("xpath", "(//span[@class='sale-basket-small-product-new-price'])[1]")
    cart_hover_go_to_cart_page = ("xpath", "(//a[@class='sale-basket-small-footer-order-button intec-ui intec-ui-control-button intec-ui-mod-block intec-ui-scheme-current intec-ui-size-2'])[1]")
    hover_cart_total_price = ("xpath","//span[@class='sale-basket-small-footer-new-sum']")

    product_name = ("xpath", "//h1[@id='pagetitle']")
    product_price = ("xpath", "//span[@class='catalog-element-price-current-value']")
    add_to_cart_button = ("xpath", "(//div[@class='catalog-element-buy-container'])[2]")


    # getters


    def get_product_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.product_name))


    def get_product_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.product_price))


    def get_add_to_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_to_cart_button))


    ## cart


    def get_cart(self):
        return self.wait.until(EC.element_to_be_clickable(self.cart))


    def get_cart_hover_filed(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_field))


    def get_cart_hover_item_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_item_text))


    def get_cart_hover_item_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_item_price))


    def get_cart_hover_go_to_cart_page(self):
        return self.wait.until(EC.element_to_be_clickable(self.cart_hover_go_to_cart_page))


    def get_hover_cart_total_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.hover_cart_total_price))


    # actions


    def press_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("add to cart button clicked")


    def compare_product_name(self):
        assert self.read_name(1) == self.get_product_name().text


    def fix_product_price(self):
        self.create_txt_price(self.get_product_price().text, 1)


    def pre_cart(self):
        self.action.move_to_element(self.get_cart()).perform()
        self.action.move_to_element(self.get_cart_hover_filed()).perform()
        assert self.read_name(1) == self.get_product_name().text
        print("item's name and name in cart match")
        assert self.read_price(1) == float(self.get_hover_cart_total_price().text.split(" ")[0])
        print("item's price and total price match")
        self.get_cart_hover_go_to_cart_page().click()


    # methods


    def add_product_to_cart(self):
        self.press_add_to_cart_button()
        self.compare_product_name()
        self.fix_product_price()
        self.pre_cart()
        print("product was successfully added to cart")