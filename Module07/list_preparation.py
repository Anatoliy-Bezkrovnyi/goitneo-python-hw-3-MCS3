def data_preparation(list_data):
    formatted_list = []

    for list in list_data:
        if len(list) > 2:
            list.remove(min(list))
            list.remove(max(list))
        formatted_list.extend(list)

    formatted_list.sort(reverse=True)
    
    return formatted_list



list_data = [[1,2,3],[3,4], [5,6]]
print(data_preparation(list_data))