
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact():
    pass

def show_phone():
    pass

def show_all(contacts):
    for key, value in contacts.items():
        return f"{key}: {value}"
