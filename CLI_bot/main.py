from commands_handler import add_contact, show_phone, change_contact, show_all, parse_input, add_birthday, show_birthday, birthdays
from AddressBook import AddressBook

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["exit", "close"]:
            print("Good bye!")
            break        
        
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, book)
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "all":
            show_all(book)
        elif command == "add-birthday":
            add_birthday(args, book)
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            birthdays(book) 
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()