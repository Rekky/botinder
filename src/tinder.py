from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
import time


class Tinder:
    url: str = None
    driver = None

    def __init__(self, url: str, driver_path: str, driver_type: str):
        self.url = url

        if driver_type == 'chrome':
            print('browser = chrome')
            options = webdriver.ChromeOptions()
            options.add_argument("--disable-notifications")
            self.driver = webdriver.Chrome(driver_path, 0, options)

        if driver_type == 'firefox':
            print('browser = firefox')
            binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            options = Options()
            options.add_argument("--disable-notifications")
            options.binary = binary
            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = True
            self.driver = webdriver.Firefox(firefox_options=options, capabilities=cap, executable_path=driver_path)

    def run_like_sequence_by_phone(self, telf: str, likes_limit: int = 1000):
        self.driver.get(self.url)

        self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_css_selector("#modal-manager > div > div > div > div > div:nth-child(4) > div:nth-child(1) > button")
        button.click()

        self.driver.implicitly_wait(10)
        input_telf = self.driver.find_element_by_css_selector("#modal-manager > div > div > div > div > div > input")
        input_telf.send_keys(telf)
        input_telf.send_keys(Keys.RETURN)

        self.driver.implicitly_wait(50)
        self.run_likes_sequence(likes_limit)
        print("FINISHED")

    def run_sequence_by_facebook(self, likes_limit: int = 1000):
        self.driver.get(self.url)

        self.driver.implicitly_wait(10)
        button = self.driver.find_element_by_css_selector("button[aria-label='Inicia sesión con Facebook']")
        button.click()

        self.driver.implicitly_wait(10)
        self.run_likes_sequence(likes_limit)

    def run_likes_sequence(self, likes_limit: int):
        likes: int = 0
        self.driver.implicitly_wait(50)

        for x in range(0, likes_limit):
            try:
                btn_like = self.driver.find_element_by_css_selector("button[aria-label='Me gusta']")
                btn_like.click()

                likes = x
                print("Like_count: " + str(likes))
                time.sleep(0.5)
            except Exception as e:
                button_add = self.driver.find_element_by_css_selector("#modal-manager > div > div > div.Pt\(16px\).Pb\(10px\).Px\(36px\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\).C\(\$c-secondary\).C\(\$c-base\)\:h")
                button_add.click()
