from pages.home_page import HomePage
from pages.reserve_page import ReservePage
from pages.purchase_page import PurchasePage
from pages.confirmation_page import ConfirmationPage


def test_successful_flight_purchase(driver):
    home_page = HomePage(driver)
    home_page.select_departure_city("Boston")
    home_page.select_destination_city("London")
    home_page.click_find_flights()

    reserve_page = ReservePage(driver)
    reserve_page.click_choose_flight()

    purchase_page = PurchasePage(driver)
    purchase_page.fill_purchase_form(
        name="Alexandra Materan",
        address="Calle 123",
        city="Cali",
        state="Valle del Cauca",
        zip_code="760001",
        card_type="Visa",
        card_number="4111111111111111",
        card_month="12",
        card_year="2027",
        name_on_card="Alexandra Materan"
    )
    purchase_page.click_purchase_flight()

    confirmation_page = ConfirmationPage(driver)
    assert confirmation_page.is_purchase_confirmed() is True


def test_purchase_with_empty_fields(driver):
    home_page = HomePage(driver)
    home_page.select_departure_city("Boston")
    home_page.select_destination_city("London")
    home_page.click_find_flights()

    reserve_page = ReservePage(driver)
    reserve_page.click_choose_flight()

    purchase_page = PurchasePage(driver)
    purchase_page.wait.until(
        lambda d: d.find_element(*purchase_page.name_field)
    )
    purchase_page.click_purchase_flight()

    confirmation_page = ConfirmationPage(driver)

    # BUG conocido: BlazeDemo no valida campos obligatorios en el formulario
    # de compra. Se esperaría que el sitio bloqueara la compra y mostrara un
    # mensaje de error, pero en su lugar confirma la compra igual.
    # Este assert documenta el comportamiento ACTUAL (incorrecto) del sitio,
    # no el comportamiento deseado.
    assert confirmation_page.is_purchase_confirmed() is True, (
        "Se esperaba reproducir el bug conocido: el sitio permite comprar "
        "sin llenar el formulario. Si este assert falla, el bug fue corregido."
    )