
def get_employees_by_profession(path, profession):

    with open(path, "r") as file_object:
        workers_list = file_object.readlines()
        res_list = list()
        for string in workers_list:
            if string.find(profession) > 0:
                string = string.rstrip("\n")
                res_list.append(string)
        res_string = "".join(res_list)
        res_string = res_string.replace(profession, "").rstrip()

        return res_string


path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module07\workers.txt"
profession = "cook"

print(get_employees_by_profession(path, profession))