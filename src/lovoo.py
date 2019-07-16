from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Lovoo:
    url: str = None
    driver = None

    def __init__(self, url: str, driver_path: str):
        self.url = url
        self.driver = webdriver.Chrome(driver_path)

    def run_like_sequence(self, telf: str, likes_limit: int):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

        button = self.driver.find_element_by_css_selector("button[aria-label='Iniciar sesión con nº de teléfono']")
        button.click()

        input_telf = self.driver.find_element_by_css_selector("input[name='phone_number']")
        input_telf.send_keys(telf)
        input_telf.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(50)

        button_permitir = self.driver.find_element_by_css_selector("button[aria-label='Permitir']")
        button_permitir.click()

        button_habilitar = self.driver.find_element_by_css_selector("button[aria-label='Habilitar']")
        button_habilitar.click()

        self.driver.implicitly_wait(50)
        like_count = 0
        print('INICIANDO LIKES SEQUENCES')

        for x in range(0, likes_limit):

            try:
                button = self.driver.find_element_by_css_selector("button[aria-label='Me gusta']")
                button.click()
                time.sleep(1)
                like_count = like_count + 1
                print("Like_count: " + like_count)
            except Exception as e:
                self.driver.find_element_by_css_selector("button[data-testid='addToHomeScreen']")
                button_add = self.driver.find_element_by_css_selector("button[data-testid='addToHomeScreen']")
                button_add.click()

        print("TERMINO TODO CORRECTO")
