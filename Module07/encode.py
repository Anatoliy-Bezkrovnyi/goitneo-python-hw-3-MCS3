def encode(data):

    if not data:
        return []
    else:
        encoded_list = [data[0]]
        string_length = 0
        for char in data:            
            if char == data[0]:
                string_length = string_length + 1
            if char != data[0]:
                encoded_list.append(string_length)
                return encoded_list
        return encoded_list + encode(data[string_length:])
        
        



data = ['X','X','X','Z','Z','X','X','Y','Y','Y','Z','Z']
print(encode(data))