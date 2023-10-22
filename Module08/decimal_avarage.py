from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    getcontext().prec = signs_count
    sum = 0
    for number in number_list:
        sum = Decimal(sum) + Decimal(number)
    average = sum / Decimal(len(number_list))
    return average


number_list = [3, 5, 77, 23, 0.57]
signs_count = 6
print(decimal_average(number_list, signs_count))