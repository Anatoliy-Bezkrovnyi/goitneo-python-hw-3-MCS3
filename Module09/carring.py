def discount_price(discount):
    def inner(price):
        price -= price * discount
        return price
    return inner
    


    