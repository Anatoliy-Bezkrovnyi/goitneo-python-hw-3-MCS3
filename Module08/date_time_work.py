from datetime import datetime


def get_days_from_today(date):

    current_datetime = datetime.now()
    #current_date = current_datetime.date()
    date_to_count_list = date.split("-")    
    date_res = datetime(year=int(date_to_count_list[0]), month=int(date_to_count_list[1]), day=int(date_to_count_list[2]))
    dif = current_datetime - date_res
    dif = dif.days
    #print(dif)
    return dif



date = "2020-10-09"
get_days_from_today(date)