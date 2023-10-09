grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    counter = 1
    formatted_grades = []
    for name, grade in students.items():
        mark = grades.get(grade)
        formatted_grades.append("{:>4}|{:<10}|{:^5}|{:^5}".format( counter, name, grade, mark))
        counter = counter + 1
    return formatted_grades

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
print(formatted_grades(students))

