import base64


def encode_data_to_base64(data):
    
    coded_list = list()
    
    for item in data:
        item_bytes = item.encode("utf-8")
        base64_bytes = base64.b64encode(item_bytes)
        base64_message = base64_bytes.decode("utf-8")
        coded_list.append(base64_message)
    return coded_list



data = ['andry:uyro18890D', 'steve:oppjM13LL9e']
print(encode_data_to_base64(data))