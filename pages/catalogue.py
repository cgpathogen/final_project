import time

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
    smart_filter_amount = ("xpath","//span[@class='smart-filter-controls-popup-text']")
    show_results = ("xpath", "//*[@id='modef']/a")
    close_smart_filter = ("xpath", "//span[@class='smart-filter-controls-popup-close far fa-times']")

    ## sort

    sort_btn = ("xpath","(//div[@class='catalog-panel-sort'])[1]")
    sort_options_block = ("xpath", "//div[@class='catalog-panel-sort-items']")
    sort_option = ("xpath", "(//div[@class='catalog-panel-sort-item'])[5]")


    ## items

    item = ("xpath","(//div[@class='catalog-section-item-wrapper'])[1]")
    item_2 = ("xpath", "(//div[@class='catalog-section-item-wrapper'])[1]")
    item_plus = ("xpath", "(//a[@class='intec-ui-part-increment'])")
    item_2_plus = ("xpath", "(//a[@class='intec-ui-part-increment'])[2]")
    item_buy = ("xpath","(//div[@class='intec-ui intec-ui-control-basket-button catalog-section-item-purchase-button catalog-section-item-purchase-button-add intec-cl-background intec-cl-background-light-hover'])[1]")
    item_2_buy = ("xpath",
                "(//div[@class='intec-ui intec-ui-control-basket-button catalog-section-item-purchase-button catalog-section-item-purchase-button-add intec-cl-background intec-cl-background-light-hover'])[2]")
    item_text = ("xpath", "(//a[@class='section-item-name intec-cl-text-hover'])[1]")
    item_2_text = ("xpath", "(//a[@class='section-item-name intec-cl-text-hover'])[2]")
    item_price = ("xpath", "(//span[@data-role='item.price.discount'])[1]")
    item_2_price = ("xpath", "(//span[@data-role='item.price.discount'])[2]")


    ## cart

    cart = ("xpath", "(//div[@class='ns-intec-universe c-sale-basket-small c-sale-basket-small-icons-1'])[1]")
    cart_hover_field = ("xpath", '(//div[@class="sale-basket-small-popup sale-basket-small-popup-basket"])[1]')
    cart_hover_item_text = ("xpath", "(//a[@class='sale-basket-small-product-name intec-cl-text-hover'])[1]")
    cart_hover_item_price = ("xpath", "(//span[@class='sale-basket-small-product-new-price'])[1]")
    cart_hover_item_text_2 = ("xpath", "(//a[@class='sale-basket-small-product-name intec-cl-text-hover'])[2]")
    cart_hover_item_price_2 = ("xpath", "(//span[@class='sale-basket-small-product-new-price'])[2]")
    cart_hover_go_to_cart_page = ("xpath", "(//a[@class='sale-basket-small-footer-order-button intec-ui intec-ui-control-button intec-ui-mod-block intec-ui-scheme-current intec-ui-size-2'])[1]")
    hover_cart_total_price = ("xpath","//span[@class='sale-basket-small-footer-new-sum']")

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
        return self.wait.until(EC.visibility_of_element_located(self.set_filter_btn))


    def get_reset_filter_btn(self): # optional
        return self.wait.until(EC.element_to_be_clickable(self.reset_filter_btn))


    ## smart filter


    def get_smart_filter(self):
       return self.wait.until(EC.visibility_of_element_located(self.smart_filter))


    def get_smart_filter_amount(self):
        return self.wait.until(EC.visibility_of_element_located(self.smart_filter_amount))


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


    ## items

    def get_item(self):
        return self.wait.until(EC.element_to_be_clickable(self.item))


    def get_item_plus(self):
        return self.wait.until(EC.element_to_be_clickable(self.item_plus))


    def get_item_buy(self):
        return self.wait.until(EC.element_to_be_clickable(self.item_buy))


    def get_item_2(self):
        return self.wait.until(EC.element_to_be_clickable(self.item_2))


    def get_item_2_plus(self):
        return self.wait.until(EC.element_to_be_clickable(self.item_2_plus))


    def get_item_2_buy(self):
        return self.wait.until(EC.element_to_be_clickable(self.item_2_buy))


    def get_item_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_text))


    def get_item_2_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_2_text))


    def get_item_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_price))


    def get_item_2_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_2_price))




    ## cart


    def get_cart(self):
        return self.wait.until(EC.element_to_be_clickable(self.cart))


    def get_cart_hover_filed(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_field))


    def get_cart_hover_item_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_item_text))


    def get_cart_hover_item_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_item_price))


    def get_cart_hover_item_text_2(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_item_text_2))


    def get_cart_hover_item_price_2(self):
        return self.wait.until(EC.visibility_of_element_located(self.cart_hover_item_price_2))


    def get_cart_hover_go_to_cart_page(self):
        return self.wait.until(EC.element_to_be_clickable(self.get_cart_hover_go_to_cart_page()))


    def get_hover_cart_total_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.hover_cart_total_price))


    # actions


    ## filters

    def filter_by_price(self):
        self.get_price_filter().click()
        self.action.drag_and_drop_by_offset(self.get_left_slider(),50,0).perform()
        self.action.drag_and_drop_by_offset(self.get_right_slider(),-80,0).perform()
        print("filtered by price")


    def filter_by_size(self):
        self.get_size_filter().click()
        self.get_size_2().click()
        self.get_size_3().click()
        print("filtered by size")


    def final_smart_filter(self): # optional
        self.get_show_results().click()
        print("smartly filtered")


    ## sort


    def sort_by_ascending(self):
        self.get_sort_btn().click()
        self.wait.until(EC.visibility_of_element_located(self.sort_options_block))
        self.wait.until(EC.element_to_be_clickable(self.sort_option)).click()
        print("sorted by price ascending")



    ## add items to cart


    def add_items_to_cart(self):
        self.action.move_to_element(self.get_item()).click(self.get_item_plus()).click(self.get_item_buy()).perform()
        self.action.move_to_element(self.get_item_2()).click(self.get_item_2_buy()).perform()
        print("items were added to cart")


    ## cart

    def pre_cart(self):
        self.action.move_to_element(self.get_cart()).perform()
        self.action.move_to_element(self.get_cart_hover_filed())

        price_1 = float(self.get_item_price().text.split(" ")[0])*2 # price of item from search results * 2
        price_2 = float(self.get_cart_hover_item_price().text.split(" ")[0]) # price of item from cart pop-up
        price_3 = float(self.get_item_2_price().text.split(" ")[0]) # price of the second item from search results
        price_4 = float(self.get_cart_hover_item_price_2().text.split(" ")[0]) # price of second item from cart pop-up
        price_5 = float(self.get_hover_cart_total_price().text.split(" ")[0]) # total price

        assert self.get_item_text().text == self.get_cart_hover_item_text().text
        assert self.get_item_2_text().text == self.get_cart_hover_item_text_2().text
        assert price_1 == price_2
        assert price_3 == price_4
        assert price_1 + price_3 == price_5
        print("prices match")

    # methods


    def filter_catalogue_and_add_to_cart(self):
        self.get_current_url()
        self.filter_by_price()
        self.get_close_smart_filter().click()
        self.filter_by_size()
        time.sleep(3) # to skip smart filter
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.get_set_filter_btn().click()
        self.sort_by_ascending()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.add_items_to_cart()
        self.pre_cart()