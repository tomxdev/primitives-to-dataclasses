from typing import Dict


class Person:
    def __init__(self, name: str, last_name: str, phone: Dict[str, str], mail: str):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail


person = Person('John', 'Textor', {'cellphone': '1234-5678'}, 'john@gmail.com')


if __name__ == '__main__':
    print(person)
    print(person.name)
    print(person.last_name)
    