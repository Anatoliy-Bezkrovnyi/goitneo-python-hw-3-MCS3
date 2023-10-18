def file_operations(path, additional_info, start_pos, count_chars):

    with open(path, "a") as file_object:
        file_object.write(additional_info)

    with open(path, "r") as file_object:
        file_object.seek(start_pos)
        string = file_object.read(count_chars)

    return string



path = "D:\GoIT\Projects\Tier_1_Python_Programming\Module07\input_file.txt"
additional_info = "Some valid string for testing"
start_pos = 5
count_chars =5

print(file_operations(path, additional_info, start_pos, count_chars))