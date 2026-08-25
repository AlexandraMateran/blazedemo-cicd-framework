import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


LOCAL_CHROMEDRIVER_PATH = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"


@pytest.fixture
def driver():
    if os.path.exists(LOCAL_CHROMEDRIVER_PATH):
        # Estamos en tu máquina local (Windows) - usa el driver descargado manualmente
        service = Service(LOCAL_CHROMEDRIVER_PATH)
        driver = webdriver.Chrome(service=service)
    else:
        # Estamos en GitHub Actions (Linux) - el driver ya está en el PATH del sistema
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get("https://blazedemo.com")
    yield driver
    driver.quit()