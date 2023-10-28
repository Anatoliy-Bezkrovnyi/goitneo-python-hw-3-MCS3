from collections import UserDict
from Record import Record
from Exceptions import RecordIsAbsent

class AddressBook(UserDict):    
    
    def add_record(self, record):
        self.record = Record(record) 
        name = self.record.name
        phones = "1234567890"     
        self.data[str(name)] = phones


    def find(self, name):
        self.name = name
        if self.name in self.data.keys():
            return self.data.get(self.name)
        else:
            raise RecordIsAbsent


    def delete(self, name):
        self.name = name
        if self.name in self.data.keys():
            self.data.pop(self.name)
            print(f"{self.name} record was deleted from adressbook")
        else:
            raise RecordIsAbsent
        
    def __str__(self):
        for key, value in self.data.items():
            return f"{key} : {value}"
        

record = Record("Test")
print(record)
record.add_phone("1234567890")
print(record)
book = AddressBook()
book.add_record(record)
print(book)
print(book.find("Test"))
