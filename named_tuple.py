from collections import namedtuple

person = namedtuple('Person', ['name', 'last_name', 'phone', 'email'])

data = [
    person('John', 'Textor', {'cellphone': '1234-5678'}, 'john@email.com'),
    person('Max', 'Textor', {'cellphone': '34567-5678'}, 'max@email.com'),
]

john = data[0]
max = data[1]


if __name__ == '__main__':
    print(john.name)  # John
    print(max.name)  # Max
