from tinydb import TinyDB, Query
from datetime import date
import uuid

db = TinyDB('db.json')
TINDER_TABLE = 'tinder'
LOVOO_TABLE = 'lovoo'


def save_tinder_likes(like: int):
    table = db.table(TINDER_TABLE)
    table.insert({
        'id': str(uuid.uuid4().hex),
        'type': 'Tinder',
        'likes': like,
        'date': str(date.today())
    })


def get_tinder_date_likes(date: str):
    table = db.table(TINDER_TABLE)

    Tinder = Query()
    result = table.search((Tinder.likes) & (Tinder.date == date))

    if not result:
        save_tinder_likes(0)
        raise TypeError('Likes not found')
    else:
        return result[0]['likes']


def get_tinder_all_likes():
    table = db.table(TINDER_TABLE)

    Tinder = Query()
    result = table.search(Tinder.likes)

    if not result:
        save_tinder_likes(0)
        raise TypeError('Likes not found')
    else:
        likes = 0
        for x in result:
            likes = likes + x['likes']
        return likes
