my_dict = {}

while True:
    student = input().split(":")
    try:
        name, id_num, course = student[0], student[1], student[2]
    except IndexError:
        course = student[0]
        break

    my_dict[name] = {}
    my_dict[name][id_num] = course
needed_students = {}
for student, info in my_dict.items():
    for num, searched_course in info.items():
        if searched_course == course.replace("_", " "):
            needed_students[student] = num

for name, idi in needed_students.items():
    print(f"{name} - {idi}")