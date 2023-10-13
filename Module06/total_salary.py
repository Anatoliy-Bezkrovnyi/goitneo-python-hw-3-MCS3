from pathlib import Path


def total_salary(path):
    file_location = Path(path)
    file_object = open(file_location, "r")
    total_salary = 0.0
    while True: 
        text_line = file_object.readline()
        if not text_line:
            break
        text_line = text_line.split(",")
        total_salary = total_salary + float(text_line[1].rstrip("\n"))
    file_object.close()

    return total_salary

path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\salary.txt"
print(total_salary(path))
