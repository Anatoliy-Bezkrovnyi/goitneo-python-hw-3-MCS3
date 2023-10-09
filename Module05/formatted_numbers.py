def formatted_numbers():

    formatted_numbers = []

    formatted_numbers.append("|{:^10}|{:^10}|{:^10}|".format( "decimal", "hex", "binary"))
    
    for number in range(16):
        formatted_numbers.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(number))

    return formatted_numbers

for line in formatted_numbers():
    print(line)