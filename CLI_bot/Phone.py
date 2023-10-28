from Field import Field
from Exceptions import InvalidPhoneNumber


class Phone(Field):
    def __init__(self, value):
        if str(value).isdigit() and len(str(value)) == 10:
            super().__init__(value)
        else:
            raise InvalidPhoneNumber

    def __str__(self):
        return super().__str__()
    
    def __eq__(self, other):
        return self.value == other.value
