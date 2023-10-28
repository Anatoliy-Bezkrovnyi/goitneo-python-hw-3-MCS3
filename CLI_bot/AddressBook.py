from collections import UserDict
from Record import Record
from Exceptions import RecordIsAbsent

class AddressBook(UserDict):   

    def __init__(self):
        self.data = {} 
    
    def add_record(self, record):
        self.data[record.name.value] = record 
        


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
        
    
        

