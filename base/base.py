

class Base:
    def __init__(self, driver):
        self.driver = driver


    def get_current_url(self):
        print(f"\n{self.driver.current_url}")