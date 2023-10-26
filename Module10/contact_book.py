class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if contact.get("id") == id:
                return contact
        return None
    
    def remove_contacts(self, id):
        for contact in self.contacts:
            if contact.get("id") == id:
                self.contacts.remove(contact)

list_contacts = Contacts()
list_contacts.add_contacts("John", "1234567890", "test@test.com", True)
list_contacts.add_contacts("Tom", "0123456789", "test1@test1.com", False)
print(list_contacts.list_contacts())
list_contacts.remove_contacts(2)
print(list_contacts.list_contacts())
