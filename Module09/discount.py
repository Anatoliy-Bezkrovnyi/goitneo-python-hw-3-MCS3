DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if "discount" in customer.keys():
        discount = customer.get("discount")
    else: 
        discount = DEFAULT_DISCOUNT

    price = price * (1 - discount)
    return price



price = 10
customer = {"name": "Boris", "discount": 0.15}

print(get_discount_price_customer(price, customer))