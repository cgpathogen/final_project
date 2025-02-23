import time
from datetime import datetime
from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


class Place_order(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.action = ActionChains(self.driver)


    # user data


    user_name = "Tester"
    user_email = "acrocanthbm@gmail.com"
    user_phone = "9270001122"


    # xpaths

    ## pay

    pay_by_card = ("xpath", "(//label[@class='intec-ui intec-ui-control-radiobox intec-ui-scheme-current intec-ui-size-2'])[1]")
    pay_in_cash = ("xpath","(//label[@class='intec-ui intec-ui-control-radiobox intec-ui-scheme-current intec-ui-size-2'])[3]")


    ## text fields

    name_input = ("xpath", "(//input[@class='intec-ui intec-ui-control-input intec-ui-mod-block form-control bx-soa-customer-input bx-ios-fix'])[1]")
    email_input = ("xpath", "(//input[@class='intec-ui intec-ui-control-input intec-ui-mod-block form-control bx-soa-customer-input bx-ios-fix'])[2]")
    phone_input = ("xpath", "(//input[@class='intec-ui intec-ui-control-input intec-ui-mod-block form-control bx-soa-customer-input bx-ios-fix'])[3]")
    call_operator_to_confirm = ("xpath", '//*[@id="bx-soa-properties"]/div[2]/div[2]/div[1]/div[6]/div/label/input[2]')
    calendar_input = ("xpath", "(//input[@class='intec-ui intec-ui-control-input intec-ui-mod-block form-control bx-soa-customer-input bx-ios-fix'])[9]")


    ### calendar

    calendar = ("xpath", "//div[@class='pika-single is-bound left-aligned bottom-aligned']")
    td_day = ("xpath", f"//td[@data-day='{datetime.today().day+1}']")


    ### delivery hours


    delivery_hours_dropdown = ("xpath","//select[@name='ORDER_PROP_122']")


    ## total


    total_1 = ("xpath","(//span[@class='bx-soa-cart-d'])[5]")
    total_2 = ("xpath","(//span[@class='bx-soa-cart-d bx-soa-changeCostSign'])[2]")
    discount = ("xpath", "(//span[@class='bx-soa-cart-d'])[10]")


    ## goods list


    item_1_name = ("xpath","(//div[@class='bx-soa-item-title']/a)[1]")
    item_1_price = ("xpath", "(//div[@class='bx-soa-item-td-text'])[2]")
    item_1_total_price = ("xpath", "(//div[@class='bx-soa-item-td-text'])[5]")

    item_2_name = ("xpath", "(//div[@class='bx-soa-item-title']/a)[2]")
    item_2_price = ("xpath", "(//div[@class='bx-soa-item-td-text'])[7]")
    item_2_total_price = ("xpath", "(//div[@class='bx-soa-item-td-text'])[10]")


    # getters


    ## pay

    def get_pay_by_card(self):
        return self.wait.until(EC.element_to_be_clickable(self.pay_by_card))


    def get_pay_in_cash(self):
        return self.wait.until(EC.element_to_be_clickable(self.pay_in_cash))


    ## text fields


    def get_name_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.name_input))


    def get_email_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.email_input))


    def get_phone_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_input))


    def get_call_operator_to_confirm(self):
        return self.wait.until(EC.element_to_be_clickable(self.call_operator_to_confirm))


    def get_calendar_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.calendar_input))


    ### calendar


    def get_calendar(self):
        return self.wait.until(EC.visibility_of_element_located(self.calendar))


    def get_td_day(self):
        return self.wait.until(EC.visibility_of_element_located(self.td_day))


    ### delivery hours


    def get_delivery_hours_dropdown(self):
        return self.wait.until(EC.element_to_be_clickable(self.delivery_hours_dropdown))


    ## total


    def get_total_1(self):
        return self.wait.until(EC.visibility_of_element_located(self.total_1))


    def get_total_2(self):
        return self.wait.until(EC.visibility_of_element_located(self.total_2))


    def get_discount(self):
        return self.wait.until(EC.visibility_of_element_located(self.discount))


    ## goods list


    def get_item_1_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_1_name))


    def get_item_1_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_1_price))


    def get_item_1_total_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_1_total_price))


    def get_item_2_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_2_name))


    def get_item_2_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_2_price))


    def get_item_2_total_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.item_2_total_price))


    # actions

    ## total


    def compare_total_order_price(self):
        total_order_price = float(self.get_total_1().text.split(" ")[0])
        total_order_price_2 = float(self.get_total_2().text.split(" ")[0])
        assert self.read_price(5) == total_order_price
        assert self.read_price(5) == total_order_price_2
        print("total order price match")


    def compare_goods_list_name(self):
        assert self.read_name(1) == self.get_item_1_name().text
        assert self.read_name(2) == self.get_item_2_name().text



    ## text fields


    def choose_payment_option(self, option):
        self.wait.until(EC.element_to_be_clickable(option)).click()
        print("payment option was chosen")


    def enter_name(self):
        self.wait.until(EC.element_to_be_clickable(self.get_name_input())).send_keys(Keys.COMMAND + "A")
        self.wait.until(EC.element_to_be_clickable(self.get_name_input())).send_keys(self.user_name)
        self.check_name_is_entered()
        print("name entered")


    def check_name_is_entered(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.name_input,self.user_name))


    def enter_email(self):
        self.wait.until(EC.element_to_be_clickable(self.get_email_input())).send_keys(Keys.COMMAND + "A")
        self.wait.until(EC.element_to_be_clickable(self.get_email_input())).send_keys(self.user_email)
        self.check_email_is_entered()
        print("email entered")


    def check_email_is_entered(self):
        self.wait.until(EC.text_to_be_present_in_element_value(self.email_input,self.user_email))


    def enter_phone(self):
        self.wait.until(EC.element_to_be_clickable(self.get_phone_input())).click()
        self.wait.until(EC.element_to_be_clickable(self.get_phone_input())).send_keys(self.user_phone)
        self.check_phone_is_entered()
        print("phone number entered")


    def check_phone_is_entered(self):
        edited_phone = f"+7 ({self.user_phone[:3]}) {self.user_phone[3:6]}-{self.user_phone[6:]}"
        self.wait.until(EC.text_to_be_present_in_element_value(self.phone_input,edited_phone))


    # methods


    def place_order(self):
        self.choose_payment_option(self.get_pay_in_cash())
        self.compare_total_order_price()
        time.sleep(3)
        self.scroll_page_with_500px()
        self.enter_name()
        self.enter_email()
        self.enter_phone()
        self.compare_goods_list_name()