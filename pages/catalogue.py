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

    ## sort

    sort_btn = ("xpath","(//div[@class='catalog-panel-sort'])[1]")
    sort_options_block = ("xpath", "//div[@class='catalog-panel-sort-items']")
    sort_option = ("xpath", "(//div[@class='catalog-panel-sort-item'])[5]")
