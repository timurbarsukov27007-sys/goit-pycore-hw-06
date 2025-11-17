import re

class Field:
    def __init__(self, value):
        self.value=value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if not re.match(r"^\d{10}$", value):
            raise ValueError("Phone must be exactly 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name=Name(name)
        self.phones=[]
    
    def add_phone(self, number):
        self.phones.append(Phone(number))

    def remove_phone(self, number):
        for p in self.phones:
            if p.value==number:
                self.phones.remove(p)
                return True
        return False

    def edit_phone(self, old, new):
        if self.remove_phone(old):
            self.add_phone(new)
            return True
        return False

    def find_phone(self, number):
        for p in self.phones:
            if p.value==number:
                return True
        return False

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(str(p) for p in self.phones)}"

class AddressBook:
    def __init__(self):
        self.data={}

    def add_record(self, record):
        self.data[record.name.value]=record

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

    def find(self, name):
        result=[]
        for key, record in self.data.items():
            if name.lower() in key.lower():
                result.append(record)
        return result
