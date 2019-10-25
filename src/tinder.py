from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import time


class Tinder:
    url: str = None
    browser = None
    current_likes: int = 0

    def __init__(self, url: str, driver_path: str, driver_type: str):
        self.url = url
        print("---->")

        if driver_type == 'chrome':
            print('browser = chrome')
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            self.browser = webdriver.Chrome(driver_path, 0, options)

        if driver_type == 'firefox':
            print('browser = firefox')
            binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            options = Options()
            options.add_argument("--disable-notifications")
            options.binary = binary
            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = True
            self.browser = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path=driver_path)

    def run_like_sequence_by_phone(self, telf: str, likes_limit: int = 1000):
        self.browser.get(self.url)
        self.browser.implicitly_wait(10)

        button = self.browser.find_element_by_css_selector("button[aria-label='Iniciar sesión con nº de teléfono']")
        button.click()

        input_telf = self.browser.find_element_by_css_selector("input[name='phone_number']")
        input_telf.send_keys(telf)
        input_telf.send_keys(Keys.ENTER)

        self.browser.implicitly_wait(50)
        self.run_likes_sequence(likes_limit)
        print("FINISHED")

    def run_sequence_by_facebook(self, likes_limit: int = 1000):
        self.browser.get(self.url)
        self.browser.implicitly_wait(10)

        button = self.browser.find_element_by_css_selector("button[aria-label='Inicia sesión con Facebook']")
        button.click()

        self.browser.implicitly_wait(50)
        self.run_likes_sequence(likes_limit)
        print("FINISHED")

    def run_likes_sequence(self, likes_limit: int):
        for x in range(0, likes_limit):
            try:
                button = self.browser.find_element_by_css_selector("button[aria-label='Me gusta']")
                button.click()

                self.current_likes = x
                print("Like_count: " + str(self.current_likes))
                time.sleep(0.3)
            except Exception as e:
                self.browser.find_element_by_css_selector("button[data-testid='addToHomeScreen']")
                button_add = self.browser.find_element_by_css_selector("button[data-testid='addToHomeScreen']")
                button_add.click()