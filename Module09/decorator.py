def format_phone_number(func):
    def wrapper(phone):
        result = func(phone)
        if len(result) == 12:
            result = f"+{result}"
        elif len(result) == 10:
            result = f"+38{result}"
        return result  
    return wrapper   
    


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number("+38(050)123-32-34"))