def all_sub_lists(data):

    sub_lists = [[]]
    single = []
    double = []
    tripple = []
    
    if data:

        i = 0
        
        while i != len(data):
            single.append(data[i:i+1]) 
            if i < len(data) - 1:
                double.append(data[i:i+2])  
            if i < len(data) - 2:
                tripple.append(data[i:i+3])           
            i = i + 1
        sub_lists.extend(single)
        sub_lists.extend(double)
        sub_lists.extend(tripple)
        
        sub_lists.append(data[:])


    return sub_lists

data = [4, 6, 1, 3]
print(all_sub_lists(data))