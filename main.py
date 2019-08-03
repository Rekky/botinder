from src.tinder import Tinder
from src.lovoo import Lovoo

CHROME_DRIVER = './chrome_driver/chromedriver.exe'
TINDER_URL = 'https://tinder.com/app/recs'
LOVOO_URL = 'https://es.lovoo.com/'


def run_tinder():
    tinder = Tinder(TINDER_URL, CHROME_DRIVER)
    # Using phone number account
    # tinder.run_like_sequence_by_phone('123456789', 50000)

    # Using facebook account
    tinder.run_sequence_by_facebook(50000)


def run_lovoo():
    lovoo = Lovoo(LOVOO_URL, CHROME_DRIVER)
    lovoo.run_like_sequence('ziroustyle@gmail.com', '', 1000000)


if __name__ == '__main__':
    run_tinder()
