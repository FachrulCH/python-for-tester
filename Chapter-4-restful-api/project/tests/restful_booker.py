import random

import requests
from faker import Faker

URL = 'https://restful-booker.herokuapp.com'
fake = Faker()


def url(path: str):
    return URL + path

class Asique():
    def __init__(self):
        print('mantap')

def generate_dummy():
    price = fake.numerify()
    checkin = random.choice(['2018-02-01', '2018-03-01', '2018-04-01', '2018-05-01', '2018-06-10'])
    checkout = random.choice(['2018-02-5', '2018-03-05', '2018-04-05', '2018-05-05', '2018-06-20'])
    additionalneeds = random.choice(['Breakfast', 'Mini Fridge', 'Extra towel', 'Dinner'])

    return {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": price,
        "depositpaid": 100,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }


def get_bookings(params=None):
    if params:
        return requests.get(url('/booking'), param=params)
    else:
        return requests.get(url('/booking'))


def get_detail_booking(id: int):
    return requests.get(url(f'/booking/{id}'))


def create_booking(booking):
    return requests.post(url('/booking'), json=booking)


def create_dummy_booking():
    booking = generate_dummy()
    return create_booking(booking)


def get_authtoken(username: str = 'admin', password: str = 'password123'):
    return requests.post(url('/auth'), json={
        'username': username,
        'password': password
    }).json().get('token')
