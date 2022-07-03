from typing import Dict


class Person:
    def __init__(self, name: str, last_name: str, phone: Dict[str, str], mail: str):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.mail = mail

    def __eq__(self, other):
        return all([
            self.name == other.name,
            self.last_name == other.last_name,
            self.phone == other.phone,
            self.mail == other.mail
        ])

    def __repr__(self):
        return f"Person({self.name}, {self.last_name}, {self.phone}, {self.mail})"


if __name__ == '__main__':
    print(Person(name='John', last_name='John', phone={"cellphone": "1234-5678"}, mail="john@example.com"))
