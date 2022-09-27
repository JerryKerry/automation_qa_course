
# Вызывая generated_person мы вызываем класс Person с нашими полями
from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

def generated_person():
    # Берем по одной итерации
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email =faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),


    )