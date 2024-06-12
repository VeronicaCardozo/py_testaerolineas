import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_result_page import AerolineasResultPage
import time


class Test:
    @allure.title("Validar y verificar boton whatsapp")
    @allure.description("Validar que el boton aceptar whatsapp funcione")
    @pytest.mark.noprod
    def test_aerolineas_home(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        # home_page.button_whatsapp()
        home_page.chat_bot()

        time.sleep(5)


if __name__ == "__main__":
    pytest.main()