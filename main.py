from datetime import date
import re


class Field:
    def __init__(self, value: Any):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: Any):
        self._value = value


class Phone(Field):
    def __init__(self, number: str):
        super().__init__(number)

    def validate(self) -> bool:
        return re.match(r"^\+380\d{9}$", self.number) is not None


class Birthday(Field):
    def __init__(self, year: int, month: int, day: int):
        super().__init__(Birthday(year, month, day))

    def validate(self) -> bool:
        return 1900 <= self.year <= 2099 and 1 <= self.month <= 12 and 1 <= self.day <= 31


class Record:
    def __init__(self, name: str, email: str, phone: Phone, birthday: Birthday = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.birthday = birthday

    def days_to_birthday(self) -> int:
        if self.birthday is None:
            return None
        else:
            today = date.today()
            birthday = self.birthday.date()
            return (birthday - today).days


class AddressBook:
    def __init__(self):
        self.records = []

    def add(self, record: Record):
        self.records.append(record)

    def iterator(self, n: int) -> Iterator[Record]:
        for i in range(0, len(self.records), n):
            yield self.records[i : i + n]


# Додавання запису з днем народження
addressbook = AddressBook()
addressbook.add(Record("Іван Іванович", "ivanov@example.com", Phone("+380999999999"), Birthday(2000, 12, 25)))

# Виведення кількості днів до наступного дня народження
print(addressbook[0].days_to_birthday())  # 191

# Додавання пагінації
for page in addressbook.iterator(5):
    for record in page:
        print(record.name)
