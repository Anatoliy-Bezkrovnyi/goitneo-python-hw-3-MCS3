from datetime import datetime


def get_str_date(date):
    separate_date_time = date.split()
    y_m_d = separate_date_time[0].split("-")
    input_date = datetime(int(y_m_d[0]), int(y_m_d[1]), int(y_m_d[2]))
    output_string = input_date.strftime("%A %d %B %Y")

    return output_string
    


date = "2021-05-27 17:08:34.149Z"
print(get_str_date(date))