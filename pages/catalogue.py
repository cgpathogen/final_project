from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Catalogue(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.action = ActionChains(self.driver)


    # x-path locators:

    ## filters

    price_filter = ("xpath","(//div[@class='smart-filter-property-name'])[1]")
    left_slider = ("xpath", "//a[@class='bx-ui-slider-handle left']")
    right_slider = ("xpath", "//a[@class='bx-ui-slider-handle right']")

    size_filter = ("xpath","(//div[@class='smart-filter-property-name'])[2]")
    size_2 = ("xpath", "(//span[@class='smart-filter-property-value-text'])[2]")
    size_3 = ("xpath", "(//span[@class='smart-filter-property-value-text'])[3]")

    ## filter buttons

    set_filter_btn = ("xpath", "//input[@id='set_filter']")
    reset_filter_btn = ("xpath", "//input[@id='del_filter']")


    ## smart filter

    smart_filter = ("xpath", "//span[@id='modef']")
    show_results = ("xpath", "//*[@id='modef']/a")
    close_smart_filter = ("xpath", "//span[@class='smart-filter-controls-popup-close far fa-times']")

    ## sort

    sort_btn = ("xpath","(//div[@class='catalog-panel-sort'])[1]")
    sort_options_block = ("xpath", "//div[@class='catalog-panel-sort-items']")
    sort_option = ("xpath", "(//div[@class='catalog-panel-sort-item'])[5]")

    ## items

    item = ("xpath","(//div[@class='catalog-section-item-wrapper'])")
    item_plus = ("xpath", "(//a[@class='intec-ui-part-increment'])")
    item_buy = ("xpath","(//div[@class='intec-ui intec-ui-control-basket-button catalog-section-item-purchase-button catalog-section-item-purchase-button-add intec-cl-background intec-cl-background-light-hover'])")


    ## cart

    cart = ("xpath", "(//div[@class='ns-intec-universe c-sale-basket-small c-sale-basket-small-icons-1'])[1]")
    cart_hover_field = ("xpath", '//*[@id="i-0-intec-universe-sale-basket-small-icons-1-gnX3eXWafXCe"]')
    cart_hover_item_text = ("xpath", "//a[@class='sale-basket-small-product-name intec-cl-text-hover']")
    cart_hover_item_price = ("xpath", "//span[@class='sale-basket-small-product-new-price']")
    cart_hover_go_to_cart_page = ("xpath", "(//a[@class='sale-basket-small-footer-order-button intec-ui intec-ui-control-button intec-ui-mod-block intec-ui-scheme-current intec-ui-size-2'])[1]")


    # getters

    ## filters

    def get_price_filter(self):
        return self.wait.until(EC.element_to_be_clickable(self.price_filter))


    def get_left_slider(self):
        return self.wait.until(EC.visibility_of_element_located(self.left_slider))


    def get_right_slider(self):
        return self.wait.until(EC.visibility_of_element_located(self.right_slider))


    def get_size_filter(self):
        return self.wait.until(EC.element_to_be_clickable(self.size_filter))


    def get_size_2(self):
        return self.wait.until(EC.element_to_be_clickable(self.size_2))


    def get_size_3(self):
        return self.wait.until(EC.element_to_be_clickable(self.size_3))


    ## filter buttons


    def get_set_filter_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.set_filter_btn))


    def get_reset_filter_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.reset_filter_btn))


    ## smart filter


    def get_smart_filter(self):
       return self.wait.until(EC.visibility_of_element_located(self.smart_filter))


    def get_show_results(self):
        return self.wait.until(EC.element_to_be_clickable(self.show_results))


    def get_close_smart_filter(self):
        return self.wait.until(EC.element_to_be_clickable(self.close_smart_filter))


    ## sort


    def get_sort_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.sort_btn))


    def get_sort_options_block(self):
        return self.wait.until(EC.visibility_of_element_located(self.sort_options_block))


    def get_sort_option(self):
        return self.wait.until(EC.element_to_be_clickable(self.sort_option))


    ## itmes

    def get_item(self):
        return self.wait.until(EC.element_to_be_clickable(self.item))


    def get_item_plus(self):
        return self.wait.until(EC.element_to_be_clickable(self.item_plus))


    def get_item_buy(self):
        return self.wait.until(EC.element_to_be_clickable(self.item_buy))


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
        return self.wait.until(EC.element_to_be_clickable(self.get_cart_hover_go_to_cart_page()))


    # actions


    ## filters

    def filter_by_price(self):
        self.get_price_filter().click()
        self.action.drag_and_drop_by_offset(self.get_left_slider(),50,0).perform()
        self.action.drag_and_drop_by_offset(self.get_right_slider(),-80,0).perform()


    def filter_by_size(self):
        self.get_size_filter().click()
        self.get_size_2().click()
        self.get_size_3().click()


    def final_smart_filter(self):
        self.get_show_results().click()


    # methods


    def filter_catalogue(self):
        self.filter_by_price()
        self.final_smart_filter()
        self.filter_by_size()
        self.final_smart_filter()