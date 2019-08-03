from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Lovoo:
    url: str = None
    driver = None

    def __init__(self, url: str, driver_path: str):
        self.url = url
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(driver_path, 0, chrome_options)

    def run_like_sequence(self, email: str, password: str, likes_limit: int):
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

        button = self.driver.find_element_by_css_selector("button[data-automation-id='login-button']")
        button.click()

        input_email = self.driver.find_element_by_css_selector("input[data-automation-id='login-enter-email-input']")
        input_email.send_keys(email)
        input_pass = self.driver.find_element_by_css_selector("input[data-automation-id='login-enter-password-input']")
        input_pass.send_keys(password)
        input_pass.send_keys(Keys.ENTER)

        link_play = self.driver.find_element_by_css_selector("a[href='/match']")
        link_play.click()

        print('INICIANDO LIKES SEQUENCES')

        for x in range(0, likes_limit):
            try:
                print("LOVOO LIKES: " + str(x))
                button_like = self.driver.find_element_by_css_selector("span[data-automation-id='vote-yes-button']")
                button_like.click()

                time.sleep(0.7)
            except Exception as e:
                print("ERROR:" + str(e))

        print("TERMINO TODO CORRECTO")
