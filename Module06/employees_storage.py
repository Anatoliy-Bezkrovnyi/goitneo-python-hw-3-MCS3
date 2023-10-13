from pathlib import Path



def write_employees_to_file(employee_list, path):
    file_location = Path(path)
    file_object = open(file_location, "w")
    for item in employee_list:
        for string in item:
            print(string)
            file_object.write(string + "\n")

    file_object.close()


path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\employees.txt"
employee_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

write_employees_to_file(employee_list, path)