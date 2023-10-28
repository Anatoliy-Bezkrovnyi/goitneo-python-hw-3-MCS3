def normal_name(list_name):

    final_list = list()

    for name in map(lambda name: name.capitalize(), list_name):
        final_list.append(name) 

    return final_list


list_name = ["dan", "jane", "steve", "mike"]
print(normal_name(list_name))