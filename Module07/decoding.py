def decode(data):
    if len(data) == 0:
        return []
    if len(data) > 0:
        decoded_list = []
        iterations = data[1]
        while iterations != 0:
            decoded_list.append(data[0])
            iterations = iterations -1
        return decoded_list + decode(data[2:])
        
    
data = ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
print(decode(data))