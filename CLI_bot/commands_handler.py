from Record import Record
from datetime import datetime

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
    return inner

def missing_name_for_search(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Give me name please."
    return inner

def contact_absent(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f"There is no contact with provided name among contacts."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, book):
    
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    book.add_record(record)    
    
    
@input_error
def change_contact(args, book):
    
    name, old_phone, new_phone = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."
    
@missing_name_for_search
@contact_absent
def show_phone(args, book):
    
    name = args[0]
    record = book.find(name)
    phones = record.show_phones()
    return phones
    

def show_all(book):
    for name, record in book.data.items():
        print(name, record)

@missing_name_for_search
def add_birthday(args, book):
    name = args[0]
    date = args[1]
    record = book.find(name)
    record.add_birthday(date)
    
@missing_name_for_search
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    birthday = record.show_birthday()
    return birthday

def birthdays(book):
    book.show_birthdays()

