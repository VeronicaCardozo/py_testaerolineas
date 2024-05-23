
# conftest.py
import pytest
from config.browser import BrowserConfig


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
            help="Escoger navegador: chrome o edge")
    
@pytest.fixture(autouse=True)
def driver(request):
    browser_selecionado = request.config.getoption("--browser")
    browser = BrowserConfig(browser_selecionado)
    driver = browser.select_browser()
    driver.maximize_window()
    yield driver
    print("Cerrar Browser")
    driver.quit()












