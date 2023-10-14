from pathlib import Path

def sanitize_file(source, output):
    source_file_location = Path(source)
    output_file_location = Path(output)

    with open(source_file_location, "r") as file_object:
        file_lines = file_object.readlines()
        sanitized_list = list()
        for item in file_lines:
            #item = item.rstrip("\n")
            for char in item:
                if char.isdigit():
                    item = item.replace(char, "")
            sanitized_list.append(item)
        print(sanitized_list)

    with open(output_file_location, "w") as file_object_output:
        string = " ".join(sanitized_list)
        file_object_output.write(string)





source = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\input.txt"
output = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\output.txt"

sanitize_file(source, output)

