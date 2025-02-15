from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.action = ActionChains(self.driver)


    # main url:

    main_url = "https://legendbaikal.ru/"

    # user data:

    user_login = "acrocanthbm@gmail.com"
    user_password = "QAwErty123"


    # x-path locators:

    enter_button = ("xpath","//*[@id='i-5-bitrix-system-auth-form-panel-iIjGFB3HxHmm']/div")
    pop_up =  ("xpath", '//*[@id="UniverseComponent"]')
    log_in_field = ("xpath", '//*[@id="USER_LOGIN_2"]')
    password_field = ("xpath", '//*[@id="USER_PASSWORD_2"]')
    login_popup_btn = ("xpath", '//*[@id="i-1-bitrix-system-auth-authorize-popup-2-0weid03RvzKY"]/form/div[3]/input')
    catalog = ("xpath", '//*[@id="i-8-bitrix-menu-horizontal-1-XEVOpkwAkIZ0"]/div[2]/div/div/div[1]/div[1]/a')
    catalog_sublink = ("xpath", '//*[@id="i-8-bitrix-menu-horizontal-1-XEVOpkwAkIZ0"]/div[2]/div/div/div[1]/div[1]/a/div[2]')


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


    def get_catalog_link(self):
        return self.wait.until(EC.visibility_of_element_located(self.catalog))

    def get_catalog_sublink(self):
        return self.wait.until(EC.visibility_of_element_located(self.catalog_sublink))


    # actions


    def click_enter_button(self):
        self.get_enter_btn().click()
        print("click enter button")


    def send_login(self):
        self.get_log_in_field().send_keys(self.user_login)
        print('login sent')


    def send_password(self):
        self.get_password_field().send_keys(self.user_password)
        print("password sent")


    def click_login_button(self):
        self.get_login_popup_btn().click()
        print("authorization passed")


    def hover_catalog(self):
        self.action.move_to_element(self.get_catalog_link()).click(self.get_catalog_sublink()).perform()


    # methods:


    def authorization(self):
        self.driver.get(url=self.main_url)
        self.click_enter_button()
        self.send_login()
        self.send_password()
        self.click_login_button()