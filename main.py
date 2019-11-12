import os
from src.tinder import Tinder
from src.lovoo import Lovoo

# WINDOWS DRIVER
# DRIVER_PATH = os.path.abspath("./drivers/windows/chromedriver.exe")
DRIVER_PATH = os.path.abspath('./drivers/windows/geckodriver.exe')

# MACOS DRIVER
# DRIVER_PATH = os.path.abspath("./drivers/macos/chromedriver")
# DRIVER_PATH = os.path.abspath("./drivers/macos/geckodriver")


def run_tinder():
    URL: str = 'https://tinder.com/app/recs'
    tinder = Tinder(URL, DRIVER_PATH, 'firefox')
    tinder.run_like_sequence_by_phone('611400206', 50000)

    # Uncomment for using facebook account
    # tinder.run_sequence_by_facebook(50000)


def run_lovoo():
    URL: str = 'https://es.lovoo.com/'
    lovoo = Lovoo(URL, DRIVER_PATH)
    lovoo.run_like_sequence_by_account('testeo@gmail.com', '', 1000000)


if __name__ == '__main__':
    run_tinder()
    # run_lovoo()
