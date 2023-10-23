
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return "Name already exists, chose anther name or use 'change' command to update existing phone number"          
        else:
            contacts[name] = phone
            return "Contact added."
    except ValueError:
        return "Contact name and phone are expected. Please try again"

def change_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact updated."
    except ValueError:
        return "Contact name and phone are expected. Please try again"

def show_phone(args, contacts):
    try:
        name = args[0]
        phone = contacts[name]
        return phone
    except ValueError:
        return "Contact name is expected. Please try again"

def show_all(contacts):
    for key, value in contacts.items():
        print(f"{key}: {value}")
