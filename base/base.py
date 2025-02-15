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


    # getters


    def get_location_popup(self):
        return self.wait.until(EC.presence_of_element_located(self.location_popup))


    def get_popup_close_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.popup_close_button))


    # actions


    def get_current_url(self):
        print(f"\nCurrent URL: {self.driver.current_url}")


    def hide_location_popup(self):
        location_popup = self.wait.until(EC.presence_of_element_located(self.location_popup))
        self.action.move_to_element(location_popup).perform()

        close_button = self.wait.until(EC.element_to_be_clickable(self.get_popup_close_button()))
        close_button.click()
        print("Location choosing pop-up was closed")