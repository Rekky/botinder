import os
from src.tinder import Tinder
from src.lovoo import Lovoo

# WINDOWS DRIVER
DRIVER_PATH = os.path.abspath("./drivers/windows/")

# MACOS DRIVER
# DRIVER_PATH = os.path.abspath("./drivers/macos/")


def run_tinder(sequence_mode: str = str(1)):
    URL: str = 'https://tinder.com/app/recs'

    if sequence_mode == str(1):
        print("======TINDER=======")
        print("Enter you phone number")
        print("===================")
        phone = input()

        tinder = Tinder(URL, DRIVER_PATH, 'chrome')
        tinder.run_like_sequence_by_phone(str(phone), 50000)
    elif sequence_mode == str(2):
        tinder = Tinder(URL, DRIVER_PATH, 'chrome')
        tinder.run_sequence_by_facebook(50000)


def run_lovoo():
    URL: str = 'https://es.lovoo.com/'
    lovoo = Lovoo(URL, DRIVER_PATH)
    lovoo.run_like_sequence_by_account('testeo@gmail.com', '', 1000000)


if __name__ == '__main__':
    print("===================")
    print("1) Tinder")
    print("2) Lovoo")
    print("===================")
    option = input()

    if option == str(1):
        print("======TINDER=======")
        print("1) By phone number")
        print("2) By facebook page")
        print("===================")
        mode = input()
        run_tinder(mode)

    elif option == str(2):
        run_lovoo()
