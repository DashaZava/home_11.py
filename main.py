from datetime import datetime
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Невірний формат номера телефону")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Невірний формат дати народження")
        super().__init__(value)

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        found = False
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                found = True
                break
        if not found:
            raise ValueError("Номер телефону не знайдено")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def days_to_birthday(self):
        if self.birthday is not None:
            today = datetime.today()
            return (self.birthday - today).days
        return None

    def __str__(self):
        phone_str = '; '.join(str(p) for p in self.phones)
        if self.birthday is None:
            birthday_str = "(не задано)"
        else:
            birthday_str = self.birthday.value
        return f"Contact name: {self.name}, phones: {phone_str}, birthday: {birthday_str}"

class AddressBook(UserDict):
    def iterator(self, n=10):
        for i in range(0, len(self.data), n):
            yield self.data[i:i + n]

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return ', '.join(str(record) for record in self.data.values())
