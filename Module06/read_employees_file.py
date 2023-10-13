from pathlib import Path


def read_employees_from_file(path):

    file_location = Path(path)
    file_object = open(file_location, "r")
    employees = list()

    while True: 
        line = file_object.readline()
        if not line:
            break        
        employees.append(line.rstrip("\n"))
    file_object.close()

    return employees


path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\employees.txt"
print(read_employees_from_file(path))