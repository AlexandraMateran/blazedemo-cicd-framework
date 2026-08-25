from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ReservePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.choose_flight_button = (By.CLASS_NAME, "btn-small")

    def click_choose_flight(self):
        self.wait.until(EC.presence_of_element_located(self.choose_flight_button))
        self.driver.find_element(*self.choose_flight_button).click()