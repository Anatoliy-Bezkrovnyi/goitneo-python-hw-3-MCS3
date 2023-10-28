from Phone import Phone
from Name import Name
from Exceptions import *


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phone = Phone(phone)
        if self.phone in self.phones:
            raise PhoneNumberExists
        else:
            self.phones.append(self.phone)
            print(f"Provided phone number '{self.phone}' was added to the record '{self.name}'")

    def remove_phone(self, phone):
        self.phone = Phone(phone)
        if self.phone in self.phones:
            self.phones.remove(self.phone)
            print(f"Provided phone number '{self.phone}' was removed from the record '{self.name}'")
        else:
            raise PhoneNumberNotFound

    def edit_phone(self, old_phone, new_phone):
        self.old_phone = Phone(old_phone)
        self.new_phone = Phone(new_phone)
        if self.old_phone in self.phones:
            self.phones.remove(self.old_phone)
            self.phones.append(self.new_phone)
            print(f"Phone number '{self.old_phone}' was updated to '{self.new_phone}'")
        else:
            raise PhoneNumberNotFound
        

    def find_phone(self, phone):
        self.phone = Phone(phone)
        for item in self.phones:
            if item == self.phone:
                return record
        raise PhoneNumberNotFound
        
    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
record = Record("Test")
    


