from functools import reduce


def amount_payment(payment):
    positive = list()
    for amount in filter(lambda amount: amount >= 0, payment):
        positive.append(amount)
    sum = reduce((lambda x, y: x + y), payment)
    return sum

payment = [1, -3, 4]
print(amount_payment(payment))