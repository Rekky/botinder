import os
from src.tinder import Tinder
from src.lovoo import Lovoo

DRIVER_PATH = os.path.abspath("./drivers/chromedriver.exe")
# DRIVER_PATH = os.path.abspath('./drivers/geckodriver.exe')
TINDER_URL = 'https://tinder.com/app/recs'
LOVOO_URL = 'https://es.lovoo.com/'


def run_tinder():
    tinder = Tinder(TINDER_URL, DRIVER_PATH, 'chrome')
    # Uncomment for using phone number account
    tinder.run_like_sequence_by_phone('611400206', 50000)

    # Uncomment for using facebook account
    # tinder.run_sequence_by_facebook(50000)


def run_lovoo():
    return True
    # lovoo = Lovoo(LOVOO_URL, DRIVER_PATH)
    # lovoo.run_like_sequence_by_account('ziroustyle@gmail.com', '', 1000000)


if __name__ == '__main__':
    run_tinder()
    # run_lovoo()
