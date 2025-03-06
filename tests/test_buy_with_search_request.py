import time

from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.place_order import Place_order

from conftest import init_driver


def test_buy_product_with_search_request(init_driver):
    driver = init_driver

    mp = Main_page(driver)

    mp.go_to_main_url()
    mp.close_location_popup()
    mp.authorization()
    mp.click_logo()
    mp.search_item()

    time.sleep(3)
    driver.quit()