from typing import Dict
from dataclasses import dataclass, field, asdict, astuple


@dataclass
class Person:
    name: str
    last_name: str
    phone: Dict[str, str]
    mail: str
    full_name: str = field(init=False)

    def __post_init__(self):
        self.full_name = f'{self.name} {self.last_name}'


if __name__ == '__main__':
    person = Person('John', 'Textor', {'cellphone': '1234-5678'}, 'john@example.com')
    print(person.full_name)

    # dict representation of person
    print(asdict(person))

    # tuple representation of person
    print(astuple(person))

