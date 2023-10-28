import re

def generator_numbers(string=""): 
    i=0   
    matches = re.findall('\d+', string)
    return matches
    

    



def sum_profit(string):
    sum = 0
    generator = generator_numbers(string)
    for string in generator:
        sum += int(string)
    return sum



string="The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

print(sum_profit(string))