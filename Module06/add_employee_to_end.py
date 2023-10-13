from pathlib import Path


def add_employee_to_file(record, path):
    file_location = Path(path)
    file_object = open(file_location, "a")
    file_object.write(record + "\n")
    file_object.close()


record = "Drake Mikelsson,19"
path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\employees.txt"

add_employee_to_file(record, path)
