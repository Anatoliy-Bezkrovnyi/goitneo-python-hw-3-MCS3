
from datetime import datetime
from collections import defaultdict

def get_birthdays_per_week(users):

    birthday_guys = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()        
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            week_day = birthday_this_year.strftime("%A")
            if week_day in ["Saturday", "Sunday"]:
                birthday_guys["Monday"].append(name)
            else:
                birthday_guys[week_day].append(name)

    for key, value in birthday_guys.items():
        print(f"{key}: {', '.join(value)}")    
    
    



users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)}, 
    {"name": "Jill Valentine", "birthday": datetime(1974, 10, 28)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 25)}, 
    {"name": "Jan Koum", "birthday": datetime(1976, 10, 24)}
]



if __name__ == "__main__":
    get_birthdays_per_week(users)