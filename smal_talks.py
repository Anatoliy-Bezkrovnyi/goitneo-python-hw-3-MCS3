def is_check_name(fullname, first_name):
    
    res = fullname.removeprefix(first_name)
    print(res)
    if res != fullname:
        return True
    else:
        return False
   


    


#text = "Alex\nKdfe23\t\f\v.\r"
print(is_check_name("Test Account", "Test"))