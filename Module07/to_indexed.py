def to_indexed(source_file, output_file):

    with open(source_file, "r") as sourse:
        lines = sourse.readlines()

    with open(output_file, "w") as output:
        for index, line in enumerate(lines):
            formatted_line = f"{index}: {line}"
            output.write(formatted_line)
    


source_file = "D:\GoIT\Projects\Tier_1_Python_Programming\Module07\\from_indexed.txt"
output_file = "D:\GoIT\Projects\Tier_1_Python_Programming\Module07\\to_indexed.txt"

to_indexed(source_file, output_file)