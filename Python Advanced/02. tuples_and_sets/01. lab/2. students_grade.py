n = int(input())
students = {}

def average_grade(lst: list) -> str:
    return f'{sum(lst) / len(lst):.2f}'


for _ in range(n):
    data = input().split()
    name, grade = data[0], float(data[1])
    if name not in students:
        students[name] = []
    students[name].append(grade)

for student, grades in students.items():
    print(f"{student} -> {' '.join(f'{x:.2f}' for x in grades)} (avg: {average_grade(grades)})")

