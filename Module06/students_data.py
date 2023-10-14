from pathlib import Path


def save_applicant_data(source, output):
    output_file_location = Path(output)

    students_data = list()

    for item in source:
        res_strirng = ""
        for value in item.values():
            res_strirng = res_strirng + f"{value},"
        res_strirng = res_strirng.rstrip(",") + "\n"
        students_data.append(res_strirng)
    print(students_data)

    
    with open(output_file_location, "w") as output_file_object:
        output_file_object.writelines(students_data)





source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
output = "D:\GoIT\Projects\Tier_1_Python_Programming\Module06\students_output.txt"

save_applicant_data(source, output)