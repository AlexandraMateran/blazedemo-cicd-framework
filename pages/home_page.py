from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.from_port = (By.NAME, "fromPort")
        self.to_port = (By.NAME, "toPort")
        self.find_flights_button = (By.CLASS_NAME, "btn-primary")

    def select_departure_city(self, city):
        dropdown = Select(self.driver.find_element(*self.from_port))
        dropdown.select_by_visible_text(city)

    def select_destination_city(self, city):
        dropdown = Select(self.driver.find_element(*self.to_port))
        dropdown.select_by_visible_text(city)

    def click_find_flights(self):
        self.driver.find_element(*self.find_flights_button).click()