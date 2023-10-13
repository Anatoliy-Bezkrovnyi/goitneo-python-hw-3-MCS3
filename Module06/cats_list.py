from pathlib import Path


def get_cats_info(path):
    file_location = Path(path)
    cats_list = []
    with open (file_location, "r") as file_object:
        while True:
            line = file_object.readline().rstrip("\n")
            if not line:
                break
            formatted_line = line.split(",")
            cat_details = {"id" : formatted_line[0], "name" : formatted_line[1], "age" : formatted_line[2]}
            #print(cat_details)
            cats_list.append(cat_details)
        return cats_list


path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\cats_list.txt"

print(get_cats_info(path))