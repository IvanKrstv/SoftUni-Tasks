def average_grade(lst: list) -> float:
    return sum(lst) / len(lst)

students = {}
n = int(input())

for i in range(n):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

for name, grades in students.items():
    if average_grade(grades) >= 4.5:
        print(f"{name} -> {average_grade(grades):.2f}")