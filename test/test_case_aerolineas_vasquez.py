import pytest
import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_result_page import AerolineasResultPage


class test:

    @allure.title("Verificar que los elementos de la pagina acceso se muestre en Aerolienas Argentinas")
    @allure.description(
        "Validar diferentes botones y caja de texto en Aerolineas Argentina"
    )
    def test_validar_Aerolineas(self, driver):
        """
        Test para validar caja de textos y diferentes botones en Aerolineas Argentina.
        """
        with allure.step("Nos dirigimos a la pagina Aerolineas Argentina"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.btn_vuelos()
        home_page.btn_check_in()



if __name__ == "__main__":
    pytest.main()

