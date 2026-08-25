from selenium.webdriver.common.by import By


class ReservePage:
    def __init__(self, driver):
        self.driver = driver
        self.choose_flight_button = (By.CLASS_NAME, "btn-small")

    def click_choose_flight(self):
        self.driver.find_element(*self.choose_flight_button).click()