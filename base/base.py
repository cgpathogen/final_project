from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10,poll_frequency=1)
        self.action = ActionChains(self.driver)


    # locators

    location_popup = ("xpath",'//*[@id="popup-window-content-i-4-intec-regionality-regions-select-template-1-b7WAH1g6DqWX-question"]/div')
    popup_close_button = ("xpath",'//*[@id="popup-window-content-i-4-intec-regionality-regions-select-template-1-b7WAH1g6DqWX-question"]/div/div[3]')
    pcb_yes = ("xpath",'//button[@class="regions-select-question-button intec-cl-background intec-cl-background-light-hover"]')
    pcb_no = ("xpath", '//button[@class="regions-select-question-button"]')
    locations_list_popup = ("xpath", "//div[@id='i-4-intec-regionality-regions-select-template-1-b7WAH1g6DqWX-dialog']")
    location_input = ("xpath","//*[@id='popup-window-content-i-4-intec-regionality-regions-select-template-1-b7WAH1g6DqWX-dialog']/div/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div")


    # getters


    def get_location_popup(self):
        return self.wait.until(EC.presence_of_element_located(self.location_popup))


    def get_popup_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.popup_close_button))


    def get_pcb_yes(self):
        return self.wait.until(EC.element_to_be_clickable(self.pcb_yes))


    def get_pcb_no(self):
        return self.wait.until(EC.element_to_be_clickable(self.pcb_no))


    def get_locations_list_popup(self):
        return self.wait.until(EC.visibility_of_element_located(self.locations_list_popup))

    def get_location_input(self):
        return self.wait.until(EC.element_to_be_clickable(self.location_input))


    # actions


    def get_current_url(self):
        print(f"\nCurrent URL: {self.driver.current_url}")


    def hide_location_popup(self):
        location_popup = self.wait.until(EC.presence_of_element_located(self.location_popup))
        self.action.move_to_element(location_popup).perform()

        close_button = self.wait.until(EC.element_to_be_clickable(self.get_popup_close_button()))
        close_button.click()
        print("Location choosing pop-up was closed")


    def choose_user_location(self):
        location_popup = self.wait.until(EC.presence_of_element_located(self.location_popup))
        self.action.move_to_element(location_popup).perform()
        self.get_pcb_no().click()
        locations_list = self.wait.until(EC.element_to_be_clickable(self.locations_list_popup))
        self.action.move_to_element(locations_list).perform()

        location_input = self.wait.until(EC.element_to_be_clickable(self.get_location_input()))
        location_input.click()