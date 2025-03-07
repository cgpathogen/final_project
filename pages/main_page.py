from selenium.common import StaleElementReferenceException

from base.base import Base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=1)
        self.action = ActionChains(self.driver)


    # user data:

    user_login = "acrocanthbm@gmail.com"
    user_password = "QAwErty123"


    # x-path locators:


    enter_button = ("xpath","//*[@id='i-5-bitrix-system-auth-form-panel-iIjGFB3HxHmm']/div")
    pop_up =  ("xpath", '//*[@id="UniverseComponent"]')
    log_in_field = ("xpath", '//*[@id="USER_LOGIN_2"]')
    password_field = ("xpath", '//*[@id="USER_PASSWORD_2"]')
    login_popup_btn = ("xpath", '//*[@id="i-1-bitrix-system-auth-authorize-popup-2-0weid03RvzKY"]/form/div[3]/input')
    pagetitle = ("xpath",'//*[@id="pagetitle"]')

    # main navbar x-paths

    catalog = ("xpath", '//div[@class="intec-grid-item-auto menu-item menu-item-section intec-cl-background-light-hover"]')
    catalog_submenu = ("xpath", '//*[@id="i-8-bitrix-menu-horizontal-1-XEVOpkwAkIZ0"]/div[2]/div/div/div[1]/div[1]/div')
    catalog_sublink = ("xpath", '//*[@id="i-8-bitrix-menu-horizontal-1-XEVOpkwAkIZ0"]/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div[1]/div/div[1]/div/a')


    # pop-up xpaths:

    location_popup = ("xpath",'//*[@id="popup-window-content-i-4-intec-regionality-regions-select-template-1-b7WAH1g6DqWX-question"]/div')
    popup_close_button = ("xpath",'//*[@id="popup-window-content-i-4-intec-regionality-regions-select-template-1-b7WAH1g6DqWX-question"]/div/div[3]')
    pcb_yes = ("xpath",'//button[@class="regions-select-question-button intec-cl-background intec-cl-background-light-hover"]')
    pcb_no = ("xpath", '//button[@class="regions-select-question-button"]')

    # search

    search_input = ("xpath", "//input[@id='-input-1']")
    search_results_block = ("xpath", "//div[@class='ns-bitrix c-search-title c-search-title-input-1 search-title-results']")
    search_results_right_sub_block = ("xpath", "//div[@class='search-title-additional']")
    right_block_item = ("xpath", "(//div[@class='catalog-section-item-wrapper'])[1]")
    right_block_item_name = ("xpath", "//div[@class='catalog-section-item-name']")


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


    def get_pagetitle(self):
        return self.wait.until(EC.visibility_of_element_located(self.pagetitle))


    def get_catalog_link(self):
        return self.wait.until(EC.visibility_of_element_located(self.catalog))


    def get_submenu(self):
        return self.wait.until(EC.visibility_of_element_located(self.catalog_submenu))


    def get_catalog_sublink(self):
        return self.wait.until(EC.visibility_of_element_located(self.catalog_sublink))


    # pop-up getters:

    def get_location_popup(self):
        return self.wait.until(EC.presence_of_element_located(self.location_popup))


    def get_popup_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.popup_close_button))


    def get_pcb_yes(self):
        return self.wait.until(EC.element_to_be_clickable(self.pcb_yes))


    def get_pcb_no(self):
        return self.wait.until(EC.element_to_be_clickable(self.pcb_no))


    # search


    def get_search_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_input))


    def get_search_results_block(self):
        return self.wait.until(EC.visibility_of_element_located(self.search_results_block))


    def get_search_results_right_sub_block(self):
        return self.wait.until(EC.visibility_of_element_located(self.search_results_right_sub_block))


    def get_right_block_item(self):
        return self.wait.until(EC.element_to_be_clickable(self.right_block_item))


    def get_right_block_item_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.right_block_item_name))


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


    def assert_pagetitle_reach(self):
        assert self.get_pagetitle().text == 'Личный кабинет пользователя'


    # search


    def enter_search_request(self, request):
        self.get_search_input().send_keys(request)
        print(f"search request intered, search request - {request}")


    def hover_search_results_block(self):
        self.action.move_to_element(self.get_search_results_block()).perform()
        print("hover on search results block")


    def hover_and_click_right_block_item(self):
        try:
            self.action.move_to_element(self.get_right_block_item()).pause(1).click(self.get_right_block_item()).perform()
        except StaleElementReferenceException:
            self.action.move_to_element(self.get_right_block_item()).pause(1).click(self.get_right_block_item()).perform()
        print("hover on right block item")


    # methods:



    def hover_catalog(self):
        # Ждем, пока элемент каталога станет видимым
        catalog_link = self.wait.until(EC.visibility_of_element_located(self.catalog))

        # Наводим курсор на элемент каталога
        self.action.move_to_element(catalog_link).perform()

        # Ждем, пока подкатегория станет видимой
        catalog_sublink = self.wait.until(EC.visibility_of_element_located(self.catalog_sublink))

        # Кликаем на подкатегорию
        catalog_sublink.click()
        print("hover and click on catalog sublink")


    def hide_location_popup(self):
        location_popup = self.wait.until(EC.presence_of_element_located(self.location_popup))
        self.action.move_to_element(location_popup).perform()

        close_button = self.wait.until(EC.element_to_be_clickable(self.get_popup_close_button()))
        close_button.click()
        print("Location choosing pop-up was closed")


    def close_location_popup(self): # закрываем модальное окно выбора локации
        self.hide_location_popup()


    def authorization(self): # авторизация
        self.accept_ccokies()
        self.get_current_url()
        self.click_enter_button()
        self.send_login()
        self.send_password()
        self.click_login_button()
        self.assert_pagetitle_reach()
        self.hover_catalog()


    def search_item(self):
        self.enter_search_request("React")
        self.hover_search_results_block()
        self.create_txt_name(self.get_right_block_item_text().text,1)
        self.hover_and_click_right_block_item()