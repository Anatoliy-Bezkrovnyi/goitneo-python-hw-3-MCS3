def get_emails(list_contacts):
    email_list = list()
    for contact in map(lambda contact: contact.get("email"), list_contacts):
        email_list.append(contact)
    return email_list



list_contacts = [
{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}, 
{
    "name": "Test Account",
    "email": "test.account@vestibul.co.uk",
    "phone": "(992) 123-4563",
    "favorite": True,
}
]

print(get_emails(list_contacts))