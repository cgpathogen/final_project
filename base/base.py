from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Base:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,10,poll_frequency=1)
        self.action = ActionChains(self.driver)

    main_url = "https://legendbaikal.ru/"

    def go_to_main_url(self):
        self.driver.get(url=self.main_url)


    def get_current_url(self):
        print(f"\nCurrent URL: {self.driver.current_url}")