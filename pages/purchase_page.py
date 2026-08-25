from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PurchasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.name_field = (By.ID, "inputName")
        self.address_field = (By.ID, "address")
        self.city_field = (By.ID, "city")
        self.state_field = (By.ID, "state")
        self.zip_code_field = (By.ID, "zipCode")
        self.card_type_dropdown = (By.ID, "cardType")
        self.card_number_field = (By.ID, "creditCardNumber")
        self.card_month_field = (By.ID, "creditCardMonth")
        self.card_year_field = (By.ID, "creditCardYear")
        self.name_on_card_field = (By.ID, "nameOnCard")
        self.purchase_button = (By.CLASS_NAME, "btn-primary")

    def fill_purchase_form(self, name, address, city, state, zip_code,
                            card_type, card_number, card_month, card_year, name_on_card):
        self.wait.until(EC.presence_of_element_located(self.name_field))

        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.city_field).send_keys(city)
        self.driver.find_element(*self.state_field).send_keys(state)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)

        card_dropdown = Select(self.driver.find_element(*self.card_type_dropdown))
        card_dropdown.select_by_visible_text(card_type)

        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        self.driver.find_element(*self.card_month_field).send_keys(card_month)
        self.driver.find_element(*self.card_year_field).send_keys(card_year)
        self.driver.find_element(*self.name_on_card_field).send_keys(name_on_card)

    def click_purchase_flight(self):
        self.driver.find_element(*self.purchase_button).click()