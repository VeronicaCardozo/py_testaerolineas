import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_result_page import AerolineasResultPage
import time


class Test:
    @allure.epic("Customer_Communication")
    @allure.title("Validar y verificar boton whatsapp")
    @allure.description("Validar que el boton whatsapp funcione")
    @pytest.mark.noprod
    def test_whatsapp_web(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.whatsapp_chat()

    @allure.epic("Chat_Features")
    @allure.title("Validar y verificar boton chat online funcione")
    @allure.description("Validar que el boton chat online inicialice el chat y muestre las opciones")
    @pytest.mark.noprod
    def test_aerolineas_chat_online(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.login_chat_online()

    @allure.epic("Chat_Features")
    @allure.title("Validar y verificar boton reservas en chat online ")
    @allure.description("Validar que el boton reservas del chat online inicialice el chat y muestre las opciones")
    @pytest.mark.noprod
    def test_aerolineas_chat_reservas(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.reservas_chat_online2()


if __name__ == "__main__":
    pytest.main()