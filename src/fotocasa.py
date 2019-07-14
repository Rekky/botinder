from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Fotocasa:
    url: str = None
    driver = None
    tipo: 0

    def __init__(self, url: str, driver_path: str):
        self.url = url
        self.driver = webdriver.Chrome(driver_path)

    def run_search_sequence(self, telf: str, email: str, rooms_length: int, max_price: int, search_limit: int):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

        button = self.driver.find_element_by_css_selector("button[data-tealium-tag='c_list_modal_contact_load']")
        button.click()
        print(button)
        self.driver.implicitly_wait(10)
