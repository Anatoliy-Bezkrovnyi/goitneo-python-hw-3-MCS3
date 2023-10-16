def is_integer(s):

    
    
    if len(s) == 0:
        return False
    else:
        s = s.strip()
        if s.startswith("+") or s.startswith("-"):
            s = s[1:]
        if s.isdigit():
            return True
        else:
            return False
        
s = " +123 "
print(is_integer(s))
