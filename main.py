from collections import UserDict
from datetime import datetime


class Field:
    def __init__(self, value):
        self._value = value

    def __repr__(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self._value


class Phone(Field):

    @property
    def values(self):
        return self._value

    @values.setter
    def values(self, new_value):
        if len(list(new_value)) >= 9:
            self._value = new_value
        else:
            print('Only 9+ numbers! Number is not add!')
            return


class Name(Field):

    @property
    def values(self):
        return self._value

    @values.setter
    def values(self, new_value):
        if len(list(new_value)) > 0:
            user_name = []
            for el in new_value.split(" "):
                user_name.append(el.capitalize())
            self._value = " ".join(user_name)
        else:
            print("More than one character! Try again")
            return


class Birthday(Field):

    @property
    def values(self):
        return self._value

    @values.setter
    def values(self, new_value):
        if len(list(new_value)) == 10 and int(new_value[0:4]) > 0 and int(new_value[5:7]) > 0 and int(
                new_value[8:10]) > 0:
            self._value = new_value
        else:
            print('Incorect data format! Data is not add')
            self._value = "Not found"
            return


class Record:
    def __init__(self, name: Name, phone: Phone, birthday=None):
        self.name = name
        self.phones = []  # спиисок экземпляр класа Phone
        self.phones.append(phone)
        self.birthday = birthday

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def days_to_birthday(self):
        if self.birthday._value != "Not found":
            today = datetime.today()
            birthday = datetime.strptime(str(self.birthday), '%Y-%m-%d')
            current_year = datetime(year=today.year, month=birthday.month, day=birthday.day + 1)
            result = current_year - today
            if result.days == 0:
                return print(f'Birthday {self.name} Today!!!')
            elif result.days < 0:
                result = datetime(year=today.year + 1, month=birthday.month, day=birthday.day) - today
                return print(f'Days to br:{result.days}')
            else:
                return print(f'Days to birthday {self.name}: {result.days}')
        else:
            print("Birthday not found")

    def delete_phone(self, phone):
        for el in self.phones:
            if phone == el._value:
                self.phones.remove(el)
                return
        print("Error number")

    def change_phone(self, phone, new_phone: Phone):
        if new_phone._value == "":
            return
        for el in self.phones:
            if phone == el._value:
                self.add_phone(new_phone)
                self.phones.remove(el)
                return
        print("Error number")

    def __str__(self):
        return f'Name: {self.name} Phones: {", ".join([str(p) for p in self.phones if str(p) != ""])} Birthday: {self.birthday}'


class AddressBook(UserDict):

    def add_record(self, args):
        for contact_name in self.data:
            if args.name == contact_name:
                return print
