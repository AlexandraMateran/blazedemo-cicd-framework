from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.confirmation_message = (By.XPATH, "//h1[text()='Thank you for your purchase today!']")

    def is_purchase_confirmed(self):
        self.wait.until(EC.presence_of_element_located(self.confirmation_message))
        return self.driver.find_element(*self.confirmation_message).is_displayed()

    def get_confirmation_text(self):
        return self.driver.find_element(*self.confirmation_message).text