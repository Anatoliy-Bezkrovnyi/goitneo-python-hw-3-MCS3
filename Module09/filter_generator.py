def positive_values(list_payment):
    positive_list = list()
    for value in filter(lambda value: value >= 0, list_payment):
        positive_list.append(value)
    return positive_list



payment = [100, -3, 400, 35, -100]
print(positive_values(payment))