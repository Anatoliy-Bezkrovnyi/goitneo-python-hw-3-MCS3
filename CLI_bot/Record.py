from Phone import Phone
from Name import Name
from Exceptions import *
from Birthday import Birthday




class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        
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
    
    def add_birthday(self, birthday):        
        self.birthday = Birthday(birthday)
        print(f"Birthday added to record '{self.name}'")

    def show_birthday(self):
        return self.birthday
    
    def show_name(self):
        return str(self.name)
    
    def show_phones(self):
        phone_str = ""
        for phone in self.phones:
            phone_str = phone_str + str(phone)
        return phone_str
        
    

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
    

    


