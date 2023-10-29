from Field import Field
from datetime import datetime

class Birthday(Field):

    def __init__(self, value):
        super().__init__(datetime.strptime(str(value), "%d-%m-%Y").date())

    def __str__(self):
        return super().__str__()
