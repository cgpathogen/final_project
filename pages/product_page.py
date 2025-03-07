import time

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
    add_to_cart_button = ("xpath", "catalog-element-buy-container")


    # getters


    def get_product_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.product_name))


    def get_product_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.product_price))


    def get_add_to_cart_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_to_cart_button))


    # actions


    def press_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("add to cart button clicked")