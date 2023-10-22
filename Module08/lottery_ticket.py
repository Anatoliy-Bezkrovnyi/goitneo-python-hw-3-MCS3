from random import randrange


def get_numbers_ticket(min, max, quantity):

    res_list = list()
    if min < 1 or max > 1000 or quantity < min or quantity > max:
        return res_list
    else:
        while quantity != 0:
            number = randrange(min, max)
            if number in res_list:
                quantity = quantity + 1
            else:
                res_list.append(number)
                quantity = quantity - 1
    return sorted(res_list)


min = 1
max = 50
quantity = 6
print(get_numbers_ticket(min, max, quantity))
