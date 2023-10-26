from collections import UserDict
from collections import UserList
from collections import UserString


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys
    
class AmountPaymentList(UserList):
    def amount_payment(self):
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        return sum
    
class NumberString(UserString):
    def number_count(self):
        counter = 0
        for char in self.data:
            if char.isdigit():
                counter += 1
        return counter
