import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_result_page import AerolineasResultPage
from selenium import webdriver
from datetime import datetime, timedelta


class Test:
    @allure.title("Validar y verificar boton aceptar cookies y la cantidad de links del home de la pagina")
    @allure.description("Validar que el boton aceptar cookies y la los links funcione")
    @pytest.mark.noprod
    def test_aerolineas_home(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.cantidad_links_home()

    @allure.title("Validar y verificar boton aceptar menu lenguaje funcione")
    @allure.description("Validar boton menu lenguaje")
    @pytest.mark.noprod
    def test_menu(self, driver):
        with allure.step("Ingreso a la pagina y validar el menu lenguaje "):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.bnt_lenguaje_menu()

    # validar compra +20 dias CM

    @allure.title("Validar y verificar la compra de un vuelo ingresando +20 dias de hoja 2")
    @allure.description("Validar que los datos se ingresen correctamente")
    @pytest.mark.noprod
    def test_validar_excel_sumar_20(self, driver):
        with allure.step("Ingreso a la página"):
            driver.get("https://www.aerolineas.com.ar/")
        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.datos_excel_sumar_20()
        home_page.cambiar_cantidad_pasajeros()
        home_page.comprar_vuelo()
        home_page.precios_vuelos()
        home_page.ver_vuelos()


if __name__ == "__main__":
    pytest.main()
