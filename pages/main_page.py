from base.base import Base

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)


    # x-path locators:

    enter_button = "//*[@id='i-5-bitrix-system-auth-form-panel-iIjGFB3HxHmm']/div"
    pop_up = '//*[@id="UniverseComponent"]'
    log_in_field = '//*[@id="USER_LOGIN_2"]'
    password_field = '//*[@id="USER_PASSWORD_2"]'
    login_popup_btn = '//*[@id="i-1-bitrix-system-auth-authorize-popup-2-0weid03RvzKY"]/form/div[3]/input'