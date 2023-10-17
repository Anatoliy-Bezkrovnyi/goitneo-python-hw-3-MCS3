def token_parser(s):
    resulted_list= []
    number = ""

    for char in s:
        if char.isdigit():
           number = number + char 
        elif char in ("(", ")", "+", "-", "*", "/"):
            if number:
                resulted_list.append(number)
                number = ""
            resulted_list.append(char)
    if number:
       resulted_list.append(number)     

    return resulted_list


s = "2+ 34-5 * 3"
print(token_parser(s))