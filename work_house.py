from faker import Faker

fake = Faker(['RU_ru'])

print(fake.name(),fake.date_of_birth(maximum_age = 99), fake.text(), fake.city(), fake.job())