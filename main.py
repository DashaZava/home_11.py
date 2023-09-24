from datetime import datetime, timedelta

class Field:
    def __init__(self, value=None):
        self.__value = value

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        self.validate(value)
        self.__value = value

    def validate(self, value):
        pass

class Phone(Field):
    def validate(self, value):
        if value is not None and not value.isdigit():
            raise ValueError("Phone number must contain only digits")

class Birthday(Field):
    def validate(self, value):
        if value is not None:
            try:
                datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                raise ValueError("Invalid date format. Use YYYY-MM-DD")

class Record:
    def __init__(self, name, phone, birthday=None):
        self.name = name
        self.phone = phone
        self.birthday = birthday

    def days_to_birthday(self):
        if self.birthday:
            birth_date = datetime.strptime(self.birthday, "%Y-%m-%d").date()
            today = datetime.now().date()
            next_birthday = birth_date.replace(year=today.year)
            if today > next_birthday:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_remaining = (next_birthday - today).days
            return days_remaining
        return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def remove_record(self, record):
        self.records.remove(record)

    def iterator(self, batch_size):
        for i in range(0, len(self.records), batch_size):
            yield self.records[i:i + batch_size]

# Example usage:
if __name__ == "__main__":
    address_book = AddressBook()

    record1 = Record("John Doe", "1234567890", "2000-05-15")
    record2 = Record("Alice Smith", "9876543210")
    record3 = Record("Bob Johnson", "5551234567", "1995-12-25")

    address_book.add_record(record1)
    address_book.add_record(record2)
    address_book.add_record(record3)

    for batch in address_book.iterator(2):
        for record in batch:
            print(f"Name: {record.name}, Phone: {record.phone}")
            if record.birthday:
                print(f"Days to Birthday: {record.days_to_birthday()}")
