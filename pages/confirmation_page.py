from selenium.webdriver.common.by import By


class ConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.confirmation_message = (By.XPATH, "//h1[text()='Thank you for your purchase today!']")

    def is_purchase_confirmed(self):
        return self.driver.find_element(*self.confirmation_message).is_displayed()

    def get_confirmation_text(self):
        return self.driver.find_element(*self.confirmation_message).text
