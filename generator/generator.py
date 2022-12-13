
# Вызывая generated_person мы вызываем класс Person с нашими полями
import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    # Берем по одной итерации
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        salary=faker_ru.random.randint(10000, 1000000),
        department=faker_ru.job(),
        email =faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),



    )