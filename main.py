import os
import platform
from src.tinder import Tinder
from src.lovoo import Lovoo


def run_tinder(sequence_mode: str = '1', driver_type: str = 'chrome'):
    URL: str = 'https://tinder.com/app/recs'

    if sequence_mode == str(1):
        print("======TINDER=======")
        print("Enter you phone number")
        print("===================")
        phone = input()

        tinder = Tinder(URL, get_driver_path(), driver_type)
        tinder.run_like_sequence_by_phone(str(phone), 50000)
    elif sequence_mode == str(2):
        tinder = Tinder(URL, get_driver_path(), driver_type)
        tinder.run_sequence_by_facebook(50000)


def run_lovoo():
    URL: str = 'https://es.lovoo.com/'
    lovoo = Lovoo(URL, get_driver_path())
    lovoo.run_like_sequence_by_account('testeo@gmail.com', '', 1000000)


def get_driver_path():
    os_type = platform.system()

    if os_type == 'Windows':
        return os.path.abspath("./drivers/windows/")
    elif os_type == 'MacOS':
        return os.path.abspath("./drivers/macos/")
    else:
        return None


def select_driver():
    print("======SELECT DRIVER=======")
    print("1) Chrome Driver")
    print("2) Firefox Driver")
    print("==========================")
    driver_type = input()
    if driver_type == '1':
        return 'chrome'
    elif driver_type == '2':
        return 'firefox'


def select_app():
    driver_type = select_driver()

    print("===================")
    print("1) Tinder")
    print("2) Lovoo")
    print("===================")
    option = input()

    if option == '1':
        print("======TINDER=======")
        print("1) By phone number")
        print("2) By facebook page")
        print("===================")
        mode = input()
        run_tinder(mode, driver_type)

    elif option == '2':
        run_lovoo()


if __name__ == '__main__':
    select_app()
