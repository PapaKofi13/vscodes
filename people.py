from inheritance import human
from inheritance import Chef
from inheritance import Female
from inheritance import Male


first_person = human("Amerley","female", 24, 'fair' , 'Harbin', 'kenkey')
second_person = human("Mikey", "Male", 24, 'dark', 'Accra', 'pizza')


print(first_person.age)


Amerley = Chef()
Amerley.make_salad()

Amerley = Female()
Amerley.wife_material()
print(f'{first_person.name}')

Mikey = Male()
Mikey.husby()
print(f'{second_person.name}')

kay = Chef()
kay.make_shawarma()


print(f'{first_person.name} makes salad and {second_person.name} makes shawarma ')
