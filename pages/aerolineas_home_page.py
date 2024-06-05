from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import allure
import time
import os
import openpyxl
import csv


class AerolineasHomePage:
    # Locators
    btn_locator_aceptar_cookies = (
        By.XPATH, "(//button[@type='cookies'])")
    btn_locator_lenguaje_menu = (
        By.XPATH, "//button[@class='styled__LanguageMenu-sc-22nvvu-8 fEfYIU']")
    box_origen = (By.XPATH, "//input[@placeholder='Origen']")
    box_destino = (By.XPATH, "//input[@placeholder='Destino']")
    box_date_from = (By.XPATH, "//input[@id='from-date']")
    box_date_return = (By.XPATH, "//input[@id='to-date']")
    number_pasajeros = (By.XPATH, "//button[@id = 'cabin-passengers']")
    sumar_pasajeros = (
        By.CSS_SELECTOR, "button.styled__IconContainer-sc-1sy3ra0-1.eoncfD.add-adt")
    btn_click_vuelo = (By. XPATH, "//button[@id= 'search-flights']")
    # Localizadores para los elementos
    fechas_ida = (
        By.XPATH, "//div[@class='styled__DateOfferItem-ty299w-6 styled__EnabledDateOffer-ty299w-8 guJlAe fdc-available-day']//div[@class='styled__ButtonDay-ty299w-3 cwDvyN fdc-button-day'][normalize-space()='30']")
    fechas_vuelta = (
        By.XPATH, "//div[@class='styled__DateOfferItem-ty299w-6 styled__EnabledDateOffer-ty299w-8 guJlAe fdc-available-day']//div[@class='styled__ButtonDay-ty299w-3 cwDvyN fdc-button-day'][normalize-space()='7']")
    label_locator_monto = (
        By.XPATH, "//div[@class = 'styled__DateOfferItem-ty299w-6 styled__EnabledDateOffer-ty299w-8 guJlAe fdc-available-day']//div[@class = 'styled__Price-ty299w-0 cbwzbP fdc-button-price'][normalize-space()]")
    btn_ver_vuelo = (By.XPATH, "//button[normalize-space()='Ver vuelos']")

    button_whatsapp_locator = (By.ID, "whatsapp_flotante")
    button_chatbot_locator = (By.XPATH, "//body/div[@id='wcx-chat']/button[1]")
    box_chatbot_name = (By.XPATH, "//input[@name='wcx_chat_name']")

    def __init__(self, driver):
        self.driver = driver
    # metodos
    # 1) Aceptar cookies y verificacion de links

    @allure.step("Verificamos el boton aceptar cookies y la cantidad de links en el home")
    def click_aceptar_cookies(self):
        btn = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(
                self.btn_locator_aceptar_cookies)
        )
        print(" Boton aceptar cookies visible")
        assert btn.is_displayed(), "El boton de cookies no esta visible"
        btn.click()
        print(" Boton aceptar cookies visible y se hizo click en el ")

    @allure.step("Verificar cuantos Links hay en el home ")
    def cantidad_links_home(self):
        links = self.driver.find_elements(By.TAG_NAME, "a")
        print("El numero de Links que hay en el home de la pagina Aerolineas Argentina es:", len(links))
        for num in links:
            print(num.text)
        assert len(links) > 0, "No hay links en el home"

    @allure.step("Verificar boton menu idiomas ")
    def bnt_lenguaje_menu(self):
        btn_lenguaje = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.btn_locator_lenguaje_menu)
        )
        if btn_lenguaje.find_element(*self.btn_locator_lenguaje_menu).is_displayed():
            btn_lenguaje.find_element(*self.btn_locator_lenguaje_menu).click()
            time.sleep(3)
            print(
                "El menu lenguaje es visible")
            assert btn_lenguaje.is_displayed(), "El boton no esta verificado"
        else:
            print("El botón de idioma no está visible")
        btn_lenguaje.find_element(*self.btn_locator_lenguaje_menu).click()

    @allure.step("Validar los datos ingresados desde un archivo plano: en este caso Excel")
    def datos_excel(self):
        archivo = openpyxl.load_workbook(
            'C:\\py_automation\\Data\\datos_qa.xlsx')
        sheet = archivo['Hoja1']
        for fila in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=sheet.max_column):
            valores_fila = [celda.value for celda in fila]
            origen, destino, ida, regreso, url = valores_fila
            ida_str = ida.strftime("%d/%m/%Y")
            regreso_str = regreso.strftime("%d/%m/%Y")
            self.buscar_vuelo(origen, destino, ida_str, regreso_str)

    def buscar_vuelo(self, origen, destino, ida_str, regreso_str):
        box_origen = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.box_origen))
        box_origen.clear()
        box_origen.send_keys(origen)
        time.sleep(2)
        box_origen.send_keys(Keys.ARROW_DOWN, Keys.ENTER, Keys.TAB)
        print("Caja de origen es visible y los datos son ingresados")

        box_destino = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.box_destino))
        box_destino.clear()
        box_destino.send_keys(destino)
        time.sleep(2)
        box_destino.send_keys(Keys.ARROW_DOWN, Keys.ENTER, Keys.TAB)
        print("Caja de destino es visible y los datos son ingresados")

        box_date_from = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.box_date_from))
        box_date_from.clear()
        box_date_from.send_keys(ida_str, Keys.TAB)
        print("Caja de date_from es visible y los datos son ingresados")

        box_date_return = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.box_date_return))
        box_date_return.clear()
        box_date_return.send_keys(regreso_str, Keys.TAB)
        print("Caja de date_return es visible y los datos son ingresados")

    @allure.step("Validar cantidad de pasajeros=2")
    def cambiar_cantidad_pasajeros(self):
        try:
            pasajeros = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.number_pasajeros))
            pasajeros.click()
            print("Boton pasajeros visible y hacemos click")

            btn_mas = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.sumar_pasajeros))
            btn_mas.click()
            time.sleep(2)
            cantidad_pasajeros = pasajeros.get_attribute("value")
            if cantidad_pasajeros != "2":
                print("La cantidad de pasajeros se cambió")
            return True
        except TimeoutException as e:
            print(f"Error: {e}")

    @allure.step("Validar la búsqueda ingresando al botón búsqueda de vuelo de un vuelo-ida-regreso")
    def comprar_vuelo(self):
        try:
            btn_comprar = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.btn_click_vuelo))

            if btn_comprar.is_enabled():
                btn_comprar.click()
                time.sleep(6)
                print("El botón de comprar de vuelo es visible y hacemos click en él")
            else:
                print("El botón de compra de vuelo no es visible.")
        except TimeoutException:
            print("No se encontró el botón de comprar de vuelo ")

    @allure.step("Validar los elementos de vuelo y precios en la grilla de vuelos")
    def precios_vuelos(self):
        vuelos_ida = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.fechas_ida))
        vuelos_vuelta = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.fechas_vuelta))

        print("Vuelos de ida:")
        for vuelo in vuelos_ida:
            dia_vuelo_ida = vuelo.text
            precio_vuelo_ida = self.obtener_precio_vuelo(vuelo)
            if precio_vuelo_ida > 0:
                print("Día:", dia_vuelo_ida, "Precio:", precio_vuelo_ida)

        print("Vuelos de regreso:")
        for vuelo in vuelos_vuelta:
            dia_vuelo_regreso = vuelo.text
            precio_vuelo_regreso = self.obtener_precio_vuelo(vuelo)
            if precio_vuelo_regreso > 0:
                print("Día:", dia_vuelo_regreso,
                      "Precio:", precio_vuelo_regreso)

    def obtener_precio_vuelo(self, vuelo_elemento):
        try:
            precio_elemento = vuelo_elemento.find_element(
                *self.label_locator_monto)
            precio_text = precio_elemento.text.replace(
                '$', '').replace(',', '').strip()
            if precio_text and precio_text.replace('.', '', 1).isdigit():
                return float(precio_text)
            return 0.0
        except Exception as e:
            print(f"Error al obtener el precio del vuelo: {e}")
            return 0.0

    @allure.step("Validar la compra ingresando al boton ver vuelos ")
    def ver_vuelos(self):
        try:
            ver_vuelo = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.btn_ver_vuelo)
            )

            if ver_vuelo.is_displayed():
                ver_vuelo.click()

                time.sleep(6)
                print(
                    "El botón de ver vuelos es visible y hacemos click en el")
            else:
                print(
                    "El botón de ver vuelos no es visible.")
        except TimeoutException:
            print(
                "No se encontró el botón de ver vuelos ")

        # falta mas assert
        # falta mas verificaciones
        # tuve problemas con los selectores
        # faltA la segunda parte
        # y arreglar lo del excel

    @allure.step("Verificamos que el boton whatsapp funcione")
    def button_whatsapp(self):
        btn_wts = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(
                self.button_whatsapp_locator)
        )
        print(" Boton whatsapp visible")
        assert btn_wts.is_displayed(), "El boton de whatsapp no esta visible"
        btn_wts.click()
        print("Se hizo click en el boton whatsapp")

        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.driver.current_url
        assert current_url == 'https://api.whatsapp.com/send?phone=541149404798', f'URL actual: {
            current_url}'
        print("Se verifica que el boton de whatsaap nos redirecciona al chat")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    @allure.step("Verificamos que el chatbot responda a preguntas basicas")
    def chat_bot(self):
        btn_wcxchat = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(
                self.button_chatbot_locator)
        )
        print(" Boton chatbot visible")

        assert btn_wcxchat.is_displayed(), "El boton de chatbot no esta visible"

        btn_wcxchat.click()
        print("Se hizo click en el boton chatbot")

        # name = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
        # self.box_chatbot_name))
        # name.send_keys("Nombre de prueba")
    # Test card Nacional
    @allure.step("Validar si se encuentran las Cards de Destinos Nacionales")
    def validate_destino_nacional_card(self):
        card_nacional = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.card_destino_nacional_2))
        actions = ActionChains(self.driver)
        actions.move_to_element(card_nacional).perform()
        allure.attach(self.driver.get_screenshot_as_png(
        ), name="Screenshot_destino_nacional", attachment_type=allure.attachment_type.PNG)
        try:
            card_element_0 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.card_destino_nacional_0))
            if card_element_0.is_displayed():
                return "Se muestra las cards Nacionales"
            else:
                return "No se muestra la cards"
        except Exception as e:
            return "Error Card 1"

    @allure.step("Validar si se encuentran las Cards de Destinos Internacionales")
    def validate_destino_internacional_card(self):
        try:
            internacional = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.btn_international_card))
            internacional.click()
            card_internacional = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.card_destino_nacional_2))
            actions = ActionChains(self.driver)
            actions.move_to_element(card_internacional).perform()
            allure.attach(self.driver.get_screenshot_as_png(
            ), name="Screenshot_destino_internacional", attachment_type=allure.attachment_type.PNG)
            card_element_0 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.card_destino_nacional_0))
            if card_element_0.is_displayed():
                return "Se muestran las cards Internacionales"
            else:
                return "No se muestran las cards"
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name="Error_Screenshot", attachment_type=allure.attachment_type.PNG)
            return f"Error Card Internacional: {str(e)}"

    @allure.step("Validar si se encuentran las Cards de Destinos Regionales")
    def validate_destino_regional_card(self):
        try:
            regional = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.btn_regionales_card))
            regional.click()
            card_regional = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.card_destino_nacional_2))
            actions = ActionChains(self.driver)
            actions.move_to_element(card_regional).perform()
            allure.attach(self.driver.get_screenshot_as_png(
            ), name="Screenshot_destino_regional", attachment_type=allure.attachment_type.PNG)
            card_element_0 = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.card_destino_nacional_0))
            if card_element_0.is_displayed():
                return "Se muestran las cards Regionales"
            else:
                return "No se muestran las cards"
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(
            ), name="Error_Screenshot", attachment_type=allure.attachment_type.PNG)
            return f"Error Card Regional: {str(e)}"

    def validate_card_nacional_csv(self, output_file='ofertas_nacionales.csv'):
        xpaths = [
            "(//a[@data-posicion='0'])",
            "(//a[@data-posicion='1'])",
            "(//a[@data-posicion='2'])",
            "(//a[@data-posicion='3'])"
        ]
        data = []
        try:
            for xpath in xpaths:
                card = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                desde = card.find_element(
                    By.XPATH, ".//div[@class='styled__SecondaryLabel-sc-17je9ro-5 tfyso thumbnail-secondary-label']").text
                hacia = card.find_element(
                    By.XPATH, ".//label[@class='styled__PrimaryLabel-sc-17je9ro-4 klasRx thumbnail-primary-label']").text
                precio = card.find_element(
                    By.XPATH, ".//label[@class='styled__Fare-sc-17je9ro-7 fYFkWK thumbnail-fare']").text
                clase = card.find_element(
                    By.XPATH, ".//label[@class='styled__Badge-sc-17je9ro-3 nRgyB thumbnail-badge']").text

                data.append([desde, hacia, clase, precio])

        finally:
            with open(output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['desde', 'hacia', 'clase', 'precio'])
                writer.writerows(data)

            print(f'Data has been written to {output_file}')

    def validate_card_internacional_csv(self, output_file='ofertas_internacionales.csv'):
        xpaths = [
            "(//a[@data-posicion='0'])",
            "(//a[@data-posicion='1'])",
            "(//a[@data-posicion='2'])",
            "(//a[@data-posicion='3'])"
        ]
        data = []

        try:
            internacional = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.btn_international_card))
            internacional.click()
            for xpath in xpaths:
                card = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                desde = card.find_element(
                    By.XPATH, ".//div[@class='styled__SecondaryLabel-sc-17je9ro-5 tfyso thumbnail-secondary-label']").text
                hacia = card.find_element(
                    By.XPATH, ".//label[@class='styled__PrimaryLabel-sc-17je9ro-4 klasRx thumbnail-primary-label']").text
                precio = card.find_element(
                    By.XPATH, ".//label[@class='styled__Fare-sc-17je9ro-7 fYFkWK thumbnail-fare']").text
                clase = card.find_element(
                    By.XPATH, ".//label[@class='styled__Badge-sc-17je9ro-3 nRgyB thumbnail-badge']").text

                data.append([desde, hacia, clase, precio])

        finally:
            with open(output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['desde', 'hacia', 'clase', 'precio'])
                writer.writerows(data)

            print(f'Data has been written to {output_file}')

    def validate_card_regional_csv(self, output_file='ofertas_regionales.csv'):
        xpaths = [
            "(//a[@data-posicion='0'])",
            "(//a[@data-posicion='1'])",
            "(//a[@data-posicion='2'])",
            "(//a[@data-posicion='3'])"
        ]
        data = []

        try:
            regional = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.btn_regionales_card))
            regional.click()
            for xpath in xpaths:
                card = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, xpath))
                )
                desde = card.find_element(
                    By.XPATH, ".//div[@class='styled__SecondaryLabel-sc-17je9ro-5 tfyso thumbnail-secondary-label']").text
                hacia = card.find_element(
                    By.XPATH, ".//label[@class='styled__PrimaryLabel-sc-17je9ro-4 klasRx thumbnail-primary-label']").text
                precio = card.find_element(
                    By.XPATH, ".//label[@class='styled__Fare-sc-17je9ro-7 fYFkWK thumbnail-fare']").text
                clase = card.find_element(
                    By.XPATH, ".//label[@class='styled__Badge-sc-17je9ro-3 nRgyB thumbnail-badge']").text

                data.append([desde, hacia, clase, precio])

        finally:
            with open(output_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['desde', 'hacia', 'clase', 'precio'])
                writer.writerows(data)

            print(f'Data has been written to {output_file}')
