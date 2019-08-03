from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import date
from src.DB import *
import time


class Tinder:
    url: str = None
    driver = None
    total_likes: int = 0
    current_likes: int = 0

    def __init__(self, url: str, driver_path: str):
        self.url = url
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(driver_path, 0, chrome_options)

    def run_like_sequence_by_phone(self, telf: str, likes_limit: int = 1000):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

        button = self.driver.find_element_by_css_selector("button[aria-label='Iniciar sesión con nº de teléfono']")
        button.click()

        input_telf = self.driver.find_element_by_css_selector("input[name='phone_number']")
        input_telf.send_keys(telf)
        input_telf.send_keys(Keys.ENTER)

        self.driver.implicitly_wait(50)
        self.run_likes_sequence(likes_limit)
        print("FINISHED")

    def run_sequence_by_facebook(self, likes_limit: int = 1000):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

        button = self.driver.find_element_by_css_selector("button[aria-label='Inicia sesión con Facebook']")
        button.click()

        self.driver.implicitly_wait(50)
        self.run_likes_sequence(likes_limit)
        print("FINISHED")

    def run_likes_sequence(self, likes_limit: int):
        for x in range(0, likes_limit):
            try:
                button = self.driver.find_element_by_css_selector("button[aria-label='Me gusta']")
                button.click()

                self.current_likes = x
                print("Like_count: " + str(self.current_likes))
                time.sleep(0.3)
            except Exception as e:
                self.driver.find_element_by_css_selector("button[data-testid='addToHomeScreen']")
                button_add = self.driver.find_element_by_css_selector("button[data-testid='addToHomeScreen']")
                button_add.click()