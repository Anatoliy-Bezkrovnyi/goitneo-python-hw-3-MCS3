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
def add_contact(args, contacts):
    
    name, phone = args
    if name in contacts:
        return "Name already exists, chose anther name or use 'change' command to update existing phone number"          
    else:
        contacts[name] = phone
        return "Contact added."
    
@input_error
def change_contact(args, contacts):
    
    name, phone = args
    contacts[name] = phone
    return "Contact updated."
    
@missing_name_for_search
@contact_absent
def show_phone(args, contacts):
    
    name = args[0]
    phone = contacts[name]
    return phone
    

def show_all(contacts):
    if len(contacts) > 0:
        for key, value in contacts.items():
            print(f"{key}: {value}")
    else:
        print("There are no contacts yet.")
