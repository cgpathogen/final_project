import time

from pages.main_page import Main_page
from pages.product_page import Product_Page
from pages.cart_page import Cart_page
from pages.place_order import Place_order

from conftest import init_driver


def test_buy_product_with_search_request(init_driver):
    driver = init_driver

    mp = Main_page(driver) # main page
    mp.go_to_main_url()
    mp.close_location_popup()
    mp.authorization()
    mp.click_logo()
    mp.search_item()


    pp = Product_Page(init_driver) # product page
    pp.add_product_to_cart()

    cp = Cart_page(init_driver) # cart page
    cp.place_order_for_one_item()

    po = Place_order(init_driver) # placing order
    po.place_order_one_item()

    time.sleep(3)
    driver.quit()