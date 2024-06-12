import pytest
import allure
from pages.aerolineas_home_page import AerolineasHomePage
from pages.aerolineas_result_page import AerolineasResultPage


class Test_cards:
    @allure.epic("Home_page_cards")
    @allure.title("Validar y verificar que las ofertas Nacionales sean visibles")
    @allure.description("Validar que el boton aceptar cookies y la los links funcione")
    @pytest.mark.smoke
    def test_aerolineas_nacional(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")

        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.validate_destino_nacional_card()
        home_page.validate_card_nacional_csv()

    @allure.epic("Home_page_cards")
    @allure.title("Validar y verificar que las ofertas Internacionales sean visibles")
    @allure.description("Validar que el boton aceptar cookies y la los links funcione")
    @pytest.mark.smoke
    def test_aerolineas_international(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")

        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.validate_destino_internacional_card()
        home_page.validate_card_internacional_csv()

    @allure.epic("Home_page_cards")
    @allure.title("Validar y verificar que las ofertas Regionales sean visibles")
    @allure.description("Validar que el boton aceptar cookies y la los links funcione")
    @pytest.mark.smoke
    def test_aerolineas_regional(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")

        home_page = AerolineasHomePage(driver)
        home_page.click_aceptar_cookies()
        home_page.validate_destino_regional_card()

    @allure.epic("Home_page_cards")
    @allure.title("Validar y verificar ofertas nacionales")
    @allure.description("Validar que el boton aceptar cookies y la los links funcione")
    @pytest.mark.smoke
    def test_aerolineas_national_card(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")

        home_page = AerolineasHomePage(driver)
        home_page.validate_card_nacional_csv()

    @allure.epic("Home_page_cards")
    @allure.title("Validar y verificar ofertas internacionales")
    @allure.description("Validar que el boton aceptar cookies y la los links funcione")
    @pytest.mark.smoke
    def test_aerolineas_international_card(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")

        home_page = AerolineasHomePage(driver)
        home_page.validate_card_internacional_csv()

    @allure.epic("Home_page_cards")
    @allure.title("Validar y verificar ofertas internacionales")
    @allure.description("Validar que el boton aceptar cookies y la los links funcione")
    @pytest.mark.smoke
    def test_aerolineas_regional_card(self, driver):
        with allure.step("Ingreso a la pagina y valida los tests solicitados"):
            driver.get("https://www.aerolineas.com.ar/")

        home_page = AerolineasHomePage(driver)
        home_page.validate_card_regional_csv()


if __name__ == "__main__":
    pytest.main()
