from datetime import date


def get_days_in_month(month, year):

    days = date(year=year, month=month%12+1, day=1) - date(year=year, month=month, day=1) 
    if int(days.days) < 0:
        return 31       

    return days.days

month = 12
year = 1985

print(get_days_in_month(month, year))