all_courses = {}

while True:
    course_info = input()
    if course_info == "end":
        break

    course_name, student_name = course_info.split(" : ")

    if course_name not in all_courses.keys():
        all_courses[course_name] = []
    all_courses[course_name].append(student_name)

for course, name in all_courses.items():
    print(f"{course}: {len(name)}")
    print(f"--", '\n-- '.join(all_courses[course]))