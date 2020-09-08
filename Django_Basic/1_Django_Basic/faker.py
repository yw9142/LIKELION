from faker import Faker

myfake = Faker()

print(myfake.name())
print(myfake.address())
print(myfake.text())
print(myfake.sentence())
print(myfake.random_number())

myfake.seed(1)