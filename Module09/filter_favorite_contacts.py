def get_favorites(contacts):
    favourite_list = list()
    for contact in filter(lambda contact: contact.get("favorite"), contacts):
        favourite_list.append(contact)
    return favourite_list



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
}, 
{
    "name": "Some Contact",
    "email": "some.contact@vestibul.co.uk",
    "phone": "(992) 678-0987",
    "favorite": False,
}
]

print(get_favorites(list_contacts))