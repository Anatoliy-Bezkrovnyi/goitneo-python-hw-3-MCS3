result = None
operand = None
operator = None
wait_for_number = True

while True:
    if operator == "=":
        break
    while wait_for_number:
        operand = input("Provide the operand, it should be integer or float: ")
        if operator is None:
            if "." in operand:
                try:
                    result = float(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
            else:
                try:
                    result = int(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
        elif operator == "+":
            if "." in operand:
                try:
                    result = result + float(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
            else:
                try:
                    result = result + int(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
        elif operator == "-":
            if "." in operand:
                try:
                    result = result - float(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
            else:
                try:
                    result = result - int(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
        elif operator == "*":
            if "." in operand:
                try:
                    result = result * float(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
            else:
                try:
                    result = result * int(operand)
                    wait_for_number = False
                except:
                    print("Provided value is not operand, please try again")
                    continue
        elif operator == "/":
            if "." in operand:
                try:
                    result = result / float(operand)
                    wait_for_number = False
                except ZeroDivisionError:
                    print("You just tried to divide on zero, which is impossible")
                    continue
                except:
                    print("Provided value is not operand, please try again")
                    continue
            else:
                try:
                    result = result / int(operand)
                    wait_for_number = False
                except ZeroDivisionError:
                    print("You just tried to divide on zero, which is impossible")
                    continue
                except:
                    print("Provided value is not operand, please try again")
                    continue
        
       
    while not wait_for_number:
        operator = input("Provide the desired operator: +, -, * or /, press \"=\" to finish calculation: ")
        if ("+" in operator) or ("-" in operator) or ("*" in operator) or ("/" in operator):            
            wait_for_number = True
        elif operator == "=":
            print(f"Result is: {result} ")
            break
        else: 
            operator = print("Provided value is not operator, please try again")
            continue

    