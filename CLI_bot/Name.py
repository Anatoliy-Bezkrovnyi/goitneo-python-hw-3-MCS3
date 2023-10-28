from Field import Field

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return super().__str__()
    
    def __eq__(self, other):
        return self.value == other.value
