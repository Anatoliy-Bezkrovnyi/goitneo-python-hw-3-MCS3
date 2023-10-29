from collections import UserDict
from Exceptions import RecordIsAbsent
from datetime import datetime
from collections import defaultdict

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
        
    def show_birthdays(self):
        birthday_guys = defaultdict(list)
        today = datetime.today().date()

        for value in self.data.values():
            name = value.show_name()
            birthday = value.show_birthday()       
            birthday_this_year = birthday.value.replace(year=today.year)

            if birthday_this_year < today:
                birthday_this_year = birthday.value.replace(year=today.year + 1)
            delta_days = (birthday_this_year - today).days

            if delta_days < 7:
                week_day = birthday_this_year.strftime("%A")
                if week_day in ["Saturday", "Sunday"]:
                    birthday_guys["Monday"].append(name)
                else:
                    birthday_guys[week_day].append(name)

        for key, value in birthday_guys.items():
            print(f"{key}: {', '.join(value)}")    

            
        
    
        

