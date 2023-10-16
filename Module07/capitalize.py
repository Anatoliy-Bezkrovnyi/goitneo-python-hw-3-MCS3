def capital_text(s):

    formatted_string = ""

    list_split = s.split()
    formatted_string = list_split[0].capitalize()
    counter = 1
    for item in list_split[counter:]:
        if list_split[counter - 1].endswith(".") or list_split[counter - 1].endswith("!") or list_split[counter - 1].endswith("?"):
            item = item.capitalize()
        formatted_string = formatted_string + f" {item}"
        counter = counter + 1
        #print(item)

    return formatted_string

s = "    some string     to verify.    if metod?    is working!    test"
print(capital_text(s))

        
