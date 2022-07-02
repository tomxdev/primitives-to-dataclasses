from typing import NamedTuple, Dict


class Person(NamedTuple):
    name: str
    last_name: str
    phone: Dict[str, str]
    mail: str


person = Person("John", "Textor", {"cellphone": "1234-5678"}, "john@gmail.com")

if __name__ == '__main__':
    print(person)
    print(person.name)
    print(person.last_name)
