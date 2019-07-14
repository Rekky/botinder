from src.tinder import Tinder
from src.fotocasa import Fotocasa


CHROME_DRIVER = './chrome_driver/chromedriver.exe'
TINDER_URL = 'https://tinder.com/app/recs'
FOTOCASA_URL = 'https://www.fotocasa.es/es/alquiler/viviendas/barcelona-capital/todas-las-zonas/l?gridType=list&combinedLocationIds=724,9,8,232,376,8019,0,0,0&latitude=41.3854&longitude=2.17754&maxPrice=1400&minRooms=3'


def run_tinder():
    tinder = Tinder(TINDER_URL, CHROME_DRIVER)
    tinder.run_like_sequence('611400206', 1000000)


def run_fotocasa():
    fotocasa = Fotocasa(FOTOCASA_URL, CHROME_DRIVER)
    fotocasa.run_search_sequence('611400206', 'ziroustyle@gmail.com', 3, 1400, 20)


if __name__ == '__main__':
    run_tinder()
    # run_fotocasa()
