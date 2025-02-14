from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
    # x-path locators:

    enter_button = ("xpath","//*[@id='i-5-bitrix-system-auth-form-panel-iIjGFB3HxHmm']/div")
    pop_up =  ("xpath", '//*[@id="UniverseComponent"]')
    log_in_field = ("xpath", '//*[@id="USER_LOGIN_2"]')
    password_field = ("xpath", '//*[@id="USER_PASSWORD_2"]')
    login_popup_btn = ("xpath", '//*[@id="i-1-bitrix-system-auth-authorize-popup-2-0weid03RvzKY"]/form/div[3]/input')


    # getters

    def get_enter_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.enter_button))


    def get_pop_up(self):
        return  self.wait.until(EC.visibility_of_element_located(self.pop_up))


    def get_log_in_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.log_in_field))


    def get_password_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.password_field))


    def get_login_popup_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.login_popup_btn))



    # actions



