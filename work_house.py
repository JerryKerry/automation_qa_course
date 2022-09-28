from faker import Faker

# fake.bothify прекрасно подходит для генерации тестовых ПД
fake = Faker(['RU_ru'])

print(fake.name() ,fake.date_of_birth(maximum_age = 99)  , "\n" + fake.city() ,"\n" + fake.job() + "\n" +
      fake.bothify(text='###-###') +'\n' + fake.bothify(text='ID продукта : ???- ###',letters='ADFS'))


# Генерация предложения из собственного списка
my_list=["привет", "Артём", "как", "твои", "дела"]

print(fake.sentence(ext_word_list= my_list))


print(fake.bban())
print(fake.iban())
print(fake.swift())


print(fake.profile())
print(fake.simple_profile())
print(fake.simple_profile(sex='M'))
print(fake.simple_profile(sex='F'))
param = ["username"]
print(fake.profile(fields=param, sex='F'))




