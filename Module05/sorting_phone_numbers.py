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


def get_phone_numbers_for_countries(list_phones):
    sorted_phones = {}
    ua_phones = []
    jp_phones = []
    tw_phones = []
    sg_phones = []
    
    for phone in list_phones:
        sanitized_phone = sanitize_phone_number(phone)
        if sanitized_phone.startswith("81"):
            jp_phones.append(sanitized_phone)
        elif sanitized_phone.startswith("65"):
            sg_phones.append(sanitized_phone)
        elif sanitized_phone.startswith("886"):
            tw_phones.append(sanitized_phone)
        else:
            ua_phones.append(sanitized_phone)

    sorted_phones.update({"UA": ua_phones, "JP": jp_phones, "TW": tw_phones, "SG": sg_phones})
    return sorted_phones

phone_list = [ "    +38(050)123-32-34",     "     0503451234",     "(050)8889900",     "8150-111-22-22",     "6550 111 22 11   ", "8860-111-22-22"]
print(get_phone_numbers_for_countries(phone_list))