import time

from pages.main_page import Main_page
from pages.catalogue import Catalogue
from pages.cart_page import Cart_page
from pages.place_order import Place_order

from conftest import init_driver

def test_buy_product(init_driver):
    driver = init_driver
    mp = Main_page(driver) # main page
    mp.go_to_main_url()
    mp.close_location_popup()
    mp.authorization()

    catalogue = Catalogue(driver) # catalogue
    catalogue.filter_catalogue_and_add_to_cart()

    cp = Cart_page(driver) # cart page
    cp.place_order()

    po = Place_order(driver) # place order
    po.place_order()


    time.sleep(3)
    driver.quit()