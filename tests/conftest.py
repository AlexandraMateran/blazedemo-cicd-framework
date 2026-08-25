import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


LOCAL_CHROMEDRIVER_PATH = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"


@pytest.fixture
def driver():
    options = Options()

    if os.path.exists(LOCAL_CHROMEDRIVER_PATH):
        # Estamos en tu máquina local (Windows) - usa el driver descargado manualmente
        service = Service(LOCAL_CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service, options=options)
    else:
        # Estamos en GitHub Actions (Linux) - sin pantalla, necesita modo headless
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    driver.get("https://blazedemo.com")
    yield driver
    driver.quit()